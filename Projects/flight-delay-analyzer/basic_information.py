def understanding_data(df):
    
    #5 data to analyze
    print("\n" + "=" * 50)
    print("DATASETS")
    print("\n" + "=" * 50)
    print(df.head())

    #Rows and column of dataset
    print((f"\nThe row and column are:{df.shape}\n"))

    #basic data informations
    print("="* 50)
    print(f"\nBasic structure and data types:")
    df.info()

    #columns names
    print("="* 50)
    print(f"\nThe columns are: {df.columns}")

    #types of data
    print("="* 50)
    print(f"The types of data:\n{df.dtypes}")

    #is the value null of finding the missing value
    print("="* 50)
    print(f"Is any value null?:\n {df.isnull().sum()}")


    #duplicate data
    print(f"The number of duplicate data is:\n{df.duplicated().sum()}")
    