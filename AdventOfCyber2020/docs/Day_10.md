# Day 10. `[Networking]` Don't be sELFish
## Intro
>The Best Festival Company (TBFC) has since upscaled its IT infrastructure after last year's attack for all the other elves to use, including a VPN server and a few other services. You breathe a sigh of relief..."That's it, Me, Elf McEager saved the Christmas of 2020! I can't wait to---"
>
>*But suddenly, a cold shiver runs down your spine, interrupting your monologue...*
>
>You suddenly recall that Elf McSkidy had set up a Samba file server just before the attack occurred - could this have been hacked too?!  What about our data...Oh no, quick! Find out what usernames may have been leaked and attempt to login to the server yourself, noting down any vulnerabilities found to report back to Elf McSkidy.

## Tasks

### 1. Using enum4linux, how many users are there on the Samba server (`10.10.000.000`)? `[*]`

`enum4linux -U 10.10.146.89`
```
Starting enum4linux v0.8.9 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Mon Mar 22 13:30:20 2021

 ========================== 
|    Target Information    |
 ========================== 
Target ........... 10.10.146.89
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ==================================================== 
|    Enumerating Workgroup/Domain on 10.10.146.89    |
 ==================================================== 
[+] Got domain/workgroup name: TBFC-SMB-01

 ===================================== 
|    Session Check on 10.10.146.89    |
 ===================================== 
[+] Server 10.10.146.89 allows sessions using username '', password ''

 =========================================== 
|    Getting domain SID for 10.10.146.89    |
 =========================================== 
Domain Name: TBFC-SMB-01
Domain Sid: (NULL SID)
[+] Can't determine if host is part of domain or part of a workgroup

 ============================= 
|    Users on 10.10.146.89    |
 ============================= 
index: 0x1 RID: 0x3e8 acb: 0x00000010 Account: elfmcskidy	    Name: 	Desc: 
index: 0x2 RID: 0x3ea acb: 0x00000010 Account: elfmceager	    Name: elfmceager	Desc: 
index: 0x3 RID: 0x3e9 acb: 0x00000010 Account: elfmcelferson	Name: 	Desc: 

user:[elfmcskidy] rid:[0x3e8]
user:[elfmceager] rid:[0x3ea]
user:[elfmcelferson] rid:[0x3e9]
enum4linux complete on Mon Mar 22 13:30:27 2021
```
Answer = `3`

### 2. Now how many "shares" are there on the Samba server? `[*]`
`enum4linux -S 10.10.146.89`

```
Starting enum4linux v0.8.9 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Mon Mar 22 13:32:26 2021

 ========================== 
|    Target Information    |
 ========================== 
Target ........... 10.10.146.89
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ==================================================== 
|    Enumerating Workgroup/Domain on 10.10.146.89    |
 ==================================================== 
[+] Got domain/workgroup name: TBFC-SMB-01

 ===================================== 
|    Session Check on 10.10.146.89    |
 ===================================== 
[+] Server 10.10.146.89 allows sessions using username '', password ''

 =========================================== 
|    Getting domain SID for 10.10.146.89    |
 =========================================== 
Domain Name: TBFC-SMB-01
Domain Sid: (NULL SID)
[+] Can't determine if host is part of domain or part of a workgroup

 ========================================= 
|    Share Enumeration on 10.10.146.89    |
 ========================================= 

	Sharename       Type      Comment
	---------       ----      -------
	tbfc-hr         Disk      tbfc-hr
	tbfc-it         Disk      tbfc-it
	tbfc-santa      Disk      tbfc-santa
	IPC$            IPC       IPC Service (tbfc-smb server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available

[+] Attempting to map shares on 10.10.146.89
//10.10.146.89/tbfc-hr	Mapping: DENIED, Listing: N/A
//10.10.146.89/tbfc-it	Mapping: DENIED, Listing: N/A
//10.10.146.89/tbfc-santa	Mapping: OK, Listing: OK
//10.10.146.89/IPC$	[E] Can't understand response:
NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*
enum4linux complete on Mon Mar 22 13:32:29 2021
```
Answer = `4`

### 3. Use smbclient to try to login to the shares on the Samba server (`10.10.000.000`). What share doesn't require a password? `[**********]`

As we got a mapping and listing for tbfc-santa, I think it's safe to assume we can access this one. 

Answer = `tbfc-santa`

### 4. Log in to this share, what directory did ElfMcSkidy leave for Santa? `[************]`

`smbclient //10.10.146.89/tbfc-santa`
```
Enter WORKGROUP\kali's password: 
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Wed Nov 11 21:12:07 2020
  ..                                  D        0  Wed Nov 11 20:32:21 2020
  jingle-tunes                        D        0  Wed Nov 11 21:10:41 2020
  note_from_mcskidy.txt               N      143  Wed Nov 11 21:12:07 2020

		10252564 blocks of size 1024. 5368116 blocks available
smb: \> get note_from_mcskidy.txt 
getting file \note_from_mcskidy.txt of size 143 as note_from_mcskidy.txt (1.4 KiloBytes/sec) (average 1.4 KiloBytes/sec)
```
Answer = `jingle-tunes`

---
```
Tags:
    enum4linux
    smb
    smbclient
    samba shares
```