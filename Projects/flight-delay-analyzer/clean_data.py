
import pandas as pd
def clean_data(df):
    #droppint the duplicate data
        #we do not have any duplicate data
        
    #removing the nah or na value
        #we need the nah or na value in this dataset cause it has more meaning to keep it as it is then filling or removing it making the dataset vague.
    
    #using the copy data so we do not accidently manipulate the real data
    df= df.copy()
    
    #Keeping it in a date and time format
    df["fl_date"] = pd.to_datetime(df["fl_date"])

    #converting it into a time format
    
    df["dep_time"]= df["dep_time"].astype("Int64").astype("string").str.zfill(4)
    df["dep_time"] = df["dep_time"].replace("2400", "0000")
    df["dep_time"]= pd.to_datetime(df["dep_time"], format="%H%M").dt.time

    df["crs_dep_time"]= df["crs_dep_time"].astype("Int64").astype("string").str.zfill(4)
    df["crs_dep_time"] = df["crs_dep_time"].replace("2400", "0000")
    df["crs_dep_time"]= pd.to_datetime(df["crs_dep_time"],format= "%H%M").dt.time

    df["crs_arr_time"]= df["crs_arr_time"].astype("Int64").astype("string").str.zfill(4)
    df["crs_arr_time"] = df["crs_arr_time"].replace("2400", "0000")
    df["crs_arr_time"]= pd.to_datetime(df["crs_arr_time"],format = "%H%M").dt.time

    df["arr_time"]= df["arr_time"].astype("Int64").astype("string").str.zfill(4)
    df["arr_time"] = df["arr_time"].replace("2400", "0000")
    df["arr_time"]= pd.to_datetime(df["arr_time"], format ="%H%M").dt.time

    return df