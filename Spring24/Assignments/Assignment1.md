# Assembly Review

This week, we will review x86 assembly in class. Our eventual goal is to work backwards from machine code to assembly, and then back to some source code that could have generated the binary.

For this review assignment, you will need a *NIX environment and the GCC C-compiler.

We will have a small refresher of assembly programming while building a tool attackers often use when taking over a program, shellcode. Our goal will be to use the linux system call `exec` to replace the currently running process with a terminal shell like `/bin/sh`.

Hang onto this shellcode, because we will use it again at the end of the course when we learn about control flow integrity attacks.

## TL;DR

Write some 64-bit x86 Linux shellcode, assemble it to binary, and test that it works with the provided tester. Grad students' shellcode must not contain any null bytes.

Submit a link to a directory within your portfolio git repo that contains at least your shellcode and a report that explains, line by line, how it works. See `Submit` section for full requirements.

### The Challenge:

Use the [syscall instruction](https://stackoverflow.com/questions/2535989/what-are-the-calling-conventions-for-unix-linux-system-calls-and-user-space-f) to ask the [OS](https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md#x86_64-64_bit) to execute (using [execve](https://man7.org/linux/man-pages/man2/execve.2.html)) the shell at [/bin/sh](https://stackoverflow.com/questions/5725296/difference-between-sh-and-bash)


### Given Files:

The following files are given to help you get started.

#### shellcode.S
Your shellcode must go into a file called: "shellcode.S" 

```
.text
.global _start
_start:
    #Your Code Here
    #...
    #...
    #...
```

#### Makefile

This makefile passes in compiler options to disable control-flow-integrity protections that would normally prevent us executing some random buffer as if it were code. It will also run the shellcode inspection script. It does not currently run the shellcode_test program, but you may want to modify it so it does so.

```
all: shellcode.S shellcode_tester.c
	gcc shellcode_tester.c -o shellcode_test -z execstack -no-pie
	as shellcode.S -o shellcode.o
	ld shellcode.o -o shellcode --oformat=binary
	rm shellcode.o
	python3 x_shellcode.py
```

#### shellcode_tester.c

Compile this file to get a testing program for your shellcode. What it will do is load your shellcode into memory, and then jump to executing it. 

*The path to your assembled binary is hard-coded so be sure to fill it in below:*
```
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define SHELLCODE_PATH "/path/to/your/shellcode/here"

int main(int argc, char** argv) {

    char exec_me[200];
    int bytes_read;
    FILE * shellcode_file;
    void* foo;

    shellcode_file = fopen(SHELLCODE_PATH, "rb");

    if (shellcode_file == NULL) {
        printf("Error opening file %s: %ld\n", SHELLCODE_PATH, (long) shellcode_file);
        return 2;
    }

    bytes_read = fread(exec_me, 1, 200, shellcode_file);

    printf("Shellcode length: %ld\n", ftell(shellcode_file));

    if (!bytes_read) {
        printf("Error: %d bytes read in shellcode file %s\n", bytes_read, SHELLCODE_PATH);
        return 1;
    }

    pclose(shellcode_file);

    foo = ((void*(*)()) exec_me)();

    return 0;
}
```

#### x_shellcode.py

A helpful function for examining your shellcode:

```
#!/usr/bin/env python3

with open("shellcode", "rb") as f:
    a = f.read()
    print(f"Generated shellcode is of length: {len(a)}")
    print(a.hex())
    if b"\0" in a:
        print("Warning: shellcode may not copy properly, it contains null bytes!")
```

### Debugging:

Debugging shellcode is tricky, when you start executing code off the stack GDB gets confused and some of its convenience functions go away. We'll practice debugging in class.

[GDB Command Cheat Sheet](https://darkdust.net/files/GDB%20Cheat%20Sheet.pdf)

#### examine what the instruction RIP is pointing at, and the next two after it:
```
x/3i $rip
```

#### set a breakpoint at a specific memory address. In this case address 0x401300
```
b *0x401300
```


### Golf:

Sometimes, code injection must fit into a small buffer. As a fun challenge, once you have a working shellcode, see how much smaller you can make it. Can you make it work in less than 50 bytes? Less than 40? 30? (The one I wrote to prep for teaching this is 35 bytes long - can you beat that?).

### Graduate Extension:

Often times injection requires that shellcode contain no NULL bytes. Your shellcode must contain no null bytes. This will require a bit of extra cleverness, since you need some null values to get this to work.

### Submit:

Just like the first week, submit a markdown report with a title, summary, and:

1. A code block containing your assembly instructions for your shellcode
2. A step-by-step explanation of your assembly code and how it sets up the system call
Report how many bytes total are in your assembly, and include the whole thing in ascii
3. The easiest way to get this information is probably with a quick python script 
Example: My shellcode is 35 bytes long. Here they are: -- 4A FE 56 08 ...
4. (Grad Students only, explain what you did to ensure there were no NULL bytes in your code)
