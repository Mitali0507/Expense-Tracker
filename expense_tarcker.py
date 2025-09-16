import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def add_expense():   #to add new expenses
    df=pd.read_csv('expenses.csv')
    date=input("Enter date (DD-MM-YYYY)= ")
    category=input("Enter Category= ")
    amount=float(input("Enter the cost= "))
    note=input("Enter a note= ")
    new_row=pd.DataFrame({
        "Date":[date],
        "Category":[category],
        "Amount":[amount],
        "Note":[note]
            })
    new_row.to_csv("expenses.csv",mode='a',header=False,index=False) #saves new entries
    print("Expense added!")

def data():
    df=pd.read_csv("expenses.csv")
    print(df)
       

def calculate_total(): #to get total amount
    df=pd.read_csv("expenses.csv")
    total=df['Amount'].sum()
    print("The total of all expenses: ",total)


def visualize_expenses():
    df=pd.read_csv('expenses.csv')
    plt.figure(figsize=(10,6))
    sns.barplot(data=df,x='Category',y='Amount',hue='Note',palette='Set2') 
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount(INR)")
    plt.tight_layout()
    plt.savefig("Expenses.png",dpi=300,bbox_inches="tight")
    plt.show()


def main(): #main menu
    while True:
        print("\n1. Add expenses")
        print("2. See Expenses")
        print("3. Calculate Total")
        print("4. Visualize Expenses")
        print("5. Exit")
        choice= int(input("\nEnter your choice= "))

        if choice==1:
            add_expense()
        elif choice==2:
            data()
        elif choice==3:
            calculate_total()
        elif choice==4:
            visualize_expenses()     
        elif choice==5:
            print("You have exited")
            break
        else:
            print("Invalid Choice") 

main()
 






