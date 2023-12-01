# Day 8. `[Networking]` What's Under the Christmas Tree?
## Intro
>After a few months of probation, intern Elf McEager has passed with glowing feedback from Elf McSkidy. During the meeting, Elf McEager asked for more access to The Best Festival Company's (TBFC's) internal network as he wishes to know more about the systems he has sworn to protect.
>
>Elf McSkidy was reluctant to agree. However, after Elf McEager's heroic actions in recovering Christmas, Elf McSkidy soon thought this was a good idea. This was uncharted territory for Elf McEager - he had no idea how to begin finding out this information for his new responsibilities. Thankfully, TBFC has a wonderful up-skill program covering the use of Nmap for ElfMcEager to enrol in.

## Tasks

### 1. When was Snort created? `[****]`

This was as simple as a google search.

Answer = `1998`

### 2. Using Nmap on 10.10.\*\*\*.\*\*\* , what are the port numbers of the three services running?  (Please provide your answer in ascending order/lowest -> highest, separated by a comma) `[**,****,****]`

Doing a quick `nmap -sS` scan resulted in the following:
```
Starting Nmap 7.91 ( https://nmap.org ) at 2021-03-17 19:12 GMT
Nmap scan report for 10.10.***.***
Host is up (0.041s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE
80/tcp   open  http
2222/tcp open  EtherNetIP-1
3389/tcp open  ms-wbt-server
```

Answer = `80,2222,3389`

### 3. Run a scan and provide the `-Pn` flag to ignore ICMP being used to determine if the host is up

`sudo nmap -Pn 10.10.***.***`
```
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times will be slower.
Starting Nmap 7.91 ( https://nmap.org ) at 2021-03-17 19:15 GMT
Nmap scan report for 10.10.***.***
Host is up (0.041s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE
80/tcp   open  http
2222/tcp open  EtherNetIP-1
3389/tcp open  ms-wbt-server
```
Host states that it is up.

No answer required.

### 4. Experiment with different scan settings such as-A and -sV whilst comparing the outputs given.
`sudo nmap -A 10.10.***.***`
```

Starting Nmap 7.91 ( https://nmap.org ) at 2021-03-17 19:17 GMT
Nmap scan report for 10.10.***.***
Host is up (0.025s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Apache httpd 2.4.29 ((Ubuntu))
|_http-generator: Hugo 0.78.2
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: TBFC&#39;s Internal Blog
2222/tcp open  ssh           OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 cf:c9:99:d0:5c:09:27:cd:a1:a8:1b:c2:b1:d5:ef:a6 (RSA)
|   256 4c:d4:f9:20:6b:ce:fc:62:99:54:7d:c2:b4:b2:f2:b2 (ECDSA)
|_  256 d0:e6:72:18:b5:20:89:75:d5:69:74:ac:cc:b8:3b:9b (ED25519)
3389/tcp open  ms-wbt-server xrdp
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.91%E=4%D=3/17%OT=80%CT=1%CU=36056%PV=Y%DS=2%DC=T%G=Y%TM=605255D
OS:C%P=x86_64-unknown-linux-gnu)SEQ(SP=FF%GCD=1%ISR=109%TI=Z%CI=Z%II=I%TS=A
OS:)OPS(O1=M505ST11NW6%O2=M505ST11NW6%O3=M505NNT11NW6%O4=M505ST11NW6%O5=M50
OS:5ST11NW6%O6=M505ST11)WIN(W1=F4B3%W2=F4B3%W3=F4B3%W4=F4B3%W5=F4B3%W6=F4B3
OS:)ECN(R=Y%DF=Y%T=40%W=F507%O=M505NNSNW6%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+
OS:%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
OS:T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A
OS:=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%D
OS:F=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=4
OS:0%CD=S)

Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 21/tcp)
HOP RTT      ADDRESS
1   48.36 ms 10.8.0.1
2   48.37 ms 10.10.***.***

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 25.48 seconds
```
`sudo nmap -sV 10.10.***.***`
```
Starting Nmap 7.91 ( https://nmap.org ) at 2021-03-17 19:21 GMT
Nmap scan report for 10.10.***.***
Host is up (0.046s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Apache httpd 2.4.29 ((Ubuntu))
2222/tcp open  ssh           OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
3389/tcp open  ms-wbt-server xrdp
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.66 seconds
```
No answer Required

### 5. Use Nmap to determine the name of the Linux distribution that is running, what is reported as the most likely distribution to be running? `[******]`

As we can see from the results of the other `nmap` scans, it is likely to be Ubuntu.

Answer = `Ubuntu`

### 6. Use Nmap's Network Scripting Engine (NSE) to retrieve the "HTTP-TITLE" of the webserver. Based on the value returned, what do we think this website might be used for? `[****]`

Again, we can also see this in the result.

Answer = `Blog`

### 7. Now use different scripts against the remaining services to discover any further information about them

No answer required.

---
```
Tags:
    nmap
    snot
    ip scanning
```