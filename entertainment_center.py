import fresh_tomatoes
import media
"""entertainment_center.py
In this file objects called Movie are instantiated. Each object must contain
5 constructors that can be found in the file media.py"""

#Creating 1st instance of movie
your_highness = media.Movie("Your Highness",
                            "Raised in the shadow of his brother, a young prince is given the chance to shine",
                            "http://upload.wikimedia.org/wikipedia/en/thumb/3/31/Your_Highness_Poster.jpg/220px-Your_Highness_Poster.jpg",
                            "https://www.youtube.com/watch?v=NJmsKhstdgE",
                            "Rated "+media.Movie.VALID_RATINGS[3])

#Creating 2nd instance of movie
super_troopers = media.Movie("Super Troopers ",
                             "A small town of police officers are in for for the bust of their careers",
                             "http://upload.wikimedia.org/wikipedia/en/thumb/1/19/Supertrooper.jpg/220px-Supertrooper.jpg",
                             "https://www.youtube.com/watch?v=5CSw2lb6i6s",
                             "Rated "+media.Movie.VALID_RATINGS[3])

#Creating 3rd instance of movie
love_guru = media.Movie ("The Love Guru",
                         "A story about true purpose and self discovery",
                         "http://upload.wikimedia.org/wikipedia/en/thumb/8/8f/Love_guru.jpg/220px-Love_guru.jpg",
                         "https://www.youtube.com/watch?v=e_lGEKikn_w",
                         "Rated "+media.Movie.VALID_RATINGS[2])

#Creating 4th instance of movie
anchorman2 = media.Movie ("Anchorman 2: The Legend Continues",
                           "The Legend is back, Ron's accident leaves him blind, through love he is able to overcome",
                           "http://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Anchorman_2_Teaser_Poster.jpg/220px-Anchorman_2_Teaser_Poster.jpg",
                           "https://www.youtube.com/watch?v=6VdGI5-z_hg",
                           "Rated "+media.Movie.VALID_RATINGS[3])

#Creating 5th instance of movie
land_ofthe_lost = media.Movie ("Land of the Lost",
                               "Renouned professor Dr. Rick Marsharll is laughed out of mainstream science only to discover if you fail, it's your own damn vault",
                               "http://upload.wikimedia.org/wikipedia/en/thumb/9/99/Land_of_the_Lost_poster.jpg/215px-Land_of_the_Lost_poster.jpg",
                               "https://www.youtube.com/watch?v=CiCDnG_AdmA",
                               "Rated "+media.Movie.VALID_RATINGS[2])

#Creating 6th instance of movie
the_other_guys = media.Movie ("The Other Guys",
                              "Two partners fall into the case that will challenge who they were and who they will become",
                              "http://upload.wikimedia.org/wikipedia/en/thumb/6/6b/Other_guys_poster.jpg/220px-Other_guys_poster.jpg",
                              "https://www.youtube.com/watch?v=D6WOoUG1eNo",
                              "Rated "+media.Movie.VALID_RATINGS[2])

#Create list of all movies
movies = [your_highness, super_troopers, love_guru, anchorman2, land_ofthe_lost, the_other_guys]

#Pass list to fresh_tomatoes for webpage display
fresh_tomatoes.open_movies_page(movies)

#print (media.Movie.__doc__)
