bitofnewsbot
============

Source of popular Reddit bot [u/bitofnewsbot](http://www.reddit.com/u/bitofnewsbot)

Install
=======
Install? Seriously just clone it and run it :)

You also need to install my other project, PyTeaser.

But how does it work?
=====================
Setup cron to run it every minute

Submissions are stored in done.txt so they're not commented on again


Variables
========
These are the variables you can set. 

* submissions_limit - number of top subissions to check during each cron period
* thresh_max - karma threshholds for commenting
* thresh_min - karma threshholds for commenting
* username - Reddit login details
* password - Reddit login password
* comments_per_run - comments per cron period
* sentences_per_summary - sentences per summary
* subreddits - "worldnews+worldpolitics"
* agent - "u/bitofnewsbot"
* filestore - to store submission ids of ones that are commented, "done.txt"