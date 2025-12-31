# Week 1 – Python Foundations Assessment

## Problem Understanding
The objective of this assessment is to analyze a CSV file using core Python concepts
without relying on high-level libraries like Pandas.
The task focuses on understanding how CSV files work internally,
handling missing and inconsistent data, and performing basic data analysis.

## Approach & Logic
The CSV file is read using Python file handling methods.
The first row of the file is treated as the header, and the remaining rows are treated as data.
Column positions are identified dynamically using column names instead of hardcoding indexes.
Each row is processed carefully to avoid runtime errors due to bad data.

## Handling Missing Values
Missing values such as empty strings, NA, null, and None are handled explicitly.
These values are ignored during calculations and frequency analysis to ensure
accurate results and prevent program crashes.

## Why NumPy Was Used
NumPy was used only for statistical calculations like mean, median,
and standard deviation.
Using NumPy ensures accurate mathematical operations and avoids manual formula errors.

## How to Run the Program
1. Place `analysis.py` and `data.csv` in the same folder
2. Open terminal in the project directory
3. Run the command:
