import pandas as pd

df = pd.read_excel("netflix_titles.xlsx")

print("First 5 Rows")
print(df.head())

print("\nDataset Info")
print(df.info())

print("\nShape")
print(df.shape)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nMovies vs TV Shows")
print(df['type'].value_counts())

print("\nTop 10 Countries")
print(df['country'].value_counts().head(10))

print("\nRatings")
print(df['rating'].value_counts())

import matplotlib.pyplot as plt

df['type'].value_counts().plot(kind='bar')

plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")

plt.show()

df['country'].value_counts().head(10).plot(kind='bar')

plt.title("Top 10 Countries on Netflix")
plt.xlabel("Country")
plt.ylabel("Number of Titles")

plt.show()

df['rating'].value_counts().head(10).plot(kind='bar')

plt.title("Top Ratings on Netflix")
plt.xlabel("Rating")
plt.ylabel("Count")

plt.show()

df['type'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Movies vs TV Shows Distribution")
plt.ylabel("")

plt.show()