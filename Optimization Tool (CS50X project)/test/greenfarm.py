from scipy.optimize import linprog

# Input values
x = float(input("Enter the amount of Special Feed Needed Daily (x): "))
y = float(input("Enter the Minimum Protein Requirement (%): "))
z = float(input("Enter the Maximum Fiber Requirement (%): "))
cost_corn = float(input("Enter the Cost of Corn (per kg): "))
cost_soybean = float(input("Enter the Cost of Soybean Meal (per kg): "))

# Objective function coefficients (minimize cost)
c = [cost_corn, cost_soybean]

# Coefficients for the inequality constraints (protein and fiber requirements)
A = [
    [-1, -1],
    [0.01*y - 0.09, 0.01*y - 0.60],  # Coefficients for protein (to be >= y)
    [-0.01*z + 0.02, -0.01*z + 0.06],    # Coefficients for fiber (to be <= z)
]

# Right-hand side values of the inequality constraints
b = [-x, 0, 0]

# Bounds for the variables (corn and soybean meal)
x_bounds = (0, None)
y_bounds = (0, None)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

if result.success:
    minimum_cost = result.fun
    corn_amount, soybean_amount = result.x
    print(f"Minimum cost: ${minimum_cost:.2f}")
    print(f"Amount of corn needed: {corn_amount:.2f} kg")
    print(f"Amount of soybean meal needed: {soybean_amount:.2f} kg")
else:
    print("The problem is infeasible or unbounded.")

