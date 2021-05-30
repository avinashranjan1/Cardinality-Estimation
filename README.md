# Cardinality-Estimation

 <div align=”center”>
⋅⋅* Set-up a local environment with Postgres and the IMDB dataset.
  
  

. Find the min and max of all columns an create a dictionary with it.

. For those columns with a low entropy, store all possible values (as we treat them like a category).

. Postgres analysis of errors for suffix and prefix matches on Job queries.

. JOB generate synthetic queries with prefix and suffix predicates.

. Train and test MSCN on JOB and JCC-H.

. Generate fine-tuning datasets from the given benchmarks, for BERT.

. Adapt the transformer next sentence prediction model to work on your task of prefix + suffix matches. 

. Train the model on these matches (collect the results of the experiment for the Thesis), also maybe try different transformer and pick the best at the end.

. Figure out and extract the prefix embedding from the model: this should become your input for MSCN. 

. Repeat the MSCN experiments with the new input. 

. For all results figure out good visualizations that help us understand the behavior for sub-populations of interest. 

. Extra: Figure out for BERT and MSCN if we could use some interpretability tools to explain our results for us. 

. Research on text encoding with a focus on prefix and suffix matches, research on how learned models deal with these matches.   
</div>
