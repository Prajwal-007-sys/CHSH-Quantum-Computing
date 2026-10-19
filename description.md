# CHSH Game — File Description and Execution Guide

## 1. Project Overview

This project implements the CHSH (Clauser-Horne-Shimony-Holt) game using both classical and quantum strategies.

It includes:
- Classical CHSH strategy and simulation
- Quantum strategy using a Bell state
- Local simulation using Qiskit Aer
- Execution on IBM Quantum hardware
- Correlation, CHSH parameter, and winning-probability analysis
- Visualization of circuits and measurement results
- Saving of raw and processed results

## 2. Project Structure

```text
CHSH-Quantum-Computing/
├── src/
│   ├── __init__.py
│   ├── classical.py
│   ├── quantum_strategy.py
│   ├── circuits.py
│   ├── simulation.py
│   ├── hardware.py
│   ├── analysis.py
│   ├── visualization.py
│   └── results_io.py
├── notebook/
│   └── chsh_implementation.ipynb
├── results/
│   ├── raw/
│   ├── processed/
│   ├── circuits/
│   └── plots/
├── requirements.txt
├── README.md
└── description.md
```

## 3. Source Code Files

### `src/__init__.py`
Initializes the `src` directory as a Python package. It contains no implementation code.

### `src/classical.py`
Implements the classical CHSH strategy and simulation.

Main functions:
- `classical_strategy()`
- `chsh_game()`
- `simulate_classical_strategy()`

The classical strategy has a theoretical winning probability of 75% and CHSH bound of 2.

### `src/quantum_strategy.py`
Contains the theoretical measurement settings used by the quantum CHSH strategy.

Main functions:
- `get_alice_angle()`
- `get_bob_angle()`
- `get_measurement_settings()`

### `src/circuits.py`
Constructs the four quantum circuits used in the CHSH experiment.

Main functions:
- `prepare_bell_state()`
- `chsh_circuit()`
- `create_all_chsh_circuits()`

The four input combinations are `(0,0)`, `(0,1)`, `(1,0)`, and `(1,1)`.

### `src/simulation.py`
Runs the CHSH circuits locally using Qiskit Aer.

Main functions:
- `run_circuit()`
- `run_chsh_simulation()`
- `quantum_strategy()`

Local simulation does not require IBM Quantum credentials.

### `src/hardware.py`
Provides functions for connecting to IBM Quantum, transpiling circuits, submitting jobs, and retrieving results.

Main functions:
- `connect_to_ibm()`
- `get_backend()`
- `create_sampler()`
- `transpile_for_backend()`
- `run_on_hardware()`
- `get_job_result()`
- `get_counts_from_result()`

Authentication credentials must not be committed to the repository.

### `src/analysis.py`
Performs mathematical analysis of measurement results.

Main functions:
- `calculate_correlation_from_counts()`
- `calculate_chsh_parameter()`
- `calculate_winning_probability_from_counts()`
- `calculate_all_correlations()`
- `calculate_overall_winning_probability()`
- `calculate_theoretical_values()`

The CHSH parameter is:

$$
S = E_{00} + E_{01} + E_{10} - E_{11}
$$

The classical bound is $S \leq 2$, while the ideal quantum maximum is $2\sqrt{2}$.

### `src/visualization.py`
Creates circuit diagrams, measurement histograms, and CHSH comparison plots.

Main functions:
- `draw_chsh_circuits()`
- `plot_measurement_histograms()`
- `plot_chsh_parameter()`

The functions can display plots and optionally save them to the `results/` directory.

### `src/results_io.py`
Handles saving raw and processed results as JSON files.

Main functions:
- `save_json()`
- `save_hardware_counts()`
- `save_simulation_counts()`
- `save_processed_results()`

## 4. Notebook

### `notebook/chsh_implementation.ipynb`

This is the main executable notebook. It imports functionality from the `src/` modules and performs the complete workflow:

1. Set up the project path.
2. Import project modules.
3. Configure IBM Quantum access.
4. Simulate the classical strategy.
5. Construct and display the four quantum circuits.
6. Run local Qiskit Aer simulation.
7. Calculate simulation correlations and CHSH parameter.
8. Transpile circuits for IBM Quantum hardware.
9. Retrieve or execute a hardware job.
10. Calculate hardware correlations and CHSH parameter.
11. Calculate winning probabilities.
12. Compare classical, simulation, hardware, and ideal quantum results.
13. Save results and figures.

## 5. Results Directory

### `results/raw/`
Contains original measurement counts:
- `simulation_counts.json` — local simulation counts.
- `hardware_counts.json` — IBM Quantum hardware counts.

### `results/processed/`
Contains calculated results:
- `simulation_results.json`
- `hardware_results.json`
- `final_comparison.json`

### `results/circuits/`
Contains the four generated circuit diagrams:
- `circuit_00.png`
- `circuit_01.png`
- `circuit_10.png`
- `circuit_11.png`

### `results/plots/`
Contains:
- `hardware_measurement_histograms.png`
- `chsh_comparison.png`

## 6. Requirements

### `requirements.txt`

Contains the Python dependencies required for the project:

```text
qiskit
qiskit-aer
qiskit-ibm-runtime
matplotlib
numpy
```

## 7. How to Execute

### Step 1 — Create a virtual environment

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

### Step 2 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3 — Start Jupyter

```bash
jupyter notebook
```

or:

```bash
jupyter lab
```

Open:

```text
notebook/chsh_implementation.ipynb
```

Run the notebook from top to bottom.

## 8. IBM Quantum Hardware Execution

Hardware execution requires an IBM Quantum account and an accessible backend.

The notebook separates hardware job submission from job retrieval. The submission cell is intentionally commented out so that running the notebook does not accidentally submit a new hardware job.

When a new hardware experiment is required:

1. Configure IBM Quantum credentials.
2. Select the backend.
3. Transpile the circuits.
4. Submit the job.
5. Record the job ID.
6. Retrieve the job using its ID.
7. Analyze the returned counts.

Previously submitted jobs can be retrieved without submitting another job.

## 9. Expected Theoretical Results

| Quantity | Classical | Ideal Quantum |
|---|---:|---:|
| Winning probability | 75% | ~85.36% |
| CHSH parameter | 2 | ~2.828 |

Real hardware results may differ from the ideal quantum prediction because of noise and hardware imperfections.

## 10. Credentials

IBM Quantum API tokens and other private authentication credentials must not be included in the submitted repository.

Use placeholders such as:

```python
token = "API_token"
```

and configure credentials locally.
