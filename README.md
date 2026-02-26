# DFS Solver — 15-Puzzle Problem

A **Depth-First Search (DFS)** based solver for the classic **15-Puzzle problem**
(4×4 sliding tile puzzle), implemented using an object-oriented approach in Python.

>  Subject: Artificial Intelligence

---

## 📌 Problem Statement

The **15-Puzzle** consists of a 4×4 grid with 15 numbered tiles and one blank space (0).
The goal is to reach the following configuration by sliding tiles into the blank:
```
[ 1,  2,  3,  4]
[ 5,  6,  7,  8]
[ 9, 10, 11, 12]
[13, 14, 15,  0]
```

This implementation uses **DFS with a depth limit** to explore the state space
and find a valid solution path.

---

## 📂 Repository Structure
```
DFS-solver-15-puzzle-problem/
│
├── DFSsolver.py          # Core logic — PuzzleState, DFSSolver, Input, Output classes
└── DFSsolver_main.py     # Main script — sets up start/goal states and runs solver
```

---

## 🧠 Algorithm: Depth-First Search

### How it works

DFS explores the puzzle state space by going as deep as possible along each branch
before backtracking. A **depth limit** is enforced to prevent infinite loops in
the large 15-puzzle state space (~10 trillion possible states).
```
Stack-based DFS:
1. Push (start_state, path) onto stack
2. Pop state → check if goal
3. If not goal and depth ≤ max_depth → push all unvisited neighbors
4. Repeat until goal found or stack empty
```

### Key Design Choices
- **Visited set** prevents revisiting already-explored states
- **max_depth = 200** limits search depth to avoid memory overflow
- **Blank tile represented as 0** (standard 15-puzzle convention)
- **Goal state is fixed** — standard ordered configuration

---

## 🧩 Object-Oriented Structure

| Class | Responsibility |
|---|---|
| `PuzzleState` | Represents a single board state; handles neighbor generation and blank tile location |
| `DFSSolver` | Stack-based DFS with visited set and depth-limit control |
| `Input` | Handles user input — reads 16 tile values from terminal |
| `Output` | Displays solution path step-by-step |

---

## ⚙️ Implementation Details

- **State representation:** Immutable Python `tuple` of 16 integers (hashable for visited set)
- **Neighbor generation:** Checks all 4 directions (up, down, left, right) with boundary validation
- **Blank tile:** Represented as `0`
- **Depth limit:** Configurable via `max_depth` parameter (default: 200)

---

## 🔍 A* vs DFS — Key Difference

> This repo is a companion to the
> [A* Search — 15-Puzzle Solver](https://github.com/Shreyaa322/A-star-Search)

| Property | DFS | A* |
|---|---|---|
| Completeness | Limited (depth-bounded) | Yes |
| Optimality | No — finds *a* solution, not the *shortest* | Yes — finds shortest path |
| Speed | Can be fast for shallow solutions | Slower but smarter |
| Memory | Lower (stack-based) | Higher (priority queue + g-scores) |
| Heuristic | None | Misplaced Tiles h(n) |

DFS is useful when **any** valid solution is acceptable and memory is constrained.
A* is preferred when the **shortest** solution is required.

---

## 🚀 How to Run
```bash
# 1. Clone the repository
git clone https://github.com/Shreyaa322/DFS-solver-15-puzzle-problem-.git
cd DFS-solver-15-puzzle-problem-

# 2. Install dependencies
pip install numpy

# 3. Run the solver
python DFSsolver_main.py
```

### Example Interaction
```
Enter 16 numbers:
Enter number 1: 1
Enter number 2: 2
...
Enter number 16: 0

Solution found in N moves:
Step 0:
(1, 2, 3, 4)
(5, 6, 7, 8)
...
--------------------
```

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)

**Standard libraries used:** `numpy`

---

## 📄 License

Developed for academic purposes at COEP Technological University, Pune.
