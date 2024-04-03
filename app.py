import streamlit as st
import pandas as pd
from joblib import load
import numpy as np


# Load the trained model
model = load('pipeline.joblib')  # Replace 'pipeline.joblib' with the path to your trained model file

# List of mutant codons
mutant_codons = ['AAA', 'AAC', 'AAG', 'AAT', 'ACA', 'ACC', 'ACG', 'ACT', 'AGA', 'AGC', 'AGG', 'AGT', 'ATA', 'ATC', 'ATG', 
                 'ATT', 'CAA', 'CAC', 'CAG', 'CAT', 'CCA', 'CCC', 'CCG', 'CCT', 'CGA', 'CGC', 'CGG', 'CGT', 'CTA', 
                 'CTC', 'CTG', 'CTT', 'GAA', 'GAC', 'GAG', 'GAT', 'GCA', 'GCC', 'GCG', 'GCT', 'GGA', 'GGC', 'GGG', 
                 'GGT', 'GTA', 'GTC', 'GTG', 'GTT', 'TAG', 'TAT', 'TCA', 'TCC', 'TCG', 'TCT', 'TGA', 'TGC', 'TGG', 
                 'TGT', 'TTA', 'TTC', 'TTG', 'TTT']

# List of diseases
diseases = ['B-Chronic lymphocytic leukemia', 'Bladder carcinoma', 'Breast carcinoma', 'Colorectal carcinoma', 
            'Esophageal SCC', 'Head and Neck SCC', 'Hepatocellular carcinoma', 'Lung (NSCLC)', 'Ovarian carcinoma', 
            'Pancreatic carcinoma']

# List of Variant Types
variant_types = ['DEL', 'INS']


def generate_encoded_df(label, options, prefix):
    # UI input
    selected_option = st.selectbox(label, options=options, key=label)

    # Create DataFrame with dummy variables
    encoded_df = pd.DataFrame(np.zeros((1, len(options))), columns=options)

    # Set value for the selected option to 1
    encoded_df.loc[0, selected_option] = 1

    # Add prefix 'x0' to column names
    encoded_df.columns = [prefix + col for col in encoded_df.columns]

    return encoded_df




# # Function to predict pathogenicity
# def predict_pathogenicity(HG38_Start, mutant_codon, disease, variant_type):
  
#     # Prepare input data with the user-selected values
#     input_data = pd.concat([HG38_Start_df, mutant_codon_df, disease_df, variant_type_df], axis=1)
    
    
#     # Check columns of the DataFrame
#     print("Columns of input_data:", input_data.columns)

#     st.write("Shape of input_data:", input_data.shape)  # Print the shape of input_data
#     st.write("Data type of input_data:", input_data.dtypes)  # Print the data type of input_data

#     # Make the prediction
#     prediction = model.predict(input_data)
#     return prediction



# Set page title
st.title('PathFinder: TP53 Variant Pathogenicity Predictor')

# Add input fields for mutant codon, disease, variant type, HG38_Start, somatic_stat, and tumor_rep
HG38_Start = st.text_input("Enter HG38 Start site:")

# Somatic_Stat = st.text_input("Enter Somatic_Stat:")
# Tumor_Repetition = st.text_input("Enter Tumor_Repetition:")

                        
mutant_codon_df = generate_encoded_df('Select Mutant Codon:', mutant_codons, 'Mutant_Codon_')
disease_df = generate_encoded_df('Select Disease:', diseases, 'Disease_')
variant_type_df = generate_encoded_df('Select Variant Type:', variant_types, 'Variant_Type_')


predict_button = st.button('Predict', key='predict_button')


# Make prediction when the 'Predict' button is clicked
if predict_button:



    HG38_Start_df = pd.DataFrame(columns=['HG38_Start'])
    HG38_Start_df.loc[0, 'HG38_Start'] = int(HG38_Start)

    # Somatic_Stat_df = pd.DataFrame(columns=['Somatic_Stat'])
    # Somatic_Stat_df.loc[0, 'Somatic_Stat'] = Somatic_Stat

    # Tumor_Repetition_df = pd.DataFrame(columns=['Tumor_Repetition'])
    # Tumor_Repetition_df.loc[0, 'Tumor_Repetition'] = int(Tumor_Repetition)

    input_data = pd.concat([HG38_Start_df, mutant_codon_df, disease_df, variant_type_df], axis=1)
    
    st.write(input_data.shape)
    st.write(input_data)
    

    prediction = model.predict(input_data)

    


            
    st.write('Prediction:', prediction)
    if prediction == 1:
        st.write("This mutant codon is Pathogenic")
    elif prediction == 2:
        st.write("This mutant codon is likely to be Pathogenic")
    elif prediction == 3:
        st.write("This mutant codon has uncertain significance")
    elif prediction == 4:
        st.write("This mutant codon is Benign")
    else:
        st.write("Unknown")
else:
    st.write('Please fill out the required fields to predict the pathogenicity')
