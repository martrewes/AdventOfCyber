# `[Web Exploit]` Santa's Watching

## Intro
>*We're going to be taking a look at some of the fundamental tools used in web application testing. You're going to learn how to use Gobuster to enumerate a web server for hidden files and folders to aid in the recovery of Elf's forums. Later on, you're going to be introduced to an important technique that is fuzzing, where you will have the opportunity to put theory into practice.*
>
>*Our malicious, despicable, vile, cruel, contemptuous, evil hacker has defaced Elf's forums and completely removed the login page! However, we may still have access to the API. The sysadmin also told us that the API creates logs using dates with a format of YYYYMMDD.*

### Additional Info to Note
#### How to approach the challenge

>Since we know there's theoretically an API directory we can use gobuster to enumerate the website and see if we can find anything. Then assuming we do find something, we should investigate it for interesting files. Let's say we then find what seems to hold the logs, we know we're searching by date, so we can infer that there's a good chance that we'll be using the date parameter to interact with the API. We also know that the API takes a date in the form of YYYYMMDD. A wordlist in that format can be found in the hint for this task, although if you want an extra challenge, you can try and build a wordlist in that format yourself.
>
>Finally, API's may not return data if the proper parameters aren't passed, so with that knowledge, we can use the options in wfuzz to filter out parameters that don't return anything.
>
>With all that in mind, we should be able to get a flag.

# Tasks

### 1. Provide a wfuzz command `[***** ** ** ****,***.*** ****://******.***/***.**************]
>Given the URL "http://shibes.xyz/api.php", what would the entire wfuzz command look like to query the "breed" parameter using the wordlist "big.txt" (assume that "big.txt" is in your current directory)

I followed the example and used what was learned about `get` examples in a previous day.

Answer = `wfuzz -c -z file,big.txt http://shibes.xyz/api.php?breed=FUZZ`

### 2. Use GoBuster to find the API directory. What file is there? `[********.***]`

I am now using my Manjaro install, so I have installed gobuster and wfuzz. I also installed seclists from the AUR. They have installed to the `/usr/share/seclists/` directory. I decided to start with `Discovery/Web-Content/common.txt` and see how I get on from there. I copied to current directory.

For the first attempt, I ran `gobuster dir -u http://10.10.229.28 -w common.txt -x php,txt`

This gave me the following response:
```
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.229.28
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,txt
[+] Timeout:                 10s
===============================================================
2021/03/11 18:06:18 Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 277]
/.htpasswd            (Status: 403) [Size: 277]
/.htaccess            (Status: 403) [Size: 277]
/.hta.php             (Status: 403) [Size: 277]
/.htaccess.php        (Status: 403) [Size: 277]
/.htpasswd.php        (Status: 403) [Size: 277]
/.hta.txt             (Status: 403) [Size: 277]
/.htpasswd.txt        (Status: 403) [Size: 277]
/.htaccess.txt        (Status: 403) [Size: 277]
/LICENSE              (Status: 200) [Size: 1086]
/api                  (Status: 301) [Size: 310] [--> http://10.10.229.28/api/]
Progress: 6171 / 14046 (43.93%)                                              ^C
[!] Keyboard interrupt detected, terminating.
```
As I knew the task asked for the API directory, I knew straight away to follow the link. I then found the file.

Answer = `site-log.php`

### 3. Fuzz the date parameter on the file you found in the API directory. What is the flag displayed in the correct post? `[***{**********}]`

There was a wordlist provided on the page, so I downloaded that and saw that it only contained what appeared to be dates. I assumed I would have needed this to complete the fuzz. I ran the following command:
```
wfuzz -c -z file,wordlist -d "date=FUZZ" -u http://10.10.229.28/api/site-log.php
```
They all gave a response code of `200` but only one came back with more than 0 words or characters. This was `20201125` so I navigated to `http://10.10.229.28/api/site-log.php?date=20201125` which gave me the flag.

Answer = `THM{D4t3_AP1}`


---
```
Tags:
    gobuster
    fuzzing
    wordlists
```