import media
import fresh_tomatoes


Toy_Story_2 = media.Movie("Toy Story 2", "THe toys go on an adventure to find Woody", "https://upload.wikimedia.org/wikipedia/en/c/c0/Toy_Story_2.jpg",
                                                "https://www.youtube.com/watch?v=Lu0sotERXhI")
Zootopia = media.Movie("Zootopia", "A bunny becomes a police officer and teams up with a fox", "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                                    "https://www.youtube.com/watch?v=jWM0ct-OLsM")
Monsters_inc = media.Movie("Monsters Inc.", "Monsters use childrens screams for power generation", "https://upload.wikimedia.org/wikipedia/en/6/63/Monsters_Inc.JPG",
                                        "https://www.youtube.com/watch?v=cvOQeozL4S0")
Fight_Club = media.Movie("Fight Club", "An insomniac starts hallucinating and creates a cult", "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                                        "https://www.youtube.com/watch?v=SUXWAEX2jlg")
The_DarK_Knight = media.Movie("The Dark Knight", "Batman vs The Joker", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                                            "https://www.youtube.com/watch?v=EXeTwQWrcwY")
The_Mask = media.Movie("The Mask", "A anvergae guy discovers a magical mask", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM3NDI5OTA5Nl5BMl5BanBnXkFtZTgwNzE4ODYxMTE@._V1_UY1200_CR86,0,630,1200_AL_.jpg",
                                    "https://www.youtube.com/watch?v=hOqVRwGVUkA")

#Array of Movies
movies = [Toy_Story_2, Zootopia, Monsters_inc, Fight_Club, The_DarK_Knight, The_Mask]

#Creates the Webpage with the movies array 
fresh_tomatoes.open_movies_page(movies)