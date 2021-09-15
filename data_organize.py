import praw, login_info, json, datatime
reddit = login_info.reddit

url = "https://www.reddit.com/r/teenagersbutpog/comments/pjg3lj/coddit_20_but_on_a_reddit_post_cause_im_stupid/"
post = reddit.submission(url = url)
data = {}

list_of_users = []
by_comment = {}
by_post = {}
by_contributions = {}

def get_by_posts(contribution_data):
	return contribution_data[1]

def get_by_comments(contribution_data):
	return contribution_data[2]

def get_by_contributions(contribution_data):
	return contribution_data[1] + contribution_data[2]


with open("data.json") as data_file:
	data = json.load(data_file)

	for user in data:
		list_of_users.append([user, data.get(user)[0], data.get(user)[1]])

	list_of_users.sort(key = get_by_comments, reverse = True)

	for i in list_of_users:
		by_comment[i[0]] = [i[1], i[2]]

	with open("data_by_comment.json", "w") as data_file:
		json.dump(by_comment, data_file, indent = 3)


	list_of_users.sort(key = get_by_posts, reverse = True)

	for i in list_of_users:
		by_post[i[0]] = [i[1], i[2]]

	with open("data_by_post.json", "w") as data_file:
		json.dump(by_post, data_file, indent = 3)


	list_of_users.sort(key = get_by_contributions, reverse = True)

	for i in list_of_users:
		by_contributions[i[0]] = [i[1], i[2]]

	with open("data_by_contribution.json", "w") as data_file:
		json.dump(by_contributions, data_file, indent = 3)
		
with open("data.json") as data_file:
	data = json.load(data_file)
	
	for user in data:
		for time in data.get(user)[4]:
			data.get(user)[2] = 0
			if (time > datetime.datetime.utcnow() - 3600):
				data.get(user)[2] = data.get(user)[2] + 1
			if (time > datetime.datetime.utcnow() - 86400):
				data.get(user)[3] = data.get(user)[3] + 1
