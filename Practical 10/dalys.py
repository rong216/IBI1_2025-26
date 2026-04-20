import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Change working directory to the folder where this script is saved
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

print("Current working directory:", os.getcwd())
print("Files in this folder:", os.listdir())

# Load the DALYs dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Explore the dataframe
print("\nFirst 5 rows:")
print(dalys_data.head(5))

print("\nDataframe information:")
dalys_data.info()

print("\nSummary statistics:")
print(dalys_data.describe())

# Basic summary values
max_dalys = dalys_data["DALYs"].max()
min_dalys = dalys_data["DALYs"].min()
first_year = dalys_data["Year"].min()
last_year = dalys_data["Year"].max()

print("\nMaximum DALYs in whole dataframe:", max_dalys)
print("Minimum DALYs in whole dataframe:", min_dalys)
print("First year recorded:", first_year)
print("Most recent year recorded:", last_year)

# Show the third and fourth columns (Year and DALYs) for the first 10 rows
afghanistan_first_10 = dalys_data.iloc[0:10, 2:4]
print("\nFirst 10 Afghanistan rows: Year and DALYs")
print(afghanistan_first_10)

# Portfolio comment: this prints the year with the maximum DALYs across the first 10 Afghanistan rows
max_afghanistan_year = afghanistan_first_10.loc[
    afghanistan_first_10["DALYs"].idxmax(), "Year"
]
print("Year with maximum DALYs across first 10 Afghanistan rows:", max_afghanistan_year)

# Use a Boolean to show all years for which DALYs were recorded in Zimbabwe
zimbabwe_years = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe", "Year"]
print("\nYears with DALYs recorded for Zimbabwe:")
print(zimbabwe_years)

# Portfolio comment: this prints the first and last year recorded for Zimbabwe
zimbabwe_first_year = zimbabwe_years.min()
zimbabwe_last_year = zimbabwe_years.max()
print("First Zimbabwe year:", zimbabwe_first_year)
print("Last Zimbabwe year:", zimbabwe_last_year)

# Restrict to likely country rows in 2019 by keeping 3-letter country codes
recent_data = dalys_data.loc[
    (dalys_data["Year"] == 2019) & (dalys_data["Code"].fillna("").str.len() == 3),
    ["Entity", "Code", "DALYs"]
]

max_country_row = recent_data.loc[recent_data["DALYs"].idxmax()]
min_country_row = recent_data.loc[recent_data["DALYs"].idxmin()]

max_country = max_country_row["Entity"]
min_country = min_country_row["Entity"]

# Portfolio comment: this prints the countries with the maximum and minimum DALYs in 2019
print("\nCountry with maximum DALYs in 2019:", max_country, max_country_row["DALYs"])
print("Country with minimum DALYs in 2019:", min_country, min_country_row["DALYs"])

# Plot DALYs over time for the country with the maximum DALYs in 2019
country_to_plot = max_country
country_data = dalys_data.loc[dalys_data["Entity"] == country_to_plot, ["Year", "DALYs"]]

plt.figure(figsize=(10, 5))
plt.plot(country_data["Year"], country_data["DALYs"], "bo-")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title(f"DALYs over time in {country_to_plot}")
plt.xticks(country_data["Year"], rotation=90)
plt.tight_layout()
plt.savefig("max_country_dalys_over_time.png")
plt.show()

# QUESTION SECTION STARTS HERE
# Question: What was the distribution of DALYs across all countries in 2019?
question_data = recent_data["DALYs"]

print("\nQuestion summary statistics for DALYs in 2019:")
print("Mean:", question_data.mean())
print("Median:", question_data.median())
print("Standard deviation:", question_data.std())

plt.figure(figsize=(10, 5))
plt.hist(question_data, bins=20, color="skyblue", edgecolor="black")
plt.xlabel("DALYs")
plt.ylabel("Number of countries")
plt.title("Distribution of DALYs across countries in 2019")
plt.tight_layout()
plt.savefig("dalys_distribution_2019.png")
plt.show()