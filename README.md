# MPK-api

py -m venv ./venv

.\venv\Scripts\Activate.ps1

pip install -r requirements.txt

uvicorn src.main:app --reload
