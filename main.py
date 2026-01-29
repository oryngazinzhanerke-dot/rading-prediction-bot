import telebot
import numpy as np
from sklearn.linear_model import LinearRegression
import time

TOKEN = '7804517099:AAH2FwvQx0q0UNl4H0ZgcQ6HZ5X0UAm0sHU'
bot = telebot.TeleBot(TOKEN)

def get_mock_prediction(ticker):
    # Generating demo data for ML model due to API restrictions
    np.random.seed(int(time.time()) % 1000)
    base_price = 150.0 if ticker == "AAPL" else 100.0
    prices = base_price + np.cumsum(np.random.randn(30) * 2)
    
    days = np.arange(len(prices)).reshape(-1, 1)
    model = LinearRegression().fit(days, prices)
    
    curr = float(prices[-1])
    pred = float(model.predict([[len(prices) + 7]])[0])
    return curr, pred

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Send /predict TICKER (e.g., /predict AAPL) to get stock forecasts.")

@bot.message_handler(commands=['predict'])
def predict(message):
    parts = message.text.split()
    ticker = parts[1].upper() if len(parts) > 1 else "AAPL"
    bot.send_message(message.chat.id, f"🔍 Analyzing {ticker} (Demo Mode)...")
    
    time.sleep(1) 
    curr, pred = get_mock_prediction(ticker)
    
    diff = pred - curr
    trend = "📈 UP" if diff > 0 else "📉 DOWN"
    
    response = (
        f"✅ **{ticker} Forecast (ML Linear Regression)**\n\n"
        f"Current Price: {curr:.2f}\n"
        f"7-Day Prediction: {pred:.2f}\n"
        f"Predicted Trend: {trend}"
    )
    bot.send_message(message.chat.id, response)

print("Bot is running in English Demo Mode...")
bot.polling()
