from utilities_cl import *
from plot_utilities_cl import *
import glob


def main():
    user_input = input("Enter the list of cleavage methods separated by commas(Ex: trypsin,chymotrypsin low specificity): ")
    methods = user_input.split(',')

    file_list = glob.glob("AF Structure Files - Collagen/*.pdb")
    peptide_list, protein_sequence_list = peptide_list_from_file_list(file_list, methods)
    plot_peptide_lengths_histogram(peptide_list)
    summary_statements(peptide_list, protein_sequence_list)


if __name__ == '__main__':
    main()