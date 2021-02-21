import discord
from pybooru import Danbooru
import praw
import random
import json
import random

fl = open("usersettings.json")

settings = json.loads(fl.read())

rList = {"standard": ['hentai', 'Hentai4Everyone', 'hentai_fish', 'Tentai', 'HentaiManga', 'HypnoHentai', 'HentaiAnime', 'HentaiSource', 'nhentai', 'hentaifemdom', 'HentaiPetgirls', 'rule34', 'hentaibondage', 'hentaihaven', 'ecchi'],
         "raphtalia": ["RaphtaliaHentai", "shieldherohentai"],
         "3d": ["porn", "pornvids", "nsfw_gifs", "porn_gifs"],
         "overwatch": ["OverwatchNSFW", "Rule34Overwatch"],
         "genshinimpact": ["GenshinImpactNSFW", "GenshinImpactHentai", "GenshinLewds"],
         "cosplay": ["cosplay", "cosplaygirls"],
         "sfw": ["AnimeART", "animeartists"]
         }


class medias(object):
    avialble_commands = ["nsfw", "hentai", "r34"]

    nsfw_allowed: bool = False

    aliases = {
        "standard": "standard",
        "raph": "raphtalia", "raphtalia": "raphtalia", "rph": "raphtalia",
        "porn": "3d", "3d": "3d",
        "overwatch": "overwatch", "ow": "overwatch", "over": "overwatch",
        "genshinimpact": "genshinimpact", "gi": "genshinimpact", "genshin": "genshinimpact",
        "cosplay": "cos", "cosplay": "cosplay",
        "art": "sfw", "sfw": "sfw"
    }

    sfw_alias = {
        "cosplay": "cos", "cosplay": "cosplay",
        "art": "sfw", "sfw": "sfw"
    }

    danbooru: Danbooru
    reddit: praw.Reddit

    def reddit_byauthor(self, arg):
        try:
            redditor = self.reddit.redditor(arg)
            if not redditor.subreddit["over_18"] or nsfw_allowed:
                posts = list(redditor.hot())
                return posts[random.randint(1, len(posts))-1]
            else:
                return "No no no"
        except Exception as e:
            pass

    def reddit_bysubreddit(self, arg):
        try:
            sub = self.reddit.subreddit(arg)
            posts = list(sub.hot())
            if self.nsfw_allowed or not sub.over18:
                return posts[random.randint(1, len(posts))-1].url
            else:
                return "No no no"
        except Exception as e:
            pass

    def danbooru_search(self, arg):
        try:
            post = self.danbooru.post_list(tags=arg, limit=1, random=True)[0]

            if self.nsfw_allowed or post["rating"] == 's':
                if "large_file_url" in list(post.keys()):
                    return post["large_file_url"]
                elif "file_url" in list(post.keys()):
                    return post["file_url"]
                else:
                    return post["id"]
            else:
                return self.danbooru_search(arg)
        except Exception as e:
            pass

    def getReddit(self, topic):
        sub_r: str
        if self.nsfw_allowed:
            sub_r = rList[topic][random.randint(0, len(rList[topic])-1)]
        else:
            tp = rList[list(rList.keys())[random.randint(-2, -1)]]
            sub_r = tp[random.randint(1, len(tp))-1]
        print(sub_r)
        sub = self.reddit.subreddit(sub_r)
        del sub_r
        if sub.random() != None:
            post = sub.random().url
            print(post)
            if (post == None or post == ""):
                return self.getReddit(topic)
            if self.__isImage(lk=post):
                return post
            else:
                return self.getReddit(topic)
        else:
            return self.getReddit(topic)

    def check(self):
        print(self.reddit.user.me())

    def __isImage(self, lk: str):
        if lk != None:
            if lk.endswith(".jpg") or lk.endswith(".png") or lk.endswith(".gif") or ("redgifs" in lk) or ("watch" in lk) or ("nhentai.xxx" in lk) or ("eahentai" in lk) or ("reddit.com/gallery" in lk) or ("nhentai.org" in lk) or ("imgur.com" in lk) or ("i.redd.it" in lk):
                return True
        return False

    rkey = {"-r": reddit_bysubreddit, "-a": reddit_byauthor}

    def safe_(self, args):
        tmp = self.nsfw_allowed
        self.nsfw_allowed = False
        res = self.handler(args)
        self.nsfw_allowed = tmp
        return res

    def handler(self, args: [] = ["standard"]) -> str:
        print("Args: " + str(args) + "nsfw allowed: " + str(self.nsfw_allowed))

        if args:
            if len(args) < 1:
                return self.getReddit("standard")
            elif len(args) < 2:
                if "-s" in args:
                    return self.safe_(args=args.remove("-s"))
                elif args[0].lower() == "overall" and nsfw_allowed:
                    return self.getReddit(self.aliases[list(self.aliases.keys())[random.randint(1, len(self.aliases.keys()))-1]])
                elif args[0].lower() == "overall":
                    return self.getReddit(self.sfw_alias[list(self.sfw_alias.keys())[random.randint(1, len(self.sfw_alias.keys()))-1]])
                elif args[0].lower() in list(self.aliases.keys()):
                    for item in self.aliases.keys():
                        if item == args[0].lower():
                            return self.getReddit(self.aliases[args[0].lower()])
                elif args[0].lower():
                    self.reddit_bysubreddit(args[0].lower())
                else:
                    return self.getReddit("standard")
                return self.getReddit("standard")
            elif len(args) >= 2:
                if "-s" in args:
                    args.remove("-s")
                    return self.safe_(args=args)
                elif "-r" in args:
                    args.remove("-r")
                    return self.reddit_bysubreddit(args[0].lower())
                elif "-a" in args:
                    args.remove("-a")
                    return self.reddit_byauthor(args[0].lower())
                elif "-d" in args:
                    args.remove("-d")
                    return self.danbooru_search(args[0].lower())
                else:
                    return self.handler(args[0].lower())

        return self.getReddit("standard")

    def __init__(self, duname: str, dapi: str, rid: str, rsec: str, rname: str, runame: str, rpass: str, nsfw_allowed=False):
        if (duname and dapi and rid and rsec and rname and runame and rpass):
            self.danbooru = Danbooru(
                site_url="https://danbooru.donmai.us/", username=duname, api_key=dapi)
            self.reddit = praw.Reddit(client_id=rid,
                                      client_secret=rsec,
                                      user_agent=rname,
                                      username=runame,
                                      password=rpass)
            self.nsfw_allowed = nsfw_allowed


if __name__ == "__main__":
    client = medias(
        duname=settings["Danbooru"]["username"],
        dapi=settings["Danbooru"]["api_key"],
        rid=settings["Reddit"]["id"],
        rsec=settings["Reddit"]["secret"],
        rname=settings["Reddit"]["scriptname"],
        runame=settings["Reddit"]["username"],
        rpass=settings["Reddit"]["password"],
        nsfw_allowed=True
    )

    client.check()
    print(client.handler(["-d", "-s", "gi"]))
