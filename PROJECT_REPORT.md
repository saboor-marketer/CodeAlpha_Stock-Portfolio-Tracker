# Stock Portfolio Tracker - Project Report

## Project Overview

**Project Name**: Stock Portfolio Tracker  
**Language**: Python  
**Completion Date**: October 7, 2026  
**Objective**: Build a simple stock tracker that calculates total investment based on manually defined stock prices

## Project Summary

The Stock Portfolio Tracker is a command-line application that allows users to input stock holdings and calculates the total investment value using hardcoded stock prices. The project demonstrates fundamental Python programming concepts including dictionaries, input/output operations, basic arithmetic, and file handling.

## Technical Specifications

### Programming Language
- Python 3.x
- No external dependencies required

### Key Features Implemented

1. **Stock Price Dictionary**
   - Hardcoded dictionary with 10 popular stocks
   - Easy to modify and extend
   - Stocks include: AAPL, TSLA, GOOGL, MSFT, AMZN, META, NVDA, JPM, V, WMT

2. **User Input System**
   - Interactive command-line interface
   - Stock symbol validation
   - Quantity input with error handling
   - Exit mechanism with 'done' command

3. **Portfolio Calculation**
   - Real-time value calculation per stock
   - Total portfolio value computation
   - Detailed breakdown display

4. **File Export**
   - TXT format for human-readable reports
   - CSV format for spreadsheet compatibility
   - User choice of export format

### Key Concepts Demonstrated

#### 1. Dictionaries
- Used to store stock prices as key-value pairs
- Efficient lookup for price retrieval
- Example:
```python
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    ...
}
```

#### 2. Input/Output Operations
- Console input using `input()` function
- Formatted output using f-strings
- User-friendly prompts and error messages

#### 3. Basic Arithmetic
- Multiplication for stock value calculation
- Addition for total portfolio value
- Floating-point arithmetic for precise values

#### 4. File Handling
- Text file writing with `open()` in write mode
- CSV file generation
- Exception handling for file operations

#### 5. Functions
- Modular code organization
- Separation of concerns
- Reusable components

#### 6. Error Handling
- Input validation
- Exception handling for file operations
- User-friendly error messages

## Code Structure

### Main Components

```
stock_tracker.py
├── STOCK_PRICES (dictionary)
├── get_user_portfolio() (function)
├── calculate_portfolio_value() (function)
├── display_results() (function)
├── save_to_file() (function)
├── save_to_csv() (function)
└── main() (function)
```

### Function Descriptions

| Function | Purpose | Parameters | Returns |
|----------|---------|------------|---------|
| `get_user_portfolio()` | Collects stock holdings from user | None | Dictionary of stocks and quantities |
| `calculate_portfolio_value()` | Computes portfolio value | Portfolio dictionary | Dictionary with total and breakdown |
| `display_results()` | Shows formatted results | Portfolio, result dictionary | None |
| `save_to_file()` | Exports to TXT file | Portfolio, result, filename | Boolean (success status) |
| `save_to_csv()` | Exports to CSV file | Portfolio, result, filename | Boolean (success status) |
| `main()` | Orchestrates program flow | None | None |

## Testing

### Test Results

A test script (`test_tracker.py`) was created to verify functionality:

**Test Portfolio:**
- AAPL: 10 shares @ $180 = $1,800
- TSLA: 5 shares @ $250 = $1,250
- NVDA: 3 shares @ $450 = $1,350

**Total Portfolio Value: $4,400**

**Output Files Generated:**
- `test_portfolio_report.txt` - Formatted text report
- `test_portfolio_report.csv` - CSV data file

### Test Coverage

✓ Dictionary lookup functionality  
✓ User input handling  
✓ Arithmetic calculations  
✓ File writing operations  
✓ Error handling for invalid inputs  
✓ Formatted output display  

## Usage Instructions

### Running the Program

```bash
python stock_tracker.py
```

### User Workflow

1. View available stocks and prices
2. Enter stock symbol
3. Enter quantity
4. Repeat for all holdings
5. Type 'done' to finish
6. View portfolio summary
7. Optionally save report (TXT/CSV/both)

### Example Output

```
==================================================
PORTFOLIO SUMMARY
==================================================

Stock Holdings:
--------------------------------------------------
Symbol     Quantity   Price      Value          
--------------------------------------------------
AAPL       10         $180       $1800.00       
TSLA       5          $250       $1250.00       
NVDA       3          $450       $1350.00       
--------------------------------------------------
TOTAL                          $4400.00       
==================================================
```

## File Organization

```
Stock Portfolio tracker/
├── stock_tracker.py           # Main application
├── test_tracker.py            # Test script
├── README.md                  # User documentation
├── PROJECT_REPORT.md          # This file
├── test_portfolio_report.txt  # Sample TXT output
└── test_portfolio_report.csv  # Sample CSV output
```

## Learning Outcomes

This project successfully demonstrates:

1. **Dictionary Operations**: Creating, accessing, and manipulating dictionaries
2. **User Interaction**: Building interactive command-line interfaces
3. **Data Processing**: Calculating and formatting data
4. **File I/O**: Reading and writing files in different formats
5. **Code Organization**: Structuring code with functions
6. **Error Handling**: Implementing robust error checking
7. **Documentation**: Creating comprehensive documentation

## Limitations

1. **Static Prices**: Stock prices are hardcoded and not real-time
2. **Limited Stock List**: Only includes 10 predefined stocks
3. **No Persistence**: Portfolio data is not saved between sessions
4. **Basic Calculations**: Does not include advanced financial metrics
5. **Command-Line Only**: No graphical user interface

## Future Enhancements

### Potential Improvements

1. **Real-time Data Integration**
   - Connect to stock price APIs (e.g., Alpha Vantage, Yahoo Finance)
   - Automatic price updates
   - Historical data tracking

2. **Advanced Features**
   - Portfolio performance tracking over time
   - Return on Investment (ROI) calculations
   - Profit/Loss analysis
   - Dividend tracking

3. **Data Persistence**
   - Database integration (SQLite, PostgreSQL)
   - Save/load portfolio configurations
   - User account management

4. **User Interface**
   - Graphical User Interface (GUI) using Tkinter or PyQt
   - Web-based interface using Flask/Django
   - Mobile application

5. **Additional Functionality**
   - Multiple portfolio support
   - Portfolio comparison tools
   - Investment recommendations
   - Risk assessment metrics

## Conclusion

The Stock Portfolio Tracker successfully achieves its stated objectives:
- ✓ Implements dictionary-based stock price storage
- ✓ Provides user input/output functionality
- ✓ Performs basic arithmetic calculations
- ✓ Includes optional file handling
- ✓ Demonstrates core Python programming concepts

The project serves as an excellent foundation for learning Python programming and can be extended with more advanced features as needed. The code is well-structured, documented, and tested, making it suitable for educational purposes and further development.

## References

- Python Documentation: https://docs.python.org/3/
- File I/O Operations: https://docs.python.org/3/tutorial/inputoutput.html
- Dictionary Data Structure: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

---

**Project Status**: ✅ Complete  
**Test Status**: ✅ Passed  
**Documentation**: ✅ Complete
