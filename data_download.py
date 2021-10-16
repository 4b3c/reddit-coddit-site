import praw, random, login_info, json, time as time_
reddit = login_info.reddit_post

submission_stream = reddit.subreddit("teenagersbutpog").stream.submissions(pause_after = -1, skip_existing = True)
comment_stream = reddit.subreddit("teenagersbutpog").stream.comments(pause_after = -1, skip_existing = True)
data = {}
old_times = []

def store_total(author, contribution_type):
	with open('data.json') as data_file:
		data = json.load(data_file)

		if (author in data):
			data[author][contribution_type] += 1


		elif (author not in data):
			data[author] = [0, 0]
			data[author][contribution_type] += 1

	with open("data.json", "w") as data_file:
		json.dump(data, data_file, indent = 3)

def store_daily(author, created_time, contribution_type):
	with open("today.json") as data_file:
		data = json.load(data_file)

		if (author in data):
			data[author][contribution_type] += 1
			data[author][contribution_type + 2].append(created_time)

		elif (author not in data):
			data[author] = [0, 0, [], []]
			data[author][contribution_type] += 1
			data[author][contribution_type + 2].append(created_time)

	with open("today.json", "w") as data_file:
		json.dump(data, data_file, indent = 3)

x = 149
while True:
	try:
		for post in submission_stream:
			if post is None:
				break
			author = str(post.author)
			store_daily(author, post.created_utc, 0)
			store_total(author, 0)
			x = x + 1

		for comment in comment_stream:
			if comment is None:
				break
			author = str(comment.author)
			store_daily(author, comment.created_utc, 1)
			store_total(author, 1)
			x = x + 1

		if (x > 1000):
			print(x)
			x = 0
			list3 = []

			with open("appreciated.json") as data_file:
				appreciated = json.load(data_file)

			with open("data.json") as data_file:
				list2 = json.load(data_file)

			list3 = list2.keys()
			list3 = list(list3)

			for item in appreciated:
				list3.remove(item)


			username = list3[0]

			if (username not in appreciated):
				post = reddit.subreddit("teenagersbutpog").submit(title = "Appreciation post for " + username, selftext = "", flair_id = "6a92db18-9a37-11eb-ad7d-0ea199717311")
				post.reply("u/" + username)
				appreciated.append(username)
				print("Posted for " + username)

				with open("appreciated.json", "w") as data_file:
					json.dump(appreciated, data_file, indent = 3)

			with open("today.json") as data_file:
				data = json.load(data_file)

				for user in data:
					for time in data.get(user)[2]:
						if (time < time_.time() - 84600):
							data.get(user)[0] = data.get(user)[0] - 1
							old_times.append(time)

						for i in old_times:
							data.get(user)[2].remove(i)
						old_times = []

				with open("today.json", "w") as data_file:
					json.dump(data, data_file, indent = 3)

			with open("today.json") as data_file:
				data = json.load(data_file)

				for user in data:
					for time in data.get(user)[3]:
						if (time < time_.time() - 84600):
							data.get(user)[1] = data.get(user)[1] - 1
							old_times.append(time)

						for i in old_times:
							data.get(user)[3].remove(i)
						old_times = []

				with open("today.json", "w") as data_file:
					json.dump(data, data_file, indent = 3)

			with open("today.json") as data_file:
				data = json.load(data_file)
				no_comments = []

				for user in data:
					if (data[user][0] == 0 and data[user][1] == 0):
						no_comments.append(user)

				for user in no_comments:
					del data[user]

				with open("today.json", "w") as data_file:
					json.dump(data, data_file, indent = 3)

	except:
		print("Error")
		time_.sleep(10)