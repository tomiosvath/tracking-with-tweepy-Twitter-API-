import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("3iuhpPZCoojfxWaGgG4VOi3aW", 
    "aiCo64DgCXNsACacdDqgw4afylWq6yqZW12rUqQUmOyqmPA0OP")
auth.set_access_token("1252006793301110784-Jjdfs2h6F6JGd78T5rFn2wDx0JrpIH", 
    "fuhFc6UpoxA7dMxg5n24SKejvaTcKslQ36RRkilFKwHNA")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#api.update_status("Test tweet from Tweepy Python")

#imeline = api.home_timeline()
#for tweet in timeline:
#    print(f"{'tamas_osvath'} said {tweet.text}")


user = api.get_user("NBA")

print("User details:")
print(user.name)
print(user.description)
print(user.location)

print("Last 20 Followers:")
for follower in user.followers():
    print(follower.name)