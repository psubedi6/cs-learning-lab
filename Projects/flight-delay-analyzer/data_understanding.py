def data_understanding(df):
    #which flight was operated on what date
    print("Dates the flight was operated")
    print(df.groupby("op_unique_carrier")["fl_date"].apply(list))

    #departure and arrival place names
    print(df.groupby("origin_city_name")["dest_city_name"].apply(list))

    #scheduled departure time and actual departure time