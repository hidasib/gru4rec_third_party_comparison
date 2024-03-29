setups = {
    "coveo": {
        "params_bprmax": {
            "loss": "bpr-max",
            "optim": "adagrad",
            "constrained_embedding": "True",
            "embedding": 0,
            "final_act": "elu-1",
            "hidden_act": "tanh",
            "layers": 512,
            "batch_size": 144,
            "dropout_p_embed": 0.35,
            "dropout_p_hidden": 0.0,
            "learning_rate": 0.05,
            "momentum": 0.4,
            "n_sample": 2048,
            "sample_alpha": 0.2,
            "bpreg": 1.85,
            "logq": 0.0,
            "n_sample" : 2048,
        },
        "params_xe": {
            "loss": "cross-entropy",
            "optim": "adagrad",
            "constrained_embedding": "True",
            "embedding": 0,
            "final_act": "softmax",
            "hidden_act": "tanh",
            "layers": 512,
            "batch_size": 32,
            "dropout_p_embed": 0.4,
            "dropout_p_hidden": 0.15,
            "learning_rate": 0.03,
            "momentum": 0.0,
            "n_sample": 2048,
            "sample_alpha": 0.0,
            "bpreg": 0.0,
            "logq": 1.0,
            "n_sample" : 2048,
        },
    },
    "diginetica": {
        "params_bprmax": {
            "loss": "bpr-max",
            "optim": "adagrad",
            "constrained_embedding": "True",
            "embedding": 0,
            "final_act": "elu-1",
            "hidden_act": "tanh",
            "layers": 512,
            "batch_size": 128,
            "dropout_p_embed": 0.5,
            "dropout_p_hidden": 0.3,
            "learning_rate": 0.05,
            "momentum": 0.15,
            "n_sample": 2048,
            "sample_alpha": 0.3,
            "bpreg": 0.9,
            "logq": 0.0,
            "n_sample" : 2048,
        },
        "params_xe": {
            "loss": "cross-entropy",
            "optim": "adagrad",
            "constrained_embedding": "True",
            "embedding": 0,
            "final_act": "softmax",
            "hidden_act": "tanh",
            "layers": 192,
            "batch_size": 128,
            "dropout_p_embed": 0.45,
            "dropout_p_hidden": 0.15,
            "learning_rate": 0.1,
            "momentum": 0.0,
            "n_sample": 2048,
            "sample_alpha": 0.0,
            "bpreg": 0.0,
            "logq": 1.0,
            "n_sample" : 2048,
        },
    },
    "retailrocket": {
        "params_bprmax": {
            "loss": "bpr-max",
            "optim": "adagrad",
            "constrained_embedding": "True",
            "embedding": 0,
            "final_act": "elu-0.5",
            "hidden_act": "tanh",
            "layers": 224,
            "batch_size": 80,
            "dropout_p_embed": 0.5,
            "dropout_p_hidden": 0.05,
            "learning_rate": 0.05,
            "momentum": 0.4,
            "n_sample": 2048,
            "sample_alpha": 0.4,
            "bpreg": 1.95,
            "logq": 0.0,
            "n_sample" : 2048,
        },
        "params_xe": {
            "loss": "cross-entropy",
            "optim": "adagrad",
            "constrained_embedding": "True",
            "embedding": 0,
            "final_act": "softmax",
            "hidden_act": "tanh",
            "layers": 192,
            "batch_size": 240,
            "dropout_p_embed": 0.5,
            "dropout_p_hidden": 0.05,
            "learning_rate": 0.085,
            "momentum": 0.3,
            "n_sample": 2048,
            "sample_alpha": 0.3,
            "bpreg": 0.0,
            "logq": 1.0,
            "n_sample" : 2048,
        },
    },
    "yoochoose": {
        "params_bprmax": {
            "loss": "bpr-max",
            "optim": "adagrad",
            "constrained_embedding": "True",
            "embedding": 0,
            "final_act": "linear",
            "hidden_act": "tanh",
            "layers": 448,
            "batch_size": 48,
            "dropout_p_embed": 0.25,
            "dropout_p_hidden": 0.0,
            "learning_rate": 0.075,
            "momentum": 0.1,
            "n_sample": 2048,
            "sample_alpha": 0.2,
            "bpreg": 0.5,
            "logq": 0.0,
            "n_sample" : 2048,
        },
        "params_xe": {
            "loss": "cross-entropy",
            "optim": "adagrad",
            "constrained_embedding": "True",
            "embedding": 0,
            "final_act": "softmax",
            "hidden_act": "tanh",
            "layers": 480,
            "batch_size": 48,
            "dropout_p_embed": 0.0,
            "dropout_p_hidden": 0.2,
            "learning_rate": 0.07,
            "momentum": 0.0,
            "n_sample": 2048,
            "sample_alpha": 0.2,
            "bpreg": 0.0,
            "logq": 1.0,
            "n_sample" : 2048,
        },
    },
    "rees46": {
        "params_bprmax": {
            "loss": "bpr-max",
            "optim": "adagrad",
            "constrained_embedding": "True",
            "embedding": 0,
            "final_act": "elu-0.5",
            "hidden_act": "tanh",
            "layers": 512,
            "batch_size": 32,
            "dropout_p_embed": 0.1,
            "dropout_p_hidden": 0.0,
            "learning_rate": 0.03,
            "momentum": 0.55,
            "n_sample": 2048,
            "sample_alpha": 0.2,
            "bpreg": 0.75,
            "logq": 0.0,
            "n_sample" : 2048,
        },
        "params_xe": {
            "loss": "cross-entropy",
            "optim": "adagrad",
            "constrained_embedding": "True",
            "embedding": 0,
            "final_act": "softmax",
            "hidden_act": "tanh",
            "layers": 512,
            "batch_size": 240,
            "dropout_p_embed": 0.45,
            "dropout_p_hidden": 0.0,
            "learning_rate": 0.065,
            "momentum": 0.0,
            "n_sample": 2048,
            "sample_alpha": 0.5,
            "bpreg": 0.0,
            "logq": 1.0,
            "n_sample" : 2048,
        },
    },
}
