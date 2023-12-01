# Day 3. `[Web Exploit]` Christmas Chaos

## Intro
>*McSkidy is walking down the corridor and hears a faint bleeping noise, Beep.... Beep.... Beep... as McSkidy gets closer to Sleigh Engineering Room the faint noise gets louder and louder.. BEEP.... BEEP.... Something is clearly wrong! McSkidy runs to the room, slamming open the door to see Santa's sleighs control panel lite up in red error messages! "Santa sleigh! It's been hacked, code red.. code red!" he screams as he runs back to the elf security command center.*
>
>*Can you help McSkidy and his team hack into Santa's Sleigh to re-gain control?*

## Tasks

>Use BurpSuite to brute force the login form.  Use the following lists for the default credentials:
>|Username|Password|
>|--------|---------
>|root|root|
>|admin|password|
>|user|12345|
<br>

>Use the correct credentials to log in to the Santa Sleigh Tracker app. Don't forget to turn off Foxyproxy once BurpSuite has finished the attack!

### 1. What is the flag? `[***{*********...}]`

This one basically allows you to follow the tutorial provided. 

I used my virtual machine in this case, it had BurpSuite already installed. The basic rundown is that I had to add the usernames and passwords to the intruder tab and then run the attack. This gave me the login information as:
>Username: admin  
>Password: 12345

This allowed me to see the tracker page after logging in with those credentials. At the bottom of the page was the flag.

Answer = `THM{885ffab980e049847516f9d8fe99ad1a}`

---
```
Tags:
    BurpSuite
    FoxyProxy
    Dictionary Attacks
    Wordlists
```