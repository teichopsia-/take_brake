import fresh_tomatoes
import media

dead_pool = media.Movie("Deadpool", "A former Special Forces operative turned mercenary is subjected to a rogue experiment that leaves him with accelerated healing powers and adopts the alter ego Deadpool.", "http://img11.deviantart.net/1326/i/2015/117/5/a/deadpool_movie_poster_by_iamnerofx-d8r9jfe.jpg", "https://www.youtube.com/watch?v=gtTfd6tISfw")
#print(dead_pool.storyline)
#dead_pool.show_trailer()

avatar = media.Movie("Avatar", 
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)

mad_max = media.Movie("Mad Max", "The world has become a desert wasteland and civilization has collapsed", "https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fi.ytimg.com%2Fvi%2FKELy4064dHw%2Fmaxresdefault.jpg&f=1","https://www.youtube.com/watch?v=hEJnMQG9ev8")

#mad_max.show_trailer()

suicide_squad = media.Movie("Suicide Squad", "Movie with Joker", "http://ia.media-imdb.com/images/M/MV5BMjMzMTM4MzM1OV5BMl5BanBnXkFtZTgwODAwMzE2NTE@._V1_SX640_SY720_.jpg", "https://www.youtube.com/watch?v=WI3hecGO_04")

risen = media.Movie("Risen", "Roman movie", "http://www.gannett-cdn.com/-mm-/18935e432144df7db451be4d32d9196020ca3ae3/c=412-0-4484-3062&r=x404&c=534x401/local/-/media/2015/04/28/USATODAY/USATODAY/635658325675827027-XXX-RISEN-MOV-JY-5898-72638074.JPG", "https://www.youtube.com/watch?v=R-R9JY4le7k")

london_has_fallen = media.Movie("London has fallen", "Death of a President", "http://cdn3-www.comingsoon.net/assets/uploads/gallery/london-has-fallen_1/london_has_fallen_ver2_xlg.jpg", "https://www.youtube.com/watch?v=q9y3z-lx-ZE")

movies = [dead_pool, avatar, mad_max, suicide_squad, risen, london_has_fallen]
fresh_tomatoes.open_movies_page(movies)
