"""
Scenario: You are organizing a movie marathon. You start with a playlist: ["Inception", "The Matrix", "Interstellar"]. 
Prompt the user to enter the name of a movie they want to add.
If the movie is already in the list, print "Already added!" and do not insert it.
If it is not in the list, append it to the end of the list. Finally, sort the movie list alphabetically and 
print the updated playlist.

Sample Input: "Interstellar"

Sample Output:
Already added!
Alphabetical Playlist: ['Inception', 'Interstellar', 'The Matrix']
Sample Input: "Avatar"
Sample Output:
Added Avatar!
Alphabetical Playlist: ['Avatar', 'Inception', 'Interstellar', 'The Matrix']
"""

def main():

    movie_playlist = ["Inception", "The Matrix", "Interstellar"]

    add_movie = input("Add movie: ")

    if add_movie in movie_playlist:
        print("Movie already added")

    else:
        movie_playlist.append(add_movie)
        print(movie_playlist)


    movie_playlist.sort()

    print("Alphabetic Playlist: ", movie_playlist)

main()