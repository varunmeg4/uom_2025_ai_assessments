# Optional CLI using typer
import typer, logging
from pathlib import Path
import numpy as np

from .io import load_signal_csv, save_features_csv
from .features import feature_vector
from .vectorize import python_rms, numpy_rms
from .generators import chunks
from time import perf_counter

app = typer.Typer(help="Intermediate Python Lab CLI")

@app.command()
def generate_data(out: Path = typer.Option(Path("data/signal.csv"), help="Output CSV path"),
                  n: int = 4000,
                  noise: float = 0.15):
    """
    Generate synthetic signal data (sine + square mixture) and save to CSV.
    TODO:
      - Implement signal synthesis similar to dataset seeded in data/signal.csv
    """
    import csv
    import math

    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as f:
        writer = csv.writer(f)
        for i in range(n):
            t = i / n * 10 * math.pi  # 5 full sine periods
            sine = math.sin(t)
            square = 1.0 if (t % (2*math.pi)) < math.pi else -1.0
            value = sine + square + noise * np.random.randn()
            writer.writerow([value])
    typer.echo(f"Generated synthetic data with {n} points to {out}")
    #typer.echo("TODO: implement generate_data")

@app.command()
def run_pipeline(inp: Path = Path("data/signal.csv"),
                 out: Path = Path("data/features.csv"),
                 chunk: int = 256):
    """
    Stream the input CSV in chunks, compute features per chunk, and save to CSV.
    TODO:
      - Use load_signal_csv, slice into chunks, compute feature_vector on each chunk (np.array)
      - Save with save_features_csv
    """
    data = load_signal_csv(inp)
    feature_rows = []
    for chunk_data in chunks(data, chunk):
        arr = np.array(chunk_data)
        features = feature_vector(arr)
        feature_rows.append(features)
    save_features_csv(out, feature_rows)
    typer.echo(f"Processed {len(data)} points in chunks of {chunk}, saved features to {out}")
    #typer.echo("TODO: implement run_pipeline")

@app.command()
def profile():
    """
    Profile Python vs NumPy RMS on a large array and print timings.
    TODO:
      - Create 1e6 random floats (np.random.randn)
      - Time pure-python and numpy versions; print ms
    """
    size = int(1e6)
    data = np.random.randn(size)

    start = perf_counter()
    py_rms = python_rms(data.tolist())
    py_time = (perf_counter() - start) * 1000

    start = perf_counter()
    np_rms = numpy_rms(data)
    np_time = (perf_counter() - start) * 1000

    typer.echo(f"Python RMS: {py_rms:.6f} in {py_time:.2f} ms")
    typer.echo(f"NumPy RMS: {np_rms:.6f} in {np_time:.2f} ms")
    #typer.echo("TODO: implement profile")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app()
