import json
from pathlib import Path


# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

RESULTS_DIR = PROJECT_ROOT / "results"
RAW_DIR = RESULTS_DIR / "raw"
PROCESSED_DIR = RESULTS_DIR / "processed"
CIRCUITS_DIR = RESULTS_DIR / "circuits"
PLOTS_DIR = RESULTS_DIR / "plots"


def save_json(data, filepath):
    """Save a Python dictionary/list as a JSON file."""
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)

    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)


def save_hardware_counts(counts):
    """Save raw IBM Quantum hardware counts."""
    data = {
        f"circuit_{i}": circuit_counts
        for i, circuit_counts in enumerate(counts)
    }

    filepath = RAW_DIR / "hardware_counts.json"
    save_json(data, filepath)


def save_simulation_counts(counts):
    """Save raw local simulation counts."""
    data = {
        f"{x}{y}": circuit_counts
        for (x, y), circuit_counts in counts.items()
    }

    filepath = RAW_DIR / "simulation_counts.json"
    save_json(data, filepath)


def save_processed_results(results, filename="chsh_results.json"):
    """Save processed results to the processed results directory."""
    filepath = PROCESSED_DIR / filename
    save_json(results, filepath)