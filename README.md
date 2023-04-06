# twitter_bot
taylor swift twitter bot hahah

This was hacked together in a few hours on a weekend, but it randomly selects and tweets a lyric from a Kaggle dataset of Taylor Swift lyrics. Made for fun. Twitter account has since been discontinued since I was running the API calls as a Cron Job through my Mac which was slowing it down


#How to schedule the python program. 
# add the following need to add this to the VIM file that opens when you type:    crontab -e

15 */3 * * * /opt/anaconda3/bin/python /Users/johngearig/Desktop/fun_coding/tswift.py
