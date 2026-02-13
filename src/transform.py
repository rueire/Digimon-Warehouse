from operator import index
import pandas as pd
from pathlib import Path


dir = Path(__file__).resolve().parent / "raw"
file_path = dir/'digimon.csv'

# Read the CSV file
data = pd.read_csv(file_path)
main_data = data[['id', 'name']]

# View the first 10 rows
print(main_data.head(10).to_string(index=False))