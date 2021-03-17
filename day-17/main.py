class User:
    # pass
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

        # print("new user being created...")


user_1 = User("001", "adrien")
user_2 = User("002", "jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# print(user_1.followers)

# user_1 = User()
# user_1.id = "001"
# user_1.username = "adrien"
#
# print(user_1.username)
#
# user_2 = User()
# user_2.id = "002"
# user_2.username = "jack"
#
# print(user_2.username)