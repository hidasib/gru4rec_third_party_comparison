KerasGRU4Rec
==================================================================

* **Out-of-the box:**
   The implementation as is.
* **Minor fix:**
   #. Hard-coded parameters: *hidden_size*, *dropout_p_hidden*, *learning_rate* now can be set.
   #. The default optimizer is changed to Adagrad.
* **Major fix:**
   #. Fixed incorrect resetting of hidden states (the same error that *GRU4REC-pytorch* has)
   #. Epochs don’t end now when the number of remaining sessions is not enough to fully fill the mini-batch.

------------------------------------------------------------------
Rees46
------------------------------------------------------------------

.. tab-set::

   .. tab-item:: Metric
      :sync: key1

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by KerasGRU4Rec

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metrics
               :class: striped_table
               :file: /data_sources/results/rees46_keras_gru4rec_metrics_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Metric Diff
      :sync: key2

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by KerasGRU4Rec

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/rees46_keras_gru4rec_metrics_change_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Hyperparameters
      :sync: key3

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by KerasGRU4Rec

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/rees46_keras_gru4rec_hyperp_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Runtimes
      :sync: key4

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by KerasGRU4Rec

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/rees46_keras_gru4rec_times_cross-entropy.csv
               :header-rows: 1
    
------------------------------------------------------------------
Yoochoose
------------------------------------------------------------------

.. tab-set::

   .. tab-item:: Metric
      :sync: key1

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by KerasGRU4Rec

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metrics
               :class: striped_table
               :file: /data_sources/results/yoochoose_keras_gru4rec_metrics_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Metric Diff
      :sync: key2

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by KerasGRU4Rec

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/yoochoose_keras_gru4rec_metrics_change_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Hyperparameters
      :sync: key3

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by KerasGRU4Rec

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/yoochoose_keras_gru4rec_hyperp_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Runtimes
      :sync: key4

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by KerasGRU4Rec

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/yoochoose_keras_gru4rec_times_cross-entropy.csv
               :header-rows: 1

------------------------------------------------------------------
Coveo
------------------------------------------------------------------

.. tab-set::

   .. tab-item:: Metric
      :sync: key1

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by KerasGRU4Rec

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metrics
               :class: striped_table
               :file: /data_sources/results/coveo_keras_gru4rec_metrics_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Metric Diff
      :sync: key2

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by KerasGRU4Rec

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/coveo_keras_gru4rec_metrics_change_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Hyperparameters
      :sync: key3

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by KerasGRU4Rec

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/coveo_keras_gru4rec_hyperp_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Runtimes
      :sync: key4

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by KerasGRU4Rec

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/coveo_keras_gru4rec_times_cross-entropy.csv
               :header-rows: 1

------------------------------------------------------------------
Retailrocket
------------------------------------------------------------------

.. tab-set::

   .. tab-item:: Metric
      :sync: key1

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by KerasGRU4Rec

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metrics
               :class: striped_table
               :file: /data_sources/results/retailrocket_keras_gru4rec_metrics_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Metric Diff
      :sync: key2

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by KerasGRU4Rec

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/retailrocket_keras_gru4rec_metrics_change_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Hyperparameters
      :sync: key3

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by KerasGRU4Rec

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/retailrocket_keras_gru4rec_hyperp_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Runtimes
      :sync: key4

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by KerasGRU4Rec

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/retailrocket_keras_gru4rec_times_cross-entropy.csv
               :header-rows: 1

------------------------------------------------------------------
Diginetica
------------------------------------------------------------------

.. tab-set::

   .. tab-item:: Metric
      :sync: key1

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by KerasGRU4Rec

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metrics
               :class: striped_table
               :file: /data_sources/results/diginetica_keras_gru4rec_metrics_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Metric Diff
      :sync: key2

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by KerasGRU4Rec

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/diginetica_keras_gru4rec_metrics_change_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Hyperparameters
      :sync: key3

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by KerasGRU4Rec

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/diginetica_keras_gru4rec_hyperp_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Runtimes
      :sync: key4

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by KerasGRU4Rec

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/diginetica_keras_gru4rec_times_cross-entropy.csv
               :header-rows: 1