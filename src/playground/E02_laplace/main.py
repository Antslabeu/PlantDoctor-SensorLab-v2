import matplotlib.pyplot as plt
import numpy as np
from skfem import Basis, BilinearForm, MeshTri, asm, condense, solve
from skfem.element import ElementTriP1
from skfem.helpers import dot, grad
from skfem.visuals.matplotlib import draw

# ==========================================================
# Simulation parameters
# ==========================================================

DOMAIN_SIZE = 1.0
GRID_POINTS = 31
LEFT_VOLTAGE = 3.3
RIGHT_VOLTAGE = 1

# ==========================================================
# Create computational mesh
# ==========================================================

x = np.linspace(
    -DOMAIN_SIZE,
    DOMAIN_SIZE,
    GRID_POINTS,
)

y = np.linspace(
    -DOMAIN_SIZE,
    DOMAIN_SIZE,
    GRID_POINTS,
)

mesh = MeshTri.init_tensor(x, y)

# ==========================================================
# Finite element
# ==========================================================

element = ElementTriP1()
basis = Basis(mesh, element)

# ==========================================================
# Weak formulation of Laplace equation
# ==========================================================

@BilinearForm
def laplace(u, v, w):
    return dot(grad(u), grad(v))

# ==========================================================
# Assemble global stiffness matrix
# ==========================================================

A = asm(laplace, basis)

# ==========================================================
# Find boundary degrees of freedom
# ==========================================================

left = basis.get_dofs(lambda x: np.isclose(x[0], -DOMAIN_SIZE))
right = basis.get_dofs(lambda x: np.isclose(x[0], DOMAIN_SIZE))

# ==========================================================
# Inspect boundary DOFs
# ==========================================================

print("\n========== BOUNDARIES ==========")

print(f"Left boundary DOFs : {left.nodal['u']}")
print(f"Right boundary DOFs: {right.nodal['u']}")

# ==========================================================
# Apply Dirichlet boundary conditions
# ==========================================================

boundary_dofs = np.concatenate([
    left.nodal["u"],
    right.nodal["u"],
])

boundary_values = np.concatenate([
    np.full(len(left.nodal["u"]), LEFT_VOLTAGE),
    np.full(len(right.nodal["u"]), RIGHT_VOLTAGE),
])

# ==========================================================
# Solve Laplace equation
# ==========================================================

# Right-hand side of Laplace equation (no source term)
b = np.zeros(basis.N)

# Initial vector containing prescribed Dirichlet values
x = np.zeros(basis.N)
x[boundary_dofs] = boundary_values

A_bc, b_bc, x_bc, I = condense(
    A,
    b,
    x=x,
    D=boundary_dofs,
)

solution = solve(A_bc, b_bc)

# Reconstruct the complete solution vector
potential = x_bc.copy()
potential[I] = solution

# ==========================================================
# Visualize electric potential
# ==========================================================

fig, ax = plt.subplots(figsize=(8, 8))

contour = ax.tricontourf(
    mesh.p[0],
    mesh.p[1],
    mesh.t.T,
    potential,
    levels=30,
    cmap="RdBu_r",
)

# Draw the mesh on top of the solution
ax.triplot(
    mesh.p[0],
    mesh.p[1],
    mesh.t.T,
    color="white",
    linewidth=0.2,
    alpha=0.35,
)

fig.colorbar(contour, ax=ax, label="Potential [V]")

ax.set_title("Solution of Laplace equation")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_aspect("equal")

plt.show()