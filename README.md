# README
​
## Usage
​
To get started with this repository, follow the instructions below:
​
1. Clone the repository.
​
2. In the root folder of the repository, run the following command to initialize the submodules:
    ```shell
    git submodule update --init --recursive
    ```

## Environments

### Third Party Implementations

Before running the code in this repository, you need to set up the necessary environments.

1. Install Anaconda by following the instructions [here](https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation). You can choose either Anaconda or Miniconda.

2. For GRU4REC-pytorch and Torch-GRU4Rec, you need to install PyTorch. The required packages for the PyTorch versions can be found in `gru4rec_conda_pytorch_env.yaml`. To create the environment, run the following command:
    ```shell
    conda env create -f gru4rec_conda_pytorch_env.yaml
    ```
3. For GRU4Rec_TensorFlow and KerasGRU4Rec, you need to install TensorFlow. The required packages for the TensorFlow versions can be found in `gru4rec_conda_tensorflow_env.yaml`. To create the environment, run the following command:
    ```shell
    conda env create -f gru4rec_conda_tensorflow_env.yaml
    ```
4. For recpack, you need to install PyTorch. The required packages for this version can be found in `gru4rec_conda_recpack_env.yaml`. To create the environment, run the following command:
    ```shell
    conda env create -f gru4rec_conda_recpack_env.yaml
    ```
5. Once the environments are created, you can activate them by running one of the following commands:
    - For TensorFlow environment:
        ```shell
        conda activate gru4rec_tensorflow
        ```
    - For PyTorch environment:
        ```shell
        conda activate gru4rec_pytorch
        ```
    - For recpack environment:
        ```shell
        conda activate gru4rec_recpack
        ```
6. To deactivate the environment, run the following command:
    ```shell
    conda deactivate
    ```

### Original Implementation
​
Please refer to the [requirements](https://github.com/hidasib/GRU4Rec/blob/87971fe397c4b44e6c7c2c0c7333cbe6e08a545d/README.md#requirements) mentioned in the repository for more details.
​
## Examples
​
This repository provides an example Jupyter Notebook for each model, along with descriptions on how to run the experiments. Refer to the notebooks for detailed instructions.
​
## Download link to the datasets
​
- Yoochoose:
    - [Official Website](https://2015.recsyschallenge.com/)
    - [Kaggle Dataset](https://www.kaggle.com/datasets/chadgostopp/recsys-challenge-2015)
​
- Rees46:
    - [Official Website](https://rees46.com/en/open-cdp)
    - [Kaggle Dataset](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)
​
- Coveo:
    - [Official Download Link](https://www.coveo.com/en/ailabs/shopper-intent-prediction-from-clickstream-e-commerce-data-with-minimal-browsing-information)
​
- Diginetica:
    - [Official Download Link](https://competitions.codalab.org/competitions/11161#learn_the_details-data2)
​
- Retailrocket:
    - [Kaggle Dataset](https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset)