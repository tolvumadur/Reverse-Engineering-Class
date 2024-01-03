# Week 1 - Simple Static Analysis

This week we learned about file hashes as tools for recognizing malware samples identical to those seen by others in the past. We also learned about how to submit to Google's VirusTotal tool to see the results of scanning a file with dozens of different antivirus tools. We learned how to use `strings` to find Unicode and ASCII strings within a binary. We learned how to use PEiD to check if a binary is packed to hide its contents. We also learned how to see what Windows system tools a portable executable uses including libraries that get dynamically linked and which functions are imported.

---
# Lab 1-1 

## Executive Summary

These files appear to be malware, and they appear to engage in some kind of filesystem manipulation. We have so far not found what they do, but there are indications that it hides a `kerne1.dll` file in the `system32` directory.

## Indicators of Compromise

**Compilation Date (presumed):** DEC 2010

**MD5 Hash (EXE):** bb7425b82141a1c0f7d60e5106676bb1 

**MD5 Hash (DLL):** 290934c61de9176ad682ffdd65f0a669  

**File to look for:** `C:\windows\system32\kerne132.dll`

## Mitigations

- Delete files that match this file's hash! 
- Scan Windows machines for `system32\kerne132.dll`

## Evidence

This malware consisted of two components, a portable executable (EXE) and a dynamically linked library (DLL). Submitting either to VirusTotal sets off dozens of vendors' virus classifiers.

Using `strings` on the `.EXE`, we find the message string "`WARNING_THIS_WILL_DESTROY_YOUR_MACHINE`", and some references to several file manipulation functions. We also see the suspicious string "`C:\windows\system32\kerne132.dll`", which replaces the `l` in kernel with a `1`. Such a file is not present in Windows by default, so it's presence could be an indicator of compromise.

Using `strings` on the `.DLL` did not yield anything useful.

Opening these files with PEview, we see that they both claim to have been compiled in late 2010. This matches what VirusTotal reported, but VirusTotal only saw samples appear in mid-2012.

Using DependencyWalker on the `.EXE`, we can see which functions are imported from various other DLLs. Two of these which are particularly notable are `CreateProcess` and `Sleep`. The `Practical Malware Analysis` textbook teaches us that these functions can be combined to create a backdoor for running this malware. *(You would really only find this if you read the solutions at the back of the book, which is fair game.)*

---
# Lab 1-2

## Executive Summary
## Indicators of Compromise
## Mitigations
## Evidence

---
# Lab 1-3

## Executive Summary
## Indicators of Compromise
## Mitigations
## Evidence

---
# Lab 1-4

## Executive Summary
## Indicators of Compromise
## Mitigations
## Evidence

