from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
import random
import requests

app = FastAPI()

MONITORING_SIM_URL = "https://YOUR-MONITORING-SIMULATOR-URL/generate-alert"

scheduler = BackgroundScheduler()


def create_incident():
    try:
        requests.post(MONITORING_SIM_URL)
        print("incident generated")
    except Exception as e:
        print("error:", e)


@app.get("/")
def root():
    return {"service": "anomiq-scenario-engine"}


@app.post("/start")
def start_generator():

    scheduler.add_job(create_incident, "interval", seconds=15)
    scheduler.start()

    return {"status": "scenario engine started"}