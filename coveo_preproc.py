import numpy as np
import pandas as pd
import gc
import datetime as dt
import glob
import argparse
import os


def main(path: str):
    data = pd.read_csv(
        os.path.join(path, "release_10_23_2020.csv"),
        sep=",",
        date_parser=["server_timestamp_epoch_ms"],
        dtype={
            "session_id_hash": str,
            "event_type": "category",
            "product_action": str,
            "product_skus_hash": str,
            "hashed_url": str,
        },
    )
    
    session_hashes = data.session_id_hash.unique()
    item_hashes = data.product_skus_hash.unique()
    data = pd.merge(
        data,
        pd.DataFrame(
            {"session_id_hash": session_hashes, "session_idx": np.arange(len(session_hashes))}
        ),
    )
    data = pd.merge(
        data,
        pd.DataFrame(
            {"product_skus_hash": item_hashes, "item_id": np.arange(len(item_hashes))}
        ),
    )
    data = data.sort_values(["session_idx", "server_timestamp_epoch_ms", "item_id"])

    data["session_id"] = np.cumsum(
        np.hstack(
            [
                False,
                (
                    data.server_timestamp_epoch_ms.values[1:]
                    - data.server_timestamp_epoch_ms.values[:-1]
                    > 3600 * 1000
                )
                | (data.session_idx.values[1:] != data.session_idx.values[:-1]),
            ]
        )
    )

    view = data[data.product_action == "detail"]
    view = pd.DataFrame(
        {
            "session_id": view.session_id,
            "time": view.server_timestamp_epoch_ms,
            "item_id": view.item_id,
        }
    )
    view = view.sort_values(by=["session_id", "time", "item_id"])
    view.reset_index(inplace=True, drop=True)

    dupmask = np.hstack(
        [
            False,
            (view.session_id.values[1:] == view.session_id.values[:-1])
            & (view.item_id.values[1:] == view.item_id.values[:-1]),
        ]
    )
    view_dedup = view[~dupmask].copy()

    pl = -1
    print(
        len(view_dedup),
        view_dedup.session_id.nunique(),
        view_dedup.item_id.nunique(),
    )
    while len(view_dedup) != pl:
        pl = len(view_dedup)
        slength = view_dedup.groupby("session_id").size()
        view_dedup.drop(
            view_dedup[view_dedup.session_id.isin(slength[slength == 1].index)].index,
            inplace=True,
        )
        gc.collect()
        print(
            len(view_dedup),
            view_dedup.session_id.nunique(),
            view_dedup.item_id.nunique(),
        )
        isupp = view_dedup.groupby("item_id").size()
        view_dedup.drop(
            view_dedup[view_dedup.item_id.isin(isupp[isupp < 5].index)].index,
            inplace=True,
        )
        gc.collect()
        print(
            len(view_dedup),
            view_dedup.session_id.nunique(),
            view_dedup.item_id.nunique(),
        )

    processed = pd.DataFrame(
        {
            "SessionId": view_dedup.session_id.values,
            "ItemId": view_dedup.item_id.values,
            "Time": view_dedup.time.values,
        }
    )
    processed.to_csv(
        f"{path}/coveo_processed_view_full.tsv",
        sep="\t",
        index=False,
    )

    sbeg = processed.groupby("SessionId").Time.min()
    tsplit = (
        processed.Time.max()
    )  # 1545782400 * 1000  # this is the end of the last full day
    tday = 86400 * 1000
    test = processed[processed.SessionId.isin(sbeg[sbeg >= tsplit - tday].index)]
    train = processed[processed.Time < tsplit - tday]

    test.to_csv(
        f"{path}/coveo_processed_view_test.tsv",
        sep="\t",
        index=False,
    )

    session_length = train.groupby("SessionId").size()
    train = train[train.SessionId.isin(session_length[session_length > 1].index)]
    train.to_csv(
        f"{path}/coveo_processed_view_train_full.tsv",
        sep="\t",
        index=False,
    )

    train2 = train[train.Time < tsplit - tday * 2]
    test2 = train[train.SessionId.isin(sbeg[sbeg >= tsplit - tday * 2].index)]
    session_length2 = train2.groupby("SessionId").size()
    train2 = train2[train2.SessionId.isin(session_length2[session_length2 > 1].index)]
    train2.to_csv(
        f"{path}/coveo_processed_view_train_tr.tsv",
        sep="\t",
        index=False,
    )

    test2.to_csv(
        f"{path}/coveo_processed_view_train_valid.tsv",
        sep="\t",
        index=False,
    )

    names = []
    num_events = []
    num_sessions = []
    num_items = []
    num_days = []
    start_times = []
    end_times = []
    length_min = []
    length_max = []
    length_avg = []
    item_view_avg = []
    diff_min = []
    diff_max = []
    for curr_path in glob.glob(f"{path}/coveo_processed_view*"):
        data = pd.read_csv(curr_path, sep="\t", dtype={"ItemId": "str"})
        data.Time = data.Time
        names.append(curr_path.split("/")[-1])
        num_events.append(len(data))
        num_sessions.append(data.SessionId.nunique())
        num_items.append(data.ItemId.nunique())
        num_days.append((data.Time.max() - data.Time.min()) / tday)
        start_times.append(
            dt.datetime.utcfromtimestamp(data.Time.min() / 1000).strftime(
                "%Y-%m-%d %H:%M:%S.%f"
            )
        )
        end_times.append(
            dt.datetime.utcfromtimestamp(data.Time.max() / 1000).strftime(
                "%Y-%m-%d %H:%M:%S.%f"
            )
        )
        slength = data.groupby("SessionId").size()
        itemview = data.groupby("ItemId").size()
        sdiff = (
            data.groupby("SessionId").Time.max() - data.groupby("SessionId").Time.min()
        )
        sdiff = sdiff / 1000
        length_min.append(slength.min())
        length_max.append(slength.max())
        length_avg.append(slength.mean())
        item_view_avg.append(itemview.mean())
        diff_min.append(sdiff.min())
        diff_max.append(sdiff.max())
    stats = pd.DataFrame(
        {
            "Dataset": names,
            "NumEvents": num_events,
            "NumSessions": num_sessions,
            "NumItems": num_items,
            "NumDays": num_days,
            "StartTime": start_times,
            "EndTime": end_times,
            "AvgItemViews": item_view_avg,
            "MinSessionLength": length_min,
            "MaxSessionLength": length_max,
            "AvgSessionLength": length_avg,
            "MinSessionTime (sec)": diff_min,
            "MaxSessionTime (sec)": diff_max,
        }
    )
    print(stats)
    stats.to_csv(
        f"{path}/stats.tsv",
        sep="\t",
        index=False,
        float_format="%.4f",
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        help="Path of the directory of the dataset",
        required=True,
    )
    args = parser.parse_args()
    main(path=args.path)
