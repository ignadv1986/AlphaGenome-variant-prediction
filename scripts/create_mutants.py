from Bio import SeqIO
import re

# Define wild-type to mutant mappings
motif_mutants = {
    "CH1UE":   ("TGTGTTA", "TGTGATA"),
    "H1_box":  ("AAACACA", "AGACGCA"),
    "TATA_box":("TATATA",  "TAGATA"),
}

input_fasta = "H1_promoters_clean.fa"
output_fasta = "H1_promoters_with_mutants.fa"

mutant_records = []

for record in SeqIO.parse(input_fasta, "fasta"):
    seq_str = str(record.seq).upper()
    mutant_records.append(record)  # Keep original (wild-type)

    for motif_name, (wt, mut) in motif_mutants.items():
        if wt in seq_str:
            # Replace first occurrence
            mutated_seq = seq_str.replace(wt, mut, 1)
            new_id = f"{record.id}_mut_{motif_name}"
            new_description = f"{record.description} [mutated {motif_name}]"
            mutant_record = record[:]
            mutant_record.id = new_id
            mutant_record.description = new_description
            mutant_record.seq = mutated_seq
            mutant_records.append(mutant_record)

# Write to output
with open(output_fasta, "w") as out_f:
    SeqIO.write(mutant_records, out_f, "fasta")

print(f"Mutant sequences written to {output_fasta}")

