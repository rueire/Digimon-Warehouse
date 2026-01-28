
import requests
import pandas as pd
from pandas import json_normalize
from pathlib import Path
# time for api rate limit. Learn later about tenacity. 
import time

# All APIs
#============================================
def get_digimons():
    all_data = []
    page = 0

    try:
        while True:
            response = requests.get(f'https://digi-api.com/api/v1/digimon?page={page}')
            response.raise_for_status()

            data = response.json()
            page_data = data['content']

            if data["pageable"]["nextPage"] == "":
                break

            # if isinstance(data, dict):
                # print(data.keys()) => dict_keys(['content', 'pageable'])

            all_data.extend(page_data)
            page += 1

        df = json_normalize(all_data)

        # path src/raw
        dir = Path(__file__).resolve().parent / "raw"
        dir.mkdir(parents=True, exist_ok=True)   

        file_path = dir/'digimon.csv'
        df.to_csv(file_path, index=False, encoding='utf-8')

        print(f'{len(all_data)} rows saved to src/raw')

    except Exception as e: 
        print('error at api request: ', e)

#=================================================

def get_digimon_levels():
    all_data = []
    page = 0

    try:
        while True:
            response = requests.get(f'https://digi-api.com/api/v1/level?page={page}')
            response.raise_for_status()

            data = response.json()

            if (isinstance(data, dict)
                and "content" in data
                and "fields" in data["content"]):
                
                page_data = data['content']['fields']
                all_data.extend(page_data)

                if data["pageable"]["nextPage"] == "":
                    break
                
                page += 1
                
            else:
                print(f"Skipped page {page}: invalid data")
                continue

        df = json_normalize(all_data)

        # path src/raw
        dir = Path(__file__).resolve().parent / "raw"
        dir.mkdir(parents=True, exist_ok=True)   

        file_path = dir/'digimon_levels.csv'
        df.to_csv(file_path, index=False, encoding='utf-8')

        print(f'{len(all_data)} rows saved to src/raw')

    except Exception as e: 
        print('error at api request: ', e)


#=================================================

# details per digimon
# done using batch, row by row caused errors
def get_digimons_details(batch_size=100):
    #consider to add retry system

    buffer=[]

     # path src/raw
    dir = Path(__file__).resolve().parent / "raw"
    dir.mkdir(parents=True, exist_ok=True)   
    file_path = dir/'digimon_details.csv'

    if file_path.exists():
        file_path.unlink()

    header = True

    for page in range(1,1500):
        try:
            response = requests.get(f'https://digi-api.com/api/v1/digimon/{page}')
            response.raise_for_status()
            data = response.json()

            #make sure is dict (every monster has id and name)
            if isinstance(data, dict) and "id" in data and "name" in data:
                buffer.append(data)
            else:
                print(f"Skipped page {page}: invalid data")
                continue


            if len(buffer) >= batch_size:
                df = json_normalize(buffer)

                #  Null => NaN, pandas v4 compatibility
                for col in df.select_dtypes(include='string'):
                    # replace \0 with "<NULL>"
                    df[col] = df[col].str.replace('\0', '<NULL>', regex=False)

                # Some data is in japanese: -sig
                # Note, mode = w is default => every new batch replaces earlier one
                df.to_csv(
                    str(file_path),
                    index=False,
                    encoding='utf-8-sig',
                    mode='a',
                    header=header
                )
                header = False
                buffer.clear()  # empty the batch
                print(f"Batch saved. Total rows so far: {len(df)}")

                time.sleep(1)  # wait 1sec

        except Exception as e: 
            print('error at api request: ', e)
            break

        # Save leftover data
    if buffer:
        df = json_normalize(buffer)
        for col in df.select_dtypes(include='string'):
            df[col] = df[col].str.replace('\0', '<NULL>', regex=False)

        df.to_csv(str(file_path), index=False, encoding='utf-8-sig', mode='a',header=header)
        print(f"Final batch saved. Total rows saved: {len(df)}")



# get_digimons()
get_digimon_levels()
# get_digimons_details(100)