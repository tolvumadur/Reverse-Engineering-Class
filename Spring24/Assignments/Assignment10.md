# Windows Crackme (Unused this semester)

This week, we will be solving a Windows crackme. You may want to pick up a windows debugging tool like [OllyDBG](https://www.ollydbg.de/) or [WinDBG](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/debugger-download-tools). For your reports, I would like to see evidence of you getting to know Windows library functions and types. You will often find yourself googling something like:

mdsn <WindowsThingHere>
This week, I want to see you using the decompiler window's capabilities to give names to variables and functions, and retype things as appropriate. I am expecting at least 4 screenshots of the decompiler window showing that you have done that.

This assignment goes along with Chapter 6 of the textbook, which describes at a high level what Ghidra is doing to recognize what C-code was likely used to create the binary.

[Crackme Link](http://crackmes.cf/users/hmx0101/decryptme_1/download/Decryptme%231.zip) (extraction password: `crackmes.de`)

## Example Report:
 
## Week 6 - Windows Crackme
This week we worked on a Windows crackme... (Summary for the week)

### Windows Functions/Types I Learned:
- LPCSTR a constant character pointer, pointing to a null-terminated string of 8-bit chars to be interpreted according to Windows' 

- HINSTANCE a handle for a ...

- GetMessageA() a function for retrieving a message from a...

- CreateFontA() creates a font for use in displaying some text

- MSG a struct representing...

... and so on ...

### How the crackme tests passwords:
When you type the password and click the `Check` button, this validation function gets called. In my screenshot here, I have made the function easier to understand by correcting some types and giving meaningful names to variables and functions:

Awesome Screenshot

I had to find a number that, when I put it in the box, would correctly decrypt the message. I found the number ___________ works by doing __________. Here is how I worked that out step-by-step:

 

Along the way, I also explored the structure and function of this program to familiarize myself with a GUI-based Windows EXE. Here is the decompiled function where the original 

Another Screenshot

Here is the code that restricts me to typing only numbers...

Another Screenshot

And here is _________

Another Screenshot

 (you need at least 4 total)
 