# PyFolio - Personal Finance Tracker

#### Video Demo: https://youtu.be/iOw4ksMNIRo

#### Description:
PennyPilot is a Python-based personal finance tracker that helps users monitor spending habits through a simple terminal interface. Built for CS50P's final project, it features:

**Core Functionality**:
- Transaction recording with date, amount, and category
- Visual spending summaries
- Category-based expense analysis
- CSV data storage for persistence

**Technical Implementation**:
- `project.py` contains:
  - `main()`: Handles user interaction loop
  - `add_transaction()`: Validates and stores new entries
  - `view_summary()`: Generates expense reports
  - `calculate_balance()`: Performs financial calculations
  - `export_to_csv()`: Bonus feature for data portability

**Testing**:
- `test_project.py` includes 5 test cases:
  - `test_add_transaction()`: Verifies input validation
  - `test_view_summary()`: Checks report accuracy
  - `test_calculate_balance()`: Tests math operations
  - `test_edge_cases()`: Handles unusual inputs
  - `test_file_operations()`: Ensures data persistence

**Design Choices**:
1. Used CSV over SQLite for simplicity
2. Implemented defensive programming for user inputs
3. Chose terminal interface for maximum compatibility
4. Added pytest fixtures for isolated testing

**How to Use**:
1. Run `python project.py`
2. Follow menu prompts
3. View automatic spending analyses

**Dependencies**:
- Python 3.10+
- pytest (for testing)

**Future Enhancements**:
- Graphical interface with Tkinter
- Cloud sync functionality
- Budget alert system
