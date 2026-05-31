#!/usr/bin/env python3

import pandas as pd

def main():

    df = pd.read_excel("data/GSE63514_series_matrix.xlsx", header=None, dtype=str)

    #Extract and standardize disease group labels from metadata row
    groups = df.iloc[41, 1:].str.split(":").str[1].str.strip()
    group_map = {"normal cervical epithelium" : "Normal", "cervical intraepithelial neoplasm, low grade lesion" : "CIN1", "cervical intraepithelial neoplasm, moderate grade lesion" : "CIN2","cervical intraepithelial neoplasm, high grade lesion" : "CIN3", "cervical squamous epithelial cancer" : "Cancer"}
    groups = groups.map(group_map)

    #Build and save sample metadata
    sample_ids = (df.iloc[69, 1:])
    metadata = pd.DataFrame({'sample_id': sample_ids,'group': groups})
    metadata.to_csv("results/metadata.csv", index=False)

    #Extract probe-level expression matrix, drop GEO end marker, and index by probe ID
    expression = df.iloc[70: , : ]
    expression = expression[expression.iloc[:, 0] != "!series_matrix_table_end"]
    expression = expression.set_index(0)

    # Assign GSM sample IDs as column names so expression matrix is identifiable
    expression.columns = sample_ids.tolist()
    expression = expression.apply(pd.to_numeric ,errors="coerce")
    expression.to_csv("results/expression_data.csv", index=True)
    print("Done! metadata.csv and expression_data.csv saved to results/")


if __name__ == "__main__":
    main()
