import pandas as pd

def import_data(file_path):
    data = pd.read_csv(file_path)
    # Add data processing logic here
    return data
