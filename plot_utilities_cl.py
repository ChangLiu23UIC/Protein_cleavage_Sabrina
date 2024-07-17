import matplotlib.pyplot as plt
from utilities_cl import *

def plot_peptide_lengths_histogram(peptides):
    # Calculate the lengths of each peptide
    peptide_lengths = [len(peptide) for peptide in peptides]

    # Plot the histogram
    plt.figure(figsize=(10, 6))
    plt.hist(peptide_lengths, bins=range(1, max(peptide_lengths) + 2), edgecolor='black')
    plt.title('Histogram of Peptide Lengths')
    plt.xlabel('Peptide Length')
    plt.ylabel('Frequency')
    plt.xticks(range(1, max(peptide_lengths) + 1, 5) )
    plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)
    plt.show()


def two_d_image(sequence, methods):
    peptide_list = peptide_list_from_protein_list([sequence], methods)
    color_list = []
    for peptide in peptide_list:
        length = len(peptide)
        if length < 7:
            color_list.extend(['R'] * length)
        if 7 <= length <= 20:
            color_list.extend(['G'] * length)
        if length > 20:
            color_list.extend(['B'] * length)
    return color_list

if __name__ == '__main__':
    print("Hello")