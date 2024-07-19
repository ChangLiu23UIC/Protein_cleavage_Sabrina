from utilities_cl import *
from plot_utilities_cl import *
import glob
from fastapi import FastAPI
import requests
import json

user_input = input("Enter the list of cleavage methods separated by commas(Ex: trypsin,chymotrypsin low specificity): ")
methods = user_input.split(',')

# Read every protein entry
file_list = glob.glob("AF Structure Files - Collagen/*.pdb")

# Get the entire peptides from the entire proteins
protein_sequence_list, protein_dict = protein_list_from_file(file_list)
peptide_total_list = peptide_list_from_protein_list(protein_sequence_list, methods)

peptide_dict = {}
for protein_id, sequence in protein_dict.items():
    peptide_dict[protein_id] = peptide_list_from_protein_list(sequence, methods)

plot_peptide_lengths_histogram(peptide_total_list)


summary_statements(peptide_total_list, protein_sequence_list)

import requests
import json

# Define the API endpoint
submit_url = "https://scv.lab.gy/external-job"
details_url = "https://scv.lab.gy/job_details"

# Prepare the job data according to the provided schema
sequence_model = {
    "id": "A2A2Y8",
    "protein_id": "A2A2Y8",
    "coverage": 100,  # Example coverage
    "sequence": "MDVTKKNKRDGTEVTERIVTETVTTRLTSLPPKGGTSNGYAKTASLGGGSRLEKQSLTHGSSGYINSTGSTRGHASTSSYRRAHSPASTLPNSPGSTFERKTHVTRHAYEGSSSGNSSPEYPRKEFASSSTRGRSQTRESEIRVRLQSASPSTRWTELDDVKRLLKGSRSASVSPTRNSSNTLPIPKKGTVETKIVTASSQSVSGTYDATILDANLPSHVWSSTLPAGSSMGTYHNNMTTQSSSLLNTNAYSAGSVFGVPNNMASCSPTLHPGLSTSSSVFGMQNNLAPSLTTLSHGTTTTSTAYGVKKNMPQSPAAVNTGVSTSAACTTSVQSDDLLHKDCKFLILEKDNTPAKKEMELLIMTKDSGKVFTASPASIAATSFSEDTLKKEKQAAYNADSGLKAEANGKNKYDCCPP",
    "UNID": "A2A2Y8",
    "description": "Test",
    "sequence_coverage": [],
    "ptms": {},
    "has_pdb": True
}

job_model = {
    "psms": {
        'A2A2Y8': [
            'MDVTK', 'DGTEVTER', 'IVTETVTTR', 'LTSLPPK', 'GGTSNGYAK', 'TASLGGGSR', 'QSLTHGSSGYINSTGSTR', 'GHASTSSYR',
            'AHSPASTLPNSPGSTFER', 'THVTR', 'HAYEGSSSGNSSPEYPR', 'EFASSSTR', 'LQSASPSTR', 'WTELDDVK', 'SASVSPTR', 'NSSNTLPIPK',
            'IVTASSQSVSGTYDATILDANLPSHVWSSTLPAGSSMGTYHNNMTTQSSSLLNTNAYSAGSVFGVPNNMASCSPTLHPGLSTSSSVFGMQNNLAPSLTTLSHGTTTTSTAYGVK',
            'NMPQSPAAVNTGVSTSAACTTSVQSDDLLHK', 'EMELLIMTK', 'VFTASPASIAATSFSEDTLK', 'QAAYNADSGLK'
        ]
    },
    "ptm_annotations": {},
    "background_color": 0,
    "species": "human",
    "usis": {}
}

job = {
    "sequence_model": sequence_model,
    "job_model": job_model
}

# Convert job data to JSON string
job_json = json.dumps(job)

# Submit the job
files = {
    'file': (r"E:\UIC_PHD\Python projects\Protein_cleavage\AF Structure Files - Collagen\AF-A2A2Y8-F1-model_v4.pdb", open(r"E:\UIC_PHD\Python projects\Protein_cleavage\AF Structure Files - Collagen\AF-A2A2Y8-F1-model_v4.pdb", 'rb'))
}
response = requests.post(submit_url, files=files, data={'job': job_json})

response_data = response.json()
print(response_data)

# Retrieve the job number
job_number = response_data.get('job_number')
if job_number:
    # Check job details
    data_details = {
        'job_number': job_number
    }
    response_details = requests.post(details_url, json=data_details)
    print(response_details.json())
else:
    print("Failed to retrieve job number")


if __name__ == '__main__':
    print("A")