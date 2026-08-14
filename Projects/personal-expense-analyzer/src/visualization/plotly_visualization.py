import plotly.express as px
def interactive_top_transactions(df):
    data= df.nlargest(10, "Amount")

    fig = px.bar(
        data,
        x="Description",
        y= "Amount",
        title="Top 10 Largest Transactions",
        hover_data=["Date","Amount","Category","Account Name"]    
    )

    fig.update_layout(
        xaxis_title="Description",
        yaxis_title="Transaction Amount($)"
    )
    fig.show()

def interactive_monthly_spending(df):
    data=df.groupby(["Month", "Transaction Type"]
        )["Amount"].sum().reset_index()
    
    fig = px.line(
        data,
        x="Month",
        y="Amount",
        color="Transaction Type",
        markers= True,
        title="Monthly Spending by Transaction Type"
    )

    fig.update_layout(
        xaxis_title= "Month",
        yaxis_title= "Total Spending($)"
    )
    fig.show()
    
def interactive_category_account_amount(df):
    data = (df.groupby(["Category", "Account Name"])["Amount"].sum().reset_index())

    fig= px.bar(
        data, x="Category", y="Amount", color= "Account Name", hover_data=["Category", "Account_name", "Amount"],
        title= "Spending by Category and Account"
    )

    fig.update_layout(
        xaxis_title = "Category",
        yaxis_title = "Total Amount($)")
    
    fig.show()