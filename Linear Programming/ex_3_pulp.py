import pulp as pl

model = pl.LpProblem('Ex',pl.LpMaximize)
x = pl.LpVariable('x',0,10)
y = pl.LpVariable('y',0,10)

model +=  -x + 2*y <= 8
model += 2*x +   y <=14
model += 2*x -   y <=10

model += x+y

status = model.solve()

x_val = pl.value(x)
y_val = pl.value(y)

print("-"*30)
print(f"Optimal solution pair: ({x_val},{y_val})")