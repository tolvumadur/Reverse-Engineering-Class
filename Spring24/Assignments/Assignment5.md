# Reverse Engineering Ransomware

A very relevant challenge for today's reverse engineers is figuring out how to stop ransomware. A large company, organization, or government entity stands to lose millions or billions of dollars if their data is encrypted and they cannot recover it. Reverse engineers who figure out a way to undo ransomware without paying the ransom are heroes.

[![Watch the video](https://img.youtube.com/vi/DdVC1eVfZUI/default.jpg)](https://youtu.be/DdVC1eVfZUI)

Of course, with a modern block cipher, you won't be able to decrypt any files without finding the key. However, the ransomware needs the key to be able to encrypt things, so sometimes dynamic analysis can uncover the key. If the malware authors were very unsophisticated, the key may be stored within the ransomware program, itself. We'll watch this example in class of a reverse engineer breaking down an ESXI ransomware - and see where the malware authors were careful, and where they were not:

In the case of these examples, the malware writers were lazy and did not use a sophisticated encryption scheme and did not hide the key very well. Your job is to write a program which can decrypt the two encrypted files in each of these samples. The ransomware program is included - and contains enough information for you to reverse engineer how to decrypt files.

For your report, submit your decryption program, along with the decrypted secret.txt file. Show your work by showing a screenshot of the decryption function in Ghidra updated with human-readable labels. Explain how your decryption works.

ransomware1.zip [Download ransomware1.zip](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring23/Samples/binaries/ransomware1.zip) 

ransomware2.zip [Download ransomware2.zip](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring23/Samples/binaries/ransomware2.zip) 

ransomware3.zip [Download ransomware3.zip(Required for grad students only)](https://github.com/tolvumadur/Reverse-Engineering-Class/blob/main/Spring23/Samples/binaries/ransomware3.zip)

The extraction password for these samples is `nmsu_re`

**As decided at the end of class, although there exists a clever way to reuse the decryption program for any file, everyone is expected to have reverse engineered ransomware1. If you kept up with us in class, you only need to write a decryption program. You may use the clever way for ransomware2 as long as it is bundled nicely into a script to automate the process of decryption. Grad students, you also need to RE ransomware2 or ransomware3 using what we learned in class.**