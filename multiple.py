from joblib import Parallel, delayed
def multiple(a, b):
        return a*b
Parallel(n_jobs=2, verbose=5)(delayed(multiple)(a=i, b=j) for i in range(1, 6) for j in range(11, 16))
