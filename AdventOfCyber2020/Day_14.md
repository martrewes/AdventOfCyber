# `[Special by TheCyberMentor]` Where's Rudolph?
## Intro

# Task 1

>While hunting and searching for any hints or clues
>Santa uncovers some details and shares the news
>Rudolph loved to use Reddit and browsed aplenty
>His username was 'IGuidetheClaus2020'
>
>Many OSINT investigations start with only a username. A user's posting history can possibly lead to further information. Sometimes, it's the smallest of clues that help us out. Comb through Rudolph's Reddit history and answer questions #1-5 below. You may need to use partial clues with a search engine to fill in the gaps.

### 1. What URL will take me directly to Rudolph's Reddit comment history?

So we know he has a reddit account, so we can just go straight to that profile on http://reddit.com/u/IGuidetheClaus2020. Then navigate to "Comments"

Answer = `https://www.reddit.com/user/IGuidetheClaus2020/comments/`

### 2. According to Rudolph, where was he born?

One of his comments reads:
>Fun fact: I was actually born in Chicago and my creator's name was Robert!

Answer = `Chicago`

### 3. Rudolph mentions Robert.  Can you use Google to tell me Robert's last name?

Doing a Google search of "robert chicago rudolph" immediately have Robert L. May's wiki page.

Answer = `May`

### 4. On what other social media platform might Rudolph have an account?

Another comment on the Reddit profile:
>Ouch. Some days I love Twitter. Some days, it's just...lol.

Answer = Twitter

### 5. What is Rudolph's username on that platform?

I done a quick search on twitter for `IGuidetheClaus2020` which was named that, but it had the handle `@IGuideClaus2020`

Answer = `IGuidetheClaus2020`

# Task 2

>Well it looks like you have uncovered Rudolph's Twitter
>Now we can read into all of his chitter
>Go through his profile and give it some views
>The deeper you dig, the better the clues
>
>By finding another account belonging to our user, we open up the possibility of gathering even more information. Utilize the information found on Rudolph's Twitter account to answer questions #6-11.

### 6. What appears to be Rudolph's favorite TV show right now?

Answer = `Bachelorette`

### 7. Based on Rudolph's post history, he took part in a parade.  Where did the parade take place?

Looking at the photos on the twitter page, one of the banners a person was holding said "Thompson Coburn LLP". A quick google search states they are based in Chicago

Answer = `Chicago`

### 8. Okay, you found the city, but where specifically was one of the photos taken?

Unfortunately this one didn't go too well. I guessed correctly to check the exif data of the higher res image (external to twitter, so it would retain that data), and sure enough I was able to extracj it using `exiftool`. This gave me the coordinates as `41 deg 53' 30.53" N, 87 deg 37' 27.40" W` which I knew wasn't the format that the answer wanted so I went about looking for an online converter. I found one and converted it to a decimal format, however this didn't work ether. I then looked for an online exif data and found one at http://exif.regex.info/. I uploaded the file and got slightly different decimals, so I tried those instead and it worked.

Answer = `41.891815, -87.624277`

### 9. Did you find a flag too?

The flag was in the exif data under copyright.

Answer = `{FLAG}ALWAYSCHECKTHEEXIFD4T4`

### 10. Has Rudolph been pwned? What password of his appeared in a breach?

I had a look his twitter profile and it contained a bussiness email address. I ran this through http://HaveIBeenPwned.com, and sure enough it was part of the `LiveJournal` breach. 

>**This took forever! Unfortunately every online service to checked for leaked passwords are now either no longer available or are behind a paywall. This had me hunting around for ages.**

I did however find a breach compilation by other means. I ran that through `grep -i "rudolphthered@hotmail.com" /file` and received no hits.. I decided to cheat a little on this one as I knew what I had to do. I had already spent well over an hour looking into this.

Answer = `spygame`

### 11. Based on all the information gathered.  It's likely that Rudolph is in the Windy City and is staying in a hotel on Magnificent Mile.  What are the street numbers of the hotel address?

This was fairly simple. On the twitter profile, he mentions:

>Yo @Marriott is where Rudolph loves to lay his head.

Had a quick look at those coordinates on Google Maps, and found a Marriot close by. Found it at 540 N Michigan Ave, Chicago, IL 60611, United States.

Answer = `540`

>It looks like finding Rudolph was a bit too easy
>His OPSEC would make any security pro queasy
>To the Windy City, Rudolph was tracked
>Christmas is saved, we brought Rudolph back
---
```
Tags:
    opsec
    osint
    usernames
    passwords
    breaches
    grep
```