# Mesoderm differentiation project
This folder contains the codes used for the quantification and analysis of immunofluorescence images and the single cell RNA sequencing. 

IF pipeline follows the order:
- _IF1_merge_datasets.py_
- _IF2_merge_all.py_
- _IF3_GMM.py_
- _IF4_threshold_loop.py_

For the scRNAseq analysis, I performed quality control, merged and normalized the datasets in _scRNAseq_QC_merg_norm.ipynb_. Analysis was conducted in _scRNAseq_leidenclustering.ipynb_. 
Integration with fully annotated embryo datasets was conducted in _scRNAseq_integration_pijuan_sala.ipynb_ (Pijuan-Sala et al. 2019) and _scRNAseq_integration_grosswendt.ipynb_ (Grosswendt et al. 2020).
