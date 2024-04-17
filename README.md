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

# Typing Speed

The typing speed challenge deals with typing a block of text correctly as fast as possible. The text is different every time; however, the website pulls text from a variety of test text blocks so repeats are fairly common.

From a coding perspective, this challenge deals with extracting text from images and re-entering it into the field provided. 

This challenge proved slightly more difficult than anticipated. There is quite a lot of nuance to the text extraction engine that I hadn't realized. It needs fairly ideal conditions to not mistake certain special characters. An early issue I encountered was that the text recognition engine would mistake the box that the text appears in for a [ or | character.

My solution for this was to simply strip any leading special characters, since none of the text options started with a special character. Another issue I encountered was that the text had to be entered character by character, which meant that I had to put a delay on the code so that it didn't enter the answer too fast for the website to catch up.

Additionally, there was another issue with processing whitespace and carriage returns. This was fixed by replacing any whitespace characters with the standard single space, that way the code didn't interpret a newline character where there wasn't supposed to be one.

# Number Memory

The number memory challenge tasks the user with remembering a number that increases with each new level. The number starts at 1 character, and grows by 1 digit each time. 

From a coding perspective this challenge is very similar to the typing speed challenge but with a few extra conditions. Firstly, the typing challenge gave users unlimited time to read through the text and only began when the first character was entered. This gave ample time to take a large screenshot and process it for text extraction. The second key difference is that instead of one long block of text, the challenge requires many small strings to be entered, and the area that is important grows as the challenge goes on. 

Initially this challenge seemed like it was going to be the same as the last. It came with many issues, however. The text for this challenge is much larger, which counterintuitively led to the engine to frequently fail to recognize the text. It was capable of recognizing all the text except for the numbers. My best guess of why this is the cas was that the numbers were dramatically different sizes in comparison to the small concise text on screen. In order to combat this, I cropped out everything except for the numbers. The second assumption I made was that the screenshot was too wide, thus containing an abundance of irrelevant blue. After implementing both of those changes, the engine was able to identify numbers correctly. 

As a result of trying to maintain the minimum screenshot size to contain all of the numbers, the bounding box had to grow with each iteration, which was not hard to implement. However, now that the code was working, it was still mistaking 5s and 9s, as well as 1s and 7s. This is only occasionally occurring, and the best score has been 15. The human average is 8 and scores fall off after 12 until plateauing at 19.

I have tried several techniques to increase the accuracy of the engine including changing the color grading of the screenshot to maximize clarity, changing the size of the screenshot, and excluding all but numbers from the pool of possible options for the engine to recognize the shape as but thus far have not been able to achieve 100% recognition. I will move on for now and possibly revisit this challenge at a later date.
