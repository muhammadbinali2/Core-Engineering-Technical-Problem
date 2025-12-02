# Core-Engineering-Technical-Problem
Basic sorting function written in python, O(1), for a screening 

Thoughtful Robotics Package Dispatch System

This document outlines the implementation of a package sorting function designed for a robotic arm in the Thoughtful automation factory. The core objective is to determine the correct stacking location for packages based on simple physical criteria (volume and mass).

Objective

To implement a single function, sort(width, height, length, mass), that efficiently determines the appropriate stack for a package based on two criteria: whether it is bulky and/or heavy.

Implementation Details

The solution is implemented in Python. The function operates in O(1) time complexity as it only performs a fixed number of arithmetic calculations and comparisons, regardless of the input values.

The sort function

sort(width: float, height: float, length: float, mass: float) -> str


Units:

Dimensions (width, height, length): Centimeters (cm)

Mass (mass): Kilograms (kg)



How to Run

Save the code above as package_sorter.py.

Run the file directly from your terminal:

python package_sorter.py


The if __name__ == "__main__": block contains six test cases that demonstrate each possible outcome and edge case (e.g., bulky by volume vs. bulky by dimension).
