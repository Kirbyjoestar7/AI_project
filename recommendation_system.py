movies = {
    "accion": ["John Wick", "Mad Max", "The Dark Knight"],
    "comedia": ["Superbad", "The Mask", "Shrek"],
    "ciencia ficcion": ["Interstellar", "The Matrix", "Blade Runner 2049"]
}

genre = input("¿Qué género te gusta? ")

if genre.lower() in movies:
    print("Te recomendamos:")
    for movie in movies[genre.lower()]:
        print("-", movie)
else:
    print("Lo siento, no tenemos recomendaciones para ese género.")