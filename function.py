# torta-cubana
# Basic configurable Reddit bot

import praw

# Obtaining and setting up credentials
c = open("client.id", "r")
id = str(c.read()).strip()
c.close()

s = open("secret.txt", "r")
secret = str(s.read()).strip()
s.close()

u = open("user.txt", "r")
user = str(u.read()).strip()
u.close()

try:
	n = open("username.txt")
	name = str(n.read()).strip()
	n.close()
	p = open("password.txt")
	pwd = str(p.read()).strip()
	p.close()
	redd = praw.Reddit(
		user_agent=user,
		client_id=id,
		client_secret=secret,
		username=name,
		password=pwd
	)
except:
	reddit = praw.Reddit(
		user_agent=user,
		client_id=id,
		client_secret=secret
	)

# Basic API calls - these do not require username or password
def hotStuff(sub, num):
	for submission in reddit.subreddit(sub).hot(limit=num):
    		print(submission.title)

def newStuff(sub, num):
	for submission in reddit.subreddit(sub).new(limit=num):
		print(submission.title)


# Write API calls - require username&password


# Tests
hotStuff("Python", 69)

