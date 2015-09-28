import praw
import re
import os.path
import time

header = "Comment scraper for sentiment analysis"

r = praw.Reddit(header)

def dumpTheBodies(submissionId, sub):
    filename = submissionId + '.txt'
    path = 'C:/reddit/' + sub + '/'
    save_path = os.path.join(path, filename)

    if not os.path.isdir(path):
        try:
            os.makedirs(path)
        except OSError as e:
            if e.errno != 17:
                raise

    submission = r.get_submission(submission_id=submissionId)
    flat_comments = praw.helpers.flatten_tree(submission.comments)
    with open(save_path, 'w', encoding='utf-8') as f:
        for comment in flat_comments:
            if hasattr(comment, 'body'):
                f.write(str(comment.body) + '\n')
    f.close()

print ("fetching comments")

targets = ['ffxiv', 'anime', 'fitness', 'askreddit', 'funny', 'pics', 'aww', 'CatsStandingUp', 'atheism', 'mildlyinteresting', 'food', 'news', 'gifs', 'reactiongifs', 'shittyreactiongifs', 'magictcg', 'gaming', 'truegaming']

for item in targets:
    subreddit = r.get_subreddit(item)
    for submission in subreddit.get_hot(limit=75):
        dumpTheBodies(submission.id, item)

quit()
