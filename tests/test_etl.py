import pandas as pd


def test_no_negative_values():
    df = pd.read_csv('data/sales_summary.csv')
    assert (df['sales'] >= 0).all()
