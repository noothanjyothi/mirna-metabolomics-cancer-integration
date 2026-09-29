# Script 1: Load and analyze miRNA sequences
# No external libraries needed except Biopython

from Bio import SeqIO

def load_mirna_sequences(fasta_file):
    """
    Load miRNA sequences from a FASTA file.
    """
    sequences = {}
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequences[record.id] = str(record.seq)
    return sequences

def calculate_gc_content(sequence):
    """
    Calculate GC content (percentage of G and C nucleotides).
    """
    seq = sequence.upper()
    if len(seq) == 0:
        return 0
    gc_count = seq.count('G') + seq.count('C')
    gc_percent = (gc_count / len(seq)) * 100
    return gc_percent

def count_nucleotides(sequence):
    """
    Count how many A, U, G, C are in the sequence.
    """
    seq = sequence.upper()
    counts = {
        'A': seq.count('A'),
        'U': seq.count('U'),
        'G': seq.count('G'),
        'C': seq.count('C')
    }
    return counts

def print_sequence_summary(mirna_id, sequence):
    """
    Print a summary of the miRNA sequence.
    """
    gc = calculate_gc_content(sequence)
    counts = count_nucleotides(sequence)
    
    print(f"\n--- miRNA ID: {mirna_id} ---")
    print(f"Sequence: {sequence}")
    print(f"Length: {len(sequence)} nucleotides")
    print(f"GC content: {gc:.2f}%")
    print(f"Nucleotide counts: {counts}")

def main():
    # Load sequences from file
    fasta_file = "data/mirna_examples.fasta"
    print("Loading miRNA sequences...")
    sequences = load_mirna_sequences(fasta_file)
    
    # Print summary for each sequence
    for mirna_id, sequence in sequences.items():
        print_sequence_summary(mirna_id, sequence)
    
    print(f"\nTotal miRNAs loaded: {len(sequences)}")

if __name__ == "__main__":
    main()
