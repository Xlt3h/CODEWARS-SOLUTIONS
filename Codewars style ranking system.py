#to be continued
class User:
    def __init__(self):
        self.rank = -8 #startup of the rank
        self.progress = 0

    def inc_progress(self ,rank_):
        self.rank_ = rank_
        self.rank += self.rank_

user = User()
print(user.rank)
user.inc_progress(5)
print(user.rank)

