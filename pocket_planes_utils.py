#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:37:43 2026
"""

# airports.py

from dataclasses import dataclass
from pathlib import Path
import json
from typing import Any
import math

@dataclass
class Airport:
    name: str
    level: int
    xcord: int
    ycord: int
    
    
@dataclass
class Trip:
    start: str
    end: str
    speed: float
    weight: float
    cost: float
    dist: float
    
    
# ------------------- DICT TO AIRPORT -----------------------------------------
def dict_to_airport(d: dict[str, Any]) -> Airport:
    """dictionary to Airport object"""
    
    a = Airport(d["name"],
                d["level"],
                d["xcord"],
                d["ycord"])
    return a
    

# ------------------- GENERATE AIRPORT REGISTRY -------------------------------
def generate_airport_registry(d: dict[str, Any]) -> dict[str, Airport]:
    """generate dict of airports from nested dict"""
    
    all_airports = {}
    for k, v, in d.items():
        all_airports[k] = dict_to_airport(v)
    return all_airports


# ------------------- LOAD DATA -----------------------------------------------
def load_data(dirname: str | Path) -> tuple[[dict], [dict]]:
    p1 = Path(f"{dirname}/airports.json")
    
    airports = json.loads(p1.read_text(encoding="utf-8")) 
    
    airport_registry = generate_airport_registry(airports)
   
    return airport_registry
    
# ------------------- GET DISTANCE BETWEEN TWO AIRPORTS -----------------------
def get_single_distance(place1: str, place2: str, airports: dict[str, Airport]) -> float | None:
    for place in [place1, place2]:
        if place not in airports.keys():
            print(f"Error, {place} airport not found")
            return None

    airp1 = airports.get(place1)
    airp2 = airports.get(place2)
    
    xdelta = airp2.xcord - airp1.xcord
    ydelta = airp2.ycord - airp1.ycord
    
    return  round(math.sqrt(xdelta**2 + ydelta**2), 1)

# ------------------- CREATE TRIP ---------------------------------------------
def create_trip(start, end, speed, weight, cost, airports):
    dist = get_single_distance(start, end, airports)
    t = Trip(
        start=start,
        end=end,
        speed=speed,
        weight=weight,
        cost=cost,
        dist=dist)
    
    return t

# ------------------- DICT TO TRIP --------------------------------------------
def dict_to_trip(lst: list[dict[str, Any]]) -> list[Trip]:
    trip_lst = []
    
    for l in lst:  
        t = Trip(
            start=l["start"],
            end=l["end"],
            speed=l["speed"],
            weight=l["weight"],
            cost=l["cost"],
            dist=l["dist"])
        
        trip_lst.append(t)
        
    return trip_lst
                 
# ------------------- LOAD TRIP DATA ------------------------------------------                
def load_trips(dirname: str | Path) -> tuple[[dict], [dict]]:
    p1 = Path(f"{dirname}/trips.json")
    
    trips = json.loads(p1.read_text(encoding="utf-8")) 
    trps = dict_to_trip(trips)
    
    
    return trps

    
