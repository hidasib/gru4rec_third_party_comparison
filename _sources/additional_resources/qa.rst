Presentation Q&A
==================================================================

Detailed answers to the questions we received through Slido after the presentation of this work at RecSys'23 on 20th September 2023 in Singapore.

----------------------------
Presentation (slides only)
----------------------------

.. raw:: html

    <iframe src="https://www.slideshare.net/slideshow/embed_code/key/5XWwL4pRmQE9n9?startSlide=1" width="597" height="486" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px;max-width: 100%;" allowfullscreen></iframe><div style="margin-bottom:5px"><strong><a href="https://www.slideshare.net/balazshidasi/the-effect-of-third-party-implementations-on-reproducibility" title="The Effect of Third Party Implementations on Reproducibility" target="_blank">The Effect of Third Party Implementations on Reproducibility</a></strong>


-------------------------
Q&A
-------------------------

**Q: How did you consolidate the errors of re-implementations?**

A: We looked at the code and identified differences to the original. These could fall into two categories: (1) something is missing (e.g. one of the 8 core features of the algorithm, or one of the hyperparameters governing some part of the original); (2) something is different to the original (e.g. does something else, or buggy). We refer to (2) as implementation errors. These then were categorized into the 5 categories you saw in the presentation. A comprehensive list of errors for each reimplementation is in the paper. We fixed errors, except for core errors - for which we would have needed to rewrite a significant portion of the code. We didn't add back any of the missing features/hyperparameters. We forked each of the third-party reimplementations and added fixes on various levels. Our improved versions can run on any of the levels we used in our experiments (out-of-the-box, inference fix, minor fix, major fix). You can find these versions of the reimplementations in the project’s repo as submodules.

.. raw:: html
    
    <hr>

**Q: How should we choose the implementation in using industry? Does the only thing we can do is compare all implementations?**

A: I would suggest using the official implementation, if it exists. An official version can still be buggy, but at least it can reproduce the results that were reported by the authors. 

If the official implementation is not fit for production use (e.g. too slow) or not available at all, then you might want to look for a third-party implementation or reimplement it on your own. The important thing here is that the reimplementation needs to be validated against the original. This is fairly straightforward if there is an official code, you just need to get very similar results on a few datasets using different hyperparameter settings. The reality now is that the task of this validation falls to whoever wants to use the algorithm. Hopefully this will change in the future. The ideal situation would be if public reimplementations would be validated by their authors (or an independent third-party) and the process and results of the validation would be available on their sites for those who are interested in using them.

Validation is much trickier if there is no official code available, because the only crutch you can lean on is the algorithm's description in the paper and the validation criteria are the results reported in the paper. However, there might be cases when these results are not reproducible (e.g. the author's private implementation had a bug, or the algorithm is not described in enough detail, or the datasets used are proprietary).

.. raw:: html
    
    <hr>

**Q: Has the situation with authors implementing their own algorithms improved over time?**

A: It is hard to say. The six reimplementations we examined in the paper and the other two we mentiones were published between 2017 and 2022 and we couldn't really see big differences between them regarding quality. However, during the conference we were approached by authors of other reimplementations that seemed to be better overall, even if not perfect. Moreover, the authors seemed willing (sometimes even enthusiastic) to learn about what their version is missing and improving their implementation. I really hope that our paper also inspired (past and future) authors of other algorithms and the authors of the six reimplementations we looked at to do the same and improve their work.

.. raw:: html
    
    <hr>

**Q: You mention that other people's work is very *flawed*. A strong claim. I'm very curious how the authors react when you approached them asking to fix their bugs?**

A: We hadn't approached any author directly yet, due to the requirements of the research project and due to the lack of time. So, in a sense, I'm also curious how they will react when they see our analysis. We were approached by two authors before the conference (one directly impacted by our analysis, and one indirectly impacted) and their reactions to our work were professional. I hope that the reaction from other authors will be positive as well, because we didn't just point out flaws in general, we also provided a comprehensive list for each reimplementation, as well as fixes for any, but the core errors. These are made available as part of the experimentation code of this project. (Of course, there is much to be done on top of this, we didn't add missing features and hyperparameters & didn't fix core errors.) 

During the conference, we were approached by other groups who had reimplementations on their own and they received the paper positively. They seemed willing (sometimes even enthusiastic) to learn about what their version is missing and improve their implementation. I really hope that our paper also inspired (past and future) authors of other algorithms and the authors of the six reimplementations we looked at to do the same and improve their work.

As for the use of the word "flawed". It might be a strong word, but we also consider it just to be a state that can temporarily apply to a work. Of course, everyone should aim to do their work to the best of their knowledge, but mistakes do happen. Since everybody can and does make mistakes, a work being flawed is not a big deal if it is corrected once the flaw is revealed & the effects of it are mitigated as much as possible. 

This work does NOT mean to be an attack on anyone's work and especially not on any individual. To ensure this, we checked as many reimplementations as was possible to avoid singling out a specific one and we are avoiding discussing certain aspects related to our findings. The goal of this work is to highlight this serious issue that has a significant negative impact on our research community and tthe reproducibility/validity of the research results in general.

.. raw:: html
    
    <hr>

**Q: How does your re-implementation compare against the original implementation? Did you find differences between them due to factors outside of your control?**

A: We tested our reimplementations against the original on five datasets under various settings. The results are generally in line with the original. The biggest relative difference I observed is less than 1%, which is less than what I observe between subsequent runs of the original code (and this latter is due to the non-deterministic order of operations on the GPU, as well as the lack of grouping the indexed gradients in the original). If the grouping of the indexed gradients is added to the original the largest observed relative difference in metrics becomes less than 0.5%. Due to discrepancies between online-offline evaluation, anything under 5% relative difference in Recall/MRR/NDCG can be considered to be on the same performance level (as these small uplifts rarely translate into any improvement when tested online). Therefore I think that this small deviation is acceptable.

Overall, there were two things outside of our control: (1) speed of the framework; (2) aggregating indexed gradients in PyTorch. 
(1) We couldn't make the reimplementations as quick as the original, because both PyTorch and TF pass the control back and forth between the python and the C++/CUDA code during the processing of a minibatch that adds an additional overhead. Theano compiles the computational graph so it has no such overhead. The public version of GRU4Rec uses IDs only, so in general, processing a minibatch is quite fast, thus the overhead of PyTorch and TF becomes significant. In theory, PyTorch2 would be able to compile the graph, but this compilation doesn't work with "sparse" embeddings, which is the usual way one uses embeddings (i.e. select a few indexes from many, update only those) and I couldn't work around this. In TF, we use `tf.function`, without that it is unbearably slow. While `tf.function`` seems to do many things, it doesn't seem to compile the graph into a monolithic C++/CUDA function.
(2) Aggregating indexed gradients before backpropagation is actually the correct way. PyTorch somewhat enforces this, while it is not in the original implementation (it didn't matter that much and needed a custom operator that I implemented much later). This accounts for a little difference, but nothing significant. I might add gradient aggregation to the original to eliminate the difference. But I must think this through from the perspective of reproducibility.

Other than these two, there were a few occasions where I couldn't use the built-in modules: GRU has many different implementations, the original GRU4Rec uses the one from the first GRU paper, but it is not the one implemented in PyTorch or TF. Also, for some reason, the Adagrad optimizers of both PyTorch and TF don't work with Nesterov's momentum, even though it can improve performance. Writing these modules is fairly straightforward but requires some knowledge on how GRU or optimizers work.
