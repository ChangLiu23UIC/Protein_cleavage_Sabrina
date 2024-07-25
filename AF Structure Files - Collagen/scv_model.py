import json
import requests


def submit_job_with_pdb(pdb, psms, ptm_annotations, background_color, species):
    url = 'https://scv.lab.gy/job'
    files = {"file": (pdb, open(pdb, 'rb'), 'text/plain')}
    data = {
        'psms': psms,
        'ptm_annotations': ptm_annotations,
        'background_color': background_color,
        'species': species,
    }
    response = requests.post(url, files=files, data={'job': json.dumps(data)})
    return response.json()


if __name__ == '__main__':
    pdb_file = "AF-A2A2Y8-F1-model_v4.pdb"  # Path to file on local machine
    psms = {'group1': ['DGTEVTER', 'IVTETVTTR', 'GGTSNGYAK', 'TASLGGGSR', 'QSLTHGSSGYINSTGSTR', 'GHASTSSYR', 'AHSPASTLPNSPGSTFER', 'HAYEGSSSGNSSPEYPR', 'EFASSSTR', 'LQSASPSTR', 'WTELDDVK', 'SASVSPTR', 'NSSNTLPIPK', 'IVTASSQSVSGTYDATILDANLPSHVWSSTLPAGSSMGTYHNNMTTQSSSLLNTNAYSAGSVFGVPNNMASCSPTLHPGLSTSSSVFGMQNNLAPSLTTLSHGTTTTSTAYGVK', 'NMPQSPAAVNTGVSTSAACTTSVQSDDLLHK', 'EMELLIMTK', 'VFTASPASIAATSFSEDTLK', 'QAAYNADSGLK']}
    ptm_annotations = {}
    background_color = 16777215
    species = "human"

    response = submit_job_with_pdb(pdb_file, psms, ptm_annotations, background_color, species)
    print(response)