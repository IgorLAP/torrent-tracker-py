# 🤖 Torrent Tracker API 

Version of the Torrent Tracker Rest API, more faster in comparasion with the node one. BeautifulSoup to crawl torrent pages getting the best results

## Techonologies
  
  - Python 3.10
  - FastAPI
  - BeautifulSoup
  - Pydantic
  
  
## Local setup
 
 Clone

```bash
git clone https://github.com/IgorLAP/torrent-tracker-py.git .
```

Creating environment

```bash
python -m venv venv
```

Active environment

```bash
# in CMD
.\venv\Scripts\activate.bat

# in PowerShell
.\venv\Scripts\activate.ps1
```

Install required dependencies

```bash
pip install -r requirements.txt
```

## Running API Locally

```bash
uvicorn main:app --reload
```

## Deploy

[DETA](https://torrent-tracker.deta.dev)
