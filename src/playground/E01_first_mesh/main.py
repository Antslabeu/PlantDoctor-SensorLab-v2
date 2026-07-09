import matplotlib.pyplot as plt
import numpy as np
from skfem import MeshTri


def main():
    x = np.linspace(0.0, 1.0, 10)
    y = np.linspace(0.0, 1.0, 10)

    mesh = MeshTri.init_tensor(x, y)

    print(mesh.p)

    # Wyświetlamy podstawowe informacje
    print("=== Mesh information ===")
    print(f"Type: {type(mesh).__name__}")
    print(f"Dimension: {mesh.dim()}")
    print(f"Nodes: {mesh.p.shape[1]}")
    print(f"Elements: {mesh.t.shape[1]}")

    # Rysujemy siatkę
    fig, ax = plt.subplots(figsize=(6, 6))
    mesh.draw(ax=ax)

    ax.set_title("E01 - First Mesh")
    ax.set_aspect("equal")

    plt.show()


if __name__ == "__main__":
    main()
