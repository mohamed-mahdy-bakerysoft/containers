import pymc as pm
with pm.Model() as model:
    x = pm.Normal("x", mu=0, sigma=1)
    trace = pm.sample(nuts_sampler="numpyro")