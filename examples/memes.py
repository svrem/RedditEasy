import redditeasy

post = redditeasy.Subreddit("dankmemes")
postoutput = post.get_post()

print(f"Posts Title: {postoutput.title}\n"
      f"Posts Content: {postoutput.content}\n"
      f"Posts Author: u/{postoutput.author}\n"
      f"Posts URL: {postoutput.post_url}\n"
      f"Spoiler?: {postoutput.spoiler}\n"
      f"Post Created At: {postoutput.created_at}\n"
      f"Posts Upvote Count: {postoutput.score}\n"
      f"Posts Award Count: {postoutput.total_awards}\n"
      f"NSFW?: {postoutput.nsfw}\n"
      f"Post Flair: {postoutput.post_flair}\n"
      f"User Flair: {postoutput.author_flair}\n"
      f"Subreddit Subscribers: {postoutput.subreddit_subscribers}")
