Hyperparameters
==================================================================

The hyperparameters were tuned for 3 different setups for BPR-Max and Cross-Entropy respectively. We select the best performing setup with the best hyperparameters (1-1 for both BPR-Max and Cross-Entropy), and use it in our experiments.

------------------------------------------------------------------
Fixed Hyperparameters
------------------------------------------------------------------

These setups are defined by setting the *constrained_embedding* and *embedding* parameters to one of the following combinations:

.. csv-table:: Combinations
    :class: striped_table
    :file: /data_sources/hyperparams/hyperparams_setups.csv
    :header-rows: 1

And by fixing the following hyperparameters:

.. tab-set::

    .. tab-item:: BPR-Max
        :sync: key_1

        .. csv-table:: Fixed hyperparameters
            :class: striped_table
            :file: /data_sources/hyperparams/hyperparams_fixed_bprmax.csv
            :header-rows: 1

    .. tab-item:: Cross-Entropy
        :sync: key_2

        .. csv-table:: Fixed hyperparameters
            :class: striped_table
            :file: /data_sources/hyperparams/hyperparams_fixed_xe.csv
            :header-rows: 1

------------------------------------------------------------------
Optimized Hyperparameters
------------------------------------------------------------------

For each setup the following hyperparameters are optimized:

.. tab-set::

    .. tab-item:: BPR-Max
        :sync: key_1

        .. csv-table:: Optimized hyperparameters
            :class: striped_table
            :file: /data_sources/hyperparams/hyperparams_bprmax.csv
            :header-rows: 1

    .. tab-item:: Cross-Entropy
        :sync: key_2

        .. csv-table:: Optimized hyperparameters
            :class: striped_table
            :file: /data_sources/hyperparams/hyperparams_cross_entropy.csv
            :header-rows: 1