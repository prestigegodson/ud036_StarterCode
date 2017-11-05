import media
import fresh_tomatoes;

#instanting Movie class with movie properties
kings_man = media.Movie("Kingsman: The Golden Circle","https://upload.wikimedia.org/wikipedia/en/f/fb/Kingsman_The_Golden_Circle.png","https://www.youtube.com/watch?v=6Nxc-3WpMbg")
thor_ragnarok = media.Movie("Thor: Ragnarok","https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg","https://www.youtube.com/watch?v=v7MGUNV8MxU")
justice_league = media.Movie("Justice League","https://upload.wikimedia.org/wikipedia/en/thumb/3/31/Justice_League_film_poster.jpg/220px-Justice_League_film_poster.jpg","https://www.youtube.com/watch?v=r9-DM9uBtVI")

#adding Movie object to movies list
movies = [kings_man,thor_ragnarok,justice_league]

#calling the open_movies_page function to display the movies trailers
fresh_tomatoes.open_movies_page(movies)