#!/usr/bin/env python3

with open("shellcode", "rb") as f:
    a = f.read()
    print(f"Generated shellcode is of length: {len(a)}")
    print(a.hex())
    print((a.replace(b"\0", b"")))


