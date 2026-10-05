#  Many user listen songs , based on their frequency of song,
# can you design an api for song recommendation
# fav_song_dict ={ user_id: {song_id:frequency,.....}}

from collections import defaultdict
class Song_Recomm(object):
    fav_song_dict = defaultdict(dict)

    def listen_song(self,song_id,user_id):
        # if user_id in self.fav_song_dict:
        if song_id in self.fav_song_dict[user_id]:
            self.fav_song_dict[user_id][song_id] += 1
        else:
            self.fav_song_dict[user_id][song_id] = 1

        # else:
        #     self.fav_song_dict[user_id][song_id] = 1
        print("Dict:",self.fav_song_dict)

    def get_fav_song(self,user_id,2):



sr = Song_Recomm()
sr.listen_song(12,'AAA')
sr.listen_song(12,'AAA')
sr.listen_song(12,'AAA')
sr.listen_song(12,'AAA')

sr.listen_song(13,'AAA')
sr.listen_song(14,'AAA')

sr.listen_song(34,'BBB')

sr.listen_song(59,'BBB')

sr.listen_song(14,'AAA')







