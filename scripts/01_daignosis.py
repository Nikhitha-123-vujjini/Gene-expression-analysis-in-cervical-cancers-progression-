#!/usr/bin/env python3

import pandas as pd

# Part of GSE63514 gene expression analysis pipeline and handles initial data ingestion from GEO series matrix format
def main():

    #Load the raw GEO series matrix file — keeps everything as strings and to avoid pandas misinterpreting probe IDs or metadata fields
    df = pd.read_excel("data/GSE63514_series_matrix.xlsx", header=None, dtype=str)

    # Scan through the metadata header section of the GEO file to find where the actual expression matrix begins
    for i, row in df.iterrows():
        labels = str(row.iloc[0])
        print("ROW" + str(i) + ":" + labels)

        # ID_REF separates GEO metadata from the expression data needed for analysis
        if "ID_REF" in labels: 
            print ("Expression Data starts here")
            break 


if __name__ == "__main__":
    main()

