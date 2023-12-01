# Day 1. `[Web Explioit]` A Christmas Crisis 

## Intro
>*The Best Festival Company's brand new OpenVPN server has been hacked. This is a crisis!*
>
>*The attacker has damaged various aspects of the company infrastructure -- including using the Christmas Control Centre to shut off the assembly line!*
>
>*It's only 24 days until Christmas, and that line has to be operational or there won't be any presents! You have to hack your way  back into Santa's account (blast that hacker changing the password!) and getting the assembly line up and running again, or Christmas will be ruined!"*

## Tasks
>Register for an account, and then login.
I used `user` as my username 

### 1. What is the name of the cookie used for authentication? `[****]`
   
Found in developer tools on Chrome:

Answer = `auth`

### 2. In what format is the value of this cookie encoded? `[***********]`
   
auth = `7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a2275736572227d`

Looking at it, it did appear to be in hexadecimal

Answer = `hexadecimal`

### 3. Having decoded the cookie, what format is the data stored in? `[****]`

I used https://cryptii.com/pipes/hex-decoder and decoded it to the following:

    {"company":"The Best Festival Company", "username":"user"}

Answer = `JSON`

>Figure out how to bypass the authentication.

### 4. What is the value of Santa's cookie? `[***********...]`

All I would need to do, I assume is change `user` to `santa` in the hex string:

Answer = `7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a2273616e7461227d`

I can now just paste that into the `auth` cookie in developer options so I can appear to be `santa`. Refreshed page afterwards.

>Now that you are the santa user, you can re-activate the assembly line!

### 5. What is the flag you're given when the line is fully active? `[***{**********...}]`

Answer = `THM{MjY0Yzg5NTJmY2Q1NzM1NjBmZWFhYmQy}` *(Appears at bottom of page)*

---
```
Tags:
    cookies
    hex
    auth
    json
```