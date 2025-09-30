from pathlib import Path
import csv
import logging
from typing import Iterable, Sequence

def load_signal_csv(path: Path) -> list[float]:
    """
    Load a single-column CSV of floats into a list.
    TODO:
      - Validate that path exists and is a file; else raise FileNotFoundError
      - Read rows; parse as float; collect into list
      - Use try/except to catch ValueError and log it (then re-raise)
    """
    # TODO: implement
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")
    
    values = []
    try:
        with path.open("r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                try:
                    val = float(row[0])
                    values.append(val)
                except ValueError as e:
                    logging.error(f"Failed to parse float from {row[0]}: {e}")
                    raise
    except Exception:
        logging.exception("Failed to load signal CSV")
        raise
    return values
    #return []

def save_features_csv(path: Path, rows: Iterable[Sequence[float]]) -> None:
    """
    Save a CSV with header: rms,zero_crossings,peak_to_peak,mad
    TODO:
      - Ensure parent dir exists (mkdir parents=True, exist_ok=True)
      - Write header and rows via csv.writer
    """
    # TODO: implement
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["rms", "zero_crossings", "peak_to_peak", "mad"])
        for row in rows:
            writer.writerow(row)
    #pass
