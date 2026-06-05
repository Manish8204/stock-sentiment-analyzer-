"""
Technical Analysis Module
Calculates technical indicators for stocks
"""

import logging
import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


class TechnicalIndicators:
    """Calculate various technical indicators"""
    
    @staticmethod
    def calculate_sma(data, period):
        """Simple Moving Average"""
        return data.rolling(window=period).mean()
    
    @staticmethod
    def calculate_ema(data, period):
        """Exponential Moving Average"""
        return data.ewm(span=period, adjust=False).mean()
    
    @staticmethod
    def calculate_rsi(data, period=14):
        """Relative Strength Index"""
        delta = data.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi
    
    @staticmethod
    def calculate_macd(data, fast=12, slow=26, signal=9):
        """MACD (Moving Average Convergence Divergence)"""
        ema_fast = data.ewm(span=fast, adjust=False).mean()
        ema_slow = data.ewm(span=slow, adjust=False).mean()
        
        macd = ema_fast - ema_slow
        signal_line = macd.ewm(span=signal, adjust=False).mean()
        histogram = macd - signal_line
        
        return pd.DataFrame({
            'macd': macd,
            'signal': signal_line,
            'histogram': histogram
        })
    
    @staticmethod
    def calculate_bollinger_bands(data, period=20, std_dev=2):
        """Bollinger Bands"""
        sma = data.rolling(window=period).mean()
        std = data.rolling(window=period).std()
        
        upper_band = sma + (std_dev * std)
        lower_band = sma - (std_dev * std)
        
        return pd.DataFrame({
            'middle': sma,
            'upper': upper_band,
            'lower': lower_band
        })
    
    @staticmethod
    def calculate_atr(high, low, close, period=14):
        """Average True Range"""
        tr1 = high - low
        tr2 = abs(high - close.shift())
        tr3 = abs(low - close.shift())
        
        tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
        atr = tr.rolling(window=period).mean()
        
        return atr
    
    @staticmethod
    def calculate_obv(close, volume):
        """On-Balance Volume"""
        obv = np.zeros(len(close))
        obv[0] = volume.iloc[0]
        
        for i in range(1, len(close)):
            if close.iloc[i] > close.iloc[i-1]:
                obv[i] = obv[i-1] + volume.iloc[i]
            elif close.iloc[i] < close.iloc[i-1]:
                obv[i] = obv[i-1] - volume.iloc[i]
            else:
                obv[i] = obv[i-1]
        
        return pd.Series(obv, index=close.index)


class TechnicalAnalysisPipeline:
    """Process stock data with technical indicators"""
    
    def __init__(self, config):
        self.config = config.get('technical_indicators', {})
        self.indicators = TechnicalIndicators()
    
    def analyze_stock(self, ohlcv_data):
        """Calculate all technical indicators for stock"""
        if ohlcv_data is None or len(ohlcv_data) == 0:
            logger.warning("Empty OHLCV data")
            return None
        
        try:
            df = ohlcv_data.copy()
            
            # Calculate indicators
            df['RSI'] = self.indicators.calculate_rsi(
                df['Close'],
                self.config.get('rsi_period', 14)
            )
            
            macd_data = self.indicators.calculate_macd(
                df['Close'],
                self.config.get('macd_fast', 12),
                self.config.get('macd_slow', 26),
                self.config.get('macd_signal', 9)
            )
            df = pd.concat([df, macd_data], axis=1)
            
            bb_data = self.indicators.calculate_bollinger_bands(
                df['Close'],
                self.config.get('bollinger_period', 20),
                self.config.get('bollinger_std', 2)
            )
            df = pd.concat([df, bb_data], axis=1)
            
            df['ATR'] = self.indicators.calculate_atr(
                df['High'],
                df['Low'],
                df['Close']
            )
            
            df['OBV'] = self.indicators.calculate_obv(
                df['Close'],
                df['Volume']
            )
            
            # Add SMA and EMA
            df['SMA_20'] = self.indicators.calculate_sma(df['Close'], 20)
            df['SMA_50'] = self.indicators.calculate_sma(df['Close'], 50)
            df['EMA_12'] = self.indicators.calculate_ema(df['Close'], 12)
            
            logger.info("Technical indicators calculated successfully")
            return df
            
        except Exception as e:
            logger.error(f"Error calculating technical indicators: {e}")
            return None
    
    def get_indicator_summary(self, df):
        """Get summary of current indicator values"""
        if df is None or len(df) == 0:
            return {}
        
        latest = df.iloc[-1]
        
        return {
            'rsi': latest.get('RSI', np.nan),
            'macd': latest.get('macd', np.nan),
            'signal': latest.get('signal', np.nan),
            'bb_upper': latest.get('upper', np.nan),
            'bb_middle': latest.get('middle', np.nan),
            'bb_lower': latest.get('lower', np.nan),
            'atr': latest.get('ATR', np.nan),
            'obv': latest.get('OBV', np.nan),
            'sma_20': latest.get('SMA_20', np.nan),
            'sma_50': latest.get('SMA_50', np.nan)
        }
