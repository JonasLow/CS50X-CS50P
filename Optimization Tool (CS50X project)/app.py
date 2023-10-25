from scipy.optimize import linprog
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        x = float(request.form.get('x'))
        y = float(request.form.get('y'))
        z = float(request.form.get('z'))
        cost_corn = float(request.form.get('cost_corn'))
        cost_soybean = float(request.form.get('cost_soybean'))

        # Objective function coefficients (minimize cost)
        c = [cost_corn, cost_soybean]

        # Coefficients for the inequality constraints (protein and fiber requirements)
        A = [
            [-1, -1],
            [0.01 * y - 0.09, 0.01 * y - 0.60],  # Coefficients for protein (to be >= y)
            [-0.01 * z + 0.02, -0.01 * z + 0.06],  # Coefficients for fiber (to be <= z)
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

            return render_template('results.html', minimum_cost=minimum_cost, corn_amount=corn_amount, soybean_amount=soybean_amount)

        else:
            return "The problem is infeasible or unbounded."

    # Render the calculate.html template for GET requests
    return render_template('calculate.html')

if __name__ == '__main__':
    app.run(debug=True)
