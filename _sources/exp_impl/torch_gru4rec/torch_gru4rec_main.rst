Torch-GRU4Rec
==================================================================

* **Out-of-the-box:** 
   A single typo needed to be fixed, so the code is able to run.
* The small differences (e.g. missing momentum parameter) add up to a noticeable difference when Torch-GRU4Rec is compared to the matching features version.
* Sampling is performed after all item scores are computed, which slows down training. This bug is rooted so deep in the code that we did not fix it.

------------------------------------------------------------------
Rees46
------------------------------------------------------------------

.. tab-set::

   .. tab-item:: Metric
      :sync: key1

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Metrics
               :class: striped_table
               :file: /data_sources/results/rees46_torch_gru4rec_metrics_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metrics
               :class: striped_table
               :file: /data_sources/results/rees46_torch_gru4rec_metrics_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Metric Diff
      :sync: key2

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/rees46_torch_gru4rec_metrics_change_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/rees46_torch_gru4rec_metrics_change_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Hyperparameters
      :sync: key3

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/rees46_torch_gru4rec_hyperp_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/rees46_torch_gru4rec_hyperp_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Runtimes
      :sync: key4

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/rees46_torch_gru4rec_times_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/rees46_torch_gru4rec_times_cross-entropy.csv
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

            .. csv-table:: Metrics
               :class: striped_table
               :file: /data_sources/results/yoochoose_torch_gru4rec_metrics_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metrics
               :class: striped_table
               :file: /data_sources/results/yoochoose_torch_gru4rec_metrics_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Metric Diff
      :sync: key2

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/yoochoose_torch_gru4rec_metrics_change_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/yoochoose_torch_gru4rec_metrics_change_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Hyperparameters
      :sync: key3

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/yoochoose_torch_gru4rec_hyperp_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/yoochoose_torch_gru4rec_hyperp_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Runtimes
      :sync: key4

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/yoochoose_torch_gru4rec_times_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/yoochoose_torch_gru4rec_times_cross-entropy.csv
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

            .. csv-table:: Metrics
               :class: striped_table
               :file: /data_sources/results/coveo_torch_gru4rec_metrics_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metrics
               :class: striped_table
               :file: /data_sources/results/coveo_torch_gru4rec_metrics_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Metric Diff
      :sync: key2

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/coveo_torch_gru4rec_metrics_change_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/coveo_torch_gru4rec_metrics_change_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Hyperparameters
      :sync: key3

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/coveo_torch_gru4rec_hyperp_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/coveo_torch_gru4rec_hyperp_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Runtimes
      :sync: key4

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/coveo_torch_gru4rec_times_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/coveo_torch_gru4rec_times_cross-entropy.csv
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

            .. csv-table:: Metrics
               :class: striped_table
               :file: /data_sources/results/retailrocket_torch_gru4rec_metrics_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metrics
               :class: striped_table
               :file: /data_sources/results/retailrocket_torch_gru4rec_metrics_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Metric Diff
      :sync: key2

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/retailrocket_torch_gru4rec_metrics_change_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/retailrocket_torch_gru4rec_metrics_change_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Hyperparameters
      :sync: key3

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/retailrocket_torch_gru4rec_hyperp_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/retailrocket_torch_gru4rec_hyperp_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Runtimes
      :sync: key4

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/retailrocket_torch_gru4rec_times_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/retailrocket_torch_gru4rec_times_cross-entropy.csv
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

            .. csv-table:: Metrics
               :class: striped_table
               :file: /data_sources/results/diginetica_torch_gru4rec_metrics_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metrics
               :class: striped_table
               :file: /data_sources/results/diginetica_torch_gru4rec_metrics_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Metric Diff
      :sync: key2

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/diginetica_torch_gru4rec_metrics_change_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/diginetica_torch_gru4rec_metrics_change_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Hyperparameters
      :sync: key3

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/diginetica_torch_gru4rec_hyperp_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/diginetica_torch_gru4rec_hyperp_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Runtimes
      :sync: key4

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/diginetica_torch_gru4rec_times_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/diginetica_torch_gru4rec_times_cross-entropy.csv
               :header-rows: 1