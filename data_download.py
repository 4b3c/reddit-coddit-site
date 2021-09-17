import praw, login_info, json, time as time_
reddit = login_info.reddit

submission_stream = reddit.subreddit("teenagersbutpog").stream.submissions(pause_after = -1, skip_existing = True)
comment_stream = reddit.subreddit("teenagersbutpog").stream.comments(pause_after = -1, skip_existing = True)
data = {}
# changed_list = []
# old_times = []

def store(author, created_time, contribution_type):
	with open('data.json') as data_file:
		data = json.load(data_file)

		if (author in data):
			data[author][contribution_type] += 1
			# data[author][contribution_type + 2].append(created_time)
			# changed_list.append(author)

		elif (author not in data):
			data[author] = [0, 0]
			data[author][contribution_type] += 1
			# data[author][contribution_type + 2].append(created_time)
			# changed_list.append(author)

	with open("data.json", "w") as data_file:
		json.dump(data, data_file, indent = 3)

while True:
	for post in submission_stream:
		if post is None:
			break
		store(str(post.author), post.created_utc, 0)

	for comment in comment_stream:
		if comment is None:
			break
		store(str(comment.author), comment.created_utc, 1)

	# with open("data.json") as data_file:
	# 	data = json.load(data_file)
		
		# for user in data:
		# 	data.get(user)[2] = 0
		# 	for time in data.get(user)[3]:
		# 		if (time > time_.time() - 604800):
		# 			data.get(user)[2] = data.get(user)[2] + 1
		# 		else:
		# 			old_times.append(time)

		# 	for i in old_times:
		# 		data.get(user)[3].remove(i)
		# 	old_times = []