# Script 5: Link miRNA with cancer gene expression
# Simple integration without external libraries

from Bio import SeqIO

def load_mirna_sequences(fasta_file):
    """
    Load miRNA sequences from FASTA file.
    """
    sequences = {}
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequences[record.id] = str(record.seq)
    return sequences

def read_cancer_expression_data(csv_file):
    """
    Read cancer gene expression data from CSV file.
    Format: gene,control,tumor
    """
    expression_data = {}
    
    with open(csv_file, 'r') as file:
        # Skip header
        header = file.readline()
        
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            parts = line.split(',')
            if len(parts) >= 3:
                gene_name = parts[0]
                control_expr = float(parts[1])
                tumor_expr = float(parts[2])
                
                expression_data[gene_name] = {
                    'control': control_expr,
                    'tumor': tumor_expr,
                    'fold_change': tumor_expr / (control_expr + 0.001)  # Avoid division by zero
                }
    
    return expression_data

def analyze_mirna_cancer_association(mirna_dict, expression_dict):
    """
    Connect miRNA sequences with cancer gene expression patterns.
    """
    results = []
    
    for mirna_id, mirna_seq in mirna_dict.items():
        for gene_name, expr_data in expression_dict.items():
            # Create a simple association based on sequence length and expression
            association_score = len(mirna_seq) * (expr_data['fold_change'] / 10)
            
            results.append({
                'miRNA': mirna_id,
                'gene': gene_name,
                'mirna_length': len(mirna_seq),
                'control_expr': expr_data['control'],
                'tumor_expr': expr_data['tumor'],
                'fold_change': expr_data['fold_change'],
                'association_score': association_score
            })
    
    return results

def print_results(results):
    """
    Print miRNA-gene association results.
    """
    print("\n" + "="*80)
    print("miRNA-CANCER GENE EXPRESSION ASSOCIATION")
    print("="*80)
    
    for result in results:
        print(f"\nmiRNA: {result['miRNA']}")
        print(f"  Sequence length: {result['mirna_length']} nucleotides")
        print(f"  Associated gene: {result['gene']}")
        print(f"    Control expression: {result['control_expr']}")
        print(f"    Tumor expression: {result['tumor_expr']}")
        print(f"    Fold change: {result['fold_change']:.2f}x")
        print(f"    Association score: {result['association_score']:.2f}")
        print("-" * 80)

def identify_dysregulated_genes(results, fold_change_threshold=2.0):
    """
    Find genes that are significantly dysregulated (overexpressed in tumor).
    """
    dysregulated = []
    
    for result in results:
        if result['fold_change'] > fold_change_threshold:
            dysregulated.append(result)
    
    print(f"\nGenes dysregulated in tumors (fold change > {fold_change_threshold}x):")
    for result in dysregulated:
        print(f"  {result['gene']}: {result['fold_change']:.2f}x upregulation")
        print(f"    Associated miRNA: {result['miRNA']}")

def main():
    print("Loading miRNA sequences...")
    mirnas = load_mirna_sequences("data/mirna_examples.fasta")
    print(f"Loaded {len(mirnas)} miRNAs")
    
    print("\nLoading cancer gene expression data...")
    expression = read_cancer_expression_data("data/cancer_gene_expression.csv")
    print(f"Loaded expression data for {len(expression)} genes")
    
    print("\nAnalyzing miRNA-cancer gene associations...")
    associations = analyze_mirna_cancer_association(mirnas, expression)
    
    # Print results
    print_results(associations)
    
    # Find dysregulated genes
    identify_dysregulated_genes(associations)

if __name__ == "__main__":
    main()
