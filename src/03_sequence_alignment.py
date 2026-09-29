# Script 3: Align miRNA sequences
# Compare sequences to find similarities

from Bio import SeqIO
from Bio import pairwise2

def load_all_mirnas(fasta_file):
    """
    Load all miRNA sequences from FASTA file.
    """
    mirnas = {}
    for record in SeqIO.parse(fasta_file, "fasta"):
        mirnas[record.id] = str(record.seq)
    return mirnas

def align_two_sequences(seq1, seq2):
    """
    Perform pairwise alignment between two sequences.
    """
    alignments = pairwise2.align.globalxx(seq1, seq2)
    if alignments:
        return alignments[0]
    return None

def calculate_similarity(seq1, seq2):
    """
    Calculate percentage similarity between two sequences.
    """
    if len(seq1) != len(seq2):
        return 0.0
    
    matches = sum(1 for a, b in zip(seq1, seq2) if a == b)
    similarity = (matches / len(seq1)) * 100
    return similarity

def print_alignment(mirna1_id, seq1, mirna2_id, seq2, alignment):
    """
    Print alignment results nicely.
    """
    print(f"\nAlignment: {mirna1_id} vs {mirna2_id}")
    print(f"Sequence 1: {seq1}")
    print(f"Sequence 2: {seq2}")
    print(f"Similarity: {calculate_similarity(seq1, seq2):.2f}%")
    
    if alignment:
        aligned_seq1, aligned_seq2, score, begin, end = alignment
        print(f"Alignment score: {score}")

def main():
    # Load miRNAs
    fasta_file = "data/mirna_examples.fasta"
    print("Loading miRNA sequences...")
    mirnas = load_all_mirnas(fasta_file)
    
    # Compare all miRNAs with each other
    mirna_list = list(mirnas.items())
    print(f"Loaded {len(mirna_list)} miRNAs\n")
    
    # Compare first few sequences
    for i in range(len(mirna_list)):
        for j in range(i + 1, len(mirna_list)):
            id1, seq1 = mirna_list[i]
            id2, seq2 = mirna_list[j]
            
            alignment = align_two_sequences(seq1, seq2)
            print_alignment(id1, seq1, id2, seq2, alignment)
            print("-" * 50)

if __name__ == "__main__":
    main()
