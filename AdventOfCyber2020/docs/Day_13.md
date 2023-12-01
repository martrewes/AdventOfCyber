# Day 13. `[Special by John Hammond]` Coal for Christmas

>Hi Santa, hop in your sleigh and deploy this machine!
>
>The Christmas GPS now says this house is at the address `10.10.*.*` Scan this machine with a port-scanning tool of your choice.

## Tasks

### 1. What old, deprecated protocol and service is running? `[******]`

I ran nmap on the IP address as suggested. Looks like it is running Telnet!

Answer = `telnet`

### 2. What credential was left for you? `[**************]`

I connected to the server with telnet and the port listed from `nmap`

`telnet 10.10.*.* 23`

I was greeted with the following:
```
HI SANTA!!! 

We knew you were coming and we wanted to make
it easy to drop off presents, so we created
an account for you to use.

Username: santa
Password: clauschristmas

We left you cookies and milk!
```
I was able to login.

Answer = `clauschristmas`

### 3. What distribution of Linux and version number is this server running? `[****** **.**]`

I did an `ls /etc/*release` to see the format of the release information. Then ran `cat /etc/lsb-release`

Answer = `Ubuntu 12.04`

>This is a very old version of Linux! This may be vulnerable to some kernel exploits, that we could use to escalate our privileges.
>
>Take a look at the cookies and milk that the server owners left for you. You can do this with the cat command as mentioned earlier.

### 4. Who got here first `[******]`

cat cookies_and_milk.txt contained a message as well as C code:

```
$ cat cookies_and_milk.txt
/*************************************************
// HAHA! Too bad Santa! I, the Grinch, got here 
// before you did! I helped myself to some of
// the goodies here, but you can still enjoy
// some half eaten cookies and this leftover
// milk! Why dont you try and refill it yourself!
//   - Yours Truly,
//         The Grinch
//*************************************************/

#include <fcntl.h>
#include <pthread.h>
#include <string.h>
#include <stdio.h>
...
```

Answer = Grinch

The C code turns out to be the DirtyCow exploit.

### 5. What is the verbatim syntax you can use to compile, taken from the real C source code comments?  `[*** ******** ********.* ** ********]`

I found the information on the GitHub page: https://github.com/FireFart/dirtycow/blob/master/dirty.c

Answer = `gcc -pthread dirty.c -o dirty -lcrypt`

### 6. What "new" username was created, with the default operations of the real C source code? `[********]`

I had to copy the source from the above link. Pasted it into a new file called `dirty.c` with `nano`. I then compiled using the command above and ran it.

Answer = `filefart`

### 7. What is the MD5 hash output? `[md5sum]`

I had to follow some instructions left in a `.txt` file in `/root`:

```
Nice work, Santa!

Wow, this house sure was DIRTY!
I think they deserve coal for Christmas, don't you?
So let's leave some coal under the Christmas `tree`!

Let's work together on this. Leave this text file here,
and leave the christmas.sh script here too...
but, create a file named `coal` in this directory!
Then, inside this directory, pipe the output
of the `tree` command into the `md5sum` command.

The output of that command (the hash itself) is
the flag you can submit to complete this task
for the Advent of Cyber!

        - Yours,
                John Hammond
                er, sorry, I mean, the Grinch

          - THE GRINCH, SERIOUSLY
```
So I did the above with `touch coal` and then `tree | md5sum`

Answer = `8b16f00dd3b51efadb02c1df7f8427cc`

---
```
Tags:
    telnet
    dirtycow
    md5
```