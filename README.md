# Mesoderm differentiation project
This folder contains the codes used for the quantification and analysis of immunofluorescence images and the single cell RNA sequencing. 

IF pipeline follows the order:
- IF1_merge_datasets.py
- IF2_merge_all.py
- IF3_GMM.py
- IF4_threshold_loop.py

For the scRNAseq analysis, I performed quality control, merged and normalized the datasets in 'scRNAseq_QC_merg_norm.ipynb'. Analysis was conducted in _scRNAseq_leidenclustering.ipynb_
