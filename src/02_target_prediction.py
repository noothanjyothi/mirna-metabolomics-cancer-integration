# Script 2: Reverse complement and target prediction
# Uses only Biopython - no other libraries

from Bio.Seq import Seq
from Bio import SeqIO

def get_reverse_complement(sequence):
    """
    Get the reverse complement of a DNA/RNA sequence.
    miRNA targets are usually complementary to the miRNA.
    """
    seq_obj = Seq(sequence)
    rev_comp = seq_obj.reverse_complement()
    return str(rev_comp)

def get_seed_region(mirna_sequence, seed_length=7):
    """
    Extract the seed region (first 7 nucleotides) of miRNA.
    This region is most important for target recognition.
    """
    return mirna_sequence[:seed_length]

def find_target_matches(mirna_sequence, target_sequence):
    """
    Check if miRNA seed region matches target sequence.
    """
    mirna_seq = mirna_sequence.upper()
    target_seq = target_sequence.upper()
    
    seed = get_seed_region(mirna_seq)
    rev_comp_seed = get_reverse_complement(seed)
    
    # Check if reverse complement of seed is in target
    if rev_comp_seed in target_seq:
        return True
    return False

def predict_targets(mirna_id, mirna_sequence, target_genes):
    """
    Predict which genes might be targets of this miRNA.
    """
    print(f"\nPredicting targets for {mirna_id}")
    print(f"miRNA sequence: {mirna_sequence}")
    
    seed = get_seed_region(mirna_sequence)
    rev_comp_seed = get_reverse_complement(seed)
    
    print(f"Seed region: {seed}")
    print(f"Reverse complement (what we look for in targets): {rev_comp_seed}")
    print("\nTarget matches:")
    
    matches = []
    for gene_name, gene_seq in target_genes.items():
        if find_target_matches(mirna_sequence, gene_seq):
            print(f"  ✓ {gene_name}: {gene_seq}")
            matches.append(gene_name)
        else:
            print(f"  ✗ {gene_name}: {gene_seq}")
    
    return matches

def main():
    # Example: hsa-miR-21 and some target genes
    mirna_id = "hsa-miR-21"
    mirna_seq = "UAGCUUAUCAGACUGAUGUUGA"
    
    # Example cancer-related genes
    target_genes = {
        "TP53": "AACACCAACAAACCTACTACC",      # Tumor suppressor
        "PTEN": "CCGATTTGCAAGTTGATGGA",      # Cancer suppressor
        "BMPR2": "ACACCAACCTACTACCTCATC",    # Growth signaling
        "PDCD4": "UUAACCCUACUACUACUACUA",   # Apoptosis regulator
    }
    
    # Predict targets
    target_hits = predict_targets(mirna_id, mirna_seq, target_genes)
    print(f"\nFound {len(target_hits)} potential targets")

if __name__ == "__main__":
    main()
