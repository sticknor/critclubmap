# Crit Club Maps
## Description
Display a map of the world with markers representing crit clubbers

## Website
A static web page (index.html) that renders the map. It is hosted on github pages.

## Updates
Run the update.py script to pull latest clubber data
### Pre-requisites
1. Make sure you are using python 3 (tested with version 3.9.2):
```
python --version
```
2. Create a python environment:
```
python -m venv env
source env/bin/activate
python -m pip install requirements.txt
```
### Command
```
export GOOGLE_MAPS_API_KEY = "<GOOGLE_MAPS_API_KEY>"
export AIRTABLE_API_KEY = "<AIRTABLE_API_KEY>"
export AIRTABLE_BASE_ID = "<AIRTABLE_BASE_ID>"
export AIRTABLE_TABLE_NAME = "<AIRTABLE_TABLE_NAME>"
python update.py
```



