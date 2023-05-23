Data Preprocessing
==================================================================

------------------------------------------------------------------
General steps
------------------------------------------------------------------

1. step
    Only view / click / detail events are kept, depending on the dataset.
    These events represent the user visiting an item's detail page, thus 
    they describe the sequences for the next-click prediction task.

2. step 
    Sessionisation of user histories.

3. step
    Keeping only the necessary data: session ID, item ID, timestamp

4. step
    Subsequent repeating item filtration.  If the user visits the 
    same item multiple times in succession, only the first occurrence is kept.

5. step
    The dataset is iteratively filtered for sessions shorter than 2 and items
    occurring less than 5 times until there is no change in the dataset.

6. step
    Time based train and test splits. The number of test days are defined for each dataset (*tday*, defined in seconds) yielding a split time *tsplit*. *tsplit* is calculated by substracting *tday* from the last timestamp of the dataset. We create a *train_full* and *test* dataset. Session starting after *tsplit* are assigned to *test*. Events with timestamps smaller than *tsplit* are assigned to *train_full*.

    .. dropdown:: Note
        :color: info
        :icon: info

        After this step *train_full* may contain sessions with only one event, these are discarded.

    This process is repeated for *train_full* yielding *train_tr* and *train_valid* 

------------------------------------------------------------------
Dataset specific steps
------------------------------------------------------------------

.. tab-set::

    .. tab-item:: Rees46

        1. step
            a) The October and November dataset is concatenated
            b) item ID and user ID is reindexed with integers to allow faster data sorting (the final dataset will contain the original IDs). 
            c) *view* events are used
        
        6. step
            - *tday* is 1 day (86400 s) for the Rees46

    .. tab-item:: Yoochoose

        1. step
            *clicks* and *test* files are concatenated

        2. step
            The sessions are precomputed, we use these.

        6. step
            *tday* is 1 for Yoochoose

    .. tab-item:: Coveo
        
        1. step
            a) *detail* events are used
        
        6. step
            *tday* is 1 for Coveo

    .. tab-item:: Diginetica

        1. step
            a) Timestamps are computed from the day of the first query and the elapsed time.

        6. step
            *tday* is 7 for Diginetica

    .. tab-item:: Retailrocket
        
        1. step
            a) *view* events are used

        6. step
            *tday* is 7 for Retailrocket
    
