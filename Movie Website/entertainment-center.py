import media
import fresh_tomatoes

#Stores the Movie Class instance of Toy Story 2
Toy_Story_2 = media.Movie("Toy Story 2",
                          "THe toys go on an adventure to find Woody",
                          "https://upload.wikimedia.org/wikipedia/en/c/c0/Toy_Story_2.jpg", # noqa
                          "https://www.youtube.com/watch?v=Lu0sotERXhI"
                          )
#Stores the Movie Class instance of Zootopia
Zootopia = media.Movie("Zootopia",
                       "A bunny becomes a police officer and teams up with a fox",
                       "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg", # noqa
                       "https://www.youtube.com/watch?v=jWM0ct-OLsM"
                       )
#Stores the Movie Class instance of Monsters Inc.
Monsters_inc = media.Movie("Monsters Inc.",
                           "Monsters use childrens screams for power generation",
                           "https://upload.wikimedia.org/wikipedia/en/6/63/Monsters_Inc.JPG", # noqa
                           "https://www.youtube.com/watch?v=cvOQeozL4S0"
                           )
#Stores the Movie Class instance of Fight Club
Fight_Club = media.Movie("Fight Club",
                         "An insomniac starts hallucinating and creates a cult",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg", # noqa
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg"
                         )
#Stores the Movie Class instance of The Dark Knight
The_DarK_Knight = media.Movie("The Dark Knight",
                              "Batman vs The Joker",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg", # noqa
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY"
                              )
#Stores the Movie Class instance of The Mask
The_Mask = media.Movie("The Mask",
                       "An avergae guy discovers a magical mask",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM3NDI5OTA5Nl5BMl5BanBnXkFtZTgwNzE4ODYxMTE@._V1_UY1200_CR86,0,630,1200_AL_.jpg", # noqa
                       "https://www.youtube.com/watch?v=hOqVRwGVUkA"
                       )

#Array of Movies
movies = [Toy_Story_2, Zootopia, Monsters_inc, Fight_Club, The_DarK_Knight, The_Mask]

#Creates the Webpage with the movies array
fresh_tomatoes.open_movies_page(movies)
