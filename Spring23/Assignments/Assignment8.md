# Detecting DLL Injection

This week corresponds with textbook chapter 12. We will be dissecting "real" malware again, so remember your lab safety protocols!

We've learned in class how malware loaders inject evil threads into legitimate programs, often using library loading as an attack vector. This week, you will be preparing malware analysis reports, but this time we will be focusing on what we can learn by observing library injection in action.

We will use the malware from Lab 12-1 for this week's assignment. We will need our RE skills honed by doing crackmes in order to understand what is going on.

To get full credit for the lab, answer the following, including a relevant Ghidra screenshot which backs up your answer. A text explanation alone doesn't show that you've followed through in Ghidra. A screenshot alone doesn't show that you understand what is going on.

 

1) Prove that the loader is using DLL injection. (Don't forget a relevant snapshot in Ghidra.)

2) Identify the process that will be injected into. Seeing a string in Ghidra isn't sufficient -- explain how the process gets selected.

3) Identify the entry point of the DLL injection. Where is DllMain?

4) This malware does something every ______ seconds. How often, and where is the loop where that waiting happens?

5) What does the malware do every _______ seconds?