# Python-Coding
Hi! This is a practice project in Python using NumPy and Pandas! 

I was inspired to do this project through the CAS PnC actuarial program and my time taking care of my sick grandpa, pushing me to use health data rather than PnC auto loss claims development data.

I will be synthesising health claims data over 12 months with gamma (right skewed) and implement the chain-ladder method on the generated loss triangle.

The first file, Chain-Ladder geenrates 1000 rows of synthetic data with developmental lag mirroring real life data, following a gamma distribution using NumPy.

It then loads the entire dataset into triangle-data.csv to be used in the next step.
