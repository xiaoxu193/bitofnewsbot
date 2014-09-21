bitofnewsbot
============

Source of popular Reddit bot [u/bitofnewsbot](http://www.reddit.com/u/bitofnewsbot)


How do  I run it?
=====================
Setup cron to run it every minute

Instructions for Ubuntu:

* Replace username and password line in bitofnewsbot
* Install cron ``sudo apt-get install cron``
* Open up crontab to edit cron ``sudo crontab -e``
* Tell it to run every minute: ``* * * * * /usr/bin/python bitofnewsbot.py``


Submissions are stored in done.txt so they're not commented on again.

``TODO: use sqllite3. The point is to have minimum setup``


Dependencies
============
* PyTeaser: ``pip install pyteaser``

Go to official [PyTeaser repo](https://github.com/xiaoxu193/PyTeaser/) for help with installation.

Variables
========
These are the variables you can set. 

TODO: Put all this shit in a config file

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
