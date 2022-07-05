# VS Code Demo File

# Import Pandas and Numpy
import numpy as np
import pandas as pd

# Create a simple DataFrame
a = np.random.random(10)
b = np.random.random(10)
df = pd.DataFrame(dict(a=a, b=b))
df.index.name = 'obs_id'