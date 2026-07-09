# SensorLab Visualization Standard

Version: 1.0

---

# Philosophy

Visualization is not decoration.

Visualization is an engineering tool.

The objective of every figure is to support engineering decisions.

Every physical quantity should always be presented in the same visual form.
A user should recognize what is being displayed without reading the title.

Consistency is more important than artistic appearance.

---

# General Rules

## One quantity = one colormap

Each physical quantity has one default colormap.

The default should never change between experiments.

Example:

❌ Potential shown once with Viridis and once with Plasma.

✔ Potential is always shown using the same colors.

---

## Colors should reflect intuition

Whenever possible, colors should match human intuition.

Examples

High temperature
→ warm colors

High electric field
→ bright colors

Material distribution
→ grayscale

Positive / negative potential
→ red / blue

---

## Mesh should never dominate the visualization

The mesh is only computational infrastructure.

Default style:

- thin
- light
- semi-transparent

The physical result should always be the dominant element.

---

## Equal aspect ratio

Unless explicitly required otherwise:

```python
ax.set_aspect("equal")
```

Geometric distortion should never be introduced.

---

# Standard Colormaps

| Physical quantity | Default colormap | Rationale |
|-------------------|------------------|-----------|
| Electric potential | `RdBu_r` | Natural positive ↔ negative interpretation |
| Electric field magnitude \|E\| | `inferno` | Strong fields appear visually "hot" |
| Electric energy density | `plasma` | Smooth monotonic intensity |
| Relative permittivity εr | `Greys` | Material property rather than field quantity |
| Sensitivity maps | `magma` | Excellent contrast for optimization problems |

---

# Vector Fields

Vector fields should not rely on color alone.

Preferred order:

1. Streamlines
2. Quiver arrows
3. Magnitude overlay (optional)

Default arrow color:

```text
black
```

unless arrows are intentionally colored by magnitude.

---

# Mesh Appearance

Default:

```text
color      = white
linewidth  = 0.2
alpha      = 0.35
```

The mesh should remain visible while never hiding the solution.

---

# Electrodes

Electrodes should have consistent colors.

| Type | Color |
|------|-------|
| Positive | Red |
| Negative | Blue |
| Ground | Black |
| Floating | Gray |

---

# Materials

Materials should not use rainbow colormaps.

Recommended:

Air
→ white

FR4
→ light green

Copper
→ orange

Water
→ blue

Soil
→ brown

Unknown material
→ gray

Discrete colors should always be preferred over gradients for material maps.

---

# Figure Layout

Default figure size:

```python
figsize = (8, 8)
```

Axis labels:

```text
x
y
```

Colorbar:

Always present for scalar quantities.

Label example:

```text
Potential [V]

Electric field [V/m]

Energy density [J/m³]

Relative permittivity [-]
```

---

# Titles

Titles should describe the physical quantity.

Good:

```text
Electric potential

Electric field magnitude

Relative permittivity

Sensitivity map
```

Avoid:

```text
Result

Plot 1

Simulation

Figure
```

---

# Numerical Visualization Rules

Visualization should never hide numerical artefacts.

Do not:

- smooth noisy results
- interpolate only for aesthetics
- manipulate color scales to exaggerate effects

Scientific correctness has priority over appearance.

---

# SensorLab API

Experiments should never specify colormaps directly.

Instead of

```python
plt.tricontourf(
    ...,
    cmap="RdBu_r",
)
```

use

```python
plot_potential(...)
```

Instead of

```python
plt.tricontourf(
    ...,
    cmap="inferno",
)
```

use

```python
plot_field(...)
```

The visualization layer is responsible for selecting:

- colormap
- mesh appearance
- colorbar
- labels
- titles

This guarantees a consistent visual language across the entire project.

---

# Future Extensions

The visualization module should eventually provide:

```python
plot_mesh(mesh)

plot_potential(mesh, potential)

plot_field(mesh, field)

plot_energy(mesh, energy)

plot_materials(mesh, materials)

plot_sensitivity(mesh, sensitivity)

plot_streamlines(mesh, field)

plot_equipotential_lines(mesh, potential)
```

Experiments should only specify **what** they want to visualize.

The visualization module should decide **how** it is presented.

---

# Design Principle

The visualization is part of the engineering workflow.

The user should focus on understanding the physics,
not on configuring plotting libraries.