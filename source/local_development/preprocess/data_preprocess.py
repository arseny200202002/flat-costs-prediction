import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv('source/local_development/test_datasets/insurance_miptstats.csv')
    print(df.info())