import matplotlib.pyplot as plt

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


def two_d_image(protein_file):
    uniprot_id = protein_file.split("-"[2])

