import pandas as pd

def create_dataframe(data, columns):
    df = pd.DataFrame(data, columns=columns)
    return df