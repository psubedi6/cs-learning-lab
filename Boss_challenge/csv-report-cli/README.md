# Section 1 — Project Information

## Project Name
csv-report-cli

## Goal
Read CSV files and generate useful summary reports
through a command-line interface.


# Section 2 — Project Structure
csv-report-cli/
│
├── main.py
├── csv_reader.py
├── report.py
├── exceptions.py
├── utils.py
│
├── sample_data/
│      └── sales.csv
│
├── reports/
│
└── README.md

# Section 3 — Module Responsibilities
main.py: Starts the application and coordinates everything
csv_reader.py:	Reads CSV files
report.py:	Generates reports from data
exceptions.py:	Stores custom exceptions
utils.py:	Helper functions used throughout the project

# Section 4 — Inputs
## INPUTS
• CSV filename
• (Optional) Report type

# Section 5 — Processing
## PROCESSING
Read CSV
↓
Validate file
↓
Load data
↓
Analyze data
↓
Generate report
↓
Format output

# Section 6 — Outputs
## OUTPUTS
Terminal Report
or
Saved Report File

Example:
========== REPORT ==========
Total Rows : 120
Average Salary : $64,000
Highest Salary : $98,000

# Section 7 — Error Cases
ERROR CASES
• File not found
• Wrong file type
• Empty CSV
• Missing columns
• Invalid data
• Permission denied
• Missing command-line argument

# Section 8 — Program Flow
                User
                  │
                  ▼
         Run main.py
                  │
                  ▼
         Validate Input
          │          │
          │          │
          ▼          ▼
      Invalid      Valid
          │          │
          ▼          ▼
     Show Error   Read CSV
                      │
                      ▼
                Analyze Data
                      │
                      ▼
               Generate Report
                      │
                      ▼
               Display Result
                      │
                      ▼
                 Program Ends

# Section 9 — Design Principles
DESIGN PRINCIPLES
• One module = one responsibility.
• Plan before coding.
• Think about errors first.
• Organize code into small modules.
• Convert raw data into useful information.
• Keep Version 1 simple.
• Design answers "What?"
• Code answers "How?"

# The Entire Project at a Glance
Goal
   │
   ▼
Inputs
   │
   ▼
Processing
   │
   ▼
Outputs
   │
   ▼
Errors
   │
   ▼
Modules
   │
   ▼
Program Flow