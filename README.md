# AI Stock Price Prediction Bot 📈

A Telegram bot that predicts stock prices using **Machine Learning** (Linear Regression).

## 🚀 Project Overview
This project was developed as part of **Team Project 2**. It analyzes historical stock data and predicts future trends to help users make informed financial decisions.

## 🛠 Technologies Used:
* **Python** 🐍
* **Telebot (pyTelegramBotAPI)** - For Telegram integration.
* **Scikit-learn** - For the Linear Regression model.
* **Numpy & Pandas** - For data processing.
* **PythonAnywhere** - For cloud deployment.

## 📊 How It Works:
1. The user sends a command like `/predict AAPL`.
2. The bot fetches historical data (using a generated dataset for demonstration due to API restrictions on the free tier).
3. The **Linear Regression** model trains on this data.
4. The bot returns the current price, the 7-day forecast, and the predicted trend (Up/Down).

## ☁️ Deployment
The bot is hosted on **PythonAnywhere**, ensuring it runs 24/7 in the cloud.
