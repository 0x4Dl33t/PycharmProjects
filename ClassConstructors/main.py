class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


user_1 = User("001", "Mawande")
user_2 = User("002", "Zizibele")

user_1.follow(user_2)
user_2.follow(user_1)

print(f"\nID: {user_1.id} \nName: {user_1.name} \nFollowers: {user_1.followers} \nFollowing: {user_1.following}")
print(f"\nID: {user_2.id} \nName: {user_2.name} \nFollowers: {user_2.followers} \nFollowers: {user_2.following}")


