# Contributing to Stock Sentiment Analyzer

We welcome contributions! Here's how you can help improve this project.

## 📋 Getting Started

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🎯 Areas for Contribution

- **New Data Sources**: Add cryptocurrency, forex, or crypto exchange data
- **Sentiment Models**: Implement BERT, GPT-based sentiment analysis
- **Prediction Models**: Add ARIMA, Prophet, or Neural Network models
- **Visualizations**: Create more interactive dashboards
- **Documentation**: Improve docs and add examples
- **Tests**: Add unit and integration tests
- **Performance**: Optimize data processing and model training

## 💡 Development Guidelines

- Follow PEP 8 style guide
- Add docstrings to all functions
- Write meaningful commit messages
- Add tests for new features
- Update README if needed

## 🐛 Reporting Issues

Please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Python version and environment details

## 📝 Code Style

```python
# Good
def calculate_rsi(data, period=14):
    """Calculate Relative Strength Index."""
    pass

# Avoid
def calc_rsi(d, p=14):
    pass
```

## 🧪 Testing

```bash
# Run tests
python -m pytest tests/

# With coverage
pytest --cov=src tests/
```

Thank you for contributing! 🙏