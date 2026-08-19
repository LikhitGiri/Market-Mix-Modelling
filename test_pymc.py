import pymc as pm

print("PyMC version:", pm.__version__)

with pm.Model() as model:
    x = pm.Normal("x", mu=0, sigma=1)

print("PyMC model created successfully!")