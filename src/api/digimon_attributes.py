import requests
import pandas as pd
from pandas import json_normalize
from pathlib import Path

def get_attribute_list():
    all_data = []
    page = 1

    for page in range(1, 10):
        try:
            response = requests.get(f'https://digi-api.com/api/v1/attribute/{page}')
            response.raise_for_status()

            data = response.json()
            all_data.append(data)

            df = json_normalize(all_data)

            # path src/raw
            dir = Path(__file__).resolve().parent.parent
            raw_dir = dir/'raw'
            raw_dir.mkdir(parents=True, exist_ok=True)  

            file_path = raw_dir/'digimon_attributes_list.csv'

            df.to_csv(file_path, index=False, encoding='utf-8')

            print(f'{len(all_data)} rows saved to src/raw')

        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 400:
                print("Bad Request: sivu ei löydy tai loppu saavutettu")
            else:
                print(f"HTTP error occurred: {http_err}")

        except Exception as e: 
            print('error at api request: ', e)
        


def attribute_info():
    
    try:
        res = requests.get( f'https://digi-api.com/api/v1/attribute')
        res_json = res.json()["content"]

        field = pd.DataFrame([{
            'id':1,
            'name': res_json['name'],
            'description': res_json['description']
        }])

        # path src/raw
        dir = Path(__file__).resolve().parent.parent
        raw_dir = dir/'raw'

        raw_dir.mkdir(parents=True, exist_ok=True)  
        file_path = raw_dir/'attribute_info.csv'

        field.to_csv(file_path, index=False, encoding='utf-8')
        print('attribute info saved')


    except Exception as e:
        print(f'error: {e}')