## Human Benchmark AI

This project is for educational purposes. 

The goal of the project is to learn python keyboard and mouse libraries to better understand automation.
This project aims to automate scoring for the novelty website <https://humanbenchmark.com>

Each task in the human benchmark poses an interesting challenge from a programming perspective, and deals with image and text processing.

This readme will be updated as each of the 8 challenges are completed, the ultimate goal is to have a program capable of 
scoring in the 99th percentile for each of the challenges.

## The Challenges
# Reaction Time

The reaction time challenge tasks the user with clicking the screen as fast as possible when it turns from green to red.
This challenge, from a coding perspective, deals with processing screenshots and extracting pixel RGB values as fast as possible.

This was the first challenge I took, as it has the least steps, but has the interesting constraint of having to process data quickly.

The median score is 273ms, and my personal best score is 214ms. The site indicates that the normal human reaction range falls between 200 and 250ms.
The AI is able to achieve a median score of 110ms, and the best I have seen has been 60ms.

# Sequence Memory

The sequence memory challenge tasks the user with remembering a sequence of inputs on a 3x3 grid which grows by 1 with each level.
While the pattern never changes, only adding to the end, it becomes increasingly difficult to remember the whole pattern with
each new step added.

From a coding perspective, this challenge deals with adding actions to a list that grows with each level. While one can assume that it is
easier to keep the old list and add the new command to the end, in practice, that solution proved fairly difficult.

Instead I leveraged the fact that there were no immediate repeats in the pattern and made the code check for when the next step appears, and re-populates
the list of steps in real time.

The typical human sequence memory lies in the range of 6-12 steps, with a median of 8. My personal best is 8. As far as I have been able to tell, the AI is
fully capable of going until stopped manually. I have implemented a limit to the number of iterations in order to prevent it from running forever, 
however you may disable that limit should you please.

**As an additional note:** The website will occasionally show ads which resize the screen by creating a banner on all edges, this immediately breaks the code
I recommend running this with an Ad blocker enabled for best results.
