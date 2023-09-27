Yoochoose
==================================================================
This dataset contains user sessions from an unnamed e-commerce site. The data is already split into proper sessions and each session consists of one or more click events and might have purchase event(s) associated with it. As we are focusing on the next item prediction task within sessions, we only use the click events. The dataset was originally released for RecSys Challenge 2015 and has been used for evaluating sessionbased recommenders since then.

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
               :file: /data_sources/results/yoochoose_gru4rec_pytorch_metrics_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metrics
               :class: striped_table, xe
               :file: /data_sources/results/yoochoose_gru4rec_pytorch_metrics_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Metric Diff
      :sync: key2

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/yoochoose_gru4rec_pytorch_metrics_change_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/yoochoose_gru4rec_pytorch_metrics_change_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Hyperparameters
      :sync: key3

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/yoochoose_gru4rec_pytorch_hyperp_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/yoochoose_gru4rec_pytorch_hyperp_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Runtimes
      :sync: key4

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/yoochoose_gru4rec_pytorch_times_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/yoochoose_gru4rec_pytorch_times_cross-entropy.csv
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
               :file: /data_sources/results/yoochoose_torch_gru4rec_metrics_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metrics
               :class: striped_table, xe
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
               :file: /data_sources/results/yoochoose_recpack_metrics_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metrics
               :class: striped_table, xe
               :file: /data_sources/results/yoochoose_recpack_metrics_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Metric Diff
      :sync: key2

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/yoochoose_recpack_metrics_change_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Metric difference compared to the "Best params" version with the corresponding loss
               :class: striped_table
               :file: /data_sources/results/yoochoose_recpack_metrics_change_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Hyperparameters
      :sync: key3

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/yoochoose_recpack_hyperp_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Hyperparameters used in the experiment
               :class: striped_table
               :file: /data_sources/results/yoochoose_recpack_hyperp_cross-entropy.csv
               :header-rows: 1

   .. tab-item:: Runtimes
      :sync: key4

      .. tab-set::

         .. tab-item:: BPR-Max
            :sync: key_sub_1

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/yoochoose_recpack_times_bpr-max.csv
               :header-rows: 1

         .. tab-item:: Cross-Entropy
            :sync: key_sub_2

            .. csv-table:: Runtime metrics
               :class: striped_table
               :file: /data_sources/results/yoochoose_recpack_times_cross-entropy.csv
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