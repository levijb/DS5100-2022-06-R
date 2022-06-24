# HW_forest_files_function_assignment.py
# DS 5100
# HW 04 Python Functions
# R.C. Alvarado
# 18 June 2022

"""
This file provides the data to be used in the HW04.

The object firedata should imported into your notebook. If this file is in the
same directory as your notebook, do this:

	from HW_forest_files_function_assignment import firedata

You don't need to understand how this script works at this point, 
although you are free to explore it.

We will learn about how to use Pandas later!

The dataset was orginally downloaded from the UCI Machine Learning Repository. 
Here is the link:

https://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv
"""

import pandas as pd

# Get the data
firedata_src = "uci_mldb_forestfires.csv"
firedata_df = pd.read_csv(firedata_src)

# Convert into simple object
class Data(): pass
firedata = Data()
for col in firedata_df.columns:
    setattr(firedata, col, firedata_df[col].values)