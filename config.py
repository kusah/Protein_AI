from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

FASTA_DIR = DATA_DIR / "fasta"
PDB_DIR = DATA_DIR / "pdb"
PREDICTED_DIR = DATA_DIR / "predicted"

REPORT_DIR = BASE_DIR / "reports"

ASSETS_DIR = BASE_DIR / "assets"

for folder in [
    FASTA_DIR,
    PDB_DIR,
    PREDICTED_DIR,
    REPORT_DIR,
]:
    folder.mkdir(parents=True, exist_ok=True)