# Digimon-Warehouse

Data Warehouse Project

This project is a Data Warehouse solution aimed at collecting data from an external API (Digi-API), processing it, and storing it for further analysis.<br>
The project is currently in an early stage: API data fetching is planned but not fully implemented yet.<br> At the moment, data is read from a CSV file (digimon.csv) and a basic DataFrame is created.<br><br>

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

### Current Intended Structure:
```
project-root/
│
├── raw/
│   └── digimon.csv
│
├── src/
│   └── api.py
│
├── requirements.txt
└── README.md
```
<br><br><br><br><br>
