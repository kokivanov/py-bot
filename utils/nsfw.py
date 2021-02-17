import discord
from pybooru import Danbooru
import praw
import random
import json
import random

fl = open("usersettings.json")

settings = json.loads(fl.read())

rList = {"standard" : ['hentai', 'Hentai4Everyone', 'hentai_fish', 'Tentai', 'HentaiManga', 'HypnoHentai', 'HentaiAnime', 'HentaiSource', 'nhentai', 'hentaifemdom', 'HentaiPetgirls', 'rule34', 'hentaibondage', 'hentaihaven', 'ecchi']}

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

        def standard(self):
            sub_r : str = rList["standard"][random.randint(0, len(rList["standard"])-1)]
            print(sub_r)
            sub = self.reddit.subreddit(sub_r)
            del sub_r
            if sub.random():
                post = sub.random().url
                print(post)
                if (sub.random().url == None):
                    return self.standard()

                if self.__isImage(post):
                    return post
                else:
                    return self.standard()
            else:
                return self.standard()
            
        def check(self):
            print(self.reddit.user.me())

        def __isImage(self, lk : str):
            if lk:
                if lk.endswith(".jpg") or lk.endswith(".png") or lk.endswith(".gif") or ("redgifs" in lk) or ("watch" in lk) or ("nhentai.xxx" in lk) or ("nhentai.org" in lk) or ("imgur.com" in lk) or ("i.redd.it" in lk):
                    return True
            return False

        #def handler(self, args : []):
        #    if len(args) < 2:

if __name__ == "__main__":
    client = nsfw(
            duname=settings["Danbooru"]["username"],
            dapi=settings["Danbooru"]["api_key"],
            rid=settings["Reddit"]["id"],
            rsec=settings["Reddit"]["secret"],
            rname=settings["Reddit"]["scriptname"],
            runame=settings["Reddit"]["username"],
            rpass=settings["Reddit"]["password"]
        )
        
    client.check()
    print(client.standard())
    
