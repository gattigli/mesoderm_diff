# Mesoderm differentiation project
This folder contains the codes used for the quantification and analysis of immunofluorescence images and the pipeline used to analyse the single cell RNA sequencing data, created with the 10x technology. 

The pipeline for the analysis of the immunofluorescence images follows the order:
- _IF1_merge_datasets.py_
- _IF2_merge_all.py_
- _IF3_GMM.py_
- _IF4_threshold_loop.py_

The pipeline for the analysis of the scRNAseq analysis follows the order:
 - _scRNAseq_QC_merg_norm.ipynb_: here I performed quality control, then I merged and normalized the datasets 
 - _scRNAseq_leidenclustering.ipynb_: here I analysed the dataset, clustering the dataset, and checking the expression levels of differentiation markers and signaling proteins/receptors
 - The integration of my dataset with fully annotated embryo datasets was conducted in _scRNAseq_integration_pijuan_sala.ipynb_ (using the dataset in Pijuan-Sala et al. 2019) and _scRNAseq_integration_grosswendt.ipynb_ (using the dataset in Grosswendt et al. 2020).
