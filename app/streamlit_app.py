import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

import streamlit as st
from src.fasta_parser import read_fasta
from src.sequence_validator import validate_sequence, get_sequence_statistics
from config import FASTA_DIR

st.set_page_config(
    page_title="ProteinAI",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 ProteinAI")
st.markdown("### AI-Powered Protein Structure Prediction & Analysis Platform")

st.info(
    """
Upload a protein sequence in FASTA format.

ProteinAI will:

✅ Validate the sequence

✅ Calculate protein statistics

🔜 Search the Protein Data Bank (PDB)

🔜 Predict unknown protein structures

🔜 Visualize proteins in 3D

🔜 Generate scientific reports
"""
)

uploaded_file = st.file_uploader(
    "Upload Protein FASTA File",
    type=["fasta", "fa", "faa"]
)

if uploaded_file:

    save_path = FASTA_DIR / uploaded_file.name

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    protein = read_fasta(save_path)

    st.success("Protein uploaded successfully!")

    st.divider()

    st.subheader("Protein Information")

    st.write("**Protein ID:**", protein["id"])
    st.write("**Description:**", protein["description"])

    sequence = protein["sequence"]

    valid, invalid = validate_sequence(sequence)

    if valid:

        st.success("Protein sequence is valid.")

        stats = get_sequence_statistics(sequence)

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Sequence Length", stats["Length"])

        with col2:
            st.metric("Molecular Weight", f"{stats['Molecular Weight']} Da")

        st.subheader("Amino Acid Composition")

        st.dataframe(stats["Composition"])

        st.subheader("Protein Sequence")

        st.code(sequence)

    else:

        st.error(f"Invalid amino acids found: {', '.join(invalid)}")