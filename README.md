# Digimon-Warehouse

Data Warehouse Project

This project is a Data Warehouse solution aimed at collecting data from an external API (Digi-API), processing it, and storing it for further analysis.<br>
The project is in an early stage: API data fetching is still under development.<br>
Currently, the data is retrieved from the API, saved as digimon.csv, and loaded into a basic DataFrame.<br><br>
Now only has facts, metadata to be added later.

### Technologies <br>
Python 3.x<br>
Pandas<br>
Digi-API (free API)<br>
Virtual environment (venv)<br>

### Installation and dependencies <br>
python -m venv venv<br>
venv\Scripts\activate<br>
pip install -r requirements.txt or python -m pip install -r requirements.txt <br> 

### Usage <br>
python src/api.py <br>
--> Creates raw .csv file into dir 'raw' where data can be used<br>

### Current Structure:
```
project-root/
│
├── src/
│ ├── api.py
│ └── raw/
│ └── digimon.csv
│
├── requirements.txt
└── README.md
```
<br><br><br><br><br>
