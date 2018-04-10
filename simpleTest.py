#!/usr/bin/env python

from joblib import Parallel, delayed

def f(x):
    return x

l = range(16)
results = Parallel(n_jobs=-1, verbose=5)(delayed(f)(i) for i in l)
