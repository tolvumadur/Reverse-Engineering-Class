# Binary Reverse Engineering with Crackmes

This week is about building confidence in solving crackmes. The extraction password for each of these is `nmsu_re`.

These first three just want you to find the password. For your report, include the password and show your work by explaining how you solved them. Your explanation should include enough detail that someone else in the class could reproduce what you did. The first two you can probably solve with just uftrace and strings. The third, you may want to look at what is happening with either gdb or Ghidra.


ezcrackme1.zip [Download ezcrackme1.zip](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring23/Samples/binaries/ezcrackme1.zip)

ezcrackme2.zip [Download ezcrackme2.zip](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring23/Samples/binaries/ezcrackme2.zip)

ezcrackme3.zip [Download ezcrackme3.zip](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring23/Samples/binaries/ezcrackme3.zip)

Now, let's practice finding where to start in a crackme that involves several functions. Remember the strategies we have to find where to get started:

1. Identify the source and sink - where does execution start and where you want to get to?
2. Work backwards from the sink towards the source
3. Read functions from the end back to the beginning
4. Use C standard library functions to figure out what variables contain

You may also want to try out Ghidra's control flow graph functionality to map out where you want to go.

controlflow1-1.zip [Download controlflow1-1.zip(fixed)](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring23/Samples/binaries/controlflow1-1.zip) 

controlflow2-1.zip [Download controlflow2-1.zip(also fixed:)](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring23/Samples/binaries/controlflow2-1.zip)

controlflow3.zip [Download controlflow3.zip Grad-Level Students Only](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring23/Samples/binaries/controlflow3.zip)

For your report, show me a code block containing a keygen for each crackme. Then, show your work by describing what rules a valid key must follow to be accepted. (Your rules will be equivalent to a symbolic execution of the program targeting the successful outcome!)