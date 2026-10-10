def add_movie():
    film = input("Ввести название фильма: ")
    stock = int (input("Ввести рейтинг от 1 до 10.: "))
    movie = ({
     "title": film,
     "rating": stock
 })
    movies.append(movie)

print(add_movie())