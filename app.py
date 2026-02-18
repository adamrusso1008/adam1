import os
from datetime import date, datetime, timedelta
from typing import Any, Dict, List, Literal, Optional

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

from plan import generate_weekly_plan

app = FastAPI(title="Calorie & Workout Tracker API")

USERS: Dict[str, Dict[str, Any]] = {}
WORKOUTS: Dict[str, List[Dict[str, Any]]] = {}
OURA_DAILY: Dict[str, Dict[str, Any]] = {}
WEEKLY_PLANS: Dict[str, Dict[str, Any]] = {}
NUTRITION_LOGS: Dict[str, Dict[str, Dict[str, Any]]] = {}
WEIGHT_LOGS: Dict[str, Dict[str, float]] = {}

DEFAULT_ZONES = {"z1": "<114", "z2": "114-132", "z3": "133-151", "z4": "152-170", "z5": "171+"}


@app.get("/", response_class=HTMLResponse)
async def home():
