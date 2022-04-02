# xzceb-flask_eng_fr

## Install

```bash
cd final_project
python3 -m virtualenv virtenv
source virtenv/bin/activate
pip install -r requirements.txt
```

## Setup

Create a file called `.env` with the following:

```env
API_KEY=<your_watson_translator_api_key>
API_URL=<your_watson_translator_api_url>
```

## Run Server

```bash
python3 server.py
```

Open a browser and go to http://localhost:8080/

## Run Tests

```bash
python -m unittest
```

## Lint

```bash
pylint *.py **/*.py
```