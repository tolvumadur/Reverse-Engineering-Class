# x86 Assembly Review and Ghidra

Welcome to Week 4, where we review assembly language and what compilers do when they turn C code into machine code. We will be looking at windows programs to learn how they are actually formatted. The setup this week should be much easier than in past weeks. The book recommends a binary reverse engineering tool called IDA Pro. IDA is still the industry standard, but is quite expensive. We will use a tool published by the NSA called Ghidra. Install [Ghidra](https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_10.2.3_build/ghidra_10.2.3_PUBLIC_20230208.zip) on your Linux VM for the activities this week.

There is a 1 to 1 [correlation](http://ref.x86asm.net/coder32.html) between machine code containing x86 instructions. That means that you can always take a binary program and return it to assembly code to make it a bit more readable. Binary reverse engineering tools are built for the much harder task of figuring out what this assembly code does. They include tools to guess at what C code might have generated the program.

This week's assignment is, by necessity, more formulaic and you will be submitting answers to questions that will take you on a tour of Ghidra and a refresher on assembly code. We will be using Intel syntax for x86 assembly to match the book. You may come across examples online that use the alternative AT&T syntax. 

Answer the following in complete sentences:

1. What is the difference between machine code and assembly?
2. If the ESP register is pointing to memory address 0x001270A4 and I execute a `push eax` instruction, what address will ESP now be pointing to?
3. What is a stack frame?
4. What would you find in a data section?
5. What is the heap used for?
6. What is in the code section of a program's virtual memory space?
7. What does the `inc` instruction do, and how many operands does it take?
8. If I perform a `div` instruction, where would I find the remainder of the binary division (modulo)?
9. How does `jz` decide whether to jump or not?
10. How does `jne` decide whether to jump or not?
11. What does a `mov` instruction do?
12. What does the `TF` flag do and why is it useful for debugging?
13. Why would an attacker want to control the EIP register inside a program they want to take control of?
14. What is the AL register and how does it relate to EAX?
What is the result of the instruction `xor eax, eax` and where is it stored?

If you are a grad student, please also answer the following. You will need to look beyond the textbook. Undergrads, I will forgive up to 2 errors in the first part if you answer these all correctly -- but they are optional for you:

15. What does the `leave` instruction do in terms of registers to leave a stack frame?
16. What `pop` instruction is `retn` equivalent to?
17. What is a stack overflow?
18. What is a segmentation fault (a.k.a. a segfault)?
19. What are the ESI and EDI registers for?
20. Also solve this [crackme](https://crackmes.one/static/crackme/5da31ebc33c5d46f00e2c661.zip), and explain how you did it using Ghidra (extraction password "crackmes.one"):

This part will be worth the equivalent of 5 questions from the above sections.

*crackme link has been updated, the one we solved in class can be found [here](https://crackmes.one/static/crackme/6296c1ff33c5d45b75903c0f.zip)