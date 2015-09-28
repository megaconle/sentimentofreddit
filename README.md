# sentimentofreddit

Comment scraper: Using the fabulous PRAW (https://github.com/praw-dev/praw), it fetches all comments from the top 75 hot posts in a variety of subreddits separated by a newline. Only the comment body is saved (no usernames), but conversations remain grouped together for context. Comments are undergoing the process of being separated into negative/positive by hand. Currently about 1000 comments from /r/ffxiv have been categorized. 

Sentiment analysis: Currently only in the first stage, will expand once there are more comments to analyze.

End goal: What are the most positive words on reddit? Are the cultures of some subreddits as positive or negative as they're perceived to be? Is there a difference in tone between offshoots and the 'parent' subreddits - will compare /r/gaming vs. /r/truegaming and /r/gifs vs. /r/reactiongifs vs /r/shittyreactiongifs.
