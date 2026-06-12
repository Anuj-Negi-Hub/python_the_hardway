# mystuff = {'apple': 'I AM APPLES'}
# print(mystuff['apple'])

# All the python the files 
# Whenever python file is imported, then entire file will 
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    # This method prints the element in the self.lyrics list / object
    def sing_me_a_song(self, end="\n"):
        for line in self.lyrics:
            print(line, end=end)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

# print(happy_bday.sing_me_a_song())


# print("Sing a song loading....")

bulls_on_parade = Song(["The rally around the family",
                        "with pocket full of shells"])

string_song = Song(["This is a song...", 785])

# happy_bday.sing_me_a_song()
# bulls_on_parade.sing_me_a_song()


# when importing this  files as module, the __name__ == "ex40_module_class_object"
# when executing this  files as module, the __name__ == "__main__". This will run as a normal file.
print(__name__)
if __name__ == "__main__":
    string_song.sing_me_a_song()




