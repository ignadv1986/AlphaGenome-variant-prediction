from pyfaidx import Fasta

# Load genome
genome = Fasta("hg38.fa")

H1-0 promoter region
chrom = "chr22"
start = 37803229
end = 37805229

promoter_seq = genome[chrom][start:end].seq.upper()

# Your motif of interest
wt_motif = "AAACACA"
mutated_base_index = 1  # 0-based index within motif, e.g., second base

# Find motif
relative_pos = promoter_seq.find(wt_motif)

if relative_pos == -1:
    print("Motif not found.")
else:
    genomic_pos = start + relative_pos + mutated_base_index
    ref_base = promoter_seq[relative_pos + mutated_base_index]
    print(f"Found motif at position: {start + relative_pos}")
    print(f"Genomic mutation: {chrom}:{genomic_pos + 1} {ref_base} > [YOUR_MUTATION]")


