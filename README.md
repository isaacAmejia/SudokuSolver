# SudokuSolver
This Sudoku solver is implemented in Python using the Pyomo optimization library, designed to handle complex constraint satisfaction problems. The solver models the 9x9 Sudoku grid as a binary decision matrix, where each cell can contain only one number from 1 to 9. Constraints are applied to ensure that each number appears exactly once in every row, column, and 3x3 block, adhering to the fundamental rules of Sudoku.

The model integrates the GLPK solver to compute valid solutions efficiently, leveraging mathematical optimization techniques to determine the correct placement of numbers. Pre-filled values are incorporated into the model as fixed constraints, ensuring the solver respects the initial puzzle setup.

This project demonstrates expertise in constraint programming, linear programming, and optimization techniques while utilizing Pyomo for modeling and solver integration. The approach used here can be extended to other constraint-based problems, making it a valuable demonstration of mathematical optimization applied to real-world puzzles.
