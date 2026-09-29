# Quick start guide for running the scripts in VS Code

## Installation

1. Open VS Code
2. Open the terminal in VS Code (Ctrl + ` or View → Terminal)
3. Run this command:
   ```
   pip install -r requirements.txt
   ```
   This installs Biopython (the only library you need)

## Running Scripts

### Method 1: Run directly in VS Code
1. Open any Python file (e.g., `01_load_mirna_sequences.py`)
2. Click the "Run" button (play icon) in the top right
3. See the output in the terminal

### Method 2: Run from terminal
1. Open terminal in VS Code
2. Type:
   ```
   python src/01_load_mirna_sequences.py
   ```
   Or:
   ```
   python src/02_target_prediction.py
   ```

## Script Order (Recommended)

1. **01_load_mirna_sequences.py** - Learn how to load and analyze sequences
2. **02_target_prediction.py** - Predict which genes miRNAs might target
3. **03_sequence_alignment.py** - Compare miRNA sequences
4. **04_genbank_parser.py** - Parse GenBank format files
5. **05_cancer_metabolomics_integration.py** - Link miRNA to cancer gene expression

## What Each Script Does

### Script 1: Load miRNA Sequences
- Reads FASTA files
- Calculates GC content (% of G and C nucleotides)
- Counts nucleotides (A, U, G, C)

### Script 2: Target Prediction
- Finds miRNA seed region (7 nucleotides)
- Checks reverse complement in target genes
- Predicts which genes are likely targets

### Script 3: Sequence Alignment
- Compares two miRNA sequences
- Calculates similarity percentage
- Uses Biopython's pairwise alignment

### Script 4: GenBank Parser
- Reads GenBank format files
- Extracts gene features (genes, CDS, etc.)
- Extracts coding sequences

### Script 5: Cancer Integration
- Loads miRNA sequences
- Loads cancer gene expression data
- Links miRNA to cancer genes
- Finds dysregulated genes

## Troubleshooting

**Error: ModuleNotFoundError: No module named 'Bio'**
- Solution: Run `pip install biopython` in the terminal

**Error: FileNotFoundError: [Errno 2] No such file or directory**
- Solution: Make sure you're running the script from the correct folder
- The script looks for files in the `data/` folder

**Script doesn't produce output**
- Make sure you click the "Run" button or use `python src/filename.py`
- Check that the data files exist in the `data/` folder

## What You'll Learn

✓ Biopython basics (SeqIO, Seq, pairwise2)
✓ FASTA file parsing
✓ Sequence analysis (GC content, nucleotide counting)
✓ Reverse complement
✓ Sequence alignment
✓ GenBank file parsing
✓ CSV file reading
✓ Cancer genomics concepts

