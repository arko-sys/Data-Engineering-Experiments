"""
Unit tests for the vct21_stats_script module.
This module tests the functionalities of the functions in the vct21_stats_script.
"""

import unittest
from io import StringIO

import pandas as pd
from scripts.vct21_stats_script import (
    get_summary_stats,
    plot_pie_chart,
)


class TestVisualizationScript(unittest.TestCase):
    """
    Tests for the vct21_stats_script functions.
    """

    def setUp(self):
        """Set up a sample DataFrame for testing."""
        # Sample CSV data as a string
        csv_data = """Map,Total,Wins,Losses
        Ascent,5,3,2
        Bind,8,5,3
        Haven,6,3,3
        Icebox,7,4,3
        Split,4,2,2
        """
        self.df = pd.read_csv(StringIO(csv_data))  # Create DataFrame from string

    def test_get_summary_stats(self):
        """Test the get_summary_stats function."""
        summary = get_summary_stats(self.df)
        self.assertIsInstance(summary, pd.DataFrame)
        self.assertIn("Total", summary.columns)
        self.assertIn("mean", summary.index)
        self.assertEqual(
            summary.loc["mean", "Total"], 6.0
        )  # Mean of the 'Total' column

    def test_plot_pie_chart_invalid_column(self):
        """Test plot_pie_chart with an invalid column name."""
        with self.assertRaises(KeyError):
            plot_pie_chart(self.df, "InvalidMap", "Total")


if __name__ == "__main__":
    unittest.main()
