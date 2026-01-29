import requests
import pandas as pd
from pandas import json_normalize
from pathlib import Path

def get_digimons():
    all_data = []
    page = 0

    try:
        while True:
            response = requests.get(f'https://digi-api.com/api/v1/digimon?page={page}')
            response.raise_for_status()

            data = response.json()
            page_data = data['content']

            all_data.extend(page_data)

            if data["pageable"]["nextPage"] == "":
                break

            page += 1

        df = json_normalize(all_data)

        # path src/raw
        dir = Path(__file__).resolve().parent.parent
        raw_dir = dir/'raw'
        raw_dir.mkdir(parents=True, exist_ok=True)   

        file_path = raw_dir/'digimon.csv'

        df.to_csv(file_path, index=False, encoding='utf-8')

        print(f'{len(all_data)} rows saved to src/raw')

    except Exception as e: 
        print('error at api request: ', e)


