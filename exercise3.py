movies = [ 

    ("The Matrix", 1999), 

    ("Avatar", 2009), 

    ("Jurassic Park", 1993), 

    ("Avengers: Endgame", 2019), 

    ("Inception", 2010), 

    ("Titanic", 1997) 

]

movies.sort(key=lambda movie: movie[1], reverse=True)

print("Newest to Oldest")
for m in movies:
    print(f"{m[0]} - {m[1]}")