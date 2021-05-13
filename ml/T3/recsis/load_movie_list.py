import io


def load_movie_list():
    """
    reads the fixed movie list in movie.txt
    and returns a cell array of the words in movieList.
    """

    ## Read the fixed movieulary list
    with io.open('../data/movie_ids.txt', encoding='ISO-8859-1') as f:

        # Store all movies in cell array movie{}
        n = 1682  # Total number of movies 

        movieList = []
        for i in range(n):
            # Read line
            line = f.readline()
            # Word Index (can ignore since it will be = i)
            str = line.split()
            # Actual Word
            movieList.append(' '.join(str[1:]).strip())
        return movieList