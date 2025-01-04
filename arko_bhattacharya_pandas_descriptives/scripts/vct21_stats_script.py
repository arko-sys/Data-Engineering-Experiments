"""
This script reads a CSV file containing data on banned maps and generates
summary statistics and a pie chart showing the ratio of maps banned.
"""

import os
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

def get_summary_stats(df):
    """
    Generates summary statistics for the given DataFrame.
    """
    summary_stats = df.describe()
    return summary_stats

def plot_pie_chart(df, label_column, value_column, title="Pie Chart"):
    """
    Plots a pie chart using columns from a DataFrame.
    """
    labels = df[label_column].tolist()
    values = df[value_column].tolist()

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.set_title(title)

    return fig, ax

if __name__ == "__main__":
    current_dir = Path(os.getcwd())
    data_folder = current_dir / "data"
    data_file = data_folder / "banned_maps_stats.csv"

    # Ensure encoding is specified
    input_df = pd.read_csv(data_file, encoding='utf-8')
    print(input_df.head(5))
    print(get_summary_stats(input_df))

    # Plotting the pie chart
    pie_chart_figure, pie_chart_axes = plot_pie_chart(
        input_df, "Map", "Total", title="Ratio of maps banned (Valorant VCT'21)"
    )
    pie_chart_axes.set_facecolor("lightgrey")

    pie_chart_figure.savefig("pie_chart.png")
    plt.show()
