
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################




# def make_album(artist_name, album_title, songs=None):
#     """Displaying albums"""

#     album = {'name': artist_name, 'album': album_title}

#     while True:    
#         print("(enter 'q' at any time to quit)")

#         artist_name = input("Name: ")
#         if artist_name == 'q':
#             break
#         else:
#             album['name'] = artist_name

#         album_title = input('Title: ')
#         if album_title == 'q':
#             break
#         else:
#             album['album'] = artist_name

#         if songs:
#             songs = input("Number of songs: ")
#             if songs == 'q':
#                 break
#             else:
#                 album['songs'] = artist_name

#             album['songs'] = songs            

#     return  album



# albums  = 
# # print(albums)

# # albums  = make_album('h0', 'mj', 13)
# # print(albums)



def make_album(artist_name, album_title, songs=None):
    """Album title and name dictionary"""

    album = {'name': artist_name, 'album': album_title}

    if songs:
        songs = input("Songs: ")
        album['songs'] = songs


    return  album

while True:    
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    artist_name = input("Name: ")
    if artist_name == 'q':
        break

    album_title = input('Title: ')
    if album_title == 'q':
        break

    album = make_album(artist_name, album_title)
    print(album)

    # if songs:
    #     songs = input("Number of songs: ")
    #     if songs == 'q':
    #         break




############################################
print('\n')  # Spaces for convention only!
############################################
