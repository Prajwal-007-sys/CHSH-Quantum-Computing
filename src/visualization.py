import matplotlib.pyplot as plt
from IPython.display import display
# cspell:ignore qiskit
from qiskit.visualization import plot_histogram  # type: ignore[import-not-found]


def draw_chsh_circuits(circuits, save=False, output_dir=None):
    for (x, y), circuit in circuits.items():
        print(f"(x,y) = ({x},{y})")

        fig = circuit.draw(output="mpl")

        if save and output_dir is not None:
            output_dir.mkdir(parents=True, exist_ok=True)
            filepath = output_dir / f"circuit_{x}{y}.png"
            fig.savefig(filepath, bbox_inches="tight")

        display(fig)


def plot_measurement_histograms(
    counts_list,
    labels=None,
    figsize=(10, 6),
    save=False,
    output_path=None
):
    if labels is None:
        labels = [
            "(x,y) = (0,0)",
            "(x,y) = (0,1)",
            "(x,y) = (1,0)",
            "(x,y) = (1,1)"
        ]

    fig = plot_histogram(
        counts_list,
        legend=labels,
        figsize=figsize
    )

    if save and output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, bbox_inches="tight")

    return fig


def plot_chsh_parameter(
    classical_S,
    hardware_S,
    quantum_S,
    save=False,
    output_path=None
):
    labels = [
        "Classical\nbound",
        "Hardware",
        "Quantum\nmaximum"
    ]

    values = [classical_S, hardware_S, quantum_S]

    fig = plt.figure(figsize=(8, 5))

    plt.bar(labels, values)
    plt.axhline(
        classical_S,
        linestyle="--",
        label="Classical bound"
    )
    plt.axhline(
        quantum_S,
        linestyle="--",
        label="Quantum maximum"
    )

    plt.ylabel("CHSH S")
    plt.title("CHSH Inequality: Hardware vs Theoretical Limits")
    plt.legend()

    if save and output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, bbox_inches="tight")

    plt.show()