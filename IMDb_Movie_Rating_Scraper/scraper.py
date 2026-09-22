import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("movies.csv")

print("Movie data loaded successfully!")
print("Total Movies:", len(df))


def movie_search():
    print("\n----- Movie Search -----")
    search = input("Enter movie title: ")

    result = df[df["Title"].str.contains(search, case=False, na=False)]

    if len(result) > 0:
        print("\nMovie Found:\n")
        print(result[["Rank", "Title", "Year", "Rating"]].to_string(index=False))
    else:
        print("\nMovie not found.")


def rating_filter():
    print("\n----- Rating Filter -----")

    try:
        min_rating = float(input("Enter minimum rating: "))

        result = df[df["Rating"] >= min_rating]

        if len(result) > 0:
            print(f"\nMovies with rating >= {min_rating}:\n")
            print(result[["Rank", "Title", "Year", "Rating"]].to_string(index=False))
            print(f"\nTotal movies: {len(result)}")
        else:
            print("\nNo movies found.")

    except ValueError:
        print("\nPlease enter a valid rating.")


def highest_rated():
    print("\n----- Highest Rated Movie -----")

    movie = df.loc[df["Rating"].idxmax()]

    print("Title:", movie["Title"])
    print("Year:", movie["Year"])
    print("Rank:", movie["Rank"])
    print("Rating:", movie["Rating"])


def top_10_movies():
    print("\n----- Top 10 Movies -----")

    top_10 = df.sort_values(by="Rating", ascending=False).head(10)

    print(top_10[["Rank", "Title", "Year", "Rating"]].to_string(index=False))


def year_explorer():
    print("\n----- Year Explorer -----")

    try:
        year = int(input("Enter year: "))

        result = df[df["Year"] == year]

        if len(result) > 0:
            print(f"\nMovies Released in {year}:\n")
            print(result[["Rank", "Title", "Year", "Rating"]].to_string(index=False))
            print(f"\nTotal movies released in {year}: {len(result)}")
        else:
            print(f"\nNo movies found for {year}.")

    except ValueError:
        print("\nPlease enter a valid year.")


def rating_statistics():
    print("\n----- Rating Statistics -----")

    average_rating = df["Rating"].mean()
    highest_rating = df["Rating"].max()
    lowest_rating = df["Rating"].min()

    print("Average Rating:", round(average_rating, 2))
    print("Highest Rating:", highest_rating)
    print("Lowest Rating:", lowest_rating)
    print("Total Movies:", len(df))


def rating_distribution():
    print("\n----- Rating Distribution -----")

    plt.figure(figsize=(8, 5))
    plt.hist(df["Rating"], bins=10)

    plt.title("IMDb Movie Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Number of Movies")

    plt.tight_layout()
    plt.show()


def top_10_chart():
    print("\n----- Top 10 Movies Chart -----")

    top_10 = df.sort_values(by="Rating", ascending=False).head(10)

    plt.figure(figsize=(10, 6))
    plt.bar(top_10["Title"], top_10["Rating"])

    plt.title("Top 10 IMDb Movies by Rating")
    plt.xlabel("Movie")
    plt.ylabel("IMDb Rating")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.show()


def year_movie_count():
    print("\n----- Year-wise Movie Count -----")

    year_counts = df["Year"].value_counts().sort_index()

    plt.figure(figsize=(14, 7))
    plt.bar(year_counts.index.astype(str), year_counts.values)

    plt.title("Year-wise Movie Count")
    plt.xlabel("Year")
    plt.ylabel("Number of Movies")

    plt.xticks(rotation=90, fontsize=8)
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.show()


def average_rating_by_year():
    print("\n----- Average Rating by Release Year -----")

    year_rating = df.groupby("Year")["Rating"].mean().reset_index()

    plt.figure(figsize=(12, 6))
    plt.plot(
        year_rating["Year"],
        year_rating["Rating"],
        marker="o",
        linewidth=2
    )

    plt.title("Average IMDb Rating by Release Year")
    plt.xlabel("Release Year")
    plt.ylabel("Average IMDb Rating")

    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.show()


while True:
    print("\n╔══════════════════════════════════════════╗")
    print("║        IMDb MOVIE RATING SCRAPER         ║")
    print("╠══════════════════════════════════════════╣")
    print("║  1. Search Movie                         ║")
    print("║  2. Rating Filter                        ║")
    print("║  3. Highest Rated Movie                 ║")
    print("║  4. Top 10 Movies                       ║")
    print("║  5. Year Explorer                       ║")
    print("║  6. Rating Statistics                   ║")
    print("║  7. Rating Distribution                 ║")
    print("║  8. Top 10 Movie Chart                  ║")
    print("║  9. Year-wise Movie Count               ║")
    print("║ 10. Average Rating by Year              ║")
    print("║  0. Exit                                ║")
    print("╚══════════════════════════════════════════╝")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        movie_search()

    elif choice == "2":
        rating_filter()

    elif choice == "3":
        highest_rated()

    elif choice == "4":
        top_10_movies()

    elif choice == "5":
        year_explorer()

    elif choice == "6":
        rating_statistics()

    elif choice == "7":
        rating_distribution()

    elif choice == "8":
        top_10_chart()

    elif choice == "9":
        year_movie_count()

    elif choice == "10":
        average_rating_by_year()

    elif choice == "0":
        print("\nThank you for using IMDb Movie Rating Scraper!")
        break

    else:
        print("\nInvalid choice. Please select a number from 0 to 10.")