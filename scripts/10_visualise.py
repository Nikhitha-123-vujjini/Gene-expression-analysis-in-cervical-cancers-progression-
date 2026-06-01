#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    analysed_data = pd.read_csv("results/analysed_df.csv")
    significant = pd.read_csv("results/significant_results.csv")

    # Get only the significant probe names
    probes = significant["probe"].tolist()
    print (probes)

    group_order = ["Normal", "CIN1", "CIN2", "CIN3", "Cancer"]

    #save individula box plots 
    for probe in probes:
            plt.figure()
            sns.boxplot(data=analysed_data, x="group", y=probe, order=group_order)
            plt.title("Expression of " + probe + " across disease stages")
            plt.xlabel("Disease Stage")
            plt.ylabel("Expression Level")
            plt.savefig("figures/" + probe + "_boxplot.png")
            plt.close()
            print("Saved boxplot for " + probe)

    #save combined boxplot
    fig, axes = plt.subplots(2, 5, figsize=(20, 8))
    axes = axes.flatten()
    for i, probe in enumerate(probes):
        sns.boxplot(data=analysed_data, x="group", y=probe, order=group_order, ax=axes[i])
        axes[i].set_title(probe)
        axes[i].set_xlabel("Disease Stage")
        axes[i].set_ylabel("Expression Level")
        axes[i].tick_params(axis='x', rotation=45)
    plt.suptitle("Top 10 Significant Probes Across Disease Stages", fontsize=14)
    plt.tight_layout()
    plt.savefig("figures/top10_probes_boxplot.png")
    plt.close()
    print("Saved combined boxplot")

if __name__ == "__main__":
    main()
