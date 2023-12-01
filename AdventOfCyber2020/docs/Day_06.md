# Day 6. `[Web Exploit]` Be careful with what you wish on a Christmas night
## Intro
>This year, Santa wanted to go fully digital and invented a "Make a wish!" system. It's an extremely simple web app that would allow people to anonymously share their wishes with others. Unfortunately, right after the hacker attack, the security team has discovered that someone has compromised the "Make a wish!". Most of the wishes have disappeared and the website is now redirecting to a malicious website.  An attacker might have pretended to submit a wish and put a malicious request on the server! The security team has pulled a back-up server for you on MACHINE_IP:5000. Your goal is to find the way the attacker could have exploited the application.

## Tasks

### 1. What vulnerability type was used to exploit the application? `[****** ********** *********]`

Referenced throughout the page:

Answer = `Stored Cross-Site Scripting`

### 2. What query string can be abused to craft a reflected XSS? `[*]`

When you write a query, the url changes to include `?q=...`

Answer = `q`

### 3. Run a ZAP (zaproxy) automated scan on the target. How many XSS alerts are in the scan?

This one was a bit annoying. The answer was `5` however the site didn't accept it. Just went through several digits until it worked.

Answer = `2` (but really 5)

---
```
Tags:
    xss
    zap
    payloads
```