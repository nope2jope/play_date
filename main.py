from scrape_me import track_lister
from playlist_brain import lovely_gesture

date_prompt = input("To what date would you like to travel? Enter in YYYY-DD-MM: ")

# passes the given date to function which compiles track list
track_list = track_lister(date_prompt)

# generates a playlist based on the tracks provided
head_nod = lovely_gesture(track_list)




