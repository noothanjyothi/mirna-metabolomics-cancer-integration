# Script 4: Parse GenBank files
# Extract information from GenBank format files

from Bio import SeqIO

def parse_genbank(genbank_file):
    """
    Read and display information from GenBank file.
    """
    print(f"Reading GenBank file: {genbank_file}\n")
    
    records = SeqIO.parse(genbank_file, "genbank")
    
    for record in records:
        print(f"ID: {record.id}")
        print(f"Description: {record.description}")
        print(f"Sequence length: {len(record.seq)} bp")
        print(f"Sequence: {str(record.seq)}")
        print(f"\nFeatures found:")
        
        for feature in record.features:
            print(f"  - Type: {feature.type}")
            print(f"    Location: {feature.location}")
            
            # Print qualifiers (metadata about the feature)
            for qual_key in feature.qualifiers:
                qual_value = feature.qualifiers[qual_key]
                print(f"    {qual_key}: {qual_value}")
        
        print("\n" + "-" * 50)

def extract_cds_sequences(genbank_file):
    """
    Extract only the coding sequences (CDS) from GenBank file.
    CDS = Coding DNA Sequence (protein-coding genes)
    """
    print(f"\nExtracting CDS from: {genbank_file}\n")
    
    cds_count = 0
    for record in SeqIO.parse(genbank_file, "genbank"):
        for feature in record.features:
            if feature.type == "CDS":
                cds_count += 1
                location = feature.location
                start = location.start
                end = location.end
                
                # Extract the coding sequence
                cds_seq = record.seq[start:end]
                
                print(f"CDS #{cds_count}")
                print(f"Location: {start}-{end}")
                print(f"Sequence: {cds_seq}")
                print(f"Length: {len(cds_seq)} bp")
                print("-" * 40)
    
    print(f"Total CDS found: {cds_count}")

def main():
    genbank_file = "data/example.gb"
    
    # Parse and display all information
    parse_genbank(genbank_file)
    
    # Extract only CDS
    extract_cds_sequences(genbank_file)

if __name__ == "__main__":
    main()
