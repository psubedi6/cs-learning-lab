#Which airlines have the highest delay rate?
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def value(value):
    print("="*50)
    print(value)
    print("="*50)

def highest_delay_rate(df):
    value("HIGHEST VALUE")
    print(df.groupby("op_unique_carrier")["dep_delay"].apply(lambda x: (x>0).mean()*100).sort_values(ascending= False).head(10).round(2))

#Which airlines have the highest average delay?
def highest_average_delay(df):
    value("HIGHEST AVERAGE DELAY")
    print(df.groupby("op_unique_carrier")["dep_delay"].mean().sort_values(ascending=False).head(10).round(2))

#Which airports have the highest delay rate?
def airport_highest_delay_rate(df):
    print("="*50)
    print("AIRPORT WITH HIGHEST DELAY RATE")
    print("="*50)
    print(df.groupby("origin_city_name")["dep_delay"].apply(lambda x: (x>0).mean()*100).sort_values(ascending= False).head(10))

#Which months/days have the most delays?
def most_delay_months(df):
    print("="*50)
    print("MONTHS/DAYS WITH MOST DELAYS")
    print("="*50)
    print(df.groupby("month")["dep_delay"].sum().sort_values(ascending =False).head(20))
    print(df.groupby("day_of_month")["dep_delay"].sum().sort_values(ascending =False).head(20))

#What are the main causes of flight delays?
def flight_delay_cause(df):
    print("="*50)
    print("FLIGHT DELAY CAUSE")
    print("="*50)

    causes= ["carrier_delay", "weather_delay", "nas_delay","security_delay", "late_aircraft_delay"]
    print(df[causes].sum().sort_values(ascending= False))

#Which routes have the highest delay rates?
def higthest_delay_routes(df):
    print("="*50)
    print("ROUTES WITH HIGHEST DELAY RATES")
    print("="*50)

    delay= df.groupby(["origin", "dest"]).agg(
        total_flights = ("dep_delay", "count"),
        delay_flights = ("dep_delay", lambda x: (x>0).sum())
    )
    delay = delay[delay["total_flights"] >= 5]
    delay["delay_rate"]= delay["delay_flights"]/ delay["total_flights"]* 100

    print(delay.sort_values("delay_rate", ascending= False).head(20))

#Airlines with highest cancelation rate
def airlines_cancelation_rate(df):
    print("="*50)
    print("AIRLINES WITH HIGHEST CANCELATION RATE")
    print("="*50)

    cancelled= df.groupby(["op_unique_carrier"]).agg(
        total_flights= ("cancelled", "count"),
        cancelled_flights = ("cancelled", "sum")
    )
    cancelled["cancelled_rate"]= cancelled["cancelled_flights"] / cancelled["total_flights"] * 100
    print(cancelled.sort_values("cancelled_rate",ascending = False))

