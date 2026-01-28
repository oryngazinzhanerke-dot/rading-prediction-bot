import telebot
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import requests

# Настройка для обхода ошибки SSL
requests.packages.urllib3.disable_warnings()

TOKEN = "7804517099:AAH2FwvQx0q0UNl4H0ZgcQ6HZ5X0UAm0sHU"
bot = telebot.TeleBot(TOKEN)


def get_prediction(ticker):
    try:
        # Тек қажетті параметрлерді қалдырдық
        data = yf.download(ticker, period="1y", interval="1d")

        if data.empty or len(data) < 10:
            return None

        prices = data["Close"].values.flatten()
        prices = prices[~np.isnan(prices)]

        days = np.arange(len(prices)).reshape(-1, 1)
        model = LinearRegression().fit(days, prices)

        curr = float(prices[-1])
        pred = float(model.predict([[len(prices) + 7]])[0])

        return curr, pred
    except Exception as e:
        print(f"Error: {e}")
        return None


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message, "Hi! Send me a ticker, e.g., /predict AAPL or /predict KSPI.KZ"
    )


@bot.message_handler(commands=["predict"])
def predict(message):
    parts = message.text.split()
    if len(parts) < 2:
        bot.reply_to(message, "Usage: /predict [ticker]")
        return

    ticker = parts[1].upper()
    bot.send_message(message.chat.id, f"Analyzing {ticker}...")

    result = get_prediction(ticker)
    if result:
        curr, pred = result
        diff = ((pred - curr) / curr) * 100
        trend = "📈 UP" if diff > 0 else "📉 DOWN"
        bot.send_message(
            message.chat.id,
            f"--- {ticker} ---\nCurrent: {curr:.2f}\n7-Day Forecast: {pred:.2f}\nTrend: {trend} ({diff:.2f}%)",
        )
    else:
        bot.send_message(message.chat.id, "Still no data. Try /predict AAPL first.")


print("Bot is running...")
bot.polling()
