def category(df):

    #looking for a unique data on specific row
    print(f"unique data in dataset:\n{df["fl_date"].unique()}")

    #looking for unique data in entire dataset
    print(f"nunique data in dataset:\n{df.nunique()}")

    print(f"Counting how many times value appears: \n{df.value_counts()}")