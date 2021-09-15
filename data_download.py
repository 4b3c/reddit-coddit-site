import praw, login_info, json
reddit = login_info.reddit

submission_stream = reddit.subreddit("teenagersbutpog").stream.submissions(pause_after = -1, skip_existing = True)
comment_stream = reddit.subreddit("teenagersbutpog").stream.comments(pause_after = -1, skip_existing = True)
data = {}

def store(author, created_time, contribution_type):
	with open('data.json') as data_file:
		data = json.load(data_file)

		if (author in data):
			data[author][contribution_type] += 1
			data[author][2].append(created_time)

		elif (author not in data):
			data[author] = [0, 0, []]
			data[author][contribution_type] += 1
			data[author][2].append(created_time)

	with open("data.json", "w") as data_file:
		json.dump(data, data_file, indent = 3)

while True:
	for post in submission_stream:
		if post is None:
			break
		store(str(post.author), str(post.created_utc), 0)

	for comment in comment_stream:
		if comment is None:
			break
		store(str(comment.author), str(comment.created_utc), 1)
