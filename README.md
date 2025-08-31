# AlphaGenome Variant Prediction
[Alphagenome](https://github.com/google-deepmind/alphagenome) prediction of the impact of H1 promoter conserved motifs on H1 expression.
## Project Summary
In this repository the AlphaGenome model recently developed by Google DeepMind is employed to create a pipeline that quantifies changes in the expression of three different H1 genes upon mutation of the three known regulatory elements in these genes´ promoters: TATA-box, H1-box and the CH1UE motif. Expression is assessed through prediction based on the RNA-Seq databases included in the model. Additionally, the script here created can be easily applied to get other outputs included in the AlphaGenome model, and/or to predict the effects of mutating other regions of the genome.
The project also includes a script that allows identification of variants that are most likely to affect gene expression based on DNA-Seq data.
## Tools
- **Python3/Google Colab:** Code generation, data management and visualization.
- **AlphaGenome:** Variant prediction.
