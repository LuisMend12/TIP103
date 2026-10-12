import ast
import sys



def first_shared_song(requests):
    # Write your code here
    song_count = dict()
    for student, song in requests:
        song_count[song] = song_count.get(song, 0) + 1

    for student, song in requests:
        if song_count[song] > 1:
            return song  # Return the first song that is shared
    return ""  # Return None if no song is shared

if __name__ == '__main__':
    _args = ast.literal_eval(sys.stdin.read().strip())
    if not isinstance(_args, tuple):
        _args = (_args,)
    print(repr(first_shared_song(*_args)))
