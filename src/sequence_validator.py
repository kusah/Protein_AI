from Bio.SeqUtils import molecular_weight
from collections import Counter

VALID_AMINO_ACIDS = set("ARNDCQEGHILKMFPSTWYV")


def validate_sequence(sequence):
    """
    Checks whether the protein sequence contains only valid amino acids.
    """

    sequence = sequence.upper()

    invalid = set(sequence) - VALID_AMINO_ACIDS

    return len(invalid) == 0, invalid


def get_sequence_statistics(sequence):
    """
    Returns useful statistics about the protein.
    """

    sequence = sequence.upper()

    stats = {
        "Length": len(sequence),
        "Molecular Weight": round(molecular_weight(sequence, seq_type="protein"), 2),
        "Composition": dict(Counter(sequence))
    }

    return stats