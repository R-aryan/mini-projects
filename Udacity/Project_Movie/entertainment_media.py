
import fresh_tomatoes
import media
kingsmen= media.Movie("kingsmen:The Golden Circle","A Crime thriller and intelligence agency",
"http://www.vanyaland.com/wp-content/uploads/2017/04/Kingsman-Poster.jpg","https://www.youtube.com/watch?v=0fvqnGmr9S8")

#print(kingsmen.storyline)
#kingsmen.show_trailer()

avatar=media.Movie("Avatar","A marine on a ailean planet",
"http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
"https://www.youtube.com/watch?v=RqHI0kE-cyo")

mockinjay_2= media.Movie("The Hunger Games: Mockinjay part 2","A really reality show",
"https://zrockr.com/user-files/uploads/2015/11/z29.jpg","https://www.youtube.com/watch?v=n-7K_OjsDCQ")

iron_man= media.Movie("Iron Man 3","A Sci-Fi Marvel Entertainment Movie",
"https://images-na.ssl-images-amazon.com/images/M/MV5BMTkzMjEzMjY1M15BMl5BanBnXkFtZTcwNTMxOTYyOQ@@._V1_UY1200_CR105,0,630,1200_AL_.jpg","https://www.youtube.com/watch?v=5EjG-1U3wqA")

avengers= media.Movie("Avengers: Age of Ultron","A Marvel Superhero movie in which Avengers assemble to defeat Ultron",
"https://static.comicvine.com/uploads/original/9/95970/4529344-dwv6bz2.jpg","https://www.youtube.com/watch?v=tmeOjFno6Do")

strange= media.Movie("Doctor Strange","A Marvel Superhero Movie Aimed to introduce Dr.Strange to the Avengers team",
"http://vignette2.wikia.nocookie.net/marvelcinematicuniverse/images/a/a4/DS_Endless_Possibilities_Poster.jpg/revision/latest?cb=20160909202223","https://www.youtube.com/watch?v=HSzx-zryEgM")

panther= media.Movie("Black Panther","A Marvel Superhero movie to introduce new character Black Panther to the Marvel Universe",
"https://images-na.ssl-images-amazon.com/images/M/MV5BOTc2NTY0NDU2OV5BMl5BanBnXkFtZTgwMTIwNDc1MjI@._V1_UX182_CR0,0,182,268_AL_.jpg","https://www.youtube.com/watch?v=dxWvtMOGAhw")

wonder_woman= media.Movie("Wonder Woman","A DC Comic Movie on Wonder Woman",
"https://am23.akamaized.net/tms/cnt/uploads/2017/05/1491990205555-1.jpg","https://www.youtube.com/watch?v=VSB4wGIdDwo")

Homecoming= media.Movie("Spider Man Homecoming","A Marvel Universe Movie on to introduce Spiderman to the avengers team",
"https://upload.wikimedia.org/wikipedia/en/archive/f/f9/20170706091137%21Spider-Man_Homecoming_poster.jpg","https://www.youtube.com/watch?v=U0D3AOldjMU")

movie= [kingsmen,avatar,mockinjay_2,iron_man,avengers,strange,panther,Homecoming,wonder_woman]
fresh_tomatoes.open_movies_page(movie)

