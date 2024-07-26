import re
from expasy import expasy_rules

cleavage_rules = {
    "trypsin" : r'(?<=[KR])(?!P)',
    "chymotrypsin" : r'(?<=[FYWL])'
}


def three_to_one(aa_sequence):
    """
    Turn the 3 letter amino acid into 1 letter amino acid (ALA to A)
    :param aa_sequence:
    :return:
    """
    three_to_one_dict = {
        'ALA': 'A', 'ARG': 'R', 'ASN': 'N', 'ASP': 'D',
        'CYS': 'C', 'GLN': 'Q', 'GLU': 'E', 'GLY': 'G',
        'HIS': 'H', 'ILE': 'I', 'LEU': 'L', 'LYS': 'K',
        'MET': 'M', 'PHE': 'F', 'PRO': 'P', 'SER': 'S',
        'THR': 'T', 'TRP': 'W', 'TYR': 'Y', 'VAL': 'V'
    }

    one_letter_sequence = ""
    for i in range(0, len(aa_sequence), 3):
        three_aa = aa_sequence[i:i + 3]
        one_aa = three_to_one_dict.get(three_aa)
        if one_aa:
            one_letter_sequence += one_aa
        else:
            one_letter_sequence += 'X'
    return one_letter_sequence


def peptide_cleavage(rule, sequence):
    """
    Method for peptide cleavage with the expasy rule selected with regular expression
    :param rule:
    :param sequence:
    :return:
    """
    exp_rule = expasy_rules[rule]
    cut_end_pos_list = [i.start() for i in re.finditer(exp_rule, sequence)] + [(len(sequence) - 1)]
    cut_start_pos_list = [0] + [i + 1 for i in cut_end_pos_list]
    cut_start_pos_list.pop()

    pieces_list = {"start_pos": cut_start_pos_list, "end_pos": cut_end_pos_list}

    result = [sequence[pieces_list["start_pos"][i]:pieces_list["end_pos"][i] + 1]
                              for i in range(0, len(pieces_list["start_pos"]) - 1)]
    return result


def grouping_by_size_for_color(peptide_list:list) -> dict:
    """
    seperate the dictionary into three color types based on length
    red unnecessary because impossible to find in scv (too short)
    :param peptide_list:
    :return:
    """
    result_dict = { "green":[], "blue":[]}
    for peptide in peptide_list:
        if 6 < len(peptide) < 21:
            result_dict["green"].append(peptide)
        elif 20 < len(peptide):
            result_dict["blue"].append(peptide)

    return result_dict


if __name__ == '__main__':
    result = peptide_cleavage("trypsin", "MDVTKKNKRDGTEVTERIVTETVTTRLTSLPPKGGTSNGYAKTASLGGGSRLEKQSLTHGSSGYINSTGSTRGHASTSSYRRAHSPASTLPNSPGSTFERKTHVTRHAYEGSSSGNSSPEYPRKEFASSSTRGRSQTRESEIRVRLQSASPSTRWTELDDVKRLLKGSRSASVSPTRNSSNTLPIPKKGTVETKIVTASSQSVSGTYDATILDANLPSHVWSSTLPAGSSMGTYHNNMTTQSSSLLNTNAYSAGSVFGVPNNMASCSPTLHPGLSTSSSVFGMQNNLAPSLTTLSHGTTTTSTAYGVKKNMPQSPAAVNTGVSTSAACTTSVQSDDLLHKDCKFLILEKDNTPAKKEMELLIMTKDSGKVFTASPASIAATSFSEDTLKKEKQAAYNADSGLKAEANGKNKYDCCPP")
    result_dict = grouping_by_size_for_color(result)