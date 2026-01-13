import matplotlib.pyplot as plt
import pandas as pd

# Load dataset with error handling
try:
    df = pd.read_csv('movie_dataset.csv')
except FileNotFoundError:
    print("Error: 'movie_dataset.csv' not found.")
    exit()

# Create DataFrame with selected columns
df = pd.DataFrame(df, columns=["Movie_Name", "Genre", "Rating", "Country", "Language"])

# Prompt user for filtering criteria
user_genre = input("Enter desired Genre (action, thriller, sci-fi, horror, drama, comedy): ").strip()
user_country = input("Enter desired Country (india, usa, china, philippines, thailand, south korea, germany, poland, uk, japan, australia): ").strip()
user_language = input("Enter desired Language (hindi, telugu, english, korean, japanese, mandarin, tagalog, thai, polish): ").strip()

# Filter based on user input (case-insensitive)
if user_genre:
    df = df[df["Genre"].str.lower() == user_genre.lower()]
if user_country:
    df = df[df["Country"].str.lower() == user_country.lower()]
if user_language:
    df = df[df["Language"].str.lower() == user_language.lower()]

# If no matching movies found
if df.empty:
    print("No movies found matching the criteria.")
    exit()
else:
    df = df.sort_values(by="Rating", ascending=True)

# 1. Horizontal Bar Chart
plt.figure(figsize=(12, 8))
plt.barh(df["Movie_Name"], df["Rating"], color='skyblue', edgecolor='black')
plt.xlabel("Rating")
plt.ylabel("Movie Name")
plt.title("Recommended Movies (Horizontal Bar Chart)")
for index, value in enumerate(df["Rating"]):
    plt.text(value - 0.2, index, f"{df.iloc[index]['Genre']}, {df.iloc[index]['Country']}", va='center', fontsize=9)
plt.tight_layout()
plt.show()

# 2. Vertical Bar Chart
plt.figure(figsize=(12, 8))
plt.bar(df["Movie_Name"], df["Rating"], color='lightgreen', edgecolor='black')
plt.xlabel("Movie Name")
plt.ylabel("Rating")
plt.title("Recommended Movies (Vertical Bar Chart)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# 3. Scatter Plot
plt.figure(figsize=(12, 8))
plt.scatter(df["Rating"], df["Movie_Name"], color='orange', edgecolor='black', s=100)
plt.xlabel("Rating")
plt.ylabel("Movie Name")
plt.title("Recommended Movies (Scatter Plot)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# 5. Pie Chart (Genre Distribution with Labels)
# Reload full dataset to get genre distribution from the entire dataset
try:
    df = pd.read_csv('movie_dataset.csv')
except FileNotFoundError:
    print("Error: 'movie_dataset.csv' not found.")
    exit()

# Genre distribution across the entire dataset
genre = df["Genre"].value_counts()

# Show only if there are genres to display
if len(genre) > 0:
    # Create labels like "Action (10)"
    labels = [f"{genre} ({count})" for genre, count in genre.items()]
    
    plt.figure(figsize=(8, 8))
    plt.pie(genre, 
            labels=labels, 
            autopct='%1.1f%%', 
            startangle=140, 
            colors=plt.cm.Set3.colors[:len(genre)])
    plt.title("Genre Distribution in Entire Dataset")
    plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
    plt.tight_layout()
    plt.show()
else:
    print("No genre data available in the full dataset.")

