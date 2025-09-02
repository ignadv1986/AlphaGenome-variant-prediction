# AlphaGenome Variant Prediction
[Alphagenome](https://github.com/google-deepmind/alphagenome) prediction of the impact of H1 promoter conserved motifs mutation on H1 expression.
## Project Summary
In this repository the AlphaGenome model recently developed by Google DeepMind is employed to create a pipeline that quantifies changes in the expression of three different H1 genes upon mutation of the three known regulatory elements present in these genes´ promoters: TATA-box, H1-box and the CH1UE motif. Expression is assessed through prediction based on the RNA-Seq databases included in the model. Additionally, the script here created can be easily applied to get other outputs included in the AlphaGenome model, and/or to predict the effects of mutating other regions of the genome.
The project also includes a script that allows identification of variants that are most likely to affect gene expression based on DNA-Seq data through in-silico mutagenesis.
## Tools
- **Python3/Google Colab:** Code generation, data management and visualization.
- **AlphaGenome:** Variant prediction.
- **Bedtools:** Fasta file management.
## Aim of the study
This work aims to create an easily reusable platform to analyze gene expression and to identify impactful mutations using AlphaGenome, while trying to get some insights into H1 promoter regulation. The Google Colab file with all functions used can be found [here]()
## Workflow
1) Generation of a .bed file with the coordinates of the H1-0, H1-2, and H1-4 promoters.
2) Sequence retrieval with bedtools getfasta to generate the .fa file.
3) Localization of the following known motifs inside the promoter region:
   - TATA-box
   - H1-box
   - CH1UE
4) Run AlphaGenome to introduce variants into the selected sequences and extract/plot the results.
5) Use in-silico mutagenesis to identify impactful variants both inside H1 genes and their promoters.
## Results

