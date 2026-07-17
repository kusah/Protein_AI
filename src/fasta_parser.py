from Bio import SeqIO

def read_fasta(file_path):
    """
    Reads a FASTA file and returns the sequence ID and protein sequence.
    """

    record = SeqIO.read(file_path, "fasta")

    return {
        "id": record.id,
        "description": record.description,
        "sequence": str(record.seq)
    }