import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os

current_directory = os.path.dirname(os.path.realpath(__file__))

def register_user(users, email, password):
    if email in users:
        return False
    users[email] = password
    return True

def authenticate_user(users, email, password):
    stored_password = users.get(email)
    
    if stored_password == password:
        return True  
    else:
        return False  
    
def get_closing_prices(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data[['Close']]

def analyze_closing_prices(closing_price):
    analysis = {
        'average': closing_price['Close'].mean(),
        'percentage_change': ((closing_price['Close'].iloc[-1] - closing_price['Close'].iloc[0]) / closing_price['Close'].iloc[0]) * 100,
        'highest': closing_price['Close'].max(),
        'lowest': closing_price['Close'].min()
    }
    return analysis

def plot_closing_prices(closing_prices, ticker):
    closing_prices['Close'].plot(figsize=(10, 6), title=f"Stock Performance: {ticker}")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.grid()
    plt.show()

def save_to_csv(email, ticker, analysis, filename='user_data.csv'):
    closing_price = {
        'email':[email],
        'ticker':[ticker],
        'average': [analysis['average']],
        'percentage_change': [analysis['percentage_change']],
        'highest': [analysis['highest']],
        'lowest': [analysis['lowest']]
    }
    df = pd.DataFrame(closing_price)
    df.to_csv(os.path.join(current_directory, filename), index=False)

def read_from_csv(filename='user_data.csv'):
    file_path = os.path.join(current_directory, filename)
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        print(df)
    else:
        print("No data found.")

