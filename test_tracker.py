"""
Test script for Stock Portfolio Tracker
Simulates user input to verify functionality
"""

from stock_tracker import STOCK_PRICES, calculate_portfolio_value, display_results, save_to_file, save_to_csv


def test_portfolio_calculation():
    """Test the portfolio calculation with sample data"""
    print("Testing Stock Portfolio Tracker...")
    print("\n" + "="*50)
    
    # Sample portfolio
    portfolio = {
        "AAPL": 10,
        "TSLA": 5,
        "NVDA": 3
    }
    
    print("Sample Portfolio:")
    for symbol, quantity in portfolio.items():
        print(f"  {symbol}: {quantity} shares @ ${STOCK_PRICES[symbol]}")
    
    # Calculate
    result = calculate_portfolio_value(portfolio)
    
    # Display
    display_results(portfolio, result)
    
    # Save to files
    print("\nSaving reports...")
    save_to_file(portfolio, result, "test_portfolio_report.txt")
    save_to_csv(portfolio, result, "test_portfolio_report.csv")
    
    print("\nTest completed successfully!")
    print("\nGenerated files:")
    print("  - test_portfolio_report.txt")
    print("  - test_portfolio_report.csv")


if __name__ == "__main__":
    test_portfolio_calculation()
