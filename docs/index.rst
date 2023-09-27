GRU4Rec Third Party Implementations
==================================================================

The original **GRU4Rec** [2,3] algorithm was implemented in **Theano**.
Since then, support for Theano has been discontinued, and newer frameworks like PyTorch or TensorFlow have arisen.
**Convenience** and/or **standardization** alongside with other factors (e.g. the popularity of the algorithm) has led to the creation of **several third party implementations**.
Our experiments compare the original implementation with third party reimplementations (created in either PyTorch or TensorFlow), on multiple datasets [`Yoochoose/RSC15 <https://www.kaggle.com/datasets/chadgostopp/recsys-challenge-2015>`_, `Rees46 <https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store>`_, `Coveo <https://github.com/coveooss/shopper-intent-prediction-nature-2020>`_, `RetailRocket <https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset>`_, `Diginetica <https://competitions.codalab.org/competitions/11161#learn_the_details-data2>`_].
We found that **third party (unofficial) reimplementations** lack many of the distinguishing features of GRU4Rec and **contain serious implementation flaws** and thus their performance - both in terms of recommendation accuracy and training times - is suboptimal [1]. 

To support research in the field of sequential recommenders, **we released an official** `PyTorch <https://github.com/hidasib/GRU4Rec_PyTorch_Official>`_ **and** `TensorFlow <https://github.com/hidasib/GRU4Rec_Tensorflow_Official>`_ **implementation of GRU4Rec** available on GitHub. These implementations are bechmarked against the original Theano implementation to ensure correctness, but runtimes still differ due to the differences in frameworks. For further information, please visit the GitHub repositories and refer to the README files.

[1] Balázs Hidasi, Ádám Czapp: `The Effect of Third Party Implementations on Reproducibility <https://arxiv.org/abs/2307.14956>`_, RecSys 2023

[2] Balázs Hidasi, Alexandros Karatzoglou, Linas Baltrunas, Domonkos Tikk: `Session-based Recommendations with Recurrent Neural Networks <https://arxiv.org/abs/1511.06939>`_, ICLR 2016  

[3] Balázs Hidasi, Alexandros Karatzoglou: `Recurrent Neural Networks with Top-k Gains for Session-based Recommendations <https://arxiv.org/abs/1706.03847>`_, CIKM 2018

.. toctree::
   :caption: Experiment Setup
   :maxdepth: 1

   data_preproc/data_preproc_main
   hyperparams/hyperparams_main
   Source Code on GitHub <https://github.com/hidasib/gru4rec_third_party_comparison/tree/master>

.. toctree::
   :maxdepth: 2
   :caption: Experiment Results

   By Dataset <exp_data/exp_dataset>
   By Implementation <exp_impl/exp_implementations>

.. toctree::
   :caption: Additional resources
   :maxdepth: 2

   Research paper <additional_resources/paper>
   additional_resources/qa
   Official GRU4rec implementations <additional_resources/official_impl>
