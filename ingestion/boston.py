import pandas as pd

def ingestion(path):
    data = pd.read_csv(path)
    return data

