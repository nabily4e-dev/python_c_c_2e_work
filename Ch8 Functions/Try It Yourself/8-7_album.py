
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################




def make_album(artist_name, album_title, songs=None):
    """Album title and name dictionary"""

    album = {'name': artist_name, 'album': album_title}

    if songs:
        album['songs'] = songs



    return  album


albums  = make_album('h0', 'mj')
print(albums)

albums  = make_album('h0', 'mj', 13)
print(albums)




############################################
print('\n')  # Spaces for convention only!
############################################
