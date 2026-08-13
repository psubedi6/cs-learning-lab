import matplotlib.pyplot as plt
def spending_by_transaction_type(df):
    data = (
        df.groupby("Transaction Type")["Amount"].sum().sort_values(ascending = False)
    )

    fig, ax = plt.subplots(figsize= (10,6))

    bars = ax.bar(data.index, data.values, color = ["green","red"])

    ax.set_title("Total Amount by Transaction Type")
    ax.set_xlabel("Transaction Type")
    ax.set_ylabel("Total Amount($)")

    ax.tick_params(axis="x", rotation=45)

    for bar in bars:
        ax.text(
            bar.get_x() + bar.get_width()/ 2,
            bar.get_height(),
            f"${bar.get_height(): ,.2f}",
            ha="center",
            va= "bottom",
            color = "blue"
        )
    plt.tight_layout()
    plt.show()

def top_spending_categories(df):
    data= (df.groupby("Category")["Amount"].sum().head(5).sort_values(ascending=False))

    fig, ax = plt.subplots(figsize= (10,6))

    bars = plt.barh(data.index, data.values, color=["green", "blue"])
    ax.margins(x=0.2)

    ax.set_title("Top Spending by Category")
    ax.set_xlabel("Total Amount($)")
    ax.set_ylabel("Category")

    for bar in bars:#x,y,text
        ax.text(
            bar.get_width(),
            bar.get_y() + bar.get_height()/ 2,
            f"${bar.get_width(): ,.2f}",
            va = "center",
        )
    plt.tight_layout()
    plt.show()

def transaction_type_percentage(df):
    data = df["Transaction Type"].value_counts()
    fig, ax = plt.subplots(figsize=(10,6))

    plt.pie(data.values, labels= data.index, autopct = "%1.1f%%", startangle= 90)

    ax.set_title("Percentage of transactions by Type")

    plt.tight_layout()
    plt.show()

def transaction_by_month(df):
    data = df.groupby("Month").size()

    fig, ax = plt.subplots(figsize = (10,6))

    plt.plot(data.index, data.values, marker = "o")

    ax.set_title("Number of Transactions by Month")
    ax.set_xlabel("Month")
    ax.set_ylabel("Number of Transactions")
    
    ax.tick_params(axis="x", rotation = 40)

    plt.tight_layout()
    plt.show()

def spending_by_month(df):
    data = df.groupby("Month")["Amount"].sum()

    fig, ax = plt.subplots(figsize= (10,6))

    plt.plot(data.index, data.values,marker = "h", color= "green")

    ax.set_title("Total transaction by month")
    ax.set_xlabel("Month")
    ax.set_ylabel("Total Amount($)")

    plt.tick_params(axis="x", rotation = 40)

    plt.tight_layout()
    plt.show()

def average_spending_by_category(df):
    data= df.groupby("Category")["Amount"].mean().head(10).sort_values()

    fig, ax = plt.subplots(figsize=(10,6))

    bars= ax.bar(data.index, data.values)
    ax.set_title("Average Transaction by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Average amount($)")

    for bar in bars:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"${bar.get_height(): ,.2f}",
            ha="center",
            va="bottom"
        )

    plt.tick_params(axis="x", rotation =40)
    plt.tight_layout()
    plt.show()

def transaction_amount_distribution(df):
    fig, ax = plt.subplots(figsize=(10,6))

    ax.hist(df["Amount"], bins=10)
    ax.set_title("Transaction amount Distribution")
    ax.set_xlabel("Transaction amount($)")
    ax.set_ylabel("Frequency")


    plt.tight_layout()
    plt.show()

def transaction_amount_outliers(df):
    fig, ax = plt.subplots(figsize=(10,6))

    ax.boxplot(df["Amount"])

    ax.set_title("Transaction Amount Distribution and Outliers")
    ax.set_ylabel("Transaction amount($)")
    plt.tight_layout()
    plt.show()