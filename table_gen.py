import numpy as np
import pandas as pd
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', type=str, help="path to the full csv containing results, hyperparams, model names")
    args = parser.parse_args()

    data = pd.read_csv(args.file_path, sep=',', header=0, na_values=[''], keep_default_na=False) #later handle N/A as nan as well, just easier to do it this way, if we want to display different values for N/A, and no percent for gru4rec
    print(data.head(n=5))
    
    dataset_names = ["Rees46", "Yoochoose", "Diginetica", "Retailrocket", "Coveo"]
    model_names = {"GRU4Rec Official": "gru4rec_official", "GRU4REC-pytorch": "gru4rec_pytorch", "Torch-GRU4Rec": "torch_gru4rec", "Recpack": "recpack", "GRU4Rec_Tensorflow": "gru4rec_tensorflow", "KerasGRU4Rec": "keras_gru4rec"}
    dataset_cols = {
        "metrics":['Implementation', 'Variant', 'loss', 'n_sample' , 'Recall@1', 'MRR@1', 'Recall@5', 'MRR@5', 'Recall@10', 'MRR@10', 'Recall@20', 'MRR@20'],
        "metrics_change": ['Implementation', 'Variant', 'loss', 'n_sample', 'Recall@1 Diff', 'MRR@1 Diff', 'Recall@5 Diff', 'MRR@5 Diff', 'Recall@10 Diff', 'MRR@10 Diff', 'Recall@20 Diff', 'MRR@20 Diff'],
        "hyperp": ['Implementation', 'Variant', 'loss', 'optim', 'constrained_embedding', 'embedding', 'final_act', 'layers', 'batch_size', 'dropout_p_embed', 'dropout_p_hidden', 'learning_rate', 'momentum', 'n_sample', 'sample_alpha', 'bpreg', 'logq']}
    new_headers = {} #TODO: if we want to ranem the columns use this

    for ds_name in dataset_names:
        for model_name, model_values in model_names.items():
            if model_name == "GRU4Rec Official": 
                continue
            chunk = data[data.Dataset == ds_name].copy()
            chunk1 = chunk[(chunk.Implementation == "GRU4Rec Official") & (chunk.Variant.str.contains(model_name) | chunk.Variant.str.contains("Best params"))]
            chunk2 = chunk[chunk.Implementation == model_name]
            chunk1 = chunk1[chunk1.loss.isin(chunk2.loss.unique())]
            chunk = pd.concat([chunk1, chunk2])
            chunk = pd.concat([chunk[chunk.loss == "bpr-max"], chunk[chunk.loss == "cross-entropy"]])
            if len(chunk) == 0:
                continue
            for sub_ds_name, cols in dataset_cols.items():
                chunk_part = chunk[cols]
                for l in ["bpr-max", "cross-entropy"]:
                    subchunk = chunk_part[chunk_part.loss == l]
                    if len(subchunk) == 0:
                        continue
                    new_fn = f"{ds_name.lower()}_{model_values}_{sub_ds_name}_{l}.csv"
                    index = False
                    if sub_ds_name == "hyperp":
                        subchunk.set_index("Implementation", drop=True, inplace=True)
                        subchunk.index.rename("Parameters", inplace=True)
                        subchunk = subchunk.T
                        index = True
                    subchunk.to_csv(os.path.join("docs", "data_sources", new_fn), index=index)
