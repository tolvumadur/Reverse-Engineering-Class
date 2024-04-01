# Dynamic Analysis

This week you will perform dynamic analysis of a RAT, a Remote Access Trojan. You will run this malware in your virtual machine, and analyze its behavior to quickly identify indicators of compromise that could be used to detect this malware in the wild.

The RAT you will be looking at will also come from the same place mentioned in Canvas for Assignment 2. It is called NjRAT. Watch out that there is a Win32.NjRAT version and a plain NjRAT version. We will use the latter.

## OSINT

OSINT stands for Open Source Intelligence, and for well-known malware there is plenty of OSINT available.

Start your report this week by summarizing what others have already written about NjRAT. A good place to start is [Wikipedia](https://en.wikipedia.org/wiki/NjRAT) and its reference list. Include at least a paragraph about when NjRAT first appeared, and where it has been seen or used since. Cite your sources by including a URL to them. 

Each fact you state must be cited. For this assignment, the Wikipedia page is not allowed as a source to encourage you to look further.

## RegShot

Use RegShot to take a snapshot of the registry.

Also take a snapshot of your VM, because you are about to run a RAT. Double-check your network is disabled. Then run NjRAT for a bit, take a new snapshot, and compare it with the first using RegShot.

**Note in your report the answers to these questions:**
- What registry keys changed? 
- What was added? 
- Does this appear to be for persistence, or something else?
- What clues (Indicators of Compromise) could someone look for in the registry to detect an NjRAT infection?

### File functionality of RegShot

RegShot allows you to take snapshots of directories as well. Identify at least one file or directory created or altered by NjRAT when it runs. You may need to revert to your pre-RAT VM snapshot to check several directories to find a change.

**Note in your report the answers to these questions:** 
- What files or directories did you see changed?
- Does this appear to be for persistence, or something else?
- What clues (Indicators of Compromise) could someone look for in their filesystem to detect an NjRAT infection?

## FakeNet

Revert to a pre-NjRAT VM snapshot, and turn on FakeNet. Run NjRAT again, and watch the logs to see NjRAT's behavior on the network.

**Note in your report the answers to these questions:** 
- What did NjRAT do on the network?
- What DNS names did it look up?
- What protocol did it use to try to contact its command and control network?
- What indicators of compromise could a network administrator look for to identify if any of their machines are infected with this same malware?

