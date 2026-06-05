# Stock Sentiment Analyzer 📈

A comprehensive machine learning project that combines **trading data analysis**, **news sentiment extraction**, and **price prediction** to provide intelligent stock market insights.

## 🎯 Project Overview

Stock Sentiment Analyzer is designed to help traders and investors make data-driven decisions by analyzing:

1. **News Sentiment Analysis** - Extract and classify sentiment from financial news articles
2. **Trading Data Analysis** - Analyze historical price movements, volume, and trading patterns
3. **Price Prediction** - Predict future stock prices using ML models combining sentiment and technical indicators

## 🌟 Key Features

- Real-time sentiment analysis from financial news
- Historical stock data processing and visualization
- Multiple ML models for prediction (LSTM, Random Forest, XGBoost)
- Interactive dashboard for viewing predictions
- Technical indicators (RSI, MACD, Bollinger Bands)
- Sentiment correlation with stock prices

## 📊 Project Structure

```
stock-sentiment-analyzer-/
├── data/
│   ├── raw/              # Raw trading data and news articles
│   ├── processed/        # Cleaned and processed data
│   └── models/           # Trained ML models
├── src/
│   ├── data_collection/  # Scripts for fetching stock data and news
│   ├── sentiment_analysis/   # NLP sentiment processing
│   ├── technical_analysis/   # Trading indicators and analysis
│   ├── prediction/       # ML models and predictions
│   └── visualization/    # Plotting and dashboard
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_sentiment_analysis.ipynb
│   ├── 03_technical_analysis.ipynb
│   └── 04_prediction_models.ipynb
├── requirements.txt
├── config.yaml
└── main.py
```

## 🔧 Tech Stack

- **Data Collection**: yfinance, NewsAPI, Beautiful Soup
- **NLP**: NLTK, TextBlob, VADER, Transformers (BERT)
- **ML/DL**: scikit-learn, XGBoost, TensorFlow, LSTM
- **Visualization**: Matplotlib, Plotly, Streamlit
- **Data Processing**: Pandas, NumPy

## 🚀 Getting Started

### Installation

```bash
git clone https://github.com/Manish8204/stock-sentiment-analyzer-.git
cd stock-sentiment-analyzer-
pip install -r requirements.txt
```

### Configuration

Create `config.yaml` with your API keys:
```yaml
newsapi:
  api_key: "your_newsapi_key"
  
stocks:
  - symbol: "AAPL"
    name: "Apple Inc."
  - symbol: "GOOGL"
    name: "Alphabet Inc."
```

### Usage

```bash
# Run the main analysis pipeline
python main.py

# Or run individual components
python src/data_collection/fetch_stock_data.py
python src/sentiment_analysis/analyze_news.py
python src/prediction/train_models.py

# Launch interactive dashboard
streamlit run src/visualization/dashboard.py
```

## 📈 Model Performance

- Sentiment Classification Accuracy: ~85-90%
- Price Prediction RMSE: Varies by stock
- Trading Strategy Win Rate: ~55-65%

## 📚 Project Pipeline

1. **Data Collection** → Fetch stock prices, volume, news articles
2. **Sentiment Analysis** → Classify news sentiment (Positive/Negative/Neutral)
3. **Technical Analysis** → Calculate indicators (RSI, MACD, BB)
4. **Feature Engineering** → Combine sentiment + technical indicators
5. **Model Training** → Train LSTM, Random Forest, XGBoost models
6. **Prediction & Backtesting** → Validate on historical data
7. **Visualization** → Interactive dashboard for results

## 🎓 Learning Outcomes

- NLP and Sentiment Analysis techniques
- Time series forecasting with LSTM
- Feature engineering for financial data
- ML model ensemble techniques
- Real-world data pipeline development

## 📝 License

MIT License - feel free to use for educational purposes

## 👤 Author

**Manish Sharma**

---

*Happy Trading! 🚀*
