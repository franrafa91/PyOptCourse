from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('GLOP')

x = solver.NumVar(0,10,'x')
y = solver.NumVar(0,10,'y')

solver.Add(-x+2*y<=8)
solver.Add(2*x+y<=14)
solver.Add(2*x-y<=10)

solver.Maximize(x+y)

results = solver.Solve()

print(f"Optimal value pair: {x.solution_value()},{y.solution_value()}")
print(f"Optimized result: {results}")