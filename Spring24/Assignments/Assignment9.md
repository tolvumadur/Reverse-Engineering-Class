# Malware Behavior

## Building an Anti-Virus Program

Last week, you performed some dynamic analysis of njRAT. This week, you will create a simple antivirus program to eliminate it. You may create this program using any language or framework you wish, but it must ultimately be packaged as a PE (.exe).

## Requirements

- Must have a GUI.
    - The GUI must include a `Scan` button to scan for njRAT that reports:
        - Whether indicators of compromise exist in the filesystem to suggest njRAT has been run
        - Whether njRAT is currently running 
    - The GUI must include a `Remove` button that triggers:
        - Ending the processes spawned by njRAT.
        - Removing files in `C:\` added by njRAT
        - Reporting an error if this version of njRAT is not running

## What to Submit

This week, submit a link to a short report explaining how your A/V system detects and removes this version of njRAT, as well as a link to a directory in your GIT repo that contains:

1) The source code of your antivirus

2) A functional .exe

3) A screen recording (e.g. taken with a tool such as OBS) demonstrating its functionality.


