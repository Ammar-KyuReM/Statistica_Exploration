# Statistical_Exploration

# Project Brief
## Introduction
This project involves analyzing datasets related to students' exam grades in a module for the years 2020 and 2024. The goal is to develop a Python script that reads the provided data files, creates histograms of the exam grades distribution for both years, calculates specific statistical values, and generates a single graph displaying all relevant information.

## Data Files
Two CSV files are required for this project:

### 2020exam:
Contains tabulated distribution data representing students' grades in the module's exam in 2020. It comprises three columns: 'Xleft' (left boundary of intervals), 'Xright' (right boundary of intervals), and 'Count' (number of students within each interval).
### 2024exam:
A one-column CSV file containing individual student grades (approximately 300 entries) for the 2024 exam.
Project Requirements

## The Python code developed for this project:
* Read data from the provided data files located in the same directory as the script. The filenames and content of the data files should not be altered.
* Generate histograms of exam grades distributions for 2020 and 2024, and plot them on a single graph.
* Print the mean values and standard deviations for both distributions on the plot.
* Calculate a specific value 'V', which represents the proportion of students with grades below 25 in the 2024 exam.
* Print both the mean values ('M') and the calculated value 'V', along with the student ID number, on the graph. Rounding up should retain at least two significant figures.
* Ensure the plot includes adequate axis labels, titles, and a legend.
* Save the generated graph as a PNG image.
