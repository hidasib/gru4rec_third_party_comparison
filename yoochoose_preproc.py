import numpy as np
import pandas as pd
import gc
import datetime as dt
import glob
import argparse
import os


def main(path: str):
    data = pd.concat(
        [
            pd.read_csv(
                os.path.join(path, "yoochoose-clicks.dat"),
                header=None,
                parse_dates=[1],
                usecols=[0, 1, 2],
            ),
            pd.read_csv(
                os.path.join(path, "yoochoose-test.dat"),
                header=None,
                parse_dates=[1],
                usecols=[0, 1, 2],
            ),
        ]
    )
    data.columns = ["SessionId", "Time", "ItemId"]
    data["Time"] = data.Time.view("int") // 10**9
    
    data.sort_values(["SessionId", "Time", "ItemId"], inplace=True)
    mask = np.hstack(
        [
            False,
            (data.SessionId.values[1:] == data.SessionId.values[:-1])
            & (data.ItemId.values[1:] == data.ItemId.values[:-1]),
        ]
    )
    data.drop(data[mask].index, inplace=True)
    
    pl = -1
    print(
        len(data),
        data.SessionId.nunique(),
        data.ItemId.nunique(),
    )
    while len(data) != pl:
        pl = len(data)
        slength = data.groupby("SessionId").size()
        data.drop(
            data[data.SessionId.isin(slength[slength == 1].index)].index,
            inplace=True,
        )
        print(
            len(data),
            data.SessionId.nunique(),
            data.ItemId.nunique(),
        )
        isupp = data.groupby("ItemId").size()
        data.drop(data[data.ItemId.isin(isupp[isupp < 5].index)].index, inplace=True)
        print(
            len(data),
            data.SessionId.nunique(),
            data.ItemId.nunique(),
        )

    processed = pd.DataFrame(
        {
            "SessionId": data.SessionId.values,
            "ItemId": data.ItemId.values,
            "Time": data.Time.values,
        }
    )
    processed.to_csv(
        f"{path}/yoochoose_processed_view_full.tsv",
        sep="\t",
        index=False,
    )

    sbeg = processed.groupby("SessionId").Time.min()
    tsplit = processed.Time.max()
    print(tsplit)
    tday = 86400
    test = processed[processed.SessionId.isin(sbeg[sbeg >= tsplit - tday].index)]
    train = processed[processed.Time < tsplit - tday]
    test.to_csv(
        f"{path}/yoochoose_processed_view_test.tsv",
        sep="\t",
        index=False,
    )
    session_length = train.groupby("SessionId").size()
    train = train[train.SessionId.isin(session_length[session_length > 1].index)]
    train.to_csv(
        f"{path}/yoochoose_processed_view_train_full.tsv",
        sep="\t",
        index=False,
    )

    train2 = train[train.Time < tsplit - tday * 2]
    test2 = train[train.SessionId.isin(sbeg[sbeg >= tsplit - tday * 2].index)]
    session_length2 = train2.groupby("SessionId").size()
    train2 = train2[train2.SessionId.isin(session_length2[session_length2 > 1].index)]
    train2.to_csv(
        f"{path}/yoochoose_processed_view_train_tr.tsv",
        sep="\t",
        index=False,
    )
    test2.to_csv(
        f"{path}/yoochoose_processed_view_train_valid.tsv",
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
    for curr_path in glob.glob(f"{path}/yoochoose_processed_view*"):
        data = pd.read_csv(curr_path, sep="\t", dtype={"ItemId": "str"})
        data.Time = data.Time
        names.append(curr_path.split("/")[-1])
        num_events.append(len(data))
        num_sessions.append(data.SessionId.nunique())
        num_items.append(data.ItemId.nunique())
        num_days.append((data.Time.max() - data.Time.min()) / tday)
        start_times.append(
            dt.datetime.utcfromtimestamp(data.Time.min()).strftime(
                "%Y-%m-%d %H:%M:%S.%f"
            )
        )
        end_times.append(
            dt.datetime.utcfromtimestamp(data.Time.max()).strftime(
                "%Y-%m-%d %H:%M:%S.%f"
            )
        )
        slength = data.groupby("SessionId").size()
        itemview = data.groupby("ItemId").size()
        sdiff = (
            data.groupby("SessionId").Time.max() - data.groupby("SessionId").Time.min()
        )
        sdiff = sdiff
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
