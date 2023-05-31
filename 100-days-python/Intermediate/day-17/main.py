class User:
    def __init__(self,userID,username):
        # print('Leonardo Davinci')
        # for i in range(number):
        #     print(i)
        self.userID=userID
        self.username=username
        self.followers=0
        self.following=0
    def follow(self,user):
        user.followers+=1
        self.following+=1
nameIs=User('001','ZahoorOnly')
print(nameIs.username,nameIs.userID)
user1=User('002','Qasim')
user1.follow(nameIs)
print(nameIs.following,nameIs.followers)
