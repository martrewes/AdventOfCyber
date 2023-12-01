# Day 2. `[Web Exploit]` The Elf Strikes Back!

## Intro
>*After your heroic deeds regaining control of the control centre yesterday, Elf McSkidy has decided to give you an important job to do.*
>
>"*We know we've been hacked, so we need a way to protect ourselves! The dev team have set up a website for the elves to upload pictures of any suspicious people hanging around the factory, but we need to make sure it's secure before we add it to the public network. Please perform a security audit on the new server and make sure it's unhackable!*

### Additional Info to Note
#### Putting it all together
This was a lot of information, so let's put it all together and look at the full process for exploiting a file upload vulnerability in a PHP web application:

>1. Find a file upload point.
>2. Try uploading some innocent files -- what does it accept? (Images, text files, PDFs, etc)
>3. Find the directory containing your uploads.
>4. Try to bypass any filters and upload a reverse shell.
>5. Start a netcat listener to receive the shell
>6. Navigate to the shell in your browser and receive a connection!

At the bottom of the dossier is a sticky note containing the following message:

>For Elf McEager:
>
>You have been assigned an ID number for your audit of the system: `ODIzODI5MTNiYmYw` . Use this to gain access to the upload section of the site.
>
>Good luck!

# Tasks

### 1. What string of text needs adding to the URL to get access to the upload page? `[?**=****************]`

The beginning of this page mentions `get` commands, so I just followed that idea and assumed I needed to adjust the url to contain the ID;

Answer = `?id=ODIzODI5MTNiYmYw`

### 2. What type of file is accepted to the site? `[*****]`

When you click the file select button, you are only allowed to select images from your filesystem

Answer = `image`

>Bypass the filter and upload a reverse shell.

### 3. In which directory are the uploaded files stored? `[/*******/]`

Looking in the network tab of devtools, I can see a response from `upload` so I tried uploads as the answer.

Answer = `/uploads/`

> Activate your reverse shell and catch it in a netcat listener!

I fired up Kali Linux in a virtual machine as I assumed it would have all I needed. It did have the php script, however I was unable to get it to call back. I assume this is due to the way I had set up the virtual machine, so I stuck with the AttackBox provided.

The information provided walked through creating a reverse shell script, so I followed that example and just changed the IP and port as suggested.

I saved the script as `webshell.png.php` to hopefully bypass the filter as the filename did contain `.png` in the name. I selected to view all files in the selection dialog, and this did allow me to upload!

I then ran the netcat listener with `nc -lvnp 443`, then went to the file using my browser. The terminal then gave me a shell session, and I was able to run `cat /var/www/flag.txt` to get the flag.

### 4. What is the flag in `/var/www/flag.txt`? `[***{****...}]`

Answer = `THM{MGU3Y2UyMGUwNjExYTY4NTAxOWJhMzhh}`

---
```
Tags:
    netcat
    reverse shell
    GET
    file extensions
    cat
```