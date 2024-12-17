import pandas as pd
import functions as ft

def main():
    users = {}

    while True:
        print("\n---STOCK SELECTION TOOL---")
        print("Welcome to Stock Selection Tool :)")
        print("\n1. Register\n2. Login\n3. EXIT")
        choice = input("Choose an option (1/2/3): ")

        if choice == '3':
            confirm_exit = input('Are you sure to EXIT? (Yes/No): ').lower()
            if confirm_exit == 'yes':
                print("Thank you. Please come again")
                return
            else:
                print('Returning to main menu...')
        

        email = input("Enter your email: ")
        if '@' not in email:
            print("Please put the right email format")
            continue

        password = input("Enter your password: ")

        if choice == '1':
            if ft.register_user(users, email, password):
                print("REGISTRATION SUCCESSFUL! Please log in.\n------------------------------")
            else:
                print("This email is already registered. Please log in.")
        elif choice == '2':
            if ft.authenticate_user(users, email, password):
                print("LOGIN SUCCESSFUL!!!\n------------------------------")
                break
            else:
                print("Invalid credentials. Please try again.\n------------------------------")
        else:
            print("Invalid choice. Please select 1 to Register, 2 to Login, or 3 to Exit.\n------------------------------")

    while True:
        print("\n1. Fetch and analyze stock data\n2. Read stored data\n3. EXIT")
        main_choice = input("Choose an option (1/2/3): ")

        if main_choice == '1':
            print("\n===STOCK TICKER===")
            print("Example of stock tickers:")
            print("1. Malayan Banking Berhad: 1155.KL")
            print("2. Bank Islam Malaysia Berhad: 5258.KL")
            print("3. Public Bank Berhad: 1295.KL")  
            print("4. CIMB Group Holdings Berhad: 1023.KL")
            
            ticker = input("\nEnter the stock ticker: ")
            start_date = input("Enter the start date (YYYY-MM-DD): ")
            end_date = input("Enter the end date (YYYY-MM-DD): ")

            closing_prices = ft.get_closing_prices(ticker, start_date, end_date)
            if closing_prices is not None:
                print("\n------------------------------\nClosing Prices:")
                print(pd.DataFrame(closing_prices))

                analysis = ft.analyze_closing_prices(closing_prices)
                
                print("\n------------------------------\nAnalysis:")
                print(f"Average closing price: {analysis['average']}")
                print(f"Percentage change: {analysis['percentage_change']}%")
                print(f"Highest closing price: {analysis['highest']}")
                print(f"Lowest closing price: {analysis['lowest']}")

                ft.save_to_csv(email, ticker, analysis)
                ft.plot_closing_prices(closing_prices, ticker)
            else:
                print("Failed to fetch closing prices. Please try again.")

        elif main_choice == '2':
            print("\n------------------------------\nUser interaction data:")
            ft.read_from_csv()

        elif main_choice == '3':
            confirm_exit1 = input('Are you sure to EXIT? (Yes/No): ').lower()
            if confirm_exit1 == 'yes':
                print("Thank you. Please come again")
                break
            else:
                print('Returning to main menu...')
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
