# Basic Static Analysis

Now that you've gotten everything set up, it is time to do some reverse engineering. The simplest static analysis tools can give you a great place to start in analyzing an unknown piece of malware. 

### Get the Textbook's RE practice files:

Grab the malware samples published alongside the textbook from this [link](https://nostarch.com/malware).

*The original distribution format was a .7z with a self-extracting executable. [Sean Whalen](https://github.com/seanthegeek) published a pull request suggesting eliminating the self-extracting .exe. If you are going to extract in a non-Windows environment, [this version](https://github.com/mikesiko/PracticalMalwareAnalysis-Labs/pull/8) is much easier to use.*

### Complete *Lab 1-1 and Lab 1-2* ~~through Lab 1-4~~: 

Treat the questions as hints for where to start. Rather than answering the questions directly, create a report for each lab. Each week, the report format will be the same, but the content will get progressively more sophisticated as you learn new RE tools.

1. Start with a title (like "Week 1 - Simple Static Analysis")
2. Write a paragraph summarizing what you learned to look for this week (like strings, VirusTotal, libraries, exported functions, packers, etc.)
3. Foreach Lab X:
    1. Create a subheading "Lab 1-X"
    2. Include the following:
        1. Executive Summary (Most important takeaways for this malware)
        2. Indicators of Compromise (What to look for to see if you are infected)
        3. Mitigations (Have you discovered anything that could be used to fix this infection?)
        4. Evidence (How did you find each of the above? You can mention here any work you did that did not yield any results.)

When you are ready for us to grade your submission, submit a link to the markdown file containing your reports for Week 1 in your github repo.

You can see a sample submission for this week [here](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring23/Samples/Week1.md)

Useful links:

[DependencyWalker](https://www.dependencywalker.com/)

[PEView](http://wjradburn.com/software/)

[Strings for Windows](https://learn.microsoft.com/en-us/sysinternals/downloads/strings)