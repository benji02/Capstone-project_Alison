<a name="readme-top"></a>
<!-- PROJECT SHIELDS -->
<br />
<div align="center">
  <a href="https://github.com/allyvaz/Capstone-project">
    <img src="https://microbenotes.com/wp-content/uploads/2023/05/Alleles.jpg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Exploring the Oncogenic Impact of <i>TP53</i> Variants and Classifying the Pathogenicity: A Comprehensive Analysis</h3>

  <p align="center">
    Project Overview
  </p>
  <p align ="justify">
    <b>Areas of Interest:</b> 
    <br/>1. Variants of <i>TP53</i> causing Cancer.
    <br/>2. Variant allele frequency of <i>TP53</i>.
    <br/>3. Longitudinal study of <i>TP53</i> variants.
    <br/>4. Exploration of <i>TP53</i> variant interactions with other genes or pathways implicated in Cancer development.
    <br/><b>Problem Statement: </b>
    <br/>In the realm of cancer research, accurately identifying mutations (also known as variants) from next-generation sequencing of tumor samples poses a significant challenge. Variants exhibit diverse characteristics within the dataset, and both biological and technical variability complicate the process for variant callers. Various metrics, such as sequencing depth around the variant, the count of reads supporting the reference or mutated allele, the quality associated with these reads, and the confidence level of the tools in making specific calls, are crucial for assessing variants. This project will specifically explore the utility of one such metric: Variant Allele Frequency (VAF), in addressing these challenges.
    <br/><b>Proposed Data Science strategy:</b>
    <br/> 1. Prioritize <i>TP53</i> variants based on their predicted functional impact, frequency in the dataset, and relevance to pathogenesis.
    <br/>2. Utilize machine learning algorithms, such as random forests, to rank  <i>TP53</i> variants according to their likelihood of driving breast cancer progression or treatment response. 
    <br/><b>Impact of this solution:</b>
    <br/>1. Improved Prioritization of Variants: Machine learning models can consider multiple features simultaneously, including variant type, allele frequency, and clinical data, to prioritize <i>TP53</i> variants more accurately. This can help researchers focus their efforts on investigating variants most likely to be clinically relevant.
    <br/>2. Identification of Biomarkers: By identifying <i>TP53</i> variants associated with disease progression or treatment response, this approach can lead to the discovery of biomarkers that could be used for patient stratification, prognosis prediction, and treatment selection like Personalized Treatment Strategies.
    <br/><b>Description of the dataset:</b>
    <br/>

## Mutation Coordinates (Nucleotide)

- **HG38_Start**: Start coordinates of the mutation using CRCh38 as reference.
- **Mutant_Codon**: Sequence of the mutated codon.

## Mutation Type and Origin

- **Variant_Type**: Variant type (SNP, DNP, TNP, INS, DEL).

## Disease and Sample Information

- **Disease**: Name of the disease associated with the mutation.
  
## Frequency and Statistics

- **Somatic_Stat**: Frequency of the variant found as a somatic event.
- **Tumor_repetition**: Denotes the total number of mutations associated with this mutant in a single tumor.

## Pathogenicity (Target Feature)

- **Pathogenicity**: Standard terminology for TP53 variants (e.g., 'pathogenic', 'likely pathogenic', 'uncertain significance', 'likely benign').

For detailed information on TP53 mutations and their analysis, refer to the corresponding publication and the TP53 Website.
    <br/>UMD_mutations_US.csv
  </p>
   
<p align='left'>
  
### Machine Learning Model: Random Forest with Cross-Validation and Grid Search

To address the classification task of TP53 variant pathogenicity, we employ a Random Forest model, a powerful ensemble learning technique that combines multiple decision trees to improve predictive performance. Random Forests are well-suited for this task due to their ability to handle complex datasets with high dimensionality and non-linear relationships between features.

### Cross-Validation

Cross-validation is a crucial technique used to assess the generalization performance of our model. By splitting the dataset into multiple subsets and training the model on different combinations of these subsets, we can evaluate its performance across various data partitions. This helps us to mitigate issues such as overfitting and ensures that our model performs well on unseen data.

### Grid Search for Hyperparameter Tuning

Hyperparameters play a critical role in the performance of machine learning models. To optimize the performance of our Random Forest classifier, we utilize grid search, a technique that exhaustively searches through a specified subset of hyperparameters to identify the combination that yields the best performance. This iterative process helps us fine-tune the model's parameters, such as the number of trees in the forest, maximum depth of the trees, and the minimum number of samples required to split a node, among others.

By leveraging cross-validation and grid search, we aim to build a robust and accurate classification model for predicting the pathogenicity of TP53 variants. This approach allows us to effectively utilize the available data and optimize the model's performance, ultimately contributing to our understanding of the oncogenic impact of TP53 variants and aiding in the development of personalized treatment strategies for cancer patients.

</p>
