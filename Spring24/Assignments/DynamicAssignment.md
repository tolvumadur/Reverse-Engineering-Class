# Basic Dynamic Analysis

Following the same format as week 1, analyze the malware in Labs 3-1 through 3-3.

Start with the static analysis tools we learned, then use dynamic analysis tools from Chapter 3 to learn more about the malware's behavior. Use the questions and answers from the book as clues for where to look. You can be confident your report is complete if it contains the information required to answer those questions and shows that you used tools from Chapter 1 and Chapter 3 to support your findings.

As usual, submit a link to your markdown report on GitHub

The online sandboxes mentioned in the textbook are no longer state-of-the-art. I recommend one that requires no login to submit samples to: hybrid-analysis.com

## "Fake Internet" Isolated Network Setup Instructions

To see the behavior of malware over the Internet, it can be helpful to let it successfully request things from the Internet. But, we don't want to let our malware loose on the real Internet. So we need a simulated version that is realistic enough to trick this malware. To do this, we will run another virtual machine with the [inetsim](https://www.inetsim.org/) tool. 

Create a second virtual machine running Linux and install inetsim. Also install net-tools. The versions in `apt` are fine:

```
sudo apt update
sudo apt install net-tools inetsim
```

Take your new Linux VM off of the internet at put it onto a VirtualBox internal network. From your VM's toolbar, choose Devices->Networking->Network settings and change the drop-down from (probably) "NAT" to "Internal Network". Take note of the name of the network ("intnet" by default).

Next, add a DHCP server to the internal network. I suggest the following settings:

```
vboxmanage dhcpserver add --enable --network "YOUR_INTERNAL_NETWORK_NAME_HERE" --upperip 10.0.0.30 --lowerip 10.0.0.20 --ip 10.0.0.3 --netmask 255.255.255.0
```

Now, reboot your guest Linux VM. This will trigger it to get a new address from the DHCP server (probably 10.0.0.20). You can see what addresses you have on Linux using the command `ifconfig` from net-tools. The command will show you all your networking interfaces. Your VM should have two -- one called `lo` that loops back to itself on IP 127.0.0.1, and the other is your connection to the internal network. If it shows an inet4 IPv4 address within the range that your DHCP server gives out, you got assigned an address!

*If you have trouble getting your DHCP server to work, your guest Linux VM will not get assigned an address. You can check on the DHCP server and the names of your internal networks with the commands:

```
vboxmanage list dhcpservers
vboxmanage list intnets 
```

Check that the DHCP server is attached to the network you expected and that your VM is using that internal network by name in VirtualBox Network Settings. Also verify that the DHCP server is enabled. You can remove DHCP servers and retry until you see what you expect.

 After your Linux VM guest has an IP address, you need to tell `inetsim` to use that address. Using sudo, edit the file located at /etc/inetsim/inetsim.conf  . On line 69, remove the `#` to uncomment the line and set the IP address to the IP address you got from your DHCP server. On line 207, remove the `#` to uncomment the line and set the IP address to the one you got from the DHCP server.  Then restart the inetsim service so it loads the new config values.

```
sudo service inetsim restart
```

When you set up your XP VM (see below), add it to the same internal VirtualBox network. In the control panel, set its DNS server to the IP address of the inetsim Linux VM and the gateway IP to the same address. The XP VM's IP address should be an unoccupied address in the range handed out by your DHCP server.

You know your setup is working if you can open up the Explorer web browser and visit a website over HTTP  and see the inetsim default file as the answer.

## XP VM Setup Instructions

We'll talk about this in class, but the malware crashes if we run it inside a Windows 10/7 VM, so we'll need an XP VM. The sandbox tool shows us this as well. Here are some instructions to get an XP VM going in VirtualBox: (Thanks to Simon Kim from NREL and [this blog post](https://helpdeskgeek.com/virtualization/how-to-set-up-a-windows-xp-virtual-machine-for-free/) for a source of an old XP VM). Get ready for some computing nostalgia!

Download a 32-bit XP machine from CNET [here](https://download.cnet.com/Windows-XP-Mode/3001-18513_4-77683344.html)

Using 7zip, open the EXE as `cab`, open `sources` directory, open `xpm` directory.

Select all and extract. Find `VirtualXPVHD` and rename to `VirtualXP.VHD`

Create a new VM in VirtualBox telling it it will hold a 32-bit XP Windows and set the hard drive to be that VirtualXP.VHD file. This will give the VM a hard drive with XP already installed on it, no need even to install from a ISO CD image. When loading the .VHD file you may need to set the loader to look for "all file types" to be able see the VirtualXP.VHD file. 

Set the network adapter to be of type `PCnet-FAST III` and connect to your internal network

Max out the video RAM (128MB)

Increase overall RAM from 0.5GB (if you want)

Boot and go through the setup steps. Hint: XP will let you set an empty administrator password :)

Install VirtualBox Tools so you can have a shared folder or clipboard.

Connect to the fake Internet. Check what IP address you got from DHCP with `ipconfig` in command prompt. Control Panel -> Network Settings -> TCP/IP Properties (It doesn't say IPv4 yet since that was the only option!) -> Set the gateway and DNS to your inetsim machine. Test you can resolve DNS names with `nslookup`. You can test inetsim is replying to http with Explorer. 

You will also need to find 32-bit versions of any tools you want to use on 32-bit XP that have 64 bit versions now. Here are some I've already found for you:

[Procmon](https://web.archive.org/web/20140627132742/http://download.sysinternals.com/files/ProcessMonitor.zip)

[Strings](https://download.cnet.com/Sysinternals-Strings/3001-2248_4-75115580.html)

[Wireshark](https://2.na.dl.wireshark.org/win32/all-versions/Wireshark-win32-1.10.14.exe)

Other things like regshot, PEID, Dependency Walker, PEView, etc. are just 32-bit. 

When you are happy with your setup, take a VM snapshot before you run any malware! 