# Control Flow Integrity Violation

TLDR: Write a python script using `pwntools` that executes the given program, leaks the stack offset, and spawns a shell. For your report, submit your code with an explanation of (1) how you designed it and (2) what it is doing

We've learned about library injection, using a loader program to force another program into loading a library in a new thread. You've also created shellcode. There is a more direct method of injecting shellcode into vulnerable processes. The method involves giving unexpected input to a program that ends up altering what is in the instruction pointer register. With control of the IP register, attackers can make the program do whatever they want. There are many ways of doing this, but we will start with one of the oldest and simplest for this assignment: a buffer overflow.

Remember that the stack grows from large addresses towards smaller ones. However, arrays and strings are read from low addresses to high addresses. When a programmer allows more data to be written to a buffer than that buffer can hold, it will start overwriting things *higher* on the stack. This obviously will cause undefined behavior or segmentation faults. Attackers can make that undefined behavior into something useful.

One of the entries stored higher on the stack is the return address where the current function will return to once it finishes running the current function and reaches a RET instruction. Attackers' goal in a buffer overflow is to overwrite that return address, because they know it will get loaded into the IP register!

From there, there are several techniques, but we are going to practice the simplest. It works by injecting shellcode also into the buffer, and making sure that the IP register gets pointed to the first address in that shellcode. Then, just like in the shellcode tester from last assignment, the shellcode will get executed by the program, calling execve and replacing the current program with a shell the attacker can use.

To pull this off we need 3 things:

1. We need to find out how many bytes after the beginning of the buffer are there before the return address.
2. We need to inject padding bytes plus a new return address, plus some shellcode.
3. We need to be able to predict at what address our shellcode will be so we can return to it.

Fortunately, there are tools that already exist to make this job much easier. We will practice with them in class. If you want to see an example of someone else doing a buffer overflow in 64-bit, try [this article](https://medium.com/@two06/solving-a-simple-buffer-overflow-with-pwntools-575a37e4ddb1).

## How to get started:

Install [pwntools](https://docs.pwntools.com/en/stable/) for python and download the victim program: [pizza](#ref?).

Run the program to see how it works. Can you get it to crash? Can you use format strings to make something strange happen?

Open it in Ghidra to really see how it works (and what library functions it is using). You may also want to run the program in GDB.

Use pwntools to create a script to run the program, get it to crash (segfault), and analyze the core dump. 

pwntools script we started from in class:

```
#!/usr/bin/env python3

from pwn import *

#context.log_level = 'error'

# Executable and Linkable Format
elf = ELF("./pizza")

context(arch='amd64', os='linux', endian='little', word_size=64)

#getname_address = elf.symbols["getname"]

#shellcode = asm(shellcraft.amd64.linux.sh())

#print(f"Shellcode: {shellcode.hex().upper()}")
#print(len(shellcode)

input1 = b"Cantinflas"

victim = process("./pizza")
#print(str(victim.recvline(), "latin-1"))
#victim.recvline()
#victim.sendline(b"10")

#victim.sendline(payload)
#victim.wait()
victim.interactive()
#core = victim.corefile
#rsp = core.rsp
#rbp = core.rbp
#rip = core.rip
```

## Report

For your report, submit (0) your code with an explanation of (1) how you designed it and (2) what it is doing.