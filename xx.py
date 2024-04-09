import os
import pandas as pd
import numpy as np

import lingdata.database as database

import code.raxmlng as raxmlng
import code.distances as distances
import code.pythia as pythia
import code.util as util
from ete3 import Tree




for (i, row) in df.iterrows():
    raxmlng.run_inference(row["msa_paths"]["bin"], "BIN+G", util.prefix(results_dir, row, "raxmlng", "bin"))

for (i, row) in df.iterrows():
    pythia.run_with_padding(row["msa_paths"]["bin"], util.prefix(results_dir, row, "pythia", "bin"))



raxmlng.exe_path = "./bin/raxml-ng"
pythia.raxmlng_path = "./bin/raxml-ng"
pythia.predictor_path = "predictors/latest.pckl"



database.read_config(config_path)
#database.download()
#database.compile()
df = database.data()
pd.set_option('display.max_rows', None)
print(df)
for (i, row) in df.iterrows():
    raxmlng.run_inference(row["msa_paths"]["bin"], "BIN+G", util.prefix(results_dir, row, "raxmlng", "bin"))

for (i, row) in df.iterrows():
    pythia.run_with_padding(row["msa_paths"]["bin"], util.prefix(results_dir, row, "pythia", "bin"))

