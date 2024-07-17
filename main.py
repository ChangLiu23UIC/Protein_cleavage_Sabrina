from utilities_cl import *
from plot_utilities_cl import *
import glob


# Generate a list of all pdb files
file_list = glob.glob("AF Structure Files - Collagen/*.pdb")
peptide_list = peptide_list_from_file_list(file_list, ["trypsin",'chymotrypsin low specificity'])
plot_peptide_lengths_histogram(peptide_list)
detectable_peptides = count_detectable_peptides(peptide_list)
print("Number of peptides that satisfy the mass spectrometer's detectability conditions:", detectable_peptides)
average_size = sum(len(peptide) for peptide in peptide_list) / len(peptide_list)
print("Average size of digested peptides:", average_size)
max_size = max(len(peptide) for peptide in peptide_list)
print("Maximum size of undigested peptides:", max_size)


if __name__ == '__main__':
    print("Hello World")