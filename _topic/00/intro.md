---
title: Getting Started
hw: true
---

## Introductions

Names and questions: everyone says the name they would like to be called, and then answers a random question, then asks Des or Carl (alternating) *any question they want, that can be answered in a few words*.

{:.randomize onclick="randomQuestion(event);"}
 - {:.shown}What is your favorite food?
 - How big is your family?
 - *Other than here*, where is the farthest you have traveled?
 - How did you hear about AIMS?
 - What do you think you will do after AIMS?
 - Who is your favorite artist?
 - *Other than maths*, what is your favorite subject?
 - What is your favorite game?
 - Where would you most like to travel?
 - How do you greet friends in your home town?

## Getting Accounts Sorted

1. Account at the lab machine (should be done)
2. [Github](https://github.com) - get an account, [create and register ssh key](https://help.github.com/articles/generating-ssh-keys)
3. optional: [StackOverflow](http://stackoverflow.com),
   [Python Forum](http://www.python-forum.org/), etc.

## Machine Setup

1. optional Python IDE: [PyCharm](http://www.jetbrains.com/pycharm/)

## Reminder

We have several goals for the programming coursework:

 1. for *you* to be able formalize a problem
 2. for *others* to be able to understand your work
 3. for *you* and *others* to be able to have confidence in your work
 4. for *you* to be able to teach yourself how to have those for less simple tasks

The first three are about you developing your algorithmic thinking, as well as
your ability to express that thinking in Python.

The final item, however, means that this class may feel unfamiliar.  For almost all
of the class, I will ask you to do accomplish various tasks *without telling you how to do so*.

How will you learn anything?  By getting feedback on these tasks.

I will answer any question you have, but only once you have followed a few steps:

 1. *Try* to accomplish the task by doing something (anything) in Python.  Read any errors or warnings carefully, try to address them.  If you can't,
 2. *Ask* one of your peers for help.  If you tried different approaches, figure out
 what the differences are, and which ones matter.  If the two of you together can't figure it out,
 3. *Search* for a solution: start with the documentation on your system, then Google or one of the Python books in the library.  Return to step 1 with what you know, and try again.  If you get back to this step with nothing new to search for, then:
 4. *Ask* your teaching assistant (or any free TA) for help.  Tell them what you did for steps 1-3, and show them your results.  Work with them from step 1 again.  If you get back to this step,
 5. *Ask* me for help.  Tell me what you did for steps 1-3, and show me your results.  We will work from step 1 again until you get it.

## More Detailed Schedule

Each programming session will begin with a short "warmup" of about 15 minutes.
I will tell you about a game (at most 5 minutes), and the you will take a few
minutes to write down the necessary pieces of a program that would provide what
people need to play the game (out to 10 minutes after class starts).  If you
finish early, you should start writing down the parts of program that can play the game against a
person.  We will then discuss what people came up with for about 5 minutes.

Next, we will review the out-of-class work.  As a general rule, some homework will be assigned at the end of every class.  That homework will be due at 9 PM **THAT EVENING**.  The TAs will
review that work, and forward to me their assessments.  The next day, we will discuss
what people did right and wrong in the assignment, what the "big idea" behind the assignment was, then we will work **in-class** with everyone to get their programs working.

We will then do a more advanced version of the problem **in-class**, and finally
class will end with the next homework assignment being presented.

## Projects

In the last week, you will have a few larger programming problems to complete,
but no specific work in class.  You may start this work early.  You will
demonstrate the work on last day of class.  **Whether you pass or not is
determined by your completion of these projects.** During the first two weeks, I
will suggest tasks you should complete for each project.

The project problems are:

 - [a shape-drawing program]({% include url.lq %}/topic/shape-drawing/)
 - [simulating the SEIR model]({% include url.lq %}/topic/SEIR/)

## Class Rules

 - It is okay to be wrong.
 - IT IS OKAY TO BE WRONG.
 - It is NOT OKAY to do NOTHING, even if you have no idea what the answer is (see previous rules).
 - Be on time.
 - No active devices - no phones, music players, etc.  Turn them off, or preferably: do not bring them.
 - Unless you are coding or trying to find the answer to something, computers closed.  Lots of our work is pen-and-paper or discussion.
 - If you don't understand something, ask.  If I am talking too quickly, let me know.
 - DO NOT DO HOMEWORK FROM THIS CLASS DURING OTHER CLASS.

## Outside of Class SUGGESTIONS

 - After you turn-in homework, go to sleep.
 - Outside of class, you may use the computers for whatever AIMS says is okay.  Keep in mind: some of your classmates will probably be using the lab at the same time to do work.  Ringing phones, videos without headphones, loud conversations, etc will make it harder for them to do so.
 - get started on any assignment as soon as possible.

## How to Turn in Homework

You should each have a directory `python-course-homework` with a bunch of empty files - corresponding
to files you will need to make for homework assignments - and a script called `turnin.sh`.

To turn in homework, you need to update your branch of that repository with the changes you make to those files.  You will need to learn how to do that, but in the meantime you can use the `turnin` script:

{% highlight bash %}
python-course-homework yourusername$ ./turnin.sh AN EXPLANATION OF ANY CHANGES YOU MADE
{% endhighlight %}

## Setting Up Access to Homework Repository

Follow these steps **IF AND ONLY IF** you have sent Carl your Github username **AND** have accepted the team invitation.

In the commands below, replace $USERNAME with your AIMS user name.

{% highlight text %}
git config --global user.email "YOURAIMSEMAIL@aims.edu.gh"
git config --global user.name "YOUR NAME"
cd ~
git clone git@github.com:AIMS-Ghana/python-course-homework.git
cd python-course-homework
git checkout -b $USERNAME-hw
touch $USERNAME.md
git add --all
git commit -m "initial commit"
git push -u origin $USERNAME-hw
git branch -d master
{% endhighlight %}
