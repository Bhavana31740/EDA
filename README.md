# Netflix Titles - Exploratory Data Analysis (EDA)

An exploratory data analysis of Netflix's movie and TV show catalog using Python and pandas.

## Contents
- `Netflix_EDA_Annotated.ipynb` — the analysis notebook, with a markdown explanation before every step
- `netflix_titles.xlsx` — the dataset (must stay in the same folder as the notebook)

## What's inside
- Loading and previewing the dataset (8,807 titles, 12 columns)
- Checking data types, missing values, and duplicate rows
- Comparing Movies vs TV Shows
- Finding the top countries producing Netflix content
- Breaking down content ratings (age classifications)
- Visualizing each finding with bar charts

## Key results
- **70% Movies vs 30% TV Shows** (6,131 vs 2,676)
- Top countries: **United States (2,818)**, **India (972)**, **United Kingdom (419)**
- Most common rating: **TV-MA** (3,207 titles), followed by **TV-14** (2,160)
- No duplicate rows; `director`, `cast`, and `country` have the most missing values

## How to run
1. Clone this repo
2. Make sure `netflix_titles.xlsx` is in the same folder as the notebook
3. Install dependencies (see below)
4. Open `Netflix_EDA_Annotated.ipynb` in Jupyter Notebook / JupyterLab / VS Code
5. Run all cells top to bottom

## Requirements
```
pandas
openpyxl
matplotlib
```
Install with:
```
pip install pandas openpyxl matplotlib
```
