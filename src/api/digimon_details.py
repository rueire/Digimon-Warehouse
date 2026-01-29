import requests
import pandas as pd
from pandas import json_normalize
from pathlib import Path
# time for api rate limit. Learn later about tenacity. 
import time


# details per digimon
# done using batch, row by row caused errors
def get_digimons_details(batch_size=100):
    #consider to add retry system

    buffer=[]

     # path src/raw
    dir = Path(__file__).resolve().parent.parent
    raw_dir = dir/'raw'
    raw_dir.mkdir(parents=True, exist_ok=True)   

    file_path = raw_dir/'digimon_details.csv'

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

