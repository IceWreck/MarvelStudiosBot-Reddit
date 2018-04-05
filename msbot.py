import praw
import re
import random
import time




def main_func():

    # praw.ini file in same folder contains config info
    reddit = praw.Reddit('msbot')

    subreddit = reddit.subreddit("marvelstudios")

    def autocorrect(prompt, reply):
        ismatch = any(string in comment_text for string in prompt)
        if ismatch:
            ms_reply = reply
            comment.reply(ms_reply)
            print("Reply: " + ms_reply)
            time.sleep(5)

    def replytoparent(prompt, reply):
        ismatch = any(string in comment_text for string in prompt)
        if ismatch:
            ms_reply = reply
            parent = comment.parent()
            parent.reply(ms_reply)
            print("Reply: " + ms_reply)
            time.sleep(5)

    # End of essential functions function

    for comment in subreddit.stream.comments():
        comment_text = comment.body.lower()
        print(comment_text)

        # Autocorrect
        """
        
        variable_P is the prompt or the trigger word
        variable_Q is the reply
        
        """

        # Spider-Man corrections.
        spiderman_P = ["spiderman", "spider man"]
        spiderman_Q = "> Spider-Man. \n\n #RespectTheHyphen"
        autocorrect(spiderman_P, spiderman_Q)

        # Iron Man correction
        ironman_P = ["ironman", "iron-man"]
        ironman_Q = "> Iron Man. \n\n FTFY"
        autocorrect(ironman_P, ironman_Q)

        # Giant man has this weird problem where it picks up and corrects to Ant-Man. We do not want this.
        # I could correct giantman to Giant-Man but don't know if that is the lingo so just ignore those.
        giantman_P = ["giant man", "giantman"]
        giantman_match = any(string in comment_text for string in giantman_P)
        antman_P = ["antman", "ant man"]
        antman_match = any(string in comment_text for string in antman_P)
        antman_Q = "> Ant-Man. \n\n #RespectTheHyphen"
        if giantman_match:
            print("NoReply: " + "Giantman found. Ignore.")
        elif antman_match:
            autocorrect(antman_P, antman_Q)

        # End of autocorrect

        # Temporary Memes
        # These also use the autocorrect function.

        # 1) Where is Hawkeye ?
        hawkeye_P = ["where's hawkeye", "where is hawkeye"]
        hawkeye_R = "I'm sure they are hiding Hawkeye to avoid spoiling Ronin. Ronin is basically Hawkeye in ninja " \
                    "Batman mode.  \n\n #JusticeForHawkeye"
        autocorrect(hawkeye_P, hawkeye_R)

        # 2) RedditVibranium

        redditvib_P = ["!redditvibranium", "!reddit vibranium", "! redditvibranium", "! reddit vibranium"]
        redditvib_Q = "#### Congrats! " + "You have received " \
                                          " [Reddit Vibranium](https://imgur.com/a/mYMCK)" \
                                          "for this submission." \
                                          "\n\n ^(I'm a bot beep beep. If you want something added to this bot," \
                                          " just PM me. BTW, AsgardCoin is coming soon.) "
        replytoparent(redditvib_P, redditvib_Q)


        # End of temporary memes

    # End of new comments stream function
# End of main function


# Initiate code
try:
    main_func()
except:
    # if you use it too much, it stops
    # Inform me about the failure of main function
    time.sleep(100)
    main_func()
# End of main code



# Samples to do stuff not yet implemented
"""
    elif re.search("i am groot", comment.body, re.IGNORECASE):
        ms_reply = random.choice(groot_quotes)
        comment.reply(ms_reply)
        print("Reply: " + ms_reply)
"""

"""
groot_quotes = \
[
    "I never thought I'd meet a groot.",
    "Well, I'm Groot Jr.",
    ""
]
"""

# Previous way to do autocorrect
"""
if re.search("spiderman", comment.body, re.IGNORECASE):
    ms_reply = "It is Spider-Man. Please respect the hyphen."
    comment.reply(ms_reply)
    print(ms_reply)
"""

"""
Things to add:

# !AsgardianCoin or !RedditVibranium
# memes like dormammu bargain or i'm groot

"""

