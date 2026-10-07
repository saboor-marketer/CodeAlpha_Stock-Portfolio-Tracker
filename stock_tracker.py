"""
Stock Portfolio Tracker
A simple tool to calculate total investment based on manually defined stock prices.
"""

# Hardcoded stock prices dictionary
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 150,
    "META": 330,
    "NVDA": 450,
    "JPM": 150,
    "V": 240,
    "WMT": 160
}


def get_user_portfolio():
    """
    Get stock holdings from user input.
    Returns a dictionary with stock symbols as keys and quantities as values.
    """
    portfolio = {}
    print("\n" + "="*50)
    print("Stock Portfolio Tracker")
    print("="*50)
    print(f"\nAvailable stocks and their prices:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price}")
    print("\nEnter your stock holdings (type 'done' when finished):")
    
    while True:
        symbol = input("\nEnter stock symbol (or 'done' to finish): ").strip().upper()
        
        if symbol.lower() == 'done':
            break
        
        if symbol not in STOCK_PRICES:
            print(f"Error: '{symbol}' is not in the available stocks list.")
            continue
        
        try:
            quantity = int(input(f"Enter quantity of {symbol}: ").strip())
            if quantity <= 0:
                print("Error: Quantity must be positive.")
                continue
            portfolio[symbol] = quantity
            print(f"Added {quantity} shares of {symbol} at ${STOCK_PRICES[symbol]} each")
        except ValueError:
            print("Error: Please enter a valid number for quantity.")
    
    return portfolio


def calculate_portfolio_value(portfolio):
    """
    Calculate the total value of the portfolio.
    Returns a dictionary with detailed breakdown.
    """
    total_value = 0
    breakdown = []
    
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        stock_value = price * quantity
        total_value += stock_value
        breakdown.append({
            'symbol': symbol,
            'quantity': quantity,
            'price': price,
            'value': stock_value
        })
    
    return {
        'total_value': total_value,
        'breakdown': breakdown
    }


def display_results(portfolio, result):
    """
    Display the portfolio analysis results.
    """
    print("\n" + "="*50)
    print("PORTFOLIO SUMMARY")
    print("="*50)
    
    print("\nStock Holdings:")
    print("-" * 50)
    print(f"{'Symbol':<10} {'Quantity':<10} {'Price':<10} {'Value':<15}")
    print("-" * 50)
    
    for item in result['breakdown']:
        print(f"{item['symbol']:<10} {item['quantity']:<10} ${item['price']:<9} ${item['value']:<14.2f}")
    
    print("-" * 50)
    print(f"{'TOTAL':<30} ${result['total_value']:<14.2f}")
    print("="*50)


def save_to_file(portfolio, result, filename="portfolio_report.txt"):
    """
    Save the portfolio report to a text file.
    """
    try:
        with open(filename, 'w') as f:
            f.write("="*50 + "\n")
            f.write("STOCK PORTFOLIO REPORT\n")
            f.write("="*50 + "\n\n")
            
            f.write("Stock Holdings:\n")
            f.write("-" * 50 + "\n")
            f.write(f"{'Symbol':<10} {'Quantity':<10} {'Price':<10} {'Value':<15}\n")
            f.write("-" * 50 + "\n")
            
            for item in result['breakdown']:
                f.write(f"{item['symbol']:<10} {item['quantity']:<10} ${item['price']:<9} ${item['value']:<14.2f}\n")
            
            f.write("-" * 50 + "\n")
            f.write(f"{'TOTAL':<30} ${result['total_value']:<14.2f}\n")
            f.write("="*50 + "\n")
        
        print(f"\nReport saved to: {filename}")
        return True
    except Exception as e:
        print(f"\nError saving file: {e}")
        return False


def save_to_csv(portfolio, result, filename="portfolio_report.csv"):
    """
    Save the portfolio report to a CSV file.
    """
    try:
        with open(filename, 'w') as f:
            f.write("Symbol,Quantity,Price,Value\n")
            for item in result['breakdown']:
                f.write(f"{item['symbol']},{item['quantity']},{item['price']},{item['value']}\n")
            f.write(f"TOTAL,,,{result['total_value']}\n")
        
        print(f"CSV report saved to: {filename}")
        return True
    except Exception as e:
        print(f"Error saving CSV file: {e}")
        return False


def main():
    """
    Main function to run the stock portfolio tracker.
    """
    # Get user input
    portfolio = get_user_portfolio()
    
    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return
    
    # Calculate portfolio value
    result = calculate_portfolio_value(portfolio)
    
    # Display results
    display_results(portfolio, result)
    
    # Ask if user wants to save the report
    save_choice = input("\nWould you like to save the report to a file? (y/n): ").strip().lower()
    
    if save_choice == 'y':
        format_choice = input("Choose format (txt/csv/both): ").strip().lower()
        
        if format_choice == 'txt' or format_choice == 'both':
            save_to_file(portfolio, result)
        
        if format_choice == 'csv' or format_choice == 'both':
            save_to_csv(portfolio, result)
    
    print("\nThank you for using the Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()
