import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)


def main():
    logging.info("ETL start")
    df = pd.read_csv('./data/sales.csv')

    df['sales'] = df['net_value'] * df['quantity']
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    summary = df.groupby(df['sale_date'].dt.to_period('M'))['sales'].sum()

    summary.to_csv('./data/sales_summary.csv')
    logging.info("ETL complete")


if __name__ == "__main__":
    main()
