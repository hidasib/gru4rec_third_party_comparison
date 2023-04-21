# README
## Usage
- Clone the rope
- Use the following commands in the root folder of the repo
    - *git submodule init*
    - *git submodule update --init*
## Environments
- Setup for the third party implementation
    - install anaconda: https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation (either Anaconda or Miniconda is ok)
    - Pytorch for GRU4REC-pytorch and Torch-GRU4Rec
        - The packages for the pytorch versions can be found in *gru4rec_conda_pytorch_env.yaml*
        - To create then environment run:
            - *conda env create -f gru4rec_conda_pytorch_env.yaml*
    - Tesnorflow for GRU4Rec_TensorFlow and KerasGRU4Rec
        - The packages for the pytorch versions can be found in *gru4rec_conda_tensorflow_env.yaml*
            - To create then environment run:
                - *conda env create -f gru4rec_conda_tensorflow_env.yaml*
    - Pytorch for recpack
        - The packages for this versions can be found in *gru4rec_conda_recpack_env.yaml*
            - To create then environment run:
                - *conda env create -f gru4rec_conda_recpack_env.yaml*
    - Now you can *activate* the environments by running either
        - *conda activate gru4rec_tensorflow*
        - *conda activate gru4rec_pytorch*
        - *conda activate gru4rec_recpack*
    - Or *deactivate* them
        - *conda deactivate*
- Requirements for the original implementation
    - https://github.com/hidasib/GRU4Rec/blob/87971fe397c4b44e6c7c2c0c7333cbe6e08a545d/README.md#requirements
- When using the notebooks, select the correct python interpreter, which is located in the directory of the correct conda environment, or in the virtual env for the original version (Theano)

## Download link to the datasets
- yoochoose:
    - https://2015.recsyschallenge.com/
    - https://www.kaggle.com/datasets/chadgostopp/recsys-challenge-2015
- rees: 
    - https://rees46.com/en/open-cdp
    - https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store
- coveo: 
    - https://www.coveo.com/en/ailabs/shopper-intent-prediction-from-clickstream-e-commerce-data-with-minimal-browsing-information
- diginetica: 
    - https://competitions.codalab.org/competitions/11161#learn_the_details-data2
- retailrocket: 
    - https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset