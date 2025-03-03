# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 22:32:58 2024

@author: Isaac
"""

import pyomo.environ as pyo


#Parameters
#Values for Row(R), Columns(C), Values (V)
R = [1,2,3,4,5,6,7,8,9]
C = [1,2,3,4,5,6,7,8,9]
V = [1,2,3,4,5,6,7,8,9]
N = 9
P = 21
#dictionary for prefilled values
v = {(1,1): 1, (1,2): 1, (1,3): 8, (2,1): 2, (2,2): 3, (2,3): 3,
     (3,1): 2, (3,2): 4, (3,3): 6, (4,1): 3, (4,2): 2, (4,3): 7,
     (5,1): 3, (5,2): 5, (5,3): 9, (6,1): 3, (6,2): 7, (6,3): 2,
     (7,1): 4, (7,2): 2, (7,3): 5, (8,1): 4, (8,2): 6, (8,3): 7,
     (9,1): 5, (9,2): 5, (9,3): 4, (10,1): 5, (10,2): 6, (10,3): 5,
     (11,1): 5, (11,2): 7, (11,3): 7, (12,1): 6, (12,2): 4, (12,3): 1,
     (13,1): 6, (13,2): 8, (13,3): 3, (14,1): 7, (14,2): 3, (14,3): 1,
     (15,1): 7, (15,2): 8, (15,3): 6, (16,1): 7, (16,2): 9, (16,3): 8,
     (17,1): 8, (17,2): 3, (17,3): 8, (18,1): 8, (18,2): 4, (18,3): 5,
     (19,1): 8, (19,2): 8, (19,3): 1, (20,1): 9, (20,2): 2, (20,3): 9,
     (21,1): 9, (21,2): 7, (21,3): 4}

#initialize model
sud = pyo.ConcreteModel()

#Declare variables x[r,c,n] - Binary Consraint
sud.x = pyo.Var(R, C, V, domain=pyo.Binary)

#Objective function: no objective, just solve
sud.obj = pyo.Objective(rule = 0, sense = pyo.maximize)

#Constraints
#One number per cell
def cell (model, r, c):
    return sum(sud.x[r, c, n]
               for n in V) == 1
sud.cell_c = pyo.Constraint(R, C, rule = cell)
#Each number appears once in each row
def row (model, r, n):
    return sum(sud.x[r, c, n]
               for c in C) == 1
sud.row_c = pyo.Constraint(R, V, rule = row)
#Each number appears once in each column
def column (model, c, n):
    return sum(sud.x[r, c, n]
               for r in R) == 1
sud.col = pyo.Constraint(C, V, rule = column)
#Each number appears once in each block
def block (model, j, i, n):
    return sum(sud.x[r + j * int(N**0.5)+1, c + i * int(N**0.5)+1, n]
               for r in range(int(N**0.5))
               for c in range (int(N**0.5))) == 1
sud.unique = pyo.Constraint(range(int(N**0.5)-1), range(int(N**0.5)-1), V, rule = block)
#Prefilled values
def pre (model, p):
    return sud.x[v[p,1], v[p,2], v[p,3]] == 1
sud.val = pyo.Constraint(range(1, P+1), rule = pre)

#Solve the model
results = pyo.SolverFactory("glpk").solve(sud, tee = True)
print(results)

#Output Result
#9x9 empty sudoku grid
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
#Iterate over each cell
for r in range(1, N+1):
    for c in range(1, N+1):
        for n in range(1, N+1):
            #check for n solution in cell r,c
            if pyo.value(sud.x[r, c, n]) == 1:
                #fill in the grid, -1 for 0 based index
                grid[r-1][c-1] = n
grid
                



