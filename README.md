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
    <br/> 1. Prioritize <i>TP53</i> variants based on their predicted functional impact, frequency in the dataset, and relevance to breast cancer pathogenesis.
    <br/>2. Utilize machine learning algorithms, such as random forests or gradient boosting, to rank  <i>TP53</i> variants according to their likelihood of driving breast cancer progression or treatment response. 
    <br/><b>Impact of this solution:</b>
    <br/>1. Improved Prioritization of Variants: Machine learning models can consider multiple features simultaneously, including variant type, allele frequency, and clinical data, to prioritize <i>TP53</i> variants more accurately. This can help researchers focus their efforts on investigating variants most likely to be clinically relevant.
    <br/>2. Identification of Biomarkers: By identifying <i>TP53</i> variants associated with disease progression or treatment response, this approach can lead to the discovery of biomarkers that could be used for patient stratification, prognosis prediction, and treatment selection like Personalized Treatment Strategies.
    <br/><b>Description of the dataset:</b>
    <br/>

## Mutation Coordinates (Nucleotide)

- **HG38_Start**: Start coordinates of the mutation using CRCh38 as reference.
- **HG38_End**: End coordinates of the mutation using CRCh38 as reference.
- **Exon:intron_Start**: Location of the mutation start in the introns or exons of the TP53 gene.
- **Exon:intron_End**: Location of the mutation end in the introns or exons of the TP53 gene.
- **Genome_Base_Coding**: Nucleotide at the start position of the mutation.
- **Codon**: Codon position using TP53 alpha (p1) as reference.
- **WT AA_3**: Wild-type amino acid.
- **Mutant AA_3**: Mutant amino acid.
- **Base_Change_Size**: Size of the substitution.
- **Ins_Size**: Size of the deletion.
- **Del_Size**: Size of the insertion.
- **Mutant_Allele**: Mutant (Alt) nucleotide.
- **WT_Codon**: Nucleotide sequence of the wild-type codon.
- **Mutant_Codon**: Sequence of the mutated codon.

## Protein Structure and Domain

- **Structure**: Structural motif of the TP53 protein.
- **Domain**: Domain of the TP53 protein.

## Mutation Type and Origin

- **Type**: Type of mutation (e.g., Ts: Transition, Tv: Transversion, Fr: Frameshift).
- **Mutation_Type**: Variant type as defined in MAF file.
- **CpG**: Indicates if the mutation occurs at a CpG dinucleotide.
- **Py-Py_Doublets**: Indicates if the mutation targets a Py-Py doublet.
- **Variant_Type**: Variant type (SNP, DNP, TNP, INS, DEL).
- **Mutation_Origin**: Origin of the mutation (Somatic, Germline).

## Disease and Sample Information

- **Disease**: Name of the disease associated with the mutation.
- **Sample_Pathology**: Pathological nature of the sample.
- **Sample_Origin**: Nature of the sample in which the mutation was identified.

## Frequency and Statistics

- **Records_Number**: Number of occurrences of the mutant in the database.
- **Leukaemia_Stat**: Frequency of the variant in hematological malignancies.
- **Solid_Stat**: Frequency of the variant in solid tumors.
- **Tumour_Stat**: Frequency of the variant in tumors only.
- **Cell_line_Stat**: Frequency of the variant in cell lines only.
- **Somatic_Stat**: Frequency of the variant found as a somatic event.
- **Tumour_Repetition**: Number of mutations associated with the mutant in a single tumor.

## Prediction and Activity

- **Comment_Prediction**: Predicted pathogenicity based on various algorithms.
- **Comment_Frequency**: Frequency information related to the mutation.
- **Comment_Activity**: Residual activity of the TP53 mutant based on transcriptional activity.

## Prediction Algorithms

- **Sift_Prediction**: Predictive value using Sift.
- **Provean_Prediction**: Prediction of deleterious or neutral impact.
- **Mutassessor_Prediction**: Functional impact of a variant.

## Pathogenicity (Target Feature)

- **Pathogenicity**: Standard terminology for TP53 variants (e.g., 'pathogenic', 'likely pathogenic', 'uncertain significance', 'likely benign').

For detailed information on TP53 mutations and their analysis, refer to the corresponding publication and the TP53 Website.
    <br/>UMD_mutations_US.csv
  </p>
   
