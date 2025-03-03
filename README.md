

```markdown
# Protein Annotation & Visualization

## Overview

This repository contains scripts and data for **protein sequence annotation and visualization**. The project utilizes **InterProScan** results to identify and plot **sequence domain architectures**, allowing for an intuitive representation of **protein functional elements** across different species. 

Key functionalities include:
- **Parsing InterProScan TSV results** to extract domain annotations.
- **Mapping sequence IDs to organisms** for meaningful visualization.
- **Generating protein domain architecture plots** using Matplotlib.
- **Identifying unique domain occurrences** across homologous sequences.

## Repository Structure

```
📂 protein-annotation-visualization
│── 📄 README.md                # Documentation for the repository
│── 📄 protein_annotation.py     # Script for parsing InterProScan results and plotting protein domains
│── 📄 protein_visualization.py  # Script for extracting and listing unique domain occurrences
│── 📂 data
│   ├── prosite_results.tsv      # InterProScan TSV output with domain annotations
│   ├── topoisomerase_msa.fasta  # FASTA file used for homology search
│── 📂 images
│   ├── protein_domains.png      # Example output of protein visualization
```

## How It Works

1. **Homology Search (HMMER)**
   - A **HMMER homology search** was performed using **DNA topoisomerase 2-alpha and 2-beta** as query sequences.
   - Hits were manually selected from a **diverse set of eukaryotic and prokaryotic species**.
   - Sequences were extracted in **FASTA format** and aligned using **Jalview**.

2. **Domain Annotation (InterProScan)**
   - The **FASTA file** was analyzed with **InterProScan**, generating a **TSV file** containing domain information.
   - This file includes **domain descriptions, positions, and associated sequence IDs**.

3. **Protein Domain Visualization**
   - The script `protein_annotation.py` processes the **TSV file** and plots **protein domain architectures**.
   - Each **protein sequence** is plotted as a horizontal line, with **domain annotations shown as colored segments**.
   - **Organism names** are used for labeling instead of raw sequence IDs.

4. **Domain Summary Extraction**
   - The script `protein_visualization.py` extracts **unique domains**, listing:
     - **Domain name**
     - **Associated sequences**
     - **Domain coordinates within each sequence**

## Installation & Requirements

To run the scripts, ensure you have **Python 3.x** installed with the following dependencies:

```sh
pip install matplotlib
```

## Usage

### 1️⃣ **Visualizing Protein Domains**
Run the `protein_annotation.py` script:

```sh
python protein_annotation.py
```

This will:
- Parse the **InterProScan TSV file**.
- Assign **colors** to unique domains.
- Generate a **domain architecture plot** for each sequence.

### 2️⃣ **Extracting Unique Domain Information**
Run the `protein_visualization.py` script:

```sh
python protein_visualization.py
```

This will:
- Parse the **TSV file**.
- List **unique domains** and their **sequence locations**.
- Print results to the terminal.

## Example Output

**Protein Domain Visualization**
![Protein Domains](images/protein_domains.png)

**Example Unique Domain Listing**
```
Domain: DNA Gyrase B subunit, carboxyl terminus
  Sequence ID: W1DF98, Organism: Klebsiella pneumoniae, Coordinates: [(252, 316)]
  Sequence ID: Q6F6X8_ACIAD, Organism: Acinetobacter baylyi, Coordinates: [(554, 616)]

Total unique domains: 44
```

## Customization

If using this tool with **different InterProScan results**, update the **sequence_id_to_organism** mapping in `protein_annotation.py`:

```python
sequence_id_to_organism = [
    ('YOUR_SEQUENCE_ID', 'Organism Name'),
    ...
]
```

## Contributions

Feel free to fork, modify, and submit **pull requests** if you'd like to contribute improvements!

## License

This project is **open-source** and available for research and educational purposes.
```

---
