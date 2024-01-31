# Basic Static Analysis Part 2

This week we will be handling malware for the first time. 
Remember to use network and system isolation to protect against accidentally running the malware.

# Malware for this week:

Making malware publicly available may be fraught with legal consequences. See Canvas for directions to the malware for this week.

# Writing an RE report

When reporting on analysis of a piece of malware, there are several pieces of information it is standard to include, to the best of your ability. When you write your report this week, please include each of these categories. At the top, provide an executive summary that summarizes the most actionable information in just a few sentences. 

## Type of Malware

Categorize the malware based on what it does and how it works:

#### What kind of malware does this seem to be? 
- What OS(es) does it target?
- Is it a virus or worm?
- Is it a dropper, loader, payload, etc.?
- Is it a botnet client, crypto-miner, RAT, keylogger, combination of things, etc.?

## Signatures

Signatures help people recognize if they have the same malware. If every byte is exactly the same, the result of a cryptographic hash like SHA-256 (or weaker hashes like MD5) will match. At minumum, you should report the hash of the file. This will also allow you to look up the malware in services like VirusTotal.

**YARA** ("Yet Another Recursive Algorithm") rules allow you to write a signature that is a bit more flexible so that you can recognize patterns within malware -- even if some bytes have changed.

## Indicators of Compromise

What clues could a system administrator look for to check if this malware has already infected their system?

#### How can this malware be recognized?
- Is there a file that gets created?
- Is a registry key changed?
- Is there a particular IP address or hostname it will contact?
- Will it open a port?
- Will it connect to a VPN or Wireguard?

## Clues about Origin

What clues are there about who maybe created this malware?
Clues could be false leads, or accidental inclusions.
Examples might be jokes that only make sense in a specific language, praise for a specific government leader, or calls for attacks against specific ethnic minorities from specific regions.

#### Where does this malware come from? 
- Is it similar to other malware from a specific threat actor?
- Does it have filenames or strings that are similar to other malware?
- Where was it found?
- What is the C2 (command and control) infrastructure

## Graduate Extension: (YARA)[https://yara.readthedocs.io/en/stable/] Rule

This section is only required for graduate students. It is helpful to share any YARA rules you may have created that detect this malware.

#### Rule

Give a YARA rule that would detect this malware in a code block. Write a couple of sentences about whether you think this rule will generate false positives, and why.