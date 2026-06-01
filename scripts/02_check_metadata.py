#!/usr/bin/env python3

import pandas as pd

def main():
    df = pd.read_excel("data/GSE63514_series_matrix.xlsx", header=None, dtype=str)
    # Spot-check key rows around the metadata/expression boundary
    for i in [40, 41, 42]:
        print("Row" + str(i) + ":" + str(df.iloc[i,0]))
        print("Values" + str(df.iloc[i,1:].tolist()))
        print()

if __name__ =="__main__":
    main()
