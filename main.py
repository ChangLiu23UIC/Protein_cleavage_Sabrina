from utilities_cl import *
from plot_utilities_cl import *
import glob


user_input = input("Enter the list of cleavage methods separated by commas(Ex: trypsin,chymotrypsin low specificity): ")
methods = user_input.split(',')

file_list = glob.glob("AF Structure Files - Collagen/*.pdb")
protein_sequence_list = protein_list_from_file(file_list)
peptide_list = peptide_list_from_file_list(protein_sequence_list, methods)
plot_peptide_lengths_histogram(peptide_list)
summary_statements(peptide_list, protein_sequence_list)


if __name__ == '__main__':
    print("HI")