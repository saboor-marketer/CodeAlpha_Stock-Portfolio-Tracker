# Stock Portfolio Tracker

A simple Python-based stock portfolio tracker that calculates total investment value based on manually defined stock prices.

## Features

- **Stock Input**: Users can input stock symbols and quantities
- **Hardcoded Prices**: Uses a predefined dictionary of stock prices
- **Real-time Calculation**: Instantly calculates total portfolio value
- **Detailed Breakdown**: Shows individual stock values and total investment
- **File Export**: Optional saving of reports to TXT or CSV format

## Key Concepts Used

- **Dictionaries**: Storing and accessing stock prices
- **Input/Output**: User interaction through console
- **Basic Arithmetic**: Calculating portfolio values
- **File Handling**: Writing reports to text and CSV files
- **Functions**: Modular code organization
- **Error Handling**: Input validation and error messages

## Requirements

- Python 3.x (no external dependencies required)

## Available Stocks

The tracker includes the following stocks with their hardcoded prices:

| Symbol | Price |
|--------|-------|
| AAPL   | $180  |
| TSLA   | $250  |
| GOOGL  | $140  |
| MSFT   | $320  |
| AMZN   | $150  |
| META   | $330  |
| NVDA   | $450  |
| JPM    | $150  |
| V      | $240  |
| WMT    | $160  |

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Ensure Python 3.x is installed on your system

## Usage

Run the program using Python:

```bash
python stock_tracker.py
```

### Step-by-Step Guide

1. **Launch the Program**: Run the script using the command above
2. **View Available Stocks**: The program displays all available stocks and their prices
3. **Enter Stock Holdings**:
   - Enter a stock symbol (e.g., AAPL)
   - Enter the quantity of shares you own
   - Repeat for each stock
   - Type 'done' when finished
4. **View Results**: The program displays a detailed breakdown of your portfolio
5. **Save Report (Optional)**: Choose to save the report as TXT, CSV, or both formats

### Example Session

```
==================================================
Stock Portfolio Tracker
==================================================

Available stocks and their prices:
  AAPL: $180
  TSLA: $250
  GOOGL: $140
  MSFT: $320
  AMZN: $150
  META: $330
  NVDA: $450
  JPM: $150
  V: $240
  WMT: $160

Enter your stock holdings (type 'done' when finished):

Enter stock symbol (or 'done' to finish): AAPL
Enter quantity of AAPL: 10
Added 10 shares of AAPL at $180 each

Enter stock symbol (or 'done' to finish): TSLA
Enter quantity of TSLA: 5
Added 5 shares of TSLA at $250 each

Enter stock symbol (or 'done' to finish): done

==================================================
PORTFOLIO SUMMARY
==================================================

Stock Holdings:
--------------------------------------------------
Symbol     Quantity  Price      Value          
--------------------------------------------------
AAPL       10        $180       $1800.00       
TSLA       5         $250       $1250.00       
--------------------------------------------------
TOTAL                            $3050.00       
==================================================

Would you like to save the report to a file? (y/n): y
Choose format (txt/csv/both): txt

Report saved to: portfolio_report.txt

Thank you for using the Stock Portfolio Tracker!
```

## Output Files

### TXT Format (`portfolio_report.txt`)
A human-readable text file with formatted portfolio summary.

### CSV Format (`portfolio_report.csv`)
A comma-separated values file suitable for spreadsheet applications like Excel or Google Sheets.

## Code Structure

- `STOCK_PRICES`: Dictionary containing hardcoded stock prices
- `get_user_portfolio()`: Collects stock holdings from user input
- `calculate_portfolio_value()`: Computes total portfolio value
- `display_results()`: Shows formatted portfolio summary
- `save_to_file()`: Exports report to TXT format
- `save_to_csv()`: Exports report to CSV format
- `main()`: Main program execution flow

## Error Handling

The program includes error handling for:
- Invalid stock symbols
- Non-numeric quantity inputs
- Negative or zero quantities
- File writing errors

## Customization

To add or modify stock prices, edit the `STOCK_PRICES` dictionary in `stock_tracker.py`:

```python
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    # Add more stocks here
    "NEW_STOCK": 100
}
```

## Limitations

- Stock prices are hardcoded and not real-time
- Limited to the stocks defined in the dictionary
- No historical data or portfolio tracking over time
- Basic functionality without advanced financial calculations

## Future Enhancements

Potential improvements for future versions:
- Integration with real-time stock price APIs
- Portfolio tracking over time
- Advanced financial metrics (ROI, P/L, etc.)
- Database support for persistent storage
- Graphical user interface
- Support for multiple portfolios

## License

This project is open source and available for educational purposes.

## Author

Created as a learning project to demonstrate Python programming concepts including dictionaries, file I/O, and basic arithmetic operations.
