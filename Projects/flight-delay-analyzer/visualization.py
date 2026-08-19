#Here we'll solve and see all the visualizations
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

#Which airlines have the highest average arrival delay?
def airlines_avg_arrival_delay(df):
    fig, ax = plt.subplots(figsize=(10,6))

    delay =(df[df["arr_delay"] < 0]
    .groupby("op_unique_carrier")["arr_delay"]
    .mean()
    .abs()
    .sort_values(ascending= False)
)
    
    ax.bar(delay.index, delay.values)
    
    ax.set_title("Airlines with highest average arrival delay")
    ax.set_xlabel("Flight Name")
    ax.set_ylabel("Average delay")

    plt.tight_layout()
    plt.show()

#What does the distribution of arrival delays look like?
def distribution_arrival_delay(df):
    fig, ax = plt.subplots(figsize = (10, 6))

    ax.hist(df["arr_delay"], bins=10)
    ax.set_title("Distribution of Arrival Delay")
    ax.set_xlabel("Arrival Delay (minutes)")
    ax.set_ylabel("Number of Flights")

    plt.tight_layout()
    plt.show()

#What percentage of flights were delayed vs not delayed?
def delayed_vs_notDelayed(df):

    fix, ax = plt.subplots(figsize = (10,6))

    ax.pie([(df["dep_delay"]>0).sum(), (df["dep_delay"]<=0).sum()])
    ax.set_title("Flight Delayed vs Not Delayed")

    plt.tight_layout()
    plt.show()

#How does average arrival delay change by month?
def avg_arr_delay_by_month(df):
    fix, ax = plt.subplots(figsize= (10,6))
    data= df.groupby("month")["arr_delay"].mean()

    ax.plot(data.index, data.values)
    ax.set_title("Average Arrival Delay by Month")
    ax.set_xlabel("Month")
    ax.set_ylabel("Number of Delays")

    plt.tight_layout()
    plt.show()

#Is flight distance related to arrival delay?
def flight_distance_vs_arr_delay(df):
    fig, ax = plt.subplots(figsize= (10,6))

    ax.scatter(df["distance"], df["arr_delay"])
    ax.set_title("Flight Distance VS Arrival Delay")
    ax.set_xlabel("Flight Distance")
    ax.set_ylabel("Arrival Delay")

    plt.tight_layout()
    plt.show()

#How does arrival-delay distribution differ between airlines?
def arr_delay_distribution_diff_airlines(df):
    fig, ax = plt.subplots(figsize= (10,6))
    
    sns.boxenplot(data=df, x= "op_unique_carrier",y= "arr_delay", ax=ax)

    ax.set_title("Arrival delay Distribution by Airlines")
    ax.set_xlabel("Airline")
    ax.set_ylabel("Arrival Delay")

    plt.tight_layout()
    plt.show()

#Which airlines operate the most flights?
def airlines_most_flights(df):
    fig, ax= plt.subplots(figsize=(10,6))
    data = df["op_unique_carrier"].value_counts()
    sns.barplot(x= data.index,y=data.values, ax=ax)

    ax.set_title("Number of Flights by Airline")
    ax.set_xlabel("Airline")
    ax.set_ylabel("Number of Flights")


    plt.tight_layout()
    plt.show()