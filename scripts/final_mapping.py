#!/usr/bin/env python3

import pandas as pd

probes = pd.read_csv("results/significant_results.csv")

annotation = pd.read_csv("data/clear_annotation.csv", sep="\t", low_memory=False)
merged = probes.merge(annotation, left_on="probe", right_on="ID")

result = merged[["probe", "p_value", "rank", "Gene Symbol", "Gene Title"]]

result.to_csv("results/probes_to_genes.csv", index=False)

print(result.to_string())
