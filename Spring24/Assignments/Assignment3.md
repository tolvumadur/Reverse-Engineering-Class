# x86 Assembly Review Exercises, IDA and Ghidra

Welcome to Week 4, where we review assembly language and what compilers do when they turn C code into machine code. We will be looking at windows programs to learn how they are actually formatted. The book recommends a binary reverse engineering tool called IDA. IDA is still the industry standard, but is quite expensive. We will compare it with a tool published by the NSA called Ghidra [Ghidra](https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_10.2.3_build/ghidra_10.2.3_PUBLIC_20230208.zip).

There is a 1 to 1 [correlation](http://ref.x86asm.net/coder32.html) between machine code containing x86 instructions. That means that you can always take a binary program and return it to assembly code to make it a bit more readable. Binary reverse engineering tools are built for the much harder task of figuring out what this assembly code does. They include tools to guess at what C code might have generated the program.

This week's assignment begins with some exercises to reinforce C/assembly concepts we have been learning.

## Assembly Review Excercises

Answer the following in complete sentences:

1. What is the difference between machine code and assembly?
2. If the ESP register is pointing to memory address `0x00000000001270A4` and I execute a `pushq rax` instruction, what address will `rsp` now be pointing to?
3. What is a stack frame?
4. What would you find in a data section?
5. What is the heap used for?
6. What is in the code section of a program's virtual memory space?
7. What does the `inc` instruction do, and how many operands does it take?
8. If I perform a `div` instruction, where would I find the remainder of the binary division (modulo)?
9. How does `jz` decide whether to jump or not?
10. How does `jne` decide whether to jump or not?
11. What does a `mov` instruction do?
12. What does the `TF` flag do, and why is it useful for debugging?
13. Why would an attacker want to control the RIP register inside a program they want to take control of?
14. What is the `ax` register and how does it relate to `rax`?
15. What is the result of the instruction `xor rax, rax` and where is it stored?
16. What does the `leave` instruction do in terms of registers to leave a stack frame?
17. What `pop` instruction is `retn` equivalent to?
18. What is a stack overflow?
19. What is a segmentation fault (a.k.a. a segfault)?
20. What are the RSI and RDI registers for that gives them their name?

## Your First Crackme

Download this [crackme](https://crackmes.one/static/crackme/5da31ebc33c5d46f00e2c661.zip). Password is `crackmes.one`.

Open it both with Ghidra and IDA. To access the decompiler in IDA you will need to use their cloud decompiler. This crackme is ok to send to them for decompilation. In general, cloud decompilers (which are gaining popularity as a way to make sure reverse engineers actually pay for services instead of pirating) are an operational security risk.

Solve the crackme by figuring out what password it is expecting. It is built for a Linux machine, and is not guaranteed to be malware-free. So run it either on your virtual machine's WSL terminal, or make a Linux VM to test with.

## What to Submit

Create a Markdown report for this week containing:

1) The answers to these 20 questions
2) Screenshots of the crackme open in Ghidra AND in IDA
3) How you solved it, and what the solution was.
4) Whether Ghidra or IDA was more helpful to you, and why.




