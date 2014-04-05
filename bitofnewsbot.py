import praw
import time
import datetime
import pyteaser

toadd = []


submissions_limit = 100 #number of top subissions to check during each cron period
thresh_max = 500 #karma threshholds for commenting
thresh_min = 10
username="bitofnewsbot"#reddit login details
password="NiceTryUseYourOwnPassword"
comments_per_run = 3 #comments per cron period
sentences_per_summary = 3 #sentences per summary
subreddits = "worldnews+worldpolitics"
agent = "u/bitofnewsbot"
filestore = "done.txt" #to store submission ids of ones that are commented

def main():
	submissions = getSubmissions()
	done = getDone()
	counts=0 #how many comments made this round

	for submission in submissions:
		if counts>=comments_per_run:
				break
		id = submission.id
		point = submission.ups - submission.downs

		if id not in done and point<thresh_max and point>thresh_min:
			putDone(submission.id)
			sentences = pyteaser.SummarizeUrl(submission.url);
			if (sentences != None):
				counts+=1
				comment = formComment(sentences, submission)
		
			submission.add_comment(comment);
			print comment

	

def getDone():
	with open(filestore) as f:
		return f.read().splitlines()

def putDone(id):
	with open(filestore, "a") as text_file:
		text_file.write(id+"\n")

def getSubmissions():
	r = praw.Reddit(user_agent=agent)
	r.login(username, password)
	return r.get_subreddit(subreddits).get_hot(limit=1000)

def formComment(sentences, submission):
	print submission.title+": "+submission.url

	point = submission.ups - submission.downs
	comment = "**Article summary:** \n"
	count = 0
	if (sentences is None or len(sentences)<3):
		return None
	for sentence in sentences:
			if count < sentences_per_summary:
				comment += ("\n>* " + sentence + "\n");
				count = count + 1
	comment += "\n^I'm ^a ^bot, ^v2. ^Report ^problems [^here](http://reddit.com/r/bitofnewsbot). \n\n**^Learn ^how ^it ^works: [^Bit ^of ^News](http://www.bitofnews.com/about.html)**"
	return comment

if __name__ == "__main__":
	main()
