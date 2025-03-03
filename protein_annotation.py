import csv
from collections import defaultdict
import matplotlib.pyplot as plt
import random

# List of tuples containing the sequence ID and organism name
sequence_id_to_organism = [
    ('Q02880', 'Homo sapiens'),
    ('K7CLW1', 'Pan troglodytes'),
    ('A0A1X7QYU6', 'Kazachstania saulgeensis'),
    ('A0A314LG72', 'Nicotiana attenuata'),
    ('tr', 'Mucor lusitanicus'),
    ('W1DF98', 'Klebsiella pneumoniae'),
    ('UPI0003547499', 'Enterococcus faecalis'),
    ('P05653', 'Bacillus subtilis'),
    ('P0AES4', 'Escherichia coli'),
    ('Q8DQB4', 'Streptococcus pneumoniae'),
    ('Q2G2Q0', 'Staphylococcus aureus'),
    ('Q9HUK1', 'Pseudomonas aeruginosa'),
    ('Q6F6X8_ACIAD', 'Acinetobacter baylyi')
]

# Convert the list of tuples into a dictionary for easy lookup
sequence_to_organism_dict = {seq_id: organism for seq_id, organism in sequence_id_to_organism}

# Parse the TSV file to extract domain information
def parse_tsv(file_path):
    """Parse the TSV file to extract domain information."""
    sequences = defaultdict(lambda: defaultdict(list))
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        headers = next(reader)  # Skip the header row
        for row in reader:
            sequence_id = row[0]  # Extract the sequence ID directly
            if '|' in sequence_id:
                sequence_id = sequence_id.split('|')[1]  # Extract the sequence ID if it contains '|'
            domain_start = int(row[6])
            domain_end = int(row[7])
            domain_description = row[5]
            sequences[sequence_id][domain_description].append((domain_start, domain_end))
    return sequences

# Generate a distinct color for each unique domain description, avoiding white/light colors
def assign_colors(sequences, exclude_keywords):
    def random_color():
        while True:
            color = (random.random(), random.random(), random.random())
            if sum(color) / len(color) < 0.75:  # Ensuring the color is not too light
                return color

    domain_colors = {}
    for domains in sequences.values():
        for description in domains:
            if any(keyword in description.lower() for keyword in exclude_keywords):
                continue
            if description not in domain_colors:
                domain_colors[description] = random_color()
    return domain_colors

# Plot the protein domains
def plot_domains(sequences, domain_colors, sequence_to_organism_dict, exclude_keywords):
    fig, ax = plt.subplots(figsize=(15, 10))
    y_labels = []
    y_positions = []
    y = 0

    for seq_id, domains in sequences.items():
        organism_name = sequence_to_organism_dict.get(seq_id, seq_id)  # Use organism name if available
        y_labels.append(organism_name)
        y_positions.append(y)

        for description, coordinates in domains.items():
            if any(keyword in description.lower() for keyword in exclude_keywords):
                continue
            color = domain_colors[description]  # Consistent color for each domain type
            for start, end in coordinates:
                ax.plot([start, end], [y, y], linewidth=8, color=color, label=description if y == 0 else "")
        
        y += 1

    ax.set_yticks(y_positions)
    ax.set_yticklabels(y_labels)
    ax.set_xlabel('Position')
    ax.set_title('Protein Domain Visualization')
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys(), loc='upper right', bbox_to_anchor=(1.1, 1.05))
    plt.tight_layout()
    plt.show()

# Usage
tsv_file = 'prosite_results.tsv'

# Parse the TSV file
sequences = parse_tsv(tsv_file)

# List of keywords to exclude from coloring
exclude_keywords = ['-']

# Assign colors to domains
domain_colors = assign_colors(sequences, exclude_keywords)

# Print parsed information (for debugging)
print("\nParsed TSV Output:")
for seq_id, domains in sequences.items():
    print(f"Sequence ID: {seq_id}")
    print(f"  Unique Domain Count: {len(domains)}")
    for description, coordinates in domains.items():
        print(f"  {description}: {coordinates}")
    print()

# Plot the domains
plot_domains(sequences, domain_colors, sequence_to_organism_dict, exclude_keywords)


