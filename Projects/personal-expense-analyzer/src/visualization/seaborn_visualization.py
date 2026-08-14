import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def amount_distribution_by_transaction_type(df):
    fig, ax = plt.subplots(figsize = (10,6))

    sns.boxplot(data=df, x="Transaction Type", y= "Amount", ax=ax)

    ax.set_title("Transaction Amount Distribution by Transaction Type")
    ax.set_xlabel("Transaction Type")
    ax.set_ylabel("Transaction Amount($)")

    ax.tick_params(axis="x", rotation= 40)
    plt.tight_layout()

    plt.show()

def top_transaction_descriptions(df):
    data = df["Description"].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=data.values, y=data.index, ax=ax
    )

    ax.set_title("Top 10 Most Frequent Transaction Descriptions")
    ax.set_xlabel("Number of Transactions")
    ax.set_ylabel("Description")

    plt.tight_layout()
    plt.show()


def category_frequency_vs_spending(df):
    data = (
        df.groupby("Category")
        .agg(
            transaction_count=("Amount", "count"),
            total_spending=("Amount", "sum")
        )
        .sort_values("total_spending", ascending=False)
        .head(15)
    )

    fig, ax = plt.subplots(figsize=(12, 6))

    sns.barplot(data=data.reset_index(),x="Category", y="transaction_count", ax=ax)

    ax.set_title("Transaction Frequency by Spending Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Number of Transactions")
    ax.tick_params(axis="x", rotation=45)

    plt.tight_layout()
    plt.show()

def spending_by_account(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(
        data=df,
        x="Account Name",
        y="Amount",
        ax=ax
    )
    ax.set_title("Transaction Amount Distribution by Account")
    ax.set_xlabel("Account")
    ax.set_ylabel("Transaction Amount ($)")

    ax.tick_params(axis="x", rotation=45)

    plt.tight_layout()
    plt.savefig("spending_by_account.png", dpi=300)
    plt.show()

def category_frequency_vs_average_amount(df):
    data = (
        df.groupby("Category")
        .agg(
            transaction_count=("Amount", "count"),
            average_amount=("Amount", "mean")
        )
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    sns.scatterplot(
        data=data,
        x="transaction_count",
        y="average_amount",
        ax=ax
    )

    ax.set_title("Transaction Frequency vs Average Amount")
    ax.set_xlabel("Number of Transactions")
    ax.set_ylabel("Average Transaction Amount ($)")

    plt.tight_layout()
    plt.savefig("category_frequency_vs_average_amount.png", dpi=300)
    plt.show()

def category_spending_comparison(df):
    data= df.groupby("Category")["Amount"].sum().head().sort_values(ascending=False).reset_index()

    fig, ax = plt.subplots(figsize = (10,6))

    sns.barplot(data=data, x= "Amount", y=("Category"), ax=ax)

    ax.set_title("Top 5 categories by Total Spending")
    ax.set_xlabel("Total spending($)")
    ax.set_ylabel("Category")

    plt.tight_layout()
    plt.show()

def monthly_spending_heatmap(df):
    data= pd.pivot_table(
        df, values= "Amount", index= "Month",\
        columns = "Transaction Type",
        aggfunc="sum", fill_value= 0)
        
    fig, ax = plt.subplots(figsize = (10,6))
    
    sns.heatmap(data, annot=True, fmt=".0f", ax=ax)

    ax.set_title("Monthly spending by Transaction Type")
    ax.set_xlabel("Transaction Type")
    ax.set_ylabel("Month")
        
    plt.tight_layout()
    plt.show()