import zmq
import time
import random

# Establish socket connection
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://localhost:5555")

def create_playlist(indices, data):
    playlist = ''
    for i in range(len(indices)):
        song = data[indices[i]]
        song_data = song.split('*')
        title = song_data[0]
        artist = song_data[1]
        album = song_data[2]

        song_string = ''
        song_string += "SONG #" + str(i+1) + "\n" + "Title: " + title + "\n" + "Artist: " + artist + "\n" + "Album: " + album + "\n"
        playlist += song_string + "\n"

    return playlist

while True:
    message = socket.recv_string()
    time.sleep(1)

    result = ''

    if message:
        if message.lower() == 'q':
            context.destroy()
            break
        else:
            data = message.split('\n')
            playlist_len = int(data[0])
            data = data[1:]
            data_len = len(data)
            print(data)
            indices = random.sample(range(data_len), playlist_len)
            playlist = create_playlist(indices, data)

        socket.send_string(playlist)