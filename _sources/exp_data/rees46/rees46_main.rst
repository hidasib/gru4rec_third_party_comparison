Rees46
==================================================================
The dataset contains 8 months of user behavior data *view*, *cart* and *purchase* events from a multicategory e-commerce website between October 2019 and April 2020. We only use the first two months of the available data. This is similar to how real-life recommenders are usually trained only on the most recent 0.5–2 months to avoid concept drift, if the traffic is large enough. We only use view events for next item prediction. The dataset does come with precomputed sessions, but it is unclear how user histories are split into sessions. E.g. a few sessions have events from multiple users, and the time gap between subsequent events within a session can be arbitrarily long. Therefore, sessions were recomputed from the user histories using the standard 1 hour session gap threshold.

.. raw:: html

   <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>


.. tab-set::

      .. tab-item:: Recall\@20

         .. tab-set::

            .. tab-item:: BPR-Max
               :sync: key_sub_1

               .. raw:: html

                  <div class=chart-container>
                     <canvas class="bar-chart" id="bprmax_Recall@20"></canvas>
                  </div>

            .. tab-item:: Cross-Entropy
               :sync: key_sub_2

               .. raw:: html

                  <div class=chart-container>
                     <canvas class="bar-chart" id="xe_Recall@20"></canvas>
                  </div>

      .. tab-item:: MRR\@20

         .. tab-set::

            .. tab-item:: BPR-Max
               :sync: key_sub_1

               .. raw:: html

                  <div class=chart-container>
                     <canvas class="bar-chart" id="bprmax_MRR@20"></canvas>
                  </div>

            .. tab-item:: Cross-Entropy
               :sync: key_sub_2

               .. raw:: html

                  <div class=chart-container>
                     <canvas class="bar-chart" id="xe_MRR@20"></canvas>
                  </div>


------------------------------------------------------------------
GRU4REC-pytorch
------------------------------------------------------------------

.. tab-set::

   .. tab-item:: Metric
      :sync: key1

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Metrics
               :class: striped_table, bprmax
               :file: /data_sources/results/rees46_gru4rec_pytorch_metrics_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metrics
               :class: striped_table, xe
               :file: /data_sources/results/rees46_gru4rec_pytorch_metrics_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Metric Diff
      :sync: key2

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/rees46_gru4rec_pytorch_metrics_change_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/rees46_gru4rec_pytorch_metrics_change_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Hyperparameters
      :sync: key3

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/rees46_gru4rec_pytorch_hyperp_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/rees46_gru4rec_pytorch_hyperp_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Runtimes
      :sync: key4

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/rees46_gru4rec_pytorch_times_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/rees46_gru4rec_pytorch_times_cross-entropy.csv
               :header-rows: 1

------------------------------------------------------------------
Torch-GRU4Rec
------------------------------------------------------------------

.. tab-set::

   .. tab-item:: Metric
      :sync: key1

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Metrics
               :class: striped_table, bprmax
               :file: /data_sources/results/rees46_torch_gru4rec_metrics_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metrics
               :class: striped_table, xe
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
Recpack
------------------------------------------------------------------

.. tab-set::

   .. tab-item:: Metric
      :sync: key1

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Metrics
               :class: striped_table, bprmax
               :file: /data_sources/results/rees46_recpack_metrics_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metrics
               :class: striped_table, xe
               :file: /data_sources/results/rees46_recpack_metrics_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Metric Diff
      :sync: key2

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/rees46_recpack_metrics_change_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/rees46_recpack_metrics_change_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Hyperparameters
      :sync: key3

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/rees46_recpack_hyperp_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/rees46_recpack_hyperp_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Runtimes
      :sync: key4

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/rees46_recpack_times_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/rees46_recpack_times_cross-entropy.csv
               :header-rows: 1

------------------------------------------------------------------
GRU4Rec_Tensorflow
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
               :class: striped_table, xe
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
KerasGRU4Rec
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
               :class: striped_table, xe
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