# Operation Research - Minimum Cost Feed Mix Calculator
#### Video Demo: https://www.youtube.com/watch?v=UtIOYCBLUH8
#### Description:
**Minimum Cost Feed Mix Calculator**
===================

The Minimum Cost Feed Mix Calculator is a Python Flask web application that helps you determine the optimal combination of feed ingredients for a livestock diet. Whether you're a farmer, animal nutritionist, or anyone involved in livestock management, this tool simplifies the process of formulating a cost-effective and nutritionally balanced feed mix.


**Introduction**

Balancing the diet for livestock, such as poultry, cattle, or swine, is crucial for their growth and overall health. The challenge is to find the right combination of ingredients that meet the specific nutritional requirements while minimizing the cost of the feed mix. This is where the Minimum Cost Feed Mix Calculator comes in.

**Key Features**

 * User-Friendly Web Interface: The program provides a user-friendly web interface for entering key parameters, making it easy for users to input their requirements and ingredient costs.

 * Optimization: It uses linear programming, specifically the SciPy library's linprog function, to find the optimal combination of ingredients that meets the nutritional requirements while minimizing the cost.

* Nutritional Constraints: Users can specify constraints for minimum protein and maximum fiber content in the feed, ensuring that the calculated mix adheres to their desired nutritional standards.

* Cost Analysis: The calculator not only finds the optimal mix but also provides the minimum cost associated with it.

* Example Calculation: To get you started, we've included a detailed example below, illustrating how to use the calculator to formulate an optimal feed mix.

**Example: Formulating an Optimal Poultry Feed Mix**

Suppose Green Farm uses at least **800kg** of special feed daily. The special feed is a mixture of corn and soyabean meal with the following compositions:

Feedstuff      | Protien (kg/kg of feedstuff) | Fiber (kg/kg of feedstuff) | Cost ($/kg) |
-------------  | ---------------------------  | -------------------------- | ----------- |
Corn           |             0.09             |             0.02           |   **0.30**  |
Soyabean meal  |             0.60             |             0.06           |   **0.90**  |

The dietary requirements of the total feed stipulate at least **30%** protein and at most **5%** fiber. Green Farm wishes to determine the daily minimum-cost feed mix.


1. Open the web interface of the calculator.

2. Input the following values into the respective fields:

    Amount of Special Feed Needed Daily (x): 800 kg
    Minimum Protein Requirement (%): 30%
    Maximum Fiber Requirement (%): 5%
    Cost of Corn (per kg): $0.30
    Cost of Soybean Meal (per kg): $0.90

3. Click the "Calculate Minimum Cost" button.
    The calculator will perform a linear programming optimization, and in a fraction of a second, you will receive the following results:

    Minimum Cost: $437.65
    Amount of Corn Needed: 470.59 kg
    Amount of Soybean Meal Needed: 329.41 kg

    You now have the ideal feed mix that satisfies the specified nutritional requirements while minimizing your feed costs.

**Conclusion**

The Minimum Cost Feed Mix Calculator simplifies the often complex task of formulating cost-effective and nutritionally balanced feed mixes for livestock. Whether you're managing a small-scale farm or a large-scale operation, this tool will help you optimize your feed formulation process and improve the efficiency of your livestock management.
