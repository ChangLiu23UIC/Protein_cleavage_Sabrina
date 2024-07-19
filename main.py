from utilities_cl import *
from plot_utilities_cl import *
import glob
import sys
import os

# Path to SCV-master/python
scv_master_python_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'SCV-master', 'python'))

# Append the SCV-master/python path to sys.path
if scv_master_python_path not in sys.path:
    sys.path.append(scv_master_python_path)

import scv_main

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


if __name__ == '__main__':
    print("A")