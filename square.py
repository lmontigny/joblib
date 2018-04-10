# Example code to demonstrate parallel for loop implementation using joblib
from joblib import Parallel, delayed
import multiprocessing

# Vars
my_list = range(1000000)
squares = []

# Function to parallelize
def find_square(i):
    return i ** 2

# Without parallel processing
for index, element in enumerate(my_list):
    squares.append(find_square(element))

# With parallel processing
num_cores = multiprocessing.cpu_count()
squares = Parallel(n_jobs=num_cores, verbose=5)(delayed(
    find_square)(i)for i in my_list)
