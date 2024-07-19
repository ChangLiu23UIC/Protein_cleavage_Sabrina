import requests
import json

# Define the API endpoint
submit_url = "https://scv.lab.gy/external-job"
details_url = "https://scv.lab.gy/job_details"

# Prepare the job data according to the provided schema
sequence_model = {
    "id": "A2A2Y8",
    "protein_id": "A2A2Y8",
    "coverage": 1,
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

# Submit the job with JSON payload and file
files = {
    'file': (r"E:\UIC_PHD\Python projects\Protein_cleavage\AF Structure Files - Collagen\AF-A2A2Y8-F1-model_v4.pdb", open(r"E:\UIC_PHD\Python projects\Protein_cleavage\AF Structure Files - Collagen\AF-A2A2Y8-F1-model_v4.pdb", 'rb')),
    'job': (None, job_json, 'application/json')
}

response = requests.post(submit_url, files=files)
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
