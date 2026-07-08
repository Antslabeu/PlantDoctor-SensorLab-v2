Playground Roadmap

Purpose

Before designing the SensorLab architecture, we first need to understand the capabilities, workflow and limitations of the scientific tools that will become its foundation.

The objective of this phase is not to build SensorLab.

The objective is to build engineering knowledge.

SensorLab should be designed after we understand what scikit-fem can do well, where it requires additional abstraction and what engineering workflow feels natural.

⸻

M02 — scikit-fem Research & Playground

Goal

Explore scikit-fem through a series of focused engineering experiments.

No production architecture should be created during this milestone.

Avoid creating abstractions until they are justified by practical experience.

Principles

* Learn the library before designing around it.
* One experiment should answer one question.
* Prefer many small experiments over one complex project.
* Record observations continuously.

Suggested experiments

Mesh generation

* First mesh
* Rectangle mesh
* Triangular mesh
* Structured vs. unstructured meshes
* Mesh refinement
* Adaptive refinement

Boundary conditions

* Dirichlet boundaries
* Neumann boundaries
* Mixed boundary conditions
* Boundary markers

Materials

* Single material
* Multiple material regions
* Piecewise permittivity
* Material interfaces

Electrostatics

* Poisson equation
* Electric potential
* Electric field
* Field interpolation
* Flux computation
* Energy computation
* Capacitance estimation

Deliverables

* Collection of independent experiments.
* Understanding of the complete scikit-fem workflow.
* Initial list of strengths and limitations.
* List of features SensorLab will eventually abstract.

⸻

M03 — Visualization & Scientific Toolbox

Goal

Create a reusable visualization toolkit that allows every simulation to be understood and verified.

Visualization is not only for presentation.

Its primary purpose is debugging, validation and engineering insight.

Mesh visualization

* Nodes
* Elements
* Mesh refinement
* Boundary markers
* Material regions
* Labels

Field visualization

* Electric potential
* Electric field vectors
* Electric field magnitude
* Energy density
* Permittivity map

Advanced visualization

* Equipotential lines
* Streamlines / field lines
* Cross-sections
* Heatmaps
* Interactive inspection (optional)

Deliverables

* Reusable plotting utilities.
* Standard visualization workflow for every experiment.
* Ability to inspect every intermediate simulation result.

⸻

M04 — Engineering Knowledge Base

Goal

Transform experiments into structured engineering knowledge that will guide the design of SensorLab.

This milestone is still part of the research phase.

The focus is understanding—not building abstractions.

Experiment structure

Each experiment should become a small self-contained project.

Example:

experiments/
E01_first_mesh/
    README.md
    main.py
E02_boundary_conditions/
    README.md
    main.py
E03_material_regions/
    README.md
    main.py

Each README.md should contain:

* Goal
* Question being investigated
* Approach
* Code reference
* Results
* Conclusions
* Impact on future SensorLab design

Knowledge to collect

scikit-fem

* Strengths
* Weaknesses
* Performance
* API patterns
* Missing features
* Possible workarounds

Engineering observations

* Useful visualization techniques
* Frequently repeated code
* Candidate abstractions
* Solver limitations
* Future optimization opportunities

Final questions

By the end of M04 we should be able to answer:

* What should the SensorLab workflow look like?
* Which concepts deserve dedicated classes?
* Which parts can remain native scikit-fem objects?
* Which abstractions actually simplify engineering work?
* What information should a future SimulationResult expose?
* What should the public API hide from the user?

⸻

Transition to SensorLab

After completing M04 we will possess:

* practical experience with scikit-fem,
* a mature visualization toolkit,
* a documented engineering knowledge base,
* a clear understanding of the scientific workflow.

Only then should the implementation of the actual SensorLab architecture begin.

The architecture should emerge from practical experience rather than assumptions.

⸻

Guiding Principle

Understand the solver.
        ↓
Understand the results.
        ↓
Understand the engineering workflow.
        ↓
Design the architecture.
        ↓
Build SensorLab.

The objective of the playground phase is not writing production code.

The objective is gaining enough knowledge to design the right production code.