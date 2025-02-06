
numpy_plain_content = """
NumPy is a fundamental library for numerical computations in Python.

Topics Covered:

1. Array Creation
import numpy as np
a = np.array([1, 2, 3])
zeros = np.zeros((2, 3))
ones = np.ones((3,))
arange = np.arange(0, 10, 2)
linspace = np.linspace(0, 1, 5)

2. Array Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
sum_array = a + b
prod_array = a * b
div_array = a / b

3. Indexing and Slicing
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a[0, 1])  # 2
print(a[:, 1])  # [2 5]

4. Reshaping Arrays
a = np.arange(6)
a_reshaped = a.reshape((2, 3))

5. Broadcasting
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([1, 0, 1])
print(a + b)

6. Aggregation Functions
a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.mean(a))
print(np.sum(a))
print(np.std(a))

7. Random Module
np.random.seed(0)
rand_array = np.random.rand(3)
randn_array = np.random.randn(3)
randint_array = np.random.randint(0, 10, size=3)

NumPy makes numerical computation efficient and concise.
"""

# Save the updated content to a new file
plain_file_path = "/mnt/data/numpy_plain.md"
with open(plain_file_path, "w") as f:
    f.write(numpy_plain_content)

plain_file_path
