
# Crime and No-Crime Dashboard (2011/12)

An interactive data visualization dashboard built with Streamlit that displays crime data and no-crime records for police forces across England and Wales.

## About This Project

This dashboard was created for the 5DATA004W Coursework at the University of Westminster. It provides an interactive way to explore the relationship between recorded crimes and "no-crimes" (incidents initially recorded as crimes but later determined not to be crimes) across different police forces in England and Wales during 2011/12.

## Features

- Interactive filtering by police force and offense group
- Responsive visualizations that update based on selected filters
- Summary metrics showing total offenses, no-crimes, and the no-crime percentage
- Bar chart showing distribution of offenses by police force
- Pie chart showing distribution of offense types
- Bar chart showing no-crime ratio by police force
- Data preview table with the filtered dataset
- Download capability for filtered data

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup Instructions

1. *Clone or download this repository*

2. *Create and activate a virtual environment (optional but recommended)*

   ```bash
   # Create a virtual environment
   python -m venv venv
   
   # Activate the virtual environment
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. *Install the required packages*

   ```bash
   pip install -r requirements.txt
   ```

4. *Prepare the data*

   Ensure the dataset file `no-crime-201112-cleaned.csv` is placed in one of these locations:
   - In the root project directory (same directory as the Python script)
   - In a `data` subdirectory within the project folder

5. *Run the application*

   ```bash
   streamlit run app.py
   ```

6. *Access the dashboard*

   The application will automatically open in your default web browser. If it doesn't, open a browser and go to:
   [http://localhost:8501](http://localhost:8501)

## Data Structure

The dashboard expects a CSV file with the following columns:
- `Force_Name`: Name of the police force
- `Offence_Group`: Category of the offense
- `Force_Offences`: Number of recorded offenses
- `Force_No_Crimes`: Number of no-crimes recorded

---

