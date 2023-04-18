# README
## Create
- forkolni a report
- .git/config ban a remote urlt átírni
- git fetch az adott mappában
- lokál és origin master ugyan ott van e még
- és utána commit
## Usage
- clone the rope
- git submodule init
- git submodule update
## Environments
- Setup
    - install anaconda: https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation (either Anaconda or Miniconda is ok)
    - Pytorch
        - The packages for the pytorch versions can be found in *gru4rec_conda_pytorch_env.yaml*
        - To create then environment run:
            - *conda env create -f gru4rec_conda_pytorch_env.yml*
    - Tesnorflow
        - The packages for the pytorch versions can be found in *gru4rec_conda_tensorflow_env.yaml*
            - To create then environment run:
                - *conda env create -f gru4rec_conda_tensorflow_env.yml*
    - Now you can *activate* the environments by running either
        - *conda activate gru4rec_tensorflow*
        - *conda activate gru4rec_pytorch*
    - Or *deactivate* them
        - *conda deactivate*
    - When using the notebooks, select the correct python interpreter, which is located in the directory of the correct conda environment

## Download link to the datasets
- coveo: filehttps://www.coveo.com/en/ailabs/shopper-intent-prediction-from-clickstream-e-commerce-data-with-minimal-browsing-information