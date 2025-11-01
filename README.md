# 🕒 Online Clock

Python web app displaying current time in any timezone. Users can select from all global timezones. Time updates every second.

---

## Features

- Display current time in any timezone  
- Full timezone list with UTC offsets  
- Default timezone: **Asia/Jerusalem**  
- Browser timezone detection  
- Fallback for errors  
- Logs errors and key events (console + file)  
- Caches timezone list once per day  

---

## Installation

Clone the repository:

`git clone git@github.com:katekatekatem/online_clock.git`  
`cd online_clock`

Create virtual environment and install dependencies:

**Mac/Linux:**  
`python3 -m venv venv`  
`source venv/bin/activate`  
`pip install -r requirements.txt`

**Windows:**  
`python -m venv venv`  
`source venv\Scripts\activate`  
`pip install -r requirements.txt`

---

## Run locally

`python run.py`

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.  
Logs are written to console and `online_clock.log`.

---

## Testing

Run minimal tests:

`pytest`

Covers:

- `TimeService` output for valid/invalid timezones  
- Timezone options generation  

---

## Tech

- Python 3.9+  
- WSGI (`wsgiref`)  
- `pytz` for timezone handling  
- Vanilla HTML, CSS, JS  

---

## Link

Live version: [https://katekatekatem.pythonanywhere.com](https://katekatekatem.pythonanywhere.com)
