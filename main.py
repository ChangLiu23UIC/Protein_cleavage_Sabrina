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

if __name__ == '__main__':
    print("A")