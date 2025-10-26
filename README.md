# Indian_Startup_Analysis
# Indian Startup Funding Analysis

A **Streamlit-based interactive dashboard** to analyze Indian startup funding trends, investor activities, and overall ecosystem growth. The project leverages **Python, Pandas, Matplotlib, and Streamlit** to provide insights from historical startup funding data.

---

## Project Overview

This project analyzes funding data of Indian startups, providing insights at three levels:  

1. **Investor Analysis** – Explore individual investor behavior, top sectors, cities of investment, and year-on-year trends.  
2. **Startup Analysis** – Evaluate funding patterns for specific startups.  
3. **Overall Analysis** – Summarize ecosystem metrics including total investment, max investment in a startup, monthly trends, and funded startups.  

The dashboard allows interactive exploration with dropdowns for investors and startups and visualizes data using **bar charts, line charts, and pie charts**.  

---

## Tech Stack

- **Python** – Data processing and analysis.  
- **Streamlit** – Interactive web dashboard.  
- **Pandas** – Data cleaning, preprocessing, and manipulation.  
- **Matplotlib** – Data visualization.  

---

## Features

### Investor Analysis
- Select an investor from a dropdown.  
- View **recent investments** (top 5).  
- Display **biggest investments** (bar chart).  
- Top **sectors** and **cities** of investment (pie charts).  
- Year-on-Year investment trends (line chart).  

### Startup Analysis
- Select a startup from a dropdown.  
- Display detailed funding information and trends. *(Future implementation can add charts similar to investor view.)*  

### Overall Analysis
- Key metrics:
  - Total investment in Indian startups  
  - Maximum investment in a single startup  
  - Average investment per startup  
  - Total funded startups  
- Month-on-Month total investments and number of startups funded (line charts).  

---

## Data Cleaning & Preprocessing

1. **Loading Data**: Original dataset `startup_funding.csv`.  

2. **Handling Missing Values**:
   - `Investors Name` missing → filled with `'Undisclosed'`.  
   - Dropped rows with missing `vertical`, `city`, or `round`.  

3. **Column Renaming**: Renamed for clarity:
   ```python
    Date dd/mm/yyyy → date
    Startup Name → startup
    Industry Vertical → vertical
    SubVertical → subvertical
    City Location → city
    Investors Name → investors
    InvestmentnType → round
    Amount in USD → amount
   ```  

5. **Amount Column Cleaning**:
      - Removed commas and non-numeric entries.  
      - Converted USD to INR (crores).  

5. **Date Column Cleaning**:
      - Converted type of date column from `object` to `datetime64[ns]`.  
      - Extracted `year` and `month` for analysis.  

6. **Investor List**:
      - Split multiple investors per startup and created a unique, sorted list for dropdown selection.  

7. **Export Cleaned Data**: `startup_cleaned.csv` for Streamlit app consumption.

