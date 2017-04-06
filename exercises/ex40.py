class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

    def sing_me_special(self):
        for kk,vv in self.lyrics.items():
            print "%s   |  %s" % (kk,vv)

# change param to dict
# happy_bday = Song({1:"Happy birthday to you",\
#                    2:"I don't want to get sued",\
#                    3:"So I'll stop right there"})
#
# bulls_on_parade = Song(["They rally around the family",
#                         "With pockets full of shells"])
# happy_bday.sing_me_special()
# bulls_on_parade.sing_me_a_song()

class TestWhyNeedSelf(object):
    def __init__(self, lyrics):
        lyrics = lyrics
        self.a = "aa"

    def sing_me_a_song(self):
        for line in self.a:
            print line

if __name__ == "__main__":
    obj = TestWhyNeedSelf(["They rally around the family",
                        "With pockets full of shells"])
    # lyrics = ["hhhh"]
    obj.sing_me_a_song()
