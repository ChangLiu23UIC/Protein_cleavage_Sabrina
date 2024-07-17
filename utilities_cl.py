from Bio.PDB import *
from cleavage_method import peptide_cleavage, three_to_one
from expasy import expasy_rules
import glob


def extract_aa_sequence(structure):
    amino_acid_sequence = ""
    for model in structure:
        for chain in model:
            for residue in chain:
                # Check if the residue is an amino acid (exclude water molecules, ligands, etc.)
                if residue.get_id()[0] == " " and residue.get_resname() not in ["HOH", "H2O", "WAT"]:
                    amino_acid_sequence += residue.get_resname()

    return amino_acid_sequence


def count_detectable_peptides(cleaved_peptides):
    # Initialize counter for peptides that satisfy the detectability conditions
    detectable_peptides = 0

    # Iterate through cleaved peptides and count those that satisfy the conditions
    for peptide in cleaved_peptides:
        peptide_length = len(peptide)
        if 7 <= peptide_length <= 30:
            detectable_peptides += 1

    return detectable_peptides


def peptide_list_from_file_list(file_list:list, methods):
    p = PDBParser()
    protein_sequence_list = [three_to_one(extract_aa_sequence(p.get_structure(protein.split('-')[2],protein)))
                           for protein in file_list]
    peptide_list = []
    for protein_sequences in protein_sequence_list:
        peptide_list += peptide_cleavage(methods[0], protein_sequences)
    if len(methods) == 1:
        return peptide_list
    else:
        new_peptide_list = []
        for method in methods[1:]:
            for peptide in peptide_list:
                new_peptide_list += peptide_cleavage(method, peptide)
            peptide_list = new_peptide_list
            return peptide_list


if __name__ == '__main__':
    file_list = glob.glob("AF Structure Files - Collagen/*.pdb")
    pl = peptide_list_from_file_list(file_list, ["trypsin", 'chymotrypsin low specificity'])

