# Week 0: Reverse Engineering Lab Setup and Lab Safety

## TL;DR

- On a *NIX machine, create a Windows 11 VM.
- Disable Windows Defender and install Flare-VM.
- Install Visual Studio.
- Install IDA Pro Education using the link in Canvas.
- Disable Networking.
- Take a snapshot.
- Turn in a link to a github repo that will become your portfolio.
    - commit a README.md describing your setup steps.

## Lab Safety

Just like a chemistry lab would teach you to properly use tools like [calorimeters](https://pubs.acs.org/doi/pdf/10.1021/ed062p902), and handle dangerous [chemicals](https://emergency.cdc.gov/agent/hydrofluoricacid/basics/facts.asp), reverse engineers must also take safety precautions when working with malware. The malware samples we will be studying should not require as strict of precautions as we are taking -- we think ;). If you work on reverse engineering malware without precautions, you endanger yourself, others on your network, and potentially other computers connected to the Internet. Failure to follow basic safety precautions is more than an accident, it is negligence.

## System Isolation

In this course, you will be statically and dynamically analyzing malware. This means that you will actually run the malware, or parts of the malware. It is essential that this malware be isolated. The main technique reverse engineers use to protect ourselves and others is isolation. We isolate the malware from interacting with the hardware of our actual computer by analyzing it inside a virtual machine. 

We will be extra careful in this course and investigate these malware samples *targeting Windows* on virtual machines running on a *\*NIX-based hypervisor*. If it accidentally escapes our isolation, it is unlikely to *also* work in the hypervisor host OS.

Environments that provide various degrees of isolation are often called "*Sandboxes*", meaning a safe playground. Large, complex sandboxes are often called "*test ranges*" after military weapons testing/practice areas.

## Network Isolation

To further prevent our malware from escaping, we will eliminate the networking capabilities of the victim Windows virtual machine. From within our hypervisor, we will disable any network interfaces the virtual machine might use. This means you will use the host OS to do any googling or downloading and then use the hypervisor to place any files onto the virtual machine. Apply network isolation *after* installing all the tools we will use and *before* placing any malware on your analysis VM.

## System Setup

Start with a Unix-based OS like Linux or MacOS. If you usually use a Windows machine, you will need to enable dual booting. If you don't want to lose secure boot or Bitlocker, you can also create a live flash drive with persistent storage to boot your laptop into Linux. You can give yourself more hard drive space by shrinking your main C: drive volume and creating some raw space that can be partitioned into another filesystem. 

Install a type-2 hypervisor of your choice.  If you want to use VMWare tooling, contact the COG staff to get a student account. There are several hypervisor tools, many open source. VMWare is a paid product that donates free limited-length licenses to the CS Department.

### Hardware Assistance - Department-Hosted VM

If you experience hardware challenges, we can also look into getting you set up on an ESXI machine available thanks to generous support from Fordham University, the NSA, and the NSF. Talk to Dr. Reynolds to get an account set up. Also talk to the COG staff to get a VMWare student license to connect to your account on our ESXi server.

### Getting a Windows 11 VM

Download a Windows 11 VM [here](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/) or an ISO to create your own [here](https://www.microsoft.com/en-us/software-download/windows11). 

*If you create your own installation, create a local-authentication account, rather than using a Microsoft account. Tell Windows you will add a license key later.*

## Virtual Machine Snapshots

Before you begin any reverse engineering work, I recommend taking a [snapshot](https://www.pugetsystems.com/support/guides/virtualbox-4-using-snapshots-1914/) of your virtual machine. Then you can revert back to that snapshot where no malware has ever been run on the system. Snapshots can be large, however, so you should be strategic about when you use them--especially if you have limited hard drive space. 

## Installing an IDE & C/C++ Compiler

Follow [Microsoft's instructions](https://learn.microsoft.com/en-us/cpp/build/vscpp-step-0-installation?view=msvc-170) to install Visual Studio with a C compiler.

### Optional Tools

Some optional tools that may be nice-to-have, but are not specifically required would be:

- WSL2
- VSCode or another IDE
    - If you use VSCode, turn off telemetry

## Installing IDA Education

Thanks to the generous support of HexRays, we have educational licenses to IDA's pro features for the duration of this course. IDA is the leading paid binary reverse engineering tool, with support for many types of microprocessors. It's interface is mature and it has many quality-of-life features. In this class you will get to try both IDA and the NSA's open-source Ghidra competitor and decide which you prefer.

Dr. Reynolds will distribute the download link and license key in Canvas, so it doesn't leak. We only have a limited number of seats we can use.

## Disabling Windows Defender

*These instructions were tested with Windows 11 23H2*

Once upon a time, it was important to have an antivirus system on your Windows machines. However, Windows Defender has grown to be quite effective in detecting and removing malware. So effective, in fact, that when you load in malware to analyze in this class it will often be quarantined and deleted within a few seconds. Your first job is to disable it.

### Motivation for Disabling Windows Defender

Windows Defender will often detect the malware you are working on and delete it, quarantine it, and/or send a copy to Microsoft. Leaking this information to a third party is a breach of trust because the virus may contain company-specific secrets/keys/PII. Having your malware deleted while you are trying to analyze it is a more obvious problem.

Windows 11 does not want you to remove Windows Defender, or turn it off.
You are working at a disadvantage in Windows because you won't have the level of control you might be used to with a root account on *NIX systems.

Windows defender is a complex distributed system, built of many interoperating components. It can be temporarily be turned off quite easily, but getting it off long-term is quite difficult. Some of these components are designed to detect and block malware when it tries to disable Windows Defender. If you think about it, we are doing exactly what malware would want to do!

Windows Defender runs several programs designed to watch for tampering with the antivirus system and its various telemetry systems. If you delete `defender.exe` you will either be blocked or it will reappear. To make a long-term change to disable Windows defender, you must edit the Windows Registry, a database of Windows configuration settings.

## Permanent Disabling of Windows Defender

Thanks to these resources for the methods:
- [1](https://www.elevenforum.com/t/how-to-properly-disable-win-defender-on-win11-22h2.16755/)
- [2](https://woshub.com/disable-windows-defender-antivirus/)

However, Windows Defender is also watching for and blocking changes to the registry that would disable it. So you must boot Windows into minimal safe mode to make your changes. Boot into recovery mode, and boot in minimal safe mode. Then open an administrator powershell command prompt and enter the following commands:

Make the following registry edits to prevent any of Windows Defender's services from ever starting:
```
reg add "HKLM\System\CurrentControlSet\Services\WdFilter" /v "Start" /t REG_DWORD /d "4" /f
reg add "HKLM\System\CurrentControlSet\Services\WdNisDrv" /v "Start" /t REG_DWORD /d "4" /f
reg add "HKLM\System\CurrentControlSet\Services\WdNisSvc" /v "Start" /t REG_DWORD /d "4" /f
reg add "HKLM\System\CurrentControlSet\Services\WinDefend" /v "Start" /t REG_DWORD /d "4" /f
reg add "HKLM\System\CurrentControlSet\Services\Sense" /v "Start" /t REG_DWORD /d "4" /f
reg add "HKLM\System\CurrentControlSet\Services\WdBoot" /v "Start" /t REG_DWORD /d "4" /f
```

Then boot back into normal mode. Run `taskschd.msc` as an administrator and disable the following tasks under `Microsoft` --> `Windows`--> `Windows Defender`:

- Windows Defender Cache Maintenance
- Windows Defender Cleanup
- Windows Defender Scheduled Scan
- Windows Defender Verification

Reboot.Verify that Windows Defender has been disabled in settings. Reboot and verify that Windows Defender has not re-enabled itself.

## Installing Flare-VM

Mandiant (recently acquired by Google) maintains a "package manager" for Reverse Engineering full of all sorts of useful tools. It is called [Flare-VM](https://www.mandiant.com/resources/blog/flare-vm-the-windows-malware) and is published on [GitHub](https://github.com/mandiant/flare-vm). Follow the instructions to install Flare-VM with the default set of tools.

A prerequisite of installing Flare-VM is that Windows Defender is disabled.
The tools installed by Flare-VM are useful, but nobody can guarantee that some of them don't contain malware. Hold off on using them until you've installed everything and have disconnected the network.

## Removing Networking Capabilities

After everything you needed to install is downloaded, use your hypervisor's menus to remove all network connectivity for the virtual machine. Take a snapshot.

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
- How you disabled Windows Defender
- Which tools you installed on the victim machine for analysis, and what they are for (you may add to this list as the semester progresses)


*Why markdown? It can be easily incorporated into a blog post later, but is text-based so git deltas can reveal version changes better than in blobs like pdf's or blogs. There are other formats that fit this description, but we chose a single one for consistency.*
