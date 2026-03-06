# Sales Data Analysis – Superstore Retail Dataset

## Project Overview

This project analyzes transactional sales data from a retail Superstore dataset to identify key business insights related to revenue generation, profitability, customer behavior, and regional performance.

The objective of this analysis is to demonstrate practical data analytics skills including data preparation, exploratory data analysis, and visualization to support data-driven decision making.

All analysis was performed using Python and organized as a reproducible analytics workflow.

---

## Dataset Description

The dataset contains detailed order-level transactional data including:

* Order information
* Customer segmentation
* Product categories and sub-categories
* Geographic sales distribution
* Discounts and profitability

Dataset summary:

| Metric           | Value  |
| ---------------- | ------ |
| Total Records    | 9,994  |
| Total Features   | 21     |
| Unique Orders    | 5,009  |
| Unique Customers | 793    |
| Total Sales      | $2.29M |
| Total Profit     | $286K  |

---

## Analytical Workflow

The project follows a structured analytics pipeline:

### 1. Data Preparation

* Raw dataset ingestion
* Column normalization
* Date conversion
* Duplicate record removal
* Missing value validation

### 2. Exploratory Data Analysis

Key exploratory questions addressed:

* Which product categories generate the highest revenue?
* Which geographic regions contribute most to profitability?
* How does sales performance change over time?
* Which customers contribute the most to overall revenue?
* How do discount levels impact profitability?

### 3. Visualization & Insights

The analysis produces visual insights for:

* Sales distribution by product category
* Regional profit comparison
* Monthly sales performance trends
* Top revenue-generating customers
* Discount vs profitability relationship

Visualization outputs are stored in the **reports/figures/** directory.

---

## Project Structure

```
Sales-Dashboard-Analysis
│
├── data
│   ├── raw
│   │   └── superstore.csv
│   └── processed
│       └── superstore_clean.csv
│
├── notebooks
│   └── eda.ipynb
│
├── src
│   └── data_cleaning.py
│
├── reports
│   └── figures
│       ├── sales_by_category.png
│       ├── profit_by_region.png
│       ├── monthly_sales_trend.png
│       ├── top_customers_sales.png
│       └── discount_vs_profit.png
│
└── README.md
```

---

## Key Business Insights

* The dataset generated over **$2.29M in total sales**, producing approximately **$286K in profit**.
* The **Technology category** contributes the highest revenue among product categories.
* The **West region** demonstrates the strongest profitability compared to other regions.
* Sales patterns show fluctuations across months, indicating potential seasonal demand cycles.
* High discount levels often correspond with reduced profitability, highlighting the importance of optimized discount strategies.

---

## Technologies Used

* Python
* Pandas
* Matplotlib
* Jupyter Notebook
* Git / GitHub

---

## Reproducing the Analysis

Clone the repository:

```
git clone https://github.com/setuchaudhari/Sales-Dashboard-Analysis.git
```

Install dependencies:

```
pip install pandas matplotlib jupyter
```

Run the data preparation script:

```
python src/data_cleaning.py
```

Launch the notebook:

```
notebooks/eda.ipynb
```

---

## Author

Setu Chaudhari

This project is part of a data analytics portfolio demonstrating practical capabilities in:

* Data preparation
* Exploratory data analysis
* Data visualization
* Analytical storytelling
* Git-based project organization
