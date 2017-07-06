import itertools


def anyTrue(predicate, sequence):
    return True in itertools.imap(predicate, sequence)


def endsWIth(s, *endings):
    return anyTrue(s.endswith, endings)


endings = [".jpg", ".png", ".tiff", ".mp3", ".avi", ".rmvb", ".mp4"]
s = "zjw.jpg"

print endsWIth(s, *endings)
