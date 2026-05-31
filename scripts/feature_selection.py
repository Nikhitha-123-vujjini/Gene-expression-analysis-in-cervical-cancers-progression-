#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Load cleaned expression data and sample metadata
    metadata = pd.read_csv("results/metadata.csv")
    expression= pd.read_csv("results/expression_data.csv", index_col=0)

    # Filter to top 20 most variable probes for downstream analysis
    variance = expression.var(axis=1)
    top_probes = variance.nlargest(20).index
    expression_subset = expression.loc[top_probes]

    #Reshape and merge with metadata for grouped analysis
    expression_subset = expression_subset.T
    expression_subset.index.name = "sample_id"
    expression_subset = expression_subset.reset_index()
    analyse_df = pd.merge(expression_subset, metadata, on="sample_id")
    analyse_df.to_csv("results/analysed_df.csv", index=False)

    #descriptive stats 
    mean_df = analyse_df.drop(columns="sample_id").groupby("group").mean()
    sd_df = analyse_df.drop(columns="sample_id").groupby("group").std()
    median_df = analyse_df.drop(columns="sample_id").groupby("group").median()

    #save csv for stats
    mean_df.to_csv("results/mean_df.csv")
    sd_df.to_csv("results/sd_df.csv")
    median_df.to_csv("results/median_df.csv")
    
    #sanity check - visualize one probe across disease progression stages
    sns.boxplot(data=analyse_df, x="group", y="220090_at", order=["Normal", "CIN1", "CIN2", "CIN3", "Cancer"])
    plt.title("Probe 220090_at Expression by Disease Stage")
    plt.savefig("figures/sanity_check.png")

    print("Done! Results saved to results/ and figures/")



if __name__ == "__main__":
    main()
