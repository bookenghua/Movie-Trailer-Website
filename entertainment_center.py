#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fresh_tomatoes
import media

#class instantiating section:
last_samurai = media.Movie("The Last Samurai", 
	"""An American military advisor embraces the Samurai culture he was 
hired to destroy after he is captured in battle.""",
	"https://upload.wikimedia.org/wikipedia/en/c/c6/The_Last_Samurai.jpg",
	"https://www.youtube.com/watch?v=T50_qHEOahQ",
	"11.20.2003")

social_network = media.Movie("The Social Network", 
	"""Harvard student Mark Zuckerberg creates the social networking site 
that would become known as Facebook, but is later sued by two 
brothers who claimed he stole their idea, and the co-founder 
who was later squeezed out of the business.""",
	"https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg""",
	"https://www.youtube.com/watch?v=2RB3edZyeYw",
	"09.24.2010")

spirited_away = media.Movie("Spirited Away (千と千尋の神隠し Sen to Chihiro no Kamikakushi", 
	"""During her family's move to the suburbs, a sullen 10-year-old girl 
wanders into a world ruled by gods, witches, and spirits, and where 
humans are changed into beasts.""",
	"https://upload.wikimedia.org/wikipedia/en/3/30/Spirited_Away_poster.JPG",
	"https://www.youtube.com/watch?v=gtXrPZIh5tQ",
	"07.20.2001")

inception = media.Movie("Inception", 
	"""A thief, who steals corporate secrets through use of dream-sharing 
technology, is given the inverse task of planting an idea into the 
mind of a CEO.""",
	"https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
	"https://www.youtube.com/watch?v=YoHD9XEInc0",
	"07.08.2010")

seven_samurai = media.Movie("Seven Samurai (七人の侍 Shichinin no Samurai)", 
	"""A poor village under attack by bandits recruits seven unemployed 
samurai to help them defend themselves.""",
	"https://upload.wikimedia.org/wikipedia/en/8/84/Seven_Samurai_movie_poster.jpg",
	"https://www.youtube.com/watch?v=bBfgNpSQm3I",
	"04.26.1954")

angels_demons = media.Movie("Angels & Demons", 
	"""Harvard symbologist Robert Langdon works to solve a murder and prevent a 
terrorist act against the Vatican.""",
	"https://upload.wikimedia.org/wikipedia/en/4/44/Angels_and_demons.jpg",
	"https://www.youtube.com/watch?v=ArdNQUUcZOM",
	"05.14.2009")

# appending movies into a list:
movies = [last_samurai, 
social_network, 
spirited_away, 
inception, 
seven_samurai, 
angels_demons]

# calling the external rendering function:
fresh_tomatoes.open_movies_page(movies)