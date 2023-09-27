GRU4Rec_Tensorflow
==================================================================

* **Out-of-the-box:**
   The code is able to run, however it is not prepared for unknown test items. The dropout parameter was fixed to regain its original meaning as it was used as keep probability instead of drop probability.
* **Minor fix:**
   #. Lowered the large initial accumulator value close to zero as it prevented sufficient convergence.
   #. The exponential learning rate decay is discarded as it is not part of the original.
   #. Now the hard-coded batch_size parameter can be changed.

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
               BPR-Max is not supported by GRU4Rec_Tensorflow

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metrics
               :class: striped_table
               :file: /data_sources/results/rees46_gru4rec_tensorflow_metrics_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Metric Diff
      :sync: key2

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by GRU4Rec_Tensorflow

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/rees46_gru4rec_tensorflow_metrics_change_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Hyperparameters
      :sync: key3

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by GRU4Rec_Tensorflow

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/rees46_gru4rec_tensorflow_hyperp_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Runtimes
      :sync: key4

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by GRU4Rec_Tensorflow

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/rees46_gru4rec_tensorflow_times_cross-entropy.csv
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
               BPR-Max is not supported by GRU4Rec_Tensorflow

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metrics
               :class: striped_table
               :file: /data_sources/results/yoochoose_gru4rec_tensorflow_metrics_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Metric Diff
      :sync: key2

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by GRU4Rec_Tensorflow

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/yoochoose_gru4rec_tensorflow_metrics_change_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Hyperparameters
      :sync: key3

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by GRU4Rec_Tensorflow

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/yoochoose_gru4rec_tensorflow_hyperp_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Runtimes
      :sync: key4

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by GRU4Rec_Tensorflow

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/yoochoose_gru4rec_tensorflow_times_cross-entropy.csv
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
               BPR-Max is not supported by GRU4Rec_Tensorflow

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metrics
               :class: striped_table
               :file: /data_sources/results/coveo_gru4rec_tensorflow_metrics_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Metric Diff
      :sync: key2

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by GRU4Rec_Tensorflow

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/coveo_gru4rec_tensorflow_metrics_change_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Hyperparameters
      :sync: key3

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by GRU4Rec_Tensorflow

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/coveo_gru4rec_tensorflow_hyperp_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Runtimes
      :sync: key4

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by GRU4Rec_Tensorflow

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/coveo_gru4rec_tensorflow_times_cross-entropy.csv
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
               BPR-Max is not supported by GRU4Rec_Tensorflow

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metrics
               :class: striped_table
               :file: /data_sources/results/retailrocket_gru4rec_tensorflow_metrics_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Metric Diff
      :sync: key2

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by GRU4Rec_Tensorflow

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/retailrocket_gru4rec_tensorflow_metrics_change_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Hyperparameters
      :sync: key3

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by GRU4Rec_Tensorflow

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/retailrocket_gru4rec_tensorflow_hyperp_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Runtimes
      :sync: key4

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by GRU4Rec_Tensorflow

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/retailrocket_gru4rec_tensorflow_times_cross-entropy.csv
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
               BPR-Max is not supported by GRU4Rec_Tensorflow

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metrics
               :class: striped_table
               :file: /data_sources/results/diginetica_gru4rec_tensorflow_metrics_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Metric Diff
      :sync: key2

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by GRU4Rec_Tensorflow

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/diginetica_gru4rec_tensorflow_metrics_change_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Hyperparameters
      :sync: key3

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by GRU4Rec_Tensorflow

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/diginetica_gru4rec_tensorflow_hyperp_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Runtimes
      :sync: key4

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. note::
               BPR-Max is not supported by GRU4Rec_Tensorflow

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/diginetica_gru4rec_tensorflow_times_cross-entropy.csv
               :header-rows: 1