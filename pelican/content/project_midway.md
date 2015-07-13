Title: Don't Give Up! Or: What it's like in the middle of a project.
Category: Technology
Tags: Learning to Code, Data
Author: Me
Status: Draft

I'm midway through a project I've been working on for some time, and of course so far I've found many more questions than answers. I'm trying to tell myself that that's OK, though. At least I think it is.

It all started with a thesis that much can be gained from Twitter metadata. To do this, I decided to collect a list of followers of a few ideology-specific accounts. From there I wanted to collect the metadata about these accounts for analysis.

I created two scripts, one for collecting the followers and another for collecting the information about the users. (I'll put those on [Github if you're curious.](https://github.com/kmb232/twitter__research)) I've been using Twython to access the API. I know Tweepy is more popular, but for some reason I've gotten along better with Twython. I ran everything on an EC2 instance since API rate limits require the timing to be spread out.

So anyway, I thought it would be good to share a few of the lessons I've learned in the process:

* **Don't Be Greedy**
	When I started, I collected information on approximately 50,000 users. It sounded exciting, and I was still thinking in terms of my old job, where I had proper resources for dealing with that much data. I tried to open the CSV's, however, and my computer just wouldn't handle it. There just wasn't enough memory available to open the file and start manipulating data. I got the numbers down to about 10,000 and it's gone much more smoothly.

* **Always Think Ahead**
	It can be something as simple as making sure data types remain consistent or figuring out how to work around Twitter's rate limits, but advanced planning can do wonders to a project like this. Even if you're a beginner and you don't even know how to proceed with your project, plan ahead. The reason is simple: Things will go wrong. You can't stop things going wrong. But if you have a good sense of where you want your project to go it's easier to find solutions and also not get discouraged (which is especially important when you're learning how to code).

* **Don't Be Afraid of a Challenge
	There's one aspect of this whole thing I was too nervous to take on. For some reason I've always had difficulty when trying to write code that takes arguments from the command line. I'm still kicking myself because I didn't force myself to integrate it into my scripts. It would have kept me from needing to constantly work on two versions of a script, which is even more annoying as I continue to work on it. 

* **ASCII is the Devil**
	This is more specific to working with text data, but it's being mentioned here because it's where I'm currently stuck. Many others have gone into detail about character systems so I won't bother, but if you're working with data from the internet this will be something you need to know about. It ties in a bit with my previous point, but plan ahead. The sooner you realize something like this is going to be a problem, the better. It's particularly frustrating for me because I like to think I know better by now.

But really the important thing is not to get discouraged. We like to think that learning is about "mastery" or a subject, but I have yet to meet a programmer who feels they've reached expert level. Hard to feel that way when a large part of what you do is finding and fixing your own mistakes. It's true no matter what your level of coding skill. If you just keep going you will find the errors, you'll figure out what issues you need to work around, and you will start to see results. 