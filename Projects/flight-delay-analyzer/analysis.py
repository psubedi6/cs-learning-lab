#What is the average arrival delay for each airline?
def average_arrival_delay(df):
    arrival_delay= df.groupby("op_unique_carrier")["arr_delay"].mean().reset_index()

    print(arrival_delay.sort_values("arr_delay", ascending=False))

#What is the cancellation rate for each airline?
def cancellation_rate(df):
    cancel = df.groupby("op_unique_carrier").agg(
        total_cancellation=("cancelled", "count"),
        cancel_flight=("cancelled", "sum")
    )

    cancel["cancelled_rate"] = (cancel["cancel_flight"]/ cancel["total_cancellation"]* 100)
    print(cancel.sort_values("cancelled_rate", ascending=False))

# How many flights were early/on-time vs delayed?
def early_vs_delayed(df):
    print("="*50)
    print("EARLY VS DELAYED")
    print("="*50)
    
    print("The delayed flights are:")
    print((df["dep_delay"]>0).count())
    
    print("The early flights are: ")
    print((df["dep_delay"]<0).count())