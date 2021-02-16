import discord
from pybooru import Danbooru
import praw
import random

class nsfw(object):
        avialble_commands = ["nsfw", "hentai", "r34"]
        dkeys = ["-a", "-k", "-t"]
        rkey = ["-s", "-r", "-a"]

        danbooru : Danbooru
        reddit : praw.Reddit

        def __init__(self, duname : str, dapi : str, rid : str, rsec : str, rname : str, runame : str, rpass : str):
            if (duname and dapi and rid and rsec and rname and  runame and rpass):
                self.client = Danbooru(site_url = "https://danbooru.donmai.us/", username=duname, api_key=dapi)
                self.reddit = praw.Reddit(client_id=rid,
                    client_secret=rsec,
                    user_agent= rname,
                    username=runame,
                    password=rpass)
        
        def reddit_byauthor(self, arg):
            posts = self.reddit.redditor(arg.lower())
            return posts

        def check(self):
            print(self.reddit.user.me())

        #def handler(self, command : str, args : []):
        #    if len(args) < 2:

if __name__ == "__main__":
    client = nsfw("""type arguments""")
    client.check()
    for post in client.reddit_byauthor("concretebeats").submissions.hot(limit=3):
        print(post.url)
