import csv
import matplotlib.pyplot as plt
import json


with open('./data.csv') as f:
    # we are using DictReader because we want our information to be in dictionary format.
    reader = csv.DictReader(f)
    # some more code
    rolling_list = []
    for i in reader:
        rolling_list.append(i)
    print(rolling_list)


def find_by_name(album_name):
    for hit in rolling_list:
        if hit["album"] == album_name:
            return hit

def find_by_rank(album_rank):
    for hit in rolling_list:
        if hit["number"] == str(album_rank):
            return hit
        
def find_by_year(year):
    album_list = []
    for hit in rolling_list:
        if hit["year"] == str(year):
            album_list.append(hit)
    return album_list

def find_by_years(start_year, end_year):
    album_by_years = []
    start = start_year
    while start <= end_year:
        album_by_years.extend(find_by_year(start))
        start += 1
    return album_by_years


def find_by_ranks(start_rank, end_rank):
    album_by_ranks = []
    start = start_rank
    while start <= end_rank:
        album_by_ranks.append(find_by_rank(start))
        start += 1
    return album_by_ranks

def all_titles():
    titles_list = []
    for hit in rolling_list:
        titles_list.append(hit['album'])
    return titles_list
                 
def all_artists():
    artists_list = []
    for hit in rolling_list:
        artists_list.append(hit['artist'])
    return artists_list

# def artist_most_hits():
#     max_count = 0
#     artist = None
#     artists_list = all_artists()
#     artists_set = set(artists_list)
#     for singer in artists_set:
#         temp_count = artists_list.count(singer)
#         if temp_count >= max_count:
#             max_count = temp_count
#             artist = singer
#     return artist

def artist_most_hits():
    return max(all_artists(), key = artists_list.count)

def popular_word():
    word_dict = {}
    titles_list = all_titles()
    for title in titles_list:
        for word in title.split():
            if word in word_dict:
                word_dict[word] +=1 
            else:
                word_dict[word] = 1
    max_count = 0
    max_word = None
    for word in word_dict:
        if word_dict[word] >= max_count:
            max_count = word_dict[word]
            max_word = word
    return max_word
    
def histogram_of_album_by_decade():
    plt.hist([int(hit["year"]) for hit in rolling_list], bins=6)
    
def histogram_by_genre():
    fig_size = plt.figure(figsize=(50, 20))
    genre_list = []
    for hit in [album['genre'] for album in rolling_list]:
        if type(hit.split(",")) == list:
            for genre in hit.split(","):
                genre = genre.rstrip().lstrip()
                genre_list.append(genre)
        else:
            genre_list.append(hit.rstrip().lstrip())
    plt.hist(genre_list, bins=14)

# part 2

text_file = open('top-500-songs.txt', 'r')
    # read each line of the text file
    # here is where you can print out the lines to your terminal and get an idea 
    # for how you might think about re-formatting the data
lines = text_file.readlines()
print(lines)

def reformat_text_file():
    reformatted = []
    for line in lines:
        reformatted.append(line.strip('\n').split('\t'))
    return reformatted

def reformat_to_dict():
    lst = reformat_text_file()
    category = ["rank", 'name', 'artist', 'year']
    album_lst = []
    albums_dict = {"rank": None, 'name':None, 'artist':None,'year':None}
    for item in lst:
        for ind in range(len(item)):
            albums_dict[category[ind]] = item[ind]
        album_lst.append(albums_dict.copy())
    return album_lst
              
    
file = open('track_data.json', 'r')
json_data = json.load(file)

def find_by_name_refactored(data, term, album_name):
    for hit in data:
        if hit[term] == album_name:
            return hit

def find_by_rank_refactored(data, term, album_rank):
    for hit in data:
        if hit[term] == str(album_rank):
            return hit
        
def find_by_year_refactored(data, year):
    album_list = []
    for hit in data:
        if hit["year"] == str(year):
            album_list.append(hit)
    return album_list

def find_by_years_refactored(data, start_year, end_year):
    album_by_years = []
    start = start_year
    while start <= end_year:
        album_by_years.extend(find_by_year_refactored(data, start))
        start += 1
    return album_by_years


def find_by_ranks_refactored(data, start_rank, end_rank):
    album_by_ranks = []
    start = start_rank
    while start <= end_rank:
        album_by_ranks.append(find_by_rank_refactored(data, start))
        start += 1
    return album_by_ranks

def all_titles_refactored(data, term):
    titles_list = []
    for hit in data:
        titles_list.append(hit[term])
    return titles_list
                 
def all_artists_refactored(data):
    artists_list = []
    for hit in data:
        artists_list.append(hit['artist'])
    return artists_list

# def artist_most_hits():
#     max_count = 0
#     artist = None
#     artists_list = all_artists()
#     artists_set = set(artists_list)
#     for singer in artists_set:
#         temp_count = artists_list.count(singer)
#         if temp_count >= max_count:
#             max_count = temp_count
#             artist = singer
#     return artist

def artist_most_hits_refactored(data):
    return max(all_artists_refactored(data), key =all_artists_refactored(data).count)

def popular_word_refactored(data, term):
    word_dict = {}
    titles_list = all_titles_refactored(data, term)
    for title in titles_list:
        for word in title.split():
            if word in word_dict:
                word_dict[word] +=1 
            else:
                word_dict[word] = 1
    max_count = 0
    max_word = None
    for word in word_dict:
        if word_dict[word] >= max_count:
            max_count = word_dict[word]
            max_word = word
    return max_word
    
def histogram_of_album_by_decade_refactored(data):
    plt.hist([int(hit["year"]) for hit in data], bins=6)
    
def artist_with_top_500_songs(data, songs_data):
    artist_count = {}
    for hit in data:
        key = (hit["artist"], hit["album"])
        for song in hit["tracks"]: 
            if song in all_titles_refactored(songs_data, "name") and key in artist_count:
                artist_count[key] += 1
            elif song in all_titles_refactored(songs_data, "name"):
                artist_count[key] = 1
    return artist_count

def albumWithMostTopSongs(data, songs_data):
    return max(artist_with_top_500_songs(data, songs_data))

def albumsWithTopSongs(data, songs_data):
    albums_lst = []
    for pair in artist_with_top_500_songs(data, songs_data):
        albums_lst.append(pair[1])
    return albums_lst
               
