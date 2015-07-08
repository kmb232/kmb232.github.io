Title: Don't Give Up! Or: What it's like in the middle of a project.
Category: Technology
Tags: Learning to Code
Author: Me
Status: Draft

I'm midway through a project I've been working on for some time, and of course so far I've found many more questions than answers. I'm trying to tell myself that that's OK, though. At least I think it is.

It all started with a thesis that much can be gained from Twitter metadata. To do this, I decided to collect a list of followers of a few ideology-specific accounts. From there I wanted to collect the metadata about these accounts for analysis.

I created two scripts, one for collecting the followers and another for collecting the information about the users. (I'll put those on Github if you're curious.) I've been using Twython to access the API. I know Tweepy is more popular, but for some reason I've 

So anyway, I thought it would be good to share a few of the lessons I've learned in the process:

* **Don't Be Greedy**
	When I started, I collected information on approximately 50,000 users. It sounded exciting, and I was still thinking in terms of my old job, where I had proper resources for dealing with GB's of data. I tried to open the CSV's, however, and my computer just wouldn't handle it. There just wasn't enough memory available to open the file and start manipulating data. I got the numbers down to about 10,000 and it's gone much more smoothly.

* **Always Think Ahead**
	It can be something as simple as making sure data types remain consistent or making sure you have the right file in the right location when it's called, but advanced planning can do wonders to a project like this. Even if you're a beginner and you don't even know what a code project is going to look like, plan ahead. The reason is simple: Things will go wrong. You can't stop things going wrong. But if you have a good sense of where you want your project to go it's easier to find solutions and also not get discouraged (which is especially important when you're learning how to code).

* **Don't Be Afraid of a Challenge
	There's one aspect of this whole thing I was too nervous to take on. For some reason I've always had difficulty when trying to write code that takes arguments from the command line. I'm still kicking myself because I didn't force myself to integrate it into my scripts. It would have kept me from needing to constantly work on two versions of a script, which is even more annoying as I continue to work on it. 

* **ASCII is the Devil**
	This is more specific to working with text data, but it's being mentioned here because it's where I'm currently stuck. Many others have gone into detail about character systems so I won't bother, but if you're working with data from the internet this will be something you need to know about. It ties in a bit with my previous point, but plan ahead. The sooner you realize something like this is going to be a problem, the better. It's particularly frustrating for me because I like to think I know better by now.

So as I conclude this, I think the ultimate lesson I have learned, or rather remembered, is how important it is to plan ahead. 