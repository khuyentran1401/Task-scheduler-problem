# fast_start_session.py

# import random
import time
import os

def main():
    FastStartSession()


def FastStartSession():
    """a routine to collect, organize and prioritize mental desk"""
    start_here = """sometimes we have an amazing amount of stuff taking up residence in our brain"""

    technique_source = """This technique was taught by a smart man named Jerry Balanger, lets make a list of everything that is on your mind"""

    writing = """go ahead and grab a new piece of paper and write down everything that is on your mind, in future versions we will have this integrated into this app and we can give feedback on what you type"""

    writing2 = """This should take about 10 to fifteen minutes, write down everything that you are worried about, thinking about, stuff that is bothering your or issues with a relatinship that needs repair, someone who needs a call or a thing you should have done a while ago and didnt"""

    writing3 = """The next step is to acknoledge that there are things beyond your ability to control the outcome and we want to consciously encourage you to let those go, release yourself from worrying about things that are outside of your control"""

    writing4 = """So go write for fifteen minutes and then come back"""

    writing5 = """Eban Pagan has this as part of his FastStartTraining and we reccomend you try his material for management and self development"""

    writing6 = """some people focus on more business, others personal but I want you to just write everything and we can workshop the flow or organizationan of the final list later."""

    writing7 = """I can't do the math if we don't know all the variables"""

    writing8 = """If you have a lever big enough you can move the world, which of these items has impact upon the rest, write a star next to them."""

    writing9 = """Now order those starred subjects and think about presidence constraints... what should be done to enable that task to be done easier, more effective or quicker. This could be a phone call, doing someone a favor so it gets expedited, apealing to someones ego, a threat or some kind of proactive social engineering"""

# condense these next pieces into one loop

    text = start_here
    os.system(f"say {text}")
    print(start_here)
    time.sleep(2)

    text = technique_source
    os.system(f"say {text}")
    print(technique_source)
    time.sleep(2)

    text = writing
    os.system(f"say {text}")
    print(writing)
    time.sleep(2)

    text = writing2
    os.system(f"say {text}")
    print(writing2)
    time.sleep(2)

    text = writing3
    os.system(f"say {text}")
    print(writing3)
    time.sleep(2)

    text = writing4
    os.system(f"say {text}")
    print(writing4)
    time.sleep(2)

    text = writing5
    os.system(f"say {text}")
    print(writing5)
    time.sleep(2)

    text = writing6
    os.system(f"say {text}")
    print(writing6)
    time.sleep(2)

    text = writing7
    os.system(f"say {text}")
    print(writing7)
    time.sleep(2)


# def faststart_input():
    # add this to journal program, user enters an item
    # each item is linked to a project number
    # user gets a daily or hourly reprint to screen of projects
    # over time add project status, planned, started, in process, blocked and completed along with date completed.
    # user is greated and this routine is inserted as a journal.
    # we condense the items on the list into their existing todo list
    # group together similar items by prerequisites
    # also read them one by one to the user, ask "does task a come before or after item b"
    # this could get absorbed into the TODO app as our custom item, a branch?


# def faststart_review():
    """we will reprint the list to the user, sorted by user selectable options of project name, project number, data created, project owner, kwarg"""
    # print(user_todo_list)


if __name__ == '__main__':
    main()