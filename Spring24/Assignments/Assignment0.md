# Week 0: Reverse Engineering Lab Setup and Lab Safety

Just like a chemistry lab would teach you to properly use tools like [calorimeters](https://pubs.acs.org/doi/pdf/10.1021/ed062p902), and handle dangerous [chemicals](https://emergency.cdc.gov/agent/hydrofluoricacid/basics/facts.asp), reverse engineers must also take safety precautions when working with malware. The malware samples we will be studying should not require as strict of precautions as we are taking -- we think ;). If you work on reverse engineering malware without precautions, you endanger yourself, others on your network, and potentially other computers connected to the Internet. Failure to follow basic safety precautions is more than an accident, it is negligence.

## System Isolation

In this course, you will be statically and dynamically analyzing malware. This means that you will actually run the malware, or parts of the malware. It is essential that this malware be isolated. The main technique reverse engineers use to protect ourselves and others is isolation. We isolate the malware from interacting with the hardware of our actual computer by analyzing it inside a virtual machine. We will be extra careful in this course and investigate these malware samples targeting Windows on virtual machines running on a Linux-based hypervisor. 

## Network Isolation

To further prevent our malware from escaping, we will eliminate the networking capabilities of the victim Windows virtual machine. From within our hypervisor, we will disable any network interfaces the virtual machine might use. This means you will use the host OS to do any googling or downloading and then use the hypervisor to place any files onto the virtual machine.

## System Setup

Start with a Unix-based OS like Linux or MacOS. If you usually use a Windows machine, you will need to enable dual booting. If you don't want to lose secure boot or Bitlocker, you can also create a live flash drive with persistent storage to boot your laptop into Linux. You can give yourself more hard drive space by shrinking your main C: drive volume and creating some blank space that can be formatted into another filesystem. 

### Hardware Assistance

If you experience hardware challenges, we can also look into getting you set up on an ESXI machine available thanks to generous support from Fordham University, the NSA, and the NSF. Talk to Dr. Reynolds to get an account set up. Also talk to the COG staff to get a VMWare student license to connect to your account on our ESXi server.

### Getting a Windows 11 VM

Install a type-2 hypervisor of your choice. 
If you want to use VMWare tooling, contact the COG staff to get a student account.

Download a Windows 11 ISO [here](https://www.microsoft.com/en-us/software-download/windows11). Use it to create a new virtual machine and install the OS. Create a local-authentication account, rather than using a Microsoft account. Tell Windows you will add a license key later.

*If you downloading from a Windows machine, you might find it easier to change your HTTP User-Agent to avoid needing to use the Microsoft download tool. For example, you can emulate an Android device in Chrome's developer console and get the regular download page.*

## Virtual Machine Snapshots

Before you begin any reverse engineering work, I recommend taking a [snapshot](https://www.pugetsystems.com/support/guides/virtualbox-4-using-snapshots-1914/) of your virtual machine. Then you can revert back to that snapshot where no malware has ever been run on the system. Snapshots can be large, however, so you should be strategic about when you use them--especially if you have limited hard drive space. 

## Disabling Windows Defender

*These instructions were tested with Windows 11 23H2*

Once upon a time, it was important to have an antivirus system on your Windows machines. However, Windows Defender has grown to be quite effective in detecting and removing malware. So effective, in fact, that when you load in malware to analyze in this class it will often be quarantined and deleted within a few seconds. Your first job is to disable it.

### Motivation

Windows 11 does not want you to remove Windows Defender, or turn it off.
You are working at a disadvantage in Windows because you won't have the level of control you might be used to with a root account on *NIX systems.

Windows defender is a complex distributed system, built of many interoperating components. It can be temporarily be turned off quite easily, but getting it off long-term is quite difficult. Some of these components are designed to detect and block malware when it tries to disable Windows Defender. If you think about it, we are doing exactly what malware would want to do!

### Disabling Windows Defender





## Removing Networking Capabilities

Use your hypervisor's menus to remove all network connectivity for the virtual machine. Take a snapshot.

## What to turn in and how

Throughout this course, you will turn in every project as a markdown Links to an external site.file, checked into a GitHub repo. You will turn in a URL linking to your repo. If you name your markdown file README.md, it will show up as the default description for the repo on GitHub.

The exercises from the textbook are not secrets, and you can keep these analysis reports as a portfolio to show to future potential employers tangible evidence of preparation for an entry level RE job. Please do not share any personal information in these public repositories. You also have the option of making a private repo on GitHub, and giving read access to my GitHub user: jr-nm

No malware is to be checked into this repo, and any script snippets you want to add to describe your reverse engineering strategies must be put into a markdown code block.

For this project, your markdown file is:

- A big title line, saying this is CS479/579 Reverse Engineering at NMSU
- A summary section, explaining that this repo (will) hold your reports on reverse engineering malware samples from "Practical Malware Analysis"
- A system setup section, describing in professional prose:
- How you set up your reverse engineering system, using system isolation and network isolation
- Why you are using isolation
- Which tools you installed on the victim machine for analysis, and what they are for (you may add to this list as the semester progresses)

*Why markdown? It can be easily incorporated into a blog post later, but is text-based so git deltas can reveal version changes better than in blobs like pdf's or blogs. There are other formats that fit this description, but we chose a single one for consistency.*