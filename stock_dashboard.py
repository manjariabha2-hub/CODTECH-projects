import urllib.request
import json
import datetime


# Free demo API
API_KEY = "demo"



def get_stock_data(symbol):

    url = (
        "https://www.alphavantage.co/query?"
        "function=GLOBAL_QUOTE&"
        f"symbol={symbol}&"
        f"apikey={API_KEY}"
    )


    try:

        response = urllib.request.urlopen(url)

        data = json.loads(
            response.read()
        )


        return data.get(
            "Global Quote",
            {}
        )


    except:

        return {}




def show_dashboard(symbol):


    print("\nLoading data...\n")


    data = get_stock_data(symbol)



    if not data:

        print(
            "Unable to get stock data"
        )

        print(
            "Try symbols like IBM or AAPL"
        )

        return



    print("==============================")

    print("     STOCK MARKET DASHBOARD")

    print("==============================")


    print(
        "Symbol:",
        data.get(
            "01. symbol"
        )
    )


    print(
        "Price:",
        data.get(
            "05. price"
        )
    )


    print(
        "Change:",
        data.get(
            "09. change"
        )
    )


    print(
        "Change Percentage:",
        data.get(
            "10. change percent"
        )
    )


    print(
        "Last Updated:",
        data.get(
            "07. latest trading day"
        )
    )


    print("==============================")





def main():


    print("""
================================
       STOCK DASHBOARD
================================
""")


    while True:


        print("""
1. Search Stock
2. Exit
""")


        choice=input(
            "Choose option: "
        )



        if choice=="1":


            symbol=input(
                "Enter stock symbol: "
            )


            show_dashboard(
                symbol.upper()
            )



        elif choice=="2":


            print(
                "Goodbye"
            )

            break



        else:


            print(
                "Invalid choice"
            )





if __name__=="__main__":

    main()