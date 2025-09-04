# AlphaGenome Variant Prediction
[Alphagenome](https://github.com/google-deepmind/alphagenome) prediction of the impact of H1 promoter conserved motifs mutation on H1 expression.
## Project Summary
This repository utilizes the AlphaGenome model, recently developed by Google DeepMind, to build a pipeline that quantifies changes in the expression of three different H1 histone genes—H1-0, H1-2, and H1-4—upon mutation of three known conserved regulatory elements within their promoter regions: the TATA-box, H1-box, and CH1UE motif.
Gene expression levels are predicted using AlphaGenome’s RNA-Seq-based models. The code provided is modular and can be adapted to analyze other genomic regions or output types supported by AlphaGenome. Additionally, the project includes an in-silico mutagenesis pipeline to identify sequence variants most likely to impact gene expression, based on DNA-Seq data.
## Tools
- **Python3/Google Colab:** Code generation, data management and visualization.
- **AlphaGenome:** Variant prediction.
- **Bedtools:** Fasta file management.
## Aim of the study
This study aims to develop an adaptable and reusable platform to analyze the effects of genomic variants on gene expression using AlphaGenome. It also seeks to provide insights into the regulation of H1 gene expression by evaluating how mutations in promoter motifs affect predicted expression levels.
A complete, ready-to-run Google Colab notebook containing all functions used in the pipeline is available [here](./Alphagenome.ipynb)
## Workflow
1) Define promoter regions: Create a .bed file with the genomic coordinates of the H1-0, H1-2, and H1-4 promoters.
2) Extract sequences: Use bedtools getfasta to generate corresponding .fa sequence files.
3) Motif localization: Identify and annotate the positions of the following regulatory motifs within each promoter:
- TATA-box
- H1-box
- CH1UE motif
4) Variant simulation and expression prediction:
- Use AlphaGenome to simulate point mutations in the motifs.
- Predict and visualize changes in gene expression.
5) In-silico mutagenesis:
- Systematically introduce variants across promoter and gene regions.
- Identify mutations with the highest predicted impact on expression.
## Results
A) **Motif Variant Analysis**

When specifically targeting mutations to known regulatory motifs using AlphaGenome, the impact varied between genes:
- H1-2 and H1-4 expression remained largely unaffected by mutations in the TATA-box, H1-box, or CH1UE motifs in the HeLa S3 cell line model.
- In contrast, H1-0 expression showed sensitivity to mutations in both the TATA-box and, to a lesser extent, the H1-box, with a measurable reduction in predicted expression levels.
Cell-Type Specific Effects
One of the strengths of AlphaGenome is its ability to assess variant effects across a wide range of cell types using RNA-Seq datasets. When analyzing other cell models:
- The H1-0 TATA-box mutation had a broader and more pronounced effect on expression across multiple cell types.
- Notably, mutations in both the H1-0 and H1-4 promoters caused a significant reduction (up to 2.5-fold) in predicted expression levels specifically in lymphocyte cell types, suggesting a cell-type-dependent regulatory role for these motifs. This is interesting given the previously reported link between H1 levels misregulation and different types of lymphomas.
  
B) **In-silico Mutagenesis**

The in-silico mutagenesis pipeline did not identify any single nucleotide variants in the promoter or coding regions of H1-0, H1-2, or H1-4 that were predicted to cause large changes in expression levels. This suggests a degree of sequence robustness in these regions or limited sensitivity of the model to isolated point mutations outside of key regulatory motifs.
