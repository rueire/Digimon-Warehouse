
from pathlib import Path
import requests
import pandas as pd

def get_digimon_fields():
    page = 1
    fields = []

    while True:
        try:
            res = requests.get( f'https://digi-api.com/api/v1/field/{page}')
            res_json = res.json()

            if 'id' not in res_json:
                break

            fields.append(res_json)
            df = pd.DataFrame(fields)

            page += 1

            # path src/raw
            dir = Path(__file__).resolve().parent.parent
            raw_dir = dir/'raw'

            raw_dir.mkdir(parents=True, exist_ok=True)  
            file_path = raw_dir/'digimon_fields.csv'

            df.to_csv(file_path, index=False, encoding='utf-8')
            print('digimon fields saved')


        except Exception as e:
            print(f'error: {e}')


def field_info():
    
    try:
        res = requests.get( f'https://digi-api.com/api/v1/field')
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
        file_path = raw_dir/'field_info.csv'

        field.to_csv(file_path, index=False, encoding='utf-8')
        print('field info saved')

    except Exception as e:
        print(f'error: {e}')
