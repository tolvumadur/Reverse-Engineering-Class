# Shellcode Creation (Golf)

We learned last week about one way that malware injects code into running processes. But what code will it inject?

Often times it will be some type of shellcode. Shellcode allows the attacker to run any terminal command they want to. It is often used in combination with a network service that allows the attacker to run these commands over the Internet. This is called a reverse shell.

In this lab, you will experiment with creating your own Linux shellcode in x86_64 assembly. Here is a Makefile that will turn assembly code into just the bytes containing those instructions in machine code:

```
 all: shellcode.S
    as shellcode.S -o shellcode.o
    ld shellcode.o -o shellcode --oformat=binary
    rm shellcode.o
```

### The Challenge:

Use the [syscall instruction](https://stackoverflow.com/questions/2535989/what-are-the-calling-conventions-for-unix-linux-system-calls-and-user-space-f) to ask the [OS](https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md#x86_64-64_bit) to execute (using [execve](https://man7.org/linux/man-pages/man2/execve.2.html)) the shell at [/bin/sh](https://stackoverflow.com/questions/5725296/difference-between-sh-and-bash)

### Testing Your Work:

You can test your shellcode using this test code. To allow this code to run your shellcode from on the stack and to make debugging easier, compile with the GCC flags:

```
gcc shellcode_tester.c -o shellcode_test -z execstack -no-pie
```

#### shellcode_tester.c

```
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define SHELLCODE_PATH "/YOUR/PATH/HERE"

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

### Debugging:

Debugging shellcode is tricky, when you start executing code off the stack GDB gets confused and some of its convenience functions go away. We'll practice debugging in class.

### Golf:

Sometimes, code injection must fit into a small buffer. As a fun challenge, once you have a working shellcode, see how much smaller you can make it. Can you make it work in less than 50 bytes? Less than 40? 30? (The one I wrote to prep for teaching this is 35 bytes long - can you beat that?).

### Graduate Extension:

Often times injection requires that shellcode contain no NULL bytes. Your shellcode must contain no null bytes. This will require a bit of extra cleverness, since you need some null values to get this to work.

### Submit:

1. A code block containing your assembly instructions for your shellcode
2. A step-by-step explanation of your assembly code and how it sets up the system call
Report how many bytes total are in your assembly, and include the whole thing in ascii
3. The easiest way to get this information is probably with a quick python script 
Example: My shellcode is 35 bytes long. Here they are: -- 4A FE 56 08 ...
4. (Grad Students only, explain what you did to ensure there were no NULL bytes in your code)
