```python
import re
import pandas as pd
import numpy as np
```


```python
f = open('WhatsApp Chat with bajrang dal 🚩.txt','r',encoding='utf-8')
```


```python
data = f.read()
```


```python
print(data)
```

    26/04/23, 11:01 am - Messages and calls are end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them. Tap to learn more.
    26/04/23, 11:01 am - You created this group
    26/04/23, 11:01 am - You updated the message timer. New messages will disappear from this chat 24 hours after they're sent, except when kept.
    26/04/23, 11:19 am - You changed this group's icon
    27/04/23, 3:20 pm - Abhi Coaching changed this group's icon
    06/06/23, 1:27 pm - You changed the group name from "Kalra ka shukla" to "Kanpuriye"
    07/06/23, 5:08 pm - Abhi Coaching turned off disappearing messages.
    07/06/23, 6:04 pm - Alka Coaching: Never too busy for you bruh
    07/06/23, 6:11 pm - Deepansh Pandey: <Media omitted>
    07/06/23, 6:20 pm - Abhi Coaching: send books
    07/06/23, 11:06 pm - Abhi Coaching: kaha mar gaye?
    07/06/23, 11:44 pm - Alka Coaching: Idhar hi hun
    08/06/23, 7:58 am - Deepansh Pandey: Aaj ka kya plan shero?
    08/06/23, 1:33 pm - Deepansh Pandey: Alka reply kro baby
    08/06/23, 1:33 pm - Abhi Coaching: bhai alakshendra yaar
    08/06/23, 1:33 pm - Deepansh Pandey: Kab ka plan banaye
    08/06/23, 1:33 pm - Abhi Coaching: itna kya bhav khaa rahe ho reply dene mei
    08/06/23, 1:33 pm - Deepansh Pandey: Kal I'll be busy
    08/06/23, 1:33 pm - Abhi Coaching: yaha fast reply pe koi judge nai karta
    08/06/23, 1:33 pm - Deepansh Pandey: 🤣🤣🤣
    08/06/23, 1:35 pm - Deepansh Pandey: Batao alka kb ka rkhe
    08/06/23, 1:35 pm - Alka Coaching: Bhai mai kal hi ghum ke aaya 
    Ma baap bol denge itne bhi acche number ni aaye hain
    08/06/23, 1:35 pm - Deepansh Pandey: Ghr ka plan rkh le?
    08/06/23, 1:36 pm - Alka Coaching: Ghar pe kuch karne ho ga ni
    08/06/23, 1:36 pm - Alka Coaching: Kal parso bahar chale?
    08/06/23, 1:36 pm - Deepansh Pandey: Kal ka I'm not sure
    08/06/23, 1:36 pm - Alka Coaching: Parso?
    08/06/23, 1:36 pm - Abhi Coaching: bahar kya karoge?
    08/06/23, 1:36 pm - Deepansh Pandey: Again shyd mai na rhu
    08/06/23, 1:37 pm - Deepansh Pandey: But Jo bhi ho parso shyd possible ho bhi... Jaisa hoga bata denge
    08/06/23, 1:37 pm - Deepansh Pandey: Ye bhi hai
    08/06/23, 1:37 pm - Alka Coaching: Khaayenge yaar 
    Scenery dekhenge 
    Ghar pe hue to abuse bhi halke se karna padega
    08/06/23, 1:37 pm - Abhi Coaching: ghar pe ekdum relax rehta
    08/06/23, 1:37 pm - Abhi Coaching: baate toh bahar bhi karenge
    08/06/23, 1:37 pm - Alka Coaching: Bhai tu kal k baad kab free hai
    08/06/23, 1:37 pm - Deepansh Pandey: I've got something to tell guys
    08/06/23, 1:37 pm - Deepansh Pandey: Abhi knows a bit
    08/06/23, 1:37 pm - Abhi Coaching: but what we can do is ghar chalte fir khane chalenge bahar
    08/06/23, 1:38 pm - Deepansh Pandey: Jldi milne ka rkho bhaiyo
    08/06/23, 1:38 pm - Alka Coaching: Sure
    08/06/23, 1:38 pm - Alka Coaching: Kyun kya hua?
    08/06/23, 1:38 pm - Deepansh Pandey: Milkr bataunga
    08/06/23, 1:38 pm - Abhi Coaching: yaar fun talks can be without gaali too yk 😂
    samjhao bhai deepansh isko
    08/06/23, 1:38 pm - Abhi Coaching: Saturday rakhe??
    08/06/23, 1:39 pm - Alka Coaching: Saturday’s okay
    08/06/23, 1:39 pm - Deepansh Pandey: Abe whi toh parso hai... I'm not sure n about parso
    08/06/23, 1:39 pm - Alka Coaching: Sunday?
    08/06/23, 1:39 pm - Deepansh Pandey: Shyd weekend or relatives ke yha jana pde
    08/06/23, 1:39 pm - Abhi Coaching: toh fir Monday ya Tuesday rakhlo
    08/06/23, 1:39 pm - Alka Coaching: Bhai Monday done karte?
    08/06/23, 1:39 pm - Abhi Coaching: kyuki Sunday is family day here
    08/06/23, 1:39 pm - Abhi Coaching: next week any day
    08/06/23, 1:39 pm - Abhi Coaching: fine by me
    08/06/23, 1:39 pm - Alka Coaching: Gotcha 
    Bandi se milne jaayega
    08/06/23, 1:40 pm - Deepansh Pandey: Acha lsn agr sat possible hua then I'll tell otherwise mon
    08/06/23, 1:40 pm - Abhi Coaching: haan wo bandi meri Nani hai
    08/06/23, 1:40 pm - Abhi Coaching: mast
    08/06/23, 1:40 pm - Alka Coaching: Done deal bhai
    08/06/23, 1:40 pm - Deepansh Pandey: You deleted this message
    08/06/23, 1:40 pm - Deepansh Pandey: You deleted this message
    08/06/23, 1:41 pm - Abhi Coaching: <Media omitted>
    08/06/23, 1:41 pm - Deepansh Pandey: You deleted this message
    08/06/23, 1:41 pm - Abhi Coaching changed the group name from "Kanpuriye" to "bajrang dal 🚩"
    08/06/23, 1:41 pm - Deepansh Pandey: You deleted this message
    08/06/23, 1:42 pm - Deepansh Pandey: You deleted this message
    08/06/23, 1:42 pm - Abhi Coaching: This message was deleted
    08/06/23, 1:42 pm - Abhi Coaching: This message was deleted
    08/06/23, 1:42 pm - Deepansh Pandey: You deleted this message
    08/06/23, 1:42 pm - Abhi Coaching: This message was deleted
    08/06/23, 1:43 pm - Abhi Coaching: This message was deleted
    08/06/23, 1:43 pm - Deepansh Pandey: You deleted this message
    08/06/23, 1:43 pm - Abhi Coaching: This message was deleted
    08/06/23, 1:44 pm - Deepansh Pandey: You deleted this message
    08/06/23, 1:44 pm - Deepansh Pandey: You deleted this message
    08/06/23, 1:45 pm - Abhi Coaching: This message was deleted
    08/06/23, 1:45 pm - Abhi Coaching: This message was deleted
    08/06/23, 1:46 pm - Deepansh Pandey: You deleted this message
    08/06/23, 1:46 pm - Abhi Coaching: This message was deleted
    08/06/23, 1:46 pm - Abhi Coaching: This message was deleted
    08/06/23, 1:47 pm - Deepansh Pandey: 😂😂
    08/06/23, 1:47 pm - Abhi Coaching: 😂😂
    08/06/23, 2:39 pm - Alka Coaching: Nice
    08/06/23, 4:19 pm - Deepansh Pandey: Tmhare liye hi kia hai.... I'm glad u liked it
    08/06/23, 6:00 pm - Alka Coaching: Shows how much you guys care:)
    08/06/23, 6:13 pm - Deepansh Pandey: We love you alka ❤
    08/06/23, 6:27 pm - Alka Coaching: Gay
    08/06/23, 6:28 pm - Deepansh Pandey: Tere liye 😍
    08/06/23, 6:28 pm - Deepansh Pandey: 🤣🤣
    08/06/23, 9:44 pm - Abhi Coaching: as a friend*
    08/06/23, 11:18 pm - Alka Coaching: Somehow that’s gayer abbhi
    09/06/23, 2:26 am - Abhi Coaching: somehow all you think about is being gay why so alex
    09/06/23, 8:53 am - Alka Coaching: Dunno
    09/06/23, 8:53 am - Abhi Coaching: thoda toh excitement dikhaya kar bhai apni zindagii mei basss thoda sa
    09/06/23, 9:32 am - Deepansh Pandey: <Media omitted>
    09/06/23, 11:44 am - Alka Coaching: Boys… kuch karne ko ni hai
    09/06/23, 11:46 am - Abhi Coaching: go read your new books
    09/06/23, 11:47 am - Deepansh Pandey: Call kr le
    09/06/23, 11:47 am - Deepansh Pandey: Bc krte hai
    09/06/23, 11:47 am - Abhi Coaching: discord pe aa jao bey teeno waha chess khel sakte, YouTube dekh sakte ya koi movie bhi
    09/06/23, 11:47 am - Deepansh Pandey: Ye bhi thik hai
    09/06/23, 12:57 pm - Alka Coaching: Done
    09/06/23, 12:57 pm - Alka Coaching: Invite bhejna
    09/06/23, 12:57 pm - Abhi Coaching: okay bhejta hu thodi der mei
    09/06/23, 1:40 pm - Abhi Coaching: https://discord.gg/pewDwSZj
    09/06/23, 9:32 pm - Deepansh Pandey: Kal ka plan rkhe?
    09/06/23, 9:41 pm - Alka Coaching: Kal thoda short term hai 
    Abbhi?
    09/06/23, 9:41 pm - Abhi Coaching: This message was deleted
    09/06/23, 9:42 pm - Abhi Coaching: rakhlo kal
    09/06/23, 9:42 pm - Abhi Coaching: waise bhi shaam ka hee rakh rahe hai
    09/06/23, 9:43 pm - Deepansh Pandey: Bhai agle month k kiye adv notice bhej du?
    09/06/23, 9:47 pm - Abhi Coaching: agar dopeher ka hota toh mai bhi bolta but since shaam ka hai toh no issues
    09/06/23, 9:49 pm - Deepansh Pandey: Yeah... So now alka u decide
    09/06/23, 10:04 pm - Abhi Coaching: keep Monday or Saturday whatever you like Alex
    09/06/23, 10:05 pm - Alka Coaching: Thik hai 
    Kal shaam ko ghar aana 
    Thoda thanda hote hi fir chalenge bahar
    09/06/23, 10:06 pm - Abhi Coaching: pacca you're fine by that na?
    09/06/23, 10:06 pm - Alka Coaching: 4:30ish tak aa jaiyo
    09/06/23, 10:06 pm - Alka Coaching: Yeah 
    Just asked ma
    09/06/23, 10:06 pm - Deepansh Pandey: 👍👍
    09/06/23, 10:06 pm - Abhi Coaching: cool
    09/06/23, 10:06 pm - Alka Coaching: Chalo chehre dekhe aakhir
    09/06/23, 10:07 pm - Alka Coaching: Especially abhhi
    09/06/23, 10:07 pm - Abhi Coaching: Shutup yaar
    09/06/23, 10:07 pm - Alka Coaching: Mere Mann me to tu takla hi hai
    09/06/23, 10:07 pm - Deepansh Pandey: Tu fir ganja hi hai n?
    09/06/23, 10:07 pm - Abhi Coaching: haan yaar
    09/06/23, 10:07 pm - Deepansh Pandey: 😂😂
    09/06/23, 10:07 pm - Abhi Coaching: 😭😭😭😭
    09/06/23, 10:07 pm - Alka Coaching: Tabla bajayenge
    09/06/23, 10:07 pm - Alka Coaching: Shivaji the boss
    09/06/23, 10:07 pm - Deepansh Pandey: 😂😂
    09/06/23, 10:08 pm - Abhi Coaching: stool ka arrangement kar lena chotu
    09/06/23, 10:08 pm - Abhi Coaching: 😂😂😂😂
    09/06/23, 10:08 pm - Alka Coaching: Too far
    09/06/23, 10:08 pm - Abhi Coaching: far beyond your reach
    09/06/23, 10:08 pm - Deepansh Pandey: @918299433225  bhai mai na sehta
    09/06/23, 10:08 pm - Alka Coaching: You know 
    That does make sense
    09/06/23, 10:09 pm - Abhi Coaching: we're not anant afterall
    09/06/23, 10:09 pm - Alka Coaching: You wish
    09/06/23, 10:09 pm - Deepansh Pandey: <Media omitted>
    09/06/23, 10:10 pm - Alka Coaching: Adv mat bola kar ab
    09/06/23, 10:11 pm - Deepansh Pandey: Mujhe bhi likhne mei ajeeb sa kaha
    09/06/23, 10:11 pm - Deepansh Pandey: Laga*
    09/06/23, 10:11 pm - Abhi Coaching: <Media omitted>
    09/06/23, 10:11 pm - Alka Coaching: Knew it
    09/06/23, 10:13 pm - Deepansh Pandey: https://www.instagram.com/reel/CtLUJWhgaj9/?igshid=MTc4MmM1YmI2Ng==
    09/06/23, 10:13 pm - Deepansh Pandey: Abe ye kaun hai sala chadarmod
    09/06/23, 10:14 pm - Abhi Coaching: tshirt nai dikhri kya
    09/06/23, 10:15 pm - Deepansh Pandey: Abe woh thik hai but ye... Sala 8vi nhi kiye hoga bhai
    09/06/23, 10:16 pm - Abhi Coaching: iska channel hai ig pe gyaan pelta hai bemtlb ka just like Praful billori
    09/06/23, 10:16 pm - Abhi Coaching: mba chaiwala
    09/06/23, 10:17 pm - Deepansh Pandey: Bhai duniya k agr ye haal hai... Toh bdne do fir global warming
    09/06/23, 10:17 pm - Deepansh Pandey: Ozone bhi hata do bhai fir
    09/06/23, 11:20 pm - Abhi Coaching: <Media omitted>
    09/06/23, 11:21 pm - Abhi Coaching: 😂😂
    10/06/23, 1:28 am - Alka Coaching: It’s funny when I do it abbhi
    Otherwise you’re bullying buddy
    10/06/23, 1:30 am - Abhi Coaching: it's you that's why I'm bullying
    10/06/23, 1:30 am - Abhi Coaching: who doesn't bully his bestfriend huh
    10/06/23, 1:31 am - Alka Coaching: I bet Anant doesn’t
    10/06/23, 1:33 am - Abhi Coaching: he doesn't have one ig
    10/06/23, 6:59 am - Deepansh Pandey: Are ye dekh k acha yaad aya
    10/06/23, 6:59 am - Deepansh Pandey: Bhai books le ana pls
    10/06/23, 9:45 am - Abhi Coaching: okay
    10/06/23, 10:32 am - Abhi Coaching: <Media omitted>
    10/06/23, 10:32 am - Abhi Coaching: that's the real Elon btw
    10/06/23, 10:35 am - Deepansh Pandey: 😂😂
    10/06/23, 1:05 pm - Alka Coaching: Very hardworking 
    Truly deserves to be the richest guy in the world
    10/06/23, 4:21 pm - Abhi Coaching: This message was deleted
    10/06/23, 9:53 pm - Deepansh Pandey: <Media omitted>
    10/06/23, 9:53 pm - Deepansh Pandey: Ye koi iski clips kato...
    10/06/23, 9:54 pm - Deepansh Pandey: Bht funny hai upload krnge stry pr
    10/06/23, 9:54 pm - Deepansh Pandey: <Media omitted>
    10/06/23, 9:54 pm - Deepansh Pandey: <Media omitted>
    10/06/23, 9:54 pm - Deepansh Pandey: <Media omitted>
    10/06/23, 9:54 pm - Deepansh Pandey: <Media omitted>
    10/06/23, 9:54 pm - Deepansh Pandey: <Media omitted>
    10/06/23, 9:54 pm - Deepansh Pandey: Baki I have these pics... Jo ki kahi upload krne lyk hai nhi
    11/06/23, 9:13 am - Deepansh Pandey: <Media omitted>
    11/06/23, 9:15 am - Abhi Coaching: <Media omitted>
    11/06/23, 9:30 am - Deepansh Pandey: Proper 10 min wla WhatsApp pr nhi ja rha
    11/06/23, 9:34 am - Abhi Coaching: fast forward looks better
    11/06/23, 9:41 am - Deepansh Pandey: Hmm
    11/06/23, 9:41 am - Deepansh Pandey: Slander jaisa
    12/06/23, 8:47 pm - Abhi Coaching: https://myflixer.pw/movie/fast-and-furious-10-8846
    12/06/23, 8:52 pm - Deepansh Pandey: https://youtu.be/NG6uCHWT03w
    12/06/23, 8:53 pm - Deepansh Pandey: Abe lo yt pr mil gyi 🤣🤣
    12/06/23, 8:54 pm - Abhi Coaching: maine jaane tu jaane na dekhi thi yt pe
    12/06/23, 8:54 pm - Abhi Coaching: yt is a bliss to mankind jab tak paid nai hota
    12/06/23, 8:56 pm - Abhi Coaching: <Media omitted>
    12/06/23, 8:57 pm - Abhi Coaching: richest man y'all
    12/06/23, 9:13 pm - Deepansh Pandey: 🤣🤣
    14/06/23, 2:07 pm - Abhi Coaching: <Media omitted>
    14/06/23, 2:36 pm - Deepansh Pandey: 👍👍
    11/07/23, 10:03 am - Deepansh Pandey: https://www.aznude.com/view/celeb/a/anjaliarora.html?jwsource=cl
    11/07/23, 10:03 am - Abhi Coaching: abet bsdk
    11/07/23, 10:03 am - Abhi Coaching: telegram bhai telegram not WhatsApp pls
    11/07/23, 10:05 am - Deepansh Pandey: Laude wha koi group nhi hai
    11/07/23, 10:05 am - Deepansh Pandey: Isliye yha bheja
    11/07/23, 10:05 am - Abhi Coaching: Banalo
    11/07/23, 10:05 am - Deepansh Pandey: Tum bhai banake wha send kr dena
    11/07/23, 5:22 pm - Deepansh Pandey: https://maps.app.goo.gl/oT6BT9Lu9wbsFCry7
    11/07/23, 9:47 pm - Deepansh Pandey: <Media omitted>
    11/07/23, 9:47 pm - Deepansh Pandey: <Media omitted>
    11/07/23, 9:47 pm - Deepansh Pandey: <Media omitted>
    11/07/23, 9:47 pm - Deepansh Pandey: <Media omitted>
    11/07/23, 9:47 pm - Deepansh Pandey: <Media omitted>
    11/07/23, 9:47 pm - Deepansh Pandey: <Media omitted>
    11/07/23, 9:47 pm - Deepansh Pandey: <Media omitted>
    11/07/23, 9:47 pm - Deepansh Pandey: <Media omitted>
    11/07/23, 9:48 pm - Abhi Coaching: <Media omitted>
    11/07/23, 9:51 pm - Deepansh Pandey: Abe aur bhejo
    11/07/23, 9:52 pm - Abhi Coaching: <Media omitted>
    11/07/23, 9:52 pm - Abhi Coaching: <Media omitted>
    11/07/23, 9:52 pm - Deepansh Pandey: Chutiye gandi wali bhejo
    11/07/23, 9:52 pm - Abhi Coaching: <Media omitted>
    11/07/23, 9:52 pm - Abhi Coaching: <Media omitted>
    11/07/23, 9:52 pm - Abhi Coaching: <Media omitted>
    11/07/23, 9:52 pm - Deepansh Pandey: Jo actual memories hai
    11/07/23, 9:52 pm - Abhi Coaching: <Media omitted>
    11/07/23, 9:52 pm - Deepansh Pandey: Ye jadoo ke grah ki pics mt bhejo
    11/07/23, 9:53 pm - Abhi Coaching: <Media omitted>
    11/07/23, 9:53 pm - Abhi Coaching: <Media omitted>
    11/07/23, 9:53 pm - Abhi Coaching: <Media omitted>
    11/07/23, 9:53 pm - Abhi Coaching: <Media omitted>
    11/07/23, 9:53 pm - Abhi Coaching: <Media omitted>
    11/07/23, 9:53 pm - Abhi Coaching: <Media omitted>
    11/07/23, 9:54 pm - Deepansh Pandey: <Media omitted>
    11/07/23, 9:54 pm - Abhi Coaching: <Media omitted>
    11/07/23, 9:54 pm - Abhi Coaching: <Media omitted>
    11/07/23, 9:54 pm - Abhi Coaching: <Media omitted>
    11/07/23, 9:54 pm - Abhi Coaching: <Media omitted>
    11/07/23, 9:54 pm - Abhi Coaching: <Media omitted>
    11/07/23, 9:54 pm - Abhi Coaching: <Media omitted>
    11/07/23, 9:54 pm - Abhi Coaching: <Media omitted>
    11/07/23, 9:55 pm - Abhi Coaching: bhai ye saari hai
    11/07/23, 9:56 pm - Deepansh Pandey: Check my story
    11/07/23, 10:01 pm - Abhi Coaching: fuckoff yaar deepu
    11/07/23, 10:01 pm - Abhi Coaching: Tera phone bhool hee jana chaiye tha
    11/07/23, 10:04 pm - Deepansh Pandey: 😂😂😂
    12/07/23, 2:28 pm - Alka Coaching: https://youtu.be/LIKPbZqsb5w
    12/07/23, 2:34 pm - Abhi Coaching: https://youtu.be/6TG68Fg3or8
    12/07/23, 2:34 pm - Abhi Coaching: ye gaana sunna ek baar
    12/07/23, 2:35 pm - Abhi Coaching: aaj mila mujhe kaafi Acha laga
    12/07/23, 2:35 pm - Abhi Coaching: vibey hai kaafi
    12/07/23, 5:48 pm - Alka Coaching: Bhai ye bahut famous bhajan hai
    12/07/23, 5:48 pm - Alka Coaching: Ye remix kaafi chill hai though
    12/07/23, 5:49 pm - Abhi Coaching: ik ik but this one's a remix
    12/07/23, 6:00 pm - Deepansh Pandey: ❤❤
    13/07/23, 6:19 pm - Deepansh Pandey: https://youtu.be/tdch76DuAvc
    14/07/23, 12:29 pm - Abhi Coaching: entertaining toh tha
    14/07/23, 1:17 pm - Deepansh Pandey: Told u
    15/07/23, 11:13 am - Alka Coaching: https://youtube.com/shorts/rWIWyfhNPsA?feature=share
    15/07/23, 1:39 pm - Abhi Coaching: This message was deleted
    15/07/23, 1:39 pm - Abhi Coaching: This message was deleted
    15/07/23, 6:46 pm - Deepansh Pandey: Are woh channel ka link bhejo jo bta rhe the
    15/07/23, 6:46 pm - Abhi Coaching: gsoc
    15/07/23, 6:47 pm - Deepansh Pandey: 👍
    15/07/23, 6:47 pm - Abhi Coaching: bhai naam nahi hai ye
    15/07/23, 6:47 pm - Abhi Coaching: naam wahi batayega
    15/07/23, 7:28 pm - Deepansh Pandey: Ok
    20/07/23, 5:31 pm - Abhi Coaching: https://youtube.com/shorts/l3feaOt2ZIk?feature=share
    20/07/23, 5:31 pm - Abhi Coaching: thapar is in Punjab na
    20/07/23, 6:26 pm - Alka Coaching: Yes bro
    20/07/23, 6:27 pm - Abhi Coaching: Bhai Delhi ho jaate tera
    20/07/23, 6:38 pm - Alka Coaching: Bhai chahte to hum bhi yahi
    14/08/23, 8:46 pm - Abhi Coaching: 10 baje tak call karte
    14/08/23, 8:46 pm - Abhi Coaching: dinner wagera bhi ho jayega
    14/08/23, 9:29 pm - Deepansh Pandey: Bhai ruk jao... Abhi thda late call kr lenge
    14/08/23, 9:30 pm - Abhi Coaching: nai nai hogaya
    14/08/23, 9:30 pm - Abhi Coaching: kal 2 baje ka decide hua
    14/08/23, 9:30 pm - Deepansh Pandey: Acha
    14/08/23, 9:30 pm - Deepansh Pandey: Okk
    14/08/23, 9:30 pm - Abhi Coaching: alex ke Ghar pe milenge fir kahi chalenge
    14/08/23, 9:30 pm - Abhi Coaching: room pe arihant hai with the broken leg
    14/08/23, 9:30 pm - Abhi Coaching: so yeah
    14/08/23, 9:30 pm - Deepansh Pandey: Okk
    14/08/23, 11:19 pm - Alka Coaching: <Media omitted>
    14/08/23, 11:19 pm - Alka Coaching: <Media omitted>
    14/08/23, 11:19 pm - Alka Coaching: <Media omitted>
    14/08/23, 11:19 pm - Alka Coaching: <Media omitted>
    14/08/23, 11:19 pm - Alka Coaching: <Media omitted>
    14/08/23, 11:19 pm - Alka Coaching: <Media omitted>
    14/08/23, 11:19 pm - Alka Coaching: <Media omitted>
    14/08/23, 11:19 pm - Alka Coaching: <Media omitted>
    14/08/23, 11:19 pm - Alka Coaching: <Media omitted>
    14/08/23, 11:19 pm - Alka Coaching: <Media omitted>
    14/08/23, 11:19 pm - Alka Coaching: <Media omitted>
    14/08/23, 11:19 pm - Alka Coaching: 21 Wall Street
    14/08/23, 11:20 pm - Alka Coaching: Baaki dominos and Pizza Hut bhi hain bagal me
    14/08/23, 11:20 pm - Alka Coaching: And 2 fancier places I know
    14/08/23, 11:24 pm - Abhi Coaching: Bhai mujhse itna nahi ho payega tum dono decide karlo
    14/08/23, 11:37 pm - Alka Coaching: Abe dekho bhai
    14/08/23, 11:39 pm - Abhi Coaching: Deepu is going
    I trust Deepu 
    Deepu will decide
    15/08/23, 6:17 am - Deepansh Pandey: Bhai imo around 200 hai sparkles mei... So 3 item udhr kr lenge... Round off 700 then agr chaho toh pizza Hut chl lenge udhr combo hai   400 k 4 pizza... Nhi toh ek aur hai 250 ke ke 2 ... Accordingly udhr bhi kr lenge
    15/08/23, 6:18 am - Deepansh Pandey: Thik m
    15/08/23, 6:18 am - Deepansh Pandey: ?
    15/08/23, 8:16 am - Abhi Coaching: <Media omitted>
    15/08/23, 9:56 am - Alka Coaching: 👌🏿
    15/08/23, 7:43 pm - Abhi Coaching: day well spent
    15/08/23, 7:43 pm - Abhi Coaching: <Media omitted>
    15/08/23, 7:43 pm - Abhi Coaching: <Media omitted>
    15/08/23, 7:43 pm - Abhi Coaching: <Media omitted>
    15/08/23, 7:43 pm - Abhi Coaching: <Media omitted>
    15/08/23, 7:43 pm - Abhi Coaching: <Media omitted>
    15/08/23, 7:43 pm - Abhi Coaching: <Media omitted>
    15/08/23, 7:43 pm - Abhi Coaching: <Media omitted>
    15/08/23, 7:43 pm - Abhi Coaching: <Media omitted>
    15/08/23, 7:43 pm - Abhi Coaching: <Media omitted>
    15/08/23, 7:43 pm - Abhi Coaching: <Media omitted>
    15/08/23, 7:43 pm - Abhi Coaching: <Media omitted>
    15/08/23, 7:43 pm - Abhi Coaching: <Media omitted>
    15/08/23, 7:43 pm - Abhi Coaching: <Media omitted>
    15/08/23, 8:05 pm - Deepansh Pandey: <Media omitted>
    15/08/23, 8:05 pm - Deepansh Pandey: <Media omitted>
    15/08/23, 8:05 pm - Deepansh Pandey: <Media omitted>
    15/08/23, 8:05 pm - Deepansh Pandey: <Media omitted>
    15/08/23, 8:05 pm - Deepansh Pandey: <Media omitted>
    15/08/23, 8:05 pm - Deepansh Pandey: <Media omitted>
    15/08/23, 8:05 pm - Deepansh Pandey: <Media omitted>
    15/08/23, 8:25 pm - Abhi Coaching: yaar teri dadi actually bahaut sweet hai
    15/08/23, 8:28 pm - Deepansh Pandey: Ha bhai...
    15/08/23, 8:28 pm - Deepansh Pandey: Actually sabhi log yr
    15/08/23, 8:35 pm - Abhi Coaching: but especially dadi ji
    15/08/23, 8:46 pm - Alka Coaching: Yeah 
    She loves meeting my friends 
    Mere jo dost unse mile hain, vo abhi tak dost hain
    15/08/23, 8:47 pm - Alka Coaching: Upar se sirf mere hi dosto se milti 
    Arihant Anwesha ke ni
    15/08/23, 8:52 pm - Alka Coaching: <Media omitted>
    15/08/23, 8:52 pm - Alka Coaching: <Media omitted>
    15/08/23, 8:52 pm - Alka Coaching: <Media omitted>
    15/08/23, 8:52 pm - Alka Coaching: <Media omitted>
    15/08/23, 8:52 pm - Alka Coaching: <Media omitted>
    15/08/23, 8:52 pm - Alka Coaching: <Media omitted>
    15/08/23, 8:52 pm - Alka Coaching: <Media omitted>
    15/08/23, 8:52 pm - Alka Coaching: <Media omitted>
    15/08/23, 8:52 pm - Alka Coaching: <Media omitted>
    15/08/23, 8:52 pm - Alka Coaching: <Media omitted>
    15/08/23, 8:52 pm - Alka Coaching: <Media omitted>
    15/08/23, 8:52 pm - Alka Coaching: <Media omitted>
    15/08/23, 8:52 pm - Alka Coaching: <Media omitted>
    15/08/23, 8:52 pm - Alka Coaching: <Media omitted>
    15/08/23, 8:52 pm - Alka Coaching: <Media omitted>
    15/08/23, 8:52 pm - Alka Coaching: <Media omitted>
    15/08/23, 8:52 pm - Alka Coaching: <Media omitted>
    15/08/23, 8:52 pm - Alka Coaching: <Media omitted>
    15/08/23, 8:52 pm - Alka Coaching: <Media omitted>
    15/08/23, 8:52 pm - Alka Coaching: <Media omitted>
    15/08/23, 8:52 pm - Alka Coaching: <Media omitted>
    15/08/23, 8:56 pm - Abhi Coaching: jo kehlo Bhai iPhone camera mei toh baap hai
    15/08/23, 8:56 pm - Deepansh Pandey: True that
    15/08/23, 9:00 pm - Alka Coaching: Bhai my photography skills yaar 
    Dekh ke moment liye hain
    15/08/23, 9:01 pm - Deepansh Pandey: Bhk
    15/08/23, 9:01 pm - Abhi Coaching: that was the joke
    15/08/23, 9:01 pm - Alka Coaching: Okay
    15/08/23, 9:01 pm - Deepansh Pandey: BTW guys 
    CSA mei I met this sigma
    15/08/23, 9:01 pm - Alka Coaching: Who?
    15/08/23, 9:02 pm - Deepansh Pandey: <Media omitted>
    15/08/23, 9:02 pm - Deepansh Pandey: <Media omitted>
    15/08/23, 9:02 pm - Deepansh Pandey: <Media omitted>
    15/08/23, 9:02 pm - Abhi Coaching: bro's buff
    15/08/23, 9:02 pm - Deepansh Pandey: Bhai bht badi hai
    15/08/23, 9:03 pm - Alka Coaching: He’s why I wanna have a mustache and wear janeu
    15/08/23, 9:04 pm - Deepansh Pandey: Bhai infact statue ki detailing dekh
    15/08/23, 9:04 pm - Deepansh Pandey: There are abs
    15/08/23, 9:04 pm - Alka Coaching: Piche banduk hogi
    15/08/23, 9:05 pm - Abhi Coaching: buff i said
    15/08/23, 9:05 pm - Abhi Coaching: tujhe bhai suit karegi you look better clean 😂😂
    15/08/23, 9:08 pm - Alka Coaching: True
    19/08/23, 6:22 pm - Deepansh Pandey: <Media omitted>
    19/08/23, 6:22 pm - Deepansh Pandey: <Media omitted>
    19/08/23, 6:22 pm - Deepansh Pandey: <Media omitted>
    19/08/23, 6:22 pm - Deepansh Pandey: <Media omitted>
    19/08/23, 6:22 pm - Deepansh Pandey: <Media omitted>
    19/08/23, 6:22 pm - Deepansh Pandey: <Media omitted>
    19/08/23, 6:22 pm - Deepansh Pandey: <Media omitted>
    19/08/23, 6:22 pm - Deepansh Pandey: <Media omitted>
    19/08/23, 6:35 pm - Alka Coaching changed their phone number to a new number. Tap to message or add the new number.
    19/08/23, 6:45 pm - Abhi Coaching: 4 seater hai?
    19/08/23, 7:40 pm - Deepansh Pandey: Temporary hai bhai
    19/08/23, 7:40 pm - Deepansh Pandey: Waise 3 seater hai yha sare
    19/08/23, 8:19 pm - You added Alka Coaching
    19/08/23, 8:20 pm - Deepansh Pandey: 9415485087 kiska hai?
    19/08/23, 8:21 pm - Deepansh Pandey: <Media omitted>
    19/08/23, 8:21 pm - Deepansh Pandey: <Media omitted>
    19/08/23, 8:21 pm - Deepansh Pandey: <Media omitted>
    19/08/23, 8:21 pm - Deepansh Pandey: <Media omitted>
    19/08/23, 8:21 pm - Deepansh Pandey: <Media omitted>
    19/08/23, 8:21 pm - Deepansh Pandey: <Media omitted>
    19/08/23, 8:21 pm - Deepansh Pandey: <Media omitted>
    19/08/23, 8:21 pm - Deepansh Pandey: <Media omitted>
    19/08/23, 8:21 pm - Alka Coaching: Bhai mummy ka
    19/08/23, 8:21 pm - Alka Coaching: Hatao ise
    19/08/23, 8:21 pm - You removed +91 94154 85087
    19/08/23, 8:22 pm - Deepansh Pandey: Done👍
    19/08/23, 8:23 pm - Alka Coaching: Bhai very posh hostel you’ve got
    19/08/23, 8:24 pm - Deepansh Pandey: Just khula hai hai n Bhai isliye
    19/08/23, 8:25 pm - Abhi Coaching: thapar ka bhi maal hai
    19/08/23, 8:26 pm - Abhi Coaching: i liked this
    19/08/23, 8:26 pm - Deepansh Pandey: Sbse bdiya toh uski library hai bhai
    19/08/23, 8:26 pm - Deepansh Pandey: Bhai ye tables hai abhi set nhi hui room mei
    19/08/23, 8:27 pm - Deepansh Pandey: They'll be set once we get into 3 seater
    19/08/23, 8:27 pm - Abhi Coaching: i thought aise hee set hai lol
    19/08/23, 8:27 pm - Abhi Coaching: yes yes
    19/08/23, 8:27 pm - Deepansh Pandey: Nhi bhai
    19/08/23, 8:27 pm - Abhi Coaching: wo bench wali feel aayegi
    19/08/23, 8:28 pm - Deepansh Pandey: Woh wali.... Na bhai 🥲
    19/08/23, 8:28 pm - Deepansh Pandey: We were just different
    19/08/23, 8:28 pm - Deepansh Pandey: Bhai 🤜🤛
    19/08/23, 8:30 pm - Abhi Coaching: 🤧🤧
    19/08/23, 8:30 pm - Abhi Coaching: senti mat kar ab firse
    19/08/23, 8:40 pm - Deepansh Pandey: 💦💦
    19/08/23, 8:55 pm - Alka Coaching: Vaha kaisi greenery bhai?
    19/08/23, 9:54 pm - Deepansh Pandey: Bs greenery hi baj
    19/08/23, 9:54 pm - Deepansh Pandey: Hai*
    19/08/23, 9:55 pm - Abhi Coaching: arey the rooms are good as compared to other hostels i meant
    19/08/23, 10:08 pm - Deepansh Pandey: But Bhai I was seriously saying... Mkc bs greenery hi hai
    19/08/23, 10:08 pm - Deepansh Pandey: Sb aisa hi hai
    19/08/23, 10:09 pm - Abhi Coaching: wo thapar ki baat kar Raha
    19/08/23, 10:16 pm - Alka Coaching: I meant big butts
    19/08/23, 10:16 pm - Abhi Coaching: teeo alag alag interpret kiye 😂
    20/08/23, 5:00 am - Deepansh Pandey: Bhai yha ldkiyo ka akaal hai
    20/08/23, 5:01 am - Deepansh Pandey: , 🥲
    20/08/23, 4:09 pm - Alka Coaching: https://youtube.com/shorts/cfFDoGLy0YM?feature=share
    20/08/23, 9:29 pm - Abhi Coaching: Bhai log meri bhi jaane ki dates aagayi 18 ko reporting 🫡
    20/08/23, 10:07 pm - Deepansh Pandey: <Media omitted>
    20/08/23, 10:41 pm - Alka Coaching: Ah shit 
    Time hai abhi 
    But new life now
    20/08/23, 10:42 pm - Abhi Coaching: yes yes acha hai na we'll meet
    20/08/23, 10:43 pm - Abhi Coaching: coincidence Deepu aur meri dates same
    20/08/23, 10:43 pm - Deepansh Pandey: Oh yeah
    30/08/23, 10:18 am - Deepansh Pandey: <Media omitted>
    30/08/23, 10:18 am - Deepansh Pandey: #couple goals
    30/08/23, 10:22 am - Abhi Coaching: fast forward mei lagra zombie dance karre
    30/08/23, 7:49 pm - Abhi Coaching: <Media omitted>
    30/08/23, 7:50 pm - Abhi Coaching: This message was deleted
    30/08/23, 7:51 pm - Deepansh Pandey: Are bc.... Baal aa gaye 🤣🤣
    30/08/23, 7:51 pm - Abhi Coaching: bhai iska expression dekh
    30/08/23, 7:51 pm - Abhi Coaching: idk kisse but similarity lagri kisi movie character se
    30/08/23, 7:51 pm - Deepansh Pandey: My boys... So happy to see them again... 
    Proud father 🥲
    30/08/23, 7:53 pm - Abhi Coaching: Bhai bhelpuri wale ke paas Tera khata khulwa Diya hai jab aana toh pay kardena
    30/08/23, 7:54 pm - Deepansh Pandey: <Media omitted>
    30/08/23, 7:56 pm - Abhi Coaching: Bhai couples dekh ke alakshendra ko tumari yaad aa rahi thi senti ho raha tha
    30/08/23, 8:12 pm - Deepansh Pandey: Couples dekh k meri??
    30/08/23, 8:13 pm - Abhi Coaching: haan tumhi toh ho humare ek laute laundiyabaz
    30/08/23, 8:13 pm - Abhi Coaching: 😂😂
    30/08/23, 8:13 pm - Deepansh Pandey: Khud ko bhul gaya sale???!
    30/08/23, 8:14 pm - Deepansh Pandey: Hypocrisy ki bhi seema hoti hai
    30/08/23, 8:14 pm - Abhi Coaching: jk hum jheel ka view dekh ke ye sochre the kaash thora aur time hota
    30/08/23, 8:14 pm - Abhi Coaching: fir socha Diwali mei aayenge ek week ke liye
    30/08/23, 8:14 pm - Abhi Coaching: tab mauj karenge
    30/08/23, 8:14 pm - Abhi Coaching: Bhai kabhi kabhi mera bhi Mann karta hai laundiyabaz bolne ka samjha karo
    30/08/23, 8:14 pm - Abhi Coaching: 😂😂😂
    30/08/23, 8:14 pm - Alka Coaching: Bhai deep thoughts with Deepu vibes thi Jheel kinare
    30/08/23, 8:15 pm - Abhi Coaching: wahi exactly
    30/08/23, 8:16 pm - Deepansh Pandey: Samay aane pr ye bhi kia jayega
    30/08/23, 9:59 pm - Alka Coaching: Inshallah
    01/09/23, 3:36 pm - Alka Coaching: <Media omitted>
    01/09/23, 3:36 pm - Alka Coaching: <Media omitted>
    01/09/23, 3:37 pm - Abhi Coaching: Perfectly dealt
    01/09/23, 3:39 pm - Abhi Coaching: if he was getting the same then why didn't he join us IIIT dwd better than bhagalpur?
    01/09/23, 3:40 pm - Alka Coaching: No it’s not 
    He’s a moron 
    Cse k chakkar me land college Gaya (usne saare cs waale upar rakhe honge)
    01/09/23, 3:41 pm - Abhi Coaching: gotcha
    01/09/23, 3:41 pm - Alka Coaching: Dharwad campus to hai hi ni 
    And placements are fuckall
    And we all make fun of Bhagalpur for being secluded, Dharwad might as well be on moon
    01/09/23, 3:41 pm - Abhi Coaching: he asked you all that just cuz he wanted to see where he's at the delusional comparison
    01/09/23, 3:41 pm - Alka Coaching: He’s at 5’4” 
    That’s where he’s at
    01/09/23, 3:42 pm - Abhi Coaching: 😂😂
    01/09/23, 3:43 pm - Deepansh Pandey: IIIT mei kewal placements achi hoti hai.. Aur dwd mei woh bhi achi nhi hoti
    01/09/23, 3:45 pm - Abhi Coaching: why did he go there fir
    01/09/23, 3:45 pm - Abhi Coaching: uska bhai bits pilani mei hai
    01/09/23, 3:45 pm - Abhi Coaching: saga bhai
    01/09/23, 3:45 pm - Deepansh Pandey: CSE k chakkar mei
    01/09/23, 3:45 pm - Alka Coaching: Government college clout and cs clout 
    Hoga jhaat ki kuch
    01/09/23, 3:45 pm - Alka Coaching: Bhai bits me bhi non circuital branches ka bura haal hai
    01/09/23, 3:46 pm - Deepansh Pandey: And after talking to others on college... IIIT mei branch hardly matters.... Curriculum is such ki yha sbko placement thdi mil jati hai
    01/09/23, 3:46 pm - Alka Coaching: Kehne ko chale jaao but fir 30 lac kharch k 9-10LPA ki job
    01/09/23, 3:46 pm - Abhi Coaching: samjha samjha
    01/09/23, 3:46 pm - Alka Coaching: Bhai udhar to sirf circuital hi hoti hai na that’s why placement is best
    01/09/23, 3:47 pm - Abhi Coaching: btw Deepu classes kabse?
    01/09/23, 3:47 pm - Alka Coaching: And bits me CSE is 300 +
    01/09/23, 3:48 pm - Deepansh Pandey: Mon
    01/09/23, 3:48 pm - Abhi Coaching: love how this gc lights up
    01/09/23, 3:48 pm - Deepansh Pandey: There are other reasons too
    01/09/23, 3:48 pm - Abhi Coaching: alka is going out today
    01/09/23, 3:48 pm - Deepansh Pandey: Yha ki ece is way different than that in other colleges
    01/09/23, 3:48 pm - Abhi Coaching: basically moving out
    01/09/23, 3:48 pm - Deepansh Pandey: Bye bye baby
    01/09/23, 3:49 pm - Alka Coaching: :)
    24/09/23, 1:56 pm - Abhi Coaching: oye photos bhej
    24/09/23, 2:16 pm - Deepansh Pandey: Ha
    24/09/23, 2:16 pm - Deepansh Pandey: Bhej
    24/09/23, 11:07 pm - Alka Coaching: Bhai upload hone de
    24/09/23, 11:33 pm - Abhi Coaching: kithe ghante mei hogi?
    25/09/23, 6:23 pm - Alka Coaching: Some time
    29/09/23, 6:29 pm - Abhi Coaching: <Media omitted>
    29/09/23, 6:31 pm - Abhi Coaching: <Media omitted>
    29/09/23, 6:35 pm - Alka Coaching: Bhai hotel ki tarah lag raha
    29/09/23, 6:35 pm - Alka Coaching: Photo dekh ke aankh bhar aayi (cum se)
    29/09/23, 6:35 pm - Alka Coaching: Sex macha ab khub
    29/09/23, 6:35 pm - Abhi Coaching: tuu kab bhejra
    29/09/23, 6:41 pm - Alka Coaching: <Media omitted>
    29/09/23, 6:44 pm - Abhi Coaching: 😂😂😂
    29/09/23, 6:52 pm - Deepansh Pandey: Bhai mai ro dunga
    29/09/23, 6:54 pm - Abhi Coaching: ayy phulwa rote nahi na
    29/09/23, 6:54 pm - Abhi Coaching: pyar karte hai tumse
    29/09/23, 6:54 pm - Abhi Coaching: itna toh karenge hee na
    29/09/23, 6:54 pm - Deepansh Pandey: 😂😂
    29/09/23, 6:54 pm - Deepansh Pandey: Aur baki sb thik?
    29/09/23, 6:55 pm - Abhi Coaching: bhai Gand faad di idhar udhar ghuma ghuma ke
    29/09/23, 6:55 pm - Abhi Coaching: finally Sara official document wala kaam khatam
    29/09/23, 6:55 pm - Abhi Coaching: ab kal se orientation
    29/09/23, 6:55 pm - Deepansh Pandey: Chl bdhiya
    29/09/23, 6:55 pm - Deepansh Pandey: Aram kr
    29/09/23, 6:55 pm - Deepansh Pandey: Ab nayi life strt teri bhi
    29/09/23, 7:00 pm - Abhi Coaching: haan abhi orientation ho jaane do teeno baith ke randi Rona karenge
    29/09/23, 7:25 pm - Deepansh Pandey: Sure sure
    30/09/23, 1:43 am - Alka Coaching: Bhai tu vaise hi kaafi hot ho raha aajkal, bus bandiyon se door rahiyo noch na le
    30/09/23, 5:05 am - Abhi Coaching: bhai yaar mai kuch bhi nahi yaha
    30/09/23, 5:05 am - Abhi Coaching: aise aise log hai na mai gayab hu
    30/09/23, 5:06 am - Abhi Coaching: ladkiya ekdum fashionable ladke behenchod model Wale kapde pehente
    30/09/23, 5:06 am - Abhi Coaching: plus point I have people taller than me here
    30/09/23, 5:06 am - Abhi Coaching: some Nigerian international students
    30/09/23, 5:06 am - Abhi Coaching: ek toh bc mujhse bhi 2-3 inch lamba tha
    30/09/23, 5:17 pm - Alka Coaching: Vo lund hai
    01/10/23, 10:13 am - Abhi Coaching: bhai tum dono mei se kisi ke pass C ke notes hai kya
    01/10/23, 10:14 am - Abhi Coaching: ho agar toh bhej diyo jab time mile
    01/10/23, 10:15 am - Deepansh Pandey: Ok
    01/10/23, 10:26 am - Abhi Coaching: <Media omitted>
    01/10/23, 12:06 pm - Alka Coaching: Sexy
    01/10/23, 12:07 pm - Alka Coaching: Let Us C khareed lo 
    Best book 
    Uske questions bhi kar lena 
    Notes chutiya hain
    01/10/23, 12:53 pm - Abhi Coaching: got it
    01/10/23, 12:53 pm - Abhi Coaching: i actually have that already
    01/10/23, 12:53 pm - Abhi Coaching: but Ghar pe padi hai bc
    01/10/23, 12:54 pm - Alka Coaching: Bus vahi kar and questions bhi uske karo saare
    01/10/23, 12:54 pm - Alka Coaching: Abe saale
    01/10/23, 12:54 pm - Abhi Coaching: mai mangwa leta hu
    01/10/23, 12:54 pm - Abhi Coaching: noted
    01/10/23, 12:57 pm - Deepansh Pandey: <Media omitted>
    01/10/23, 1:05 pm - Abhi Coaching: 🥰🥰
    01/10/23, 3:28 pm - Alka Coaching: Sexy
    09/10/23, 10:48 pm - Abhi Coaching: <Media omitted>
    09/10/23, 10:48 pm - Abhi Coaching: <Media omitted>
    09/10/23, 10:48 pm - Abhi Coaching: bach gaya bhai
    09/10/23, 10:57 pm - Deepansh Pandey: Nice bhai
    09/10/23, 10:57 pm - Alka Coaching: Kitti bandiyon ka DM aaya ye batao
    09/10/23, 11:27 pm - Abhi Coaching: Bhai pela gaya hu aur kuch nahi
    12/10/23, 2:46 pm - Abhi Coaching: null
    12/10/23, 2:47 pm - Alka Coaching: Hotel jaisa hostel 
    Model jaisa resident
    12/10/23, 2:47 pm - Abhi Coaching: Abey tute dil ka aashiq sala pichle 10 min se haaye jaa raha same song
    15/10/23, 1:47 pm - Abhi Coaching: <Media omitted>
    15/10/23, 1:48 pm - Abhi Coaching: ye dekho kya bakchodi karte ye hostel mei 😂😂
    15/10/23, 1:48 pm - Abhi Coaching: ek ladke photo click kari aur edit kardi
    15/10/23, 1:48 pm - Deepansh Pandey: Teri jhalak asharfee
    15/10/23, 1:48 pm - Abhi Coaching: bhayavah drishya bhai
    15/10/23, 1:48 pm - Alka Coaching: Bhai shitttt
    15/10/23, 1:49 pm - Abhi Coaching: iss tarah ka bully hota yaha 😂
    15/10/23, 1:49 pm - Alka Coaching: Bhai bahut acchi editing
    15/10/23, 1:49 pm - Abhi Coaching: bc upar se launda niche se patani kya kardiya
    15/10/23, 1:50 pm - Alka Coaching: Accha kiya
    15/10/23, 1:50 pm - Abhi Coaching: <Media omitted>
    15/10/23, 1:50 pm - Abhi Coaching: ye hai ladka
    15/10/23, 1:51 pm - Alka Coaching: Itni ladkiyan?!?!
    15/10/23, 1:51 pm - Deepansh Pandey: <Media omitted>
    15/10/23, 1:54 pm - Abhi Coaching: 😂😂😂
    15/10/23, 1:54 pm - Abhi Coaching: haan bhai lekin launda inke triple the
    16/10/23, 7:47 pm - Abhi Coaching: <Media omitted>
    16/10/23, 7:59 pm - Deepansh Pandey: <Media omitted>
    16/10/23, 7:59 pm - Abhi Coaching: <Media omitted>
    16/10/23, 7:59 pm - Abhi Coaching: do not use headphones
    16/10/23, 8:00 pm - Deepansh Pandey: 😂😂
    16/10/23, 8:01 pm - Abhi Coaching: <Media omitted>
    16/10/23, 8:15 pm - Alka Coaching: With great power cums
    16/10/23, 8:15 pm - Abhi Coaching: wo hawa ki power hai
    20/10/23, 12:16 am - Deepansh Pandey: <Media omitted>
    20/10/23, 12:18 am - Abhi Coaching: 😂😂😂
    20/10/23, 12:18 am - Abhi Coaching: badhiya Deepu ekdum mazdoor
    21/10/23, 12:15 am - Deepansh Pandey: <Media omitted>
    21/10/23, 12:15 am - Deepansh Pandey: <Media omitted>
    21/10/23, 12:16 am - Deepansh Pandey: <Media omitted>
    21/10/23, 12:17 am - Alka Coaching: Deepu ho Gaya hot
    21/10/23, 12:19 am - Alka Coaching: Abe zyada hi 
    Mai ghur raha 10 mint se
    21/10/23, 12:19 am - Deepansh Pandey: Bhai isiliye bheja
    21/10/23, 12:19 am - Deepansh Pandey: Hila le
    21/10/23, 12:19 am - Deepansh Pandey: Woh mujhe bhej dena
    21/10/23, 12:21 am - Deepansh Pandey: Bhai knp jake maine jo kaam kaha tha kr dena
    21/10/23, 12:22 am - Alka Coaching: Bilkul huzoor
    21/10/23, 12:33 am - Abhi Coaching: kya?
    21/10/23, 12:33 am - Abhi Coaching: mujhe bhi toh batao
    21/10/23, 12:33 am - Alka Coaching: Secret
    21/10/23, 12:34 am - Abhi Coaching: all is well wala feel
    21/10/23, 12:34 am - Deepansh Pandey: Totally
    21/10/23, 12:34 am - Abhi Coaching: 🥹🥹
    21/10/23, 12:40 am - Abhi Coaching: This message was deleted
    24/10/23, 9:51 pm - Deepansh Pandey: <Media omitted>
    24/10/23, 10:11 pm - Abhi Coaching: Abey bhai mera toh aur kharab tha yaar 😭😭
    24/10/23, 10:44 pm - Deepansh Pandey: Bhai but mera acha tha aaj ka
    25/10/23, 9:36 am - Abhi Coaching: dekhne mei bhi kaafi better lagra
    25/10/23, 9:36 am - Abhi Coaching: mere mei toh machine se roti banti hai moti moti aadhi kachii
    25/10/23, 9:47 am - Deepansh Pandey: Same here 
    But kal special tha
    25/10/23, 10:51 am - Abhi Coaching: maze toh alka le raha hai
    25/10/23, 11:03 am - Deepansh Pandey: 😒
    25/10/23, 12:37 pm - Alka Coaching: You know it buddy
    03/11/23, 11:57 pm - Abhi Coaching: pollution dekh
    03/11/23, 11:57 pm - Abhi Coaching: <Media omitted>
    03/11/23, 11:57 pm - Deepansh Pandey: Nice
    04/11/23, 12:00 am - Abhi Coaching: ye pehli building is my hostel
    04/11/23, 12:02 am - Deepansh Pandey: Earthquake aa gya guys
    04/11/23, 12:02 am - Deepansh Pandey: 😵‍💫
    04/11/23, 12:02 am - Abhi Coaching: haan bhai wo bhi
    06/11/23, 3:24 am - Abhi Coaching: <Media omitted>
    06/11/23, 8:45 am - Alka Coaching: Sojaya kar
    06/11/23, 10:06 am - Abhi Coaching: bas kal thoda crazy hogaya warna usually i sleep around 1
    06/11/23, 3:41 pm - Deepansh Pandey: <Media omitted>
    09/11/23, 7:32 am - Abhi Coaching: I'm home boys
    09/11/23, 7:33 am - Alka Coaching: Welcome back brother
    09/11/23, 7:36 am - Abhi Coaching: bhai kasam se itni oxygen aayi na kanpur enter karte hee
    09/11/23, 9:47 am - Deepansh Pandey: Ruk aa rha mai 5 min mei
    09/11/23, 10:39 am - Abhi Coaching: bhai I'm too tired ig poora time bas sounga
    09/11/23, 10:39 am - Abhi Coaching: kal subha milte
    09/11/23, 11:01 am - Deepansh Pandey: Mai aa rhaa.. Ghr ke bhr nikl
    09/11/23, 12:50 pm - Alka Coaching: Jala lo laudo
    09/11/23, 7:55 pm - Abhi Coaching: 😂😂😂
    09/11/23, 7:55 pm - Abhi Coaching: aao bey tum bhi jaldi aao
    09/11/23, 8:08 pm - Alka Coaching: null
    09/11/23, 8:09 pm - Abhi Coaching: Lolita padhne ka time kaha se milra 
    
    bags toh maine bhi 2 din pehle hee pach kardiye the 😂
    09/11/23, 8:10 pm - Abhi Coaching: null
    09/11/23, 8:41 pm - Alka Coaching: On bus adda
    09/11/23, 8:41 pm - Abhi Coaching: aaj nikalra?
    09/11/23, 8:42 pm - Alka Coaching: Ji
    09/11/23, 8:45 pm - Abhi Coaching: lessgooo
    09/11/23, 8:45 pm - Abhi Coaching: kab tak aayega?
    09/11/23, 9:02 pm - Deepansh Pandey: <Media omitted>
    09/11/23, 9:04 pm - Abhi Coaching: kya mtlb ghar jaa raha hu toh bag mei pathar aur cement le jaane ki zaroorat nahi
    09/11/23, 9:14 pm - Alka Coaching: Kal subah
    10/11/23, 7:54 am - Deepansh Pandey: Daddy's home bitch
    10/11/23, 8:11 am - Alka Coaching: Pranaam
    10/11/23, 9:49 am - Alka Coaching: null
    10/11/23, 9:51 am - Abhi Coaching: pardesi ghar aaya
    11/11/23, 3:32 pm - You started a call
    12/11/23, 12:19 am - Abhi Coaching: Diwali mein आपको मुंह से लेकर पिछवाड़े तक सुख समृधि दे; कोई भोसड़ी का आपकी झाट का बाल ना उखाड़ सके; आप सफलता की ऐसी माँ चोदे; कि सबकी फट जाये; आप पर आने वाले दुखों की बहन चुद जाये; कामयाबी हमेशा आपकी गांड में घुसी रहे। Diwali ki गांड फाड़ बधाई। 😎Bhai😝 Ki Taraf Se 😝 अब मत कहना कि बधाई नही दी।शुभ दीपावली
    12/11/23, 12:19 am - Abhi Coaching: boys hostel
    13/11/23, 11:59 am - Deepansh Pandey: Shaam ka kya scene?
    13/11/23, 12:42 pm - Abhi Coaching: alka batao
    13/11/23, 12:43 pm - Alka Coaching: Bhai ghar pe thodi dikkat coz vahi log vaala scene 
    But shaam ko bahar chalte 
    And ghar pe bhi mummy papa se mil lena
    13/11/23, 12:43 pm - Alka Coaching: Sham ko chalna kidhar vo aap log batayen
    13/11/23, 12:44 pm - Abhi Coaching: haan wo toh theek hai kaha chalre ye bata
    13/11/23, 12:45 pm - Alka Coaching: Tum dekho kuch 
    Mai bata ek do dhundh k
    13/11/23, 12:45 pm - Abhi Coaching: dekhta hu mai bhi
    13/11/23, 12:51 pm - Deepansh Pandey: 4??
    13/11/23, 12:51 pm - Abhi Coaching: pehle jagah toh dekh bhosdu
    13/11/23, 12:52 pm - Abhi Coaching: time toh ho hee jayega 😂
    13/11/23, 12:52 pm - Deepansh Pandey: Woh tu dekh
    13/11/23, 12:52 pm - Deepansh Pandey: Party teri pending hai🤣🤣
    13/11/23, 12:53 pm - Abhi Coaching: Abey yaar hum yahi nautanki karte at the end scooty ride karke aise hee kahi khaa ke aa jate 😂
    13/11/23, 12:53 pm - Abhi Coaching: raat gyi baat gyi 😂
    13/11/23, 12:54 pm - Deepansh Pandey: Chlega
    13/11/23, 12:54 pm - Abhi Coaching: done!
    13/11/23, 12:54 pm - Abhi Coaching: it's 4 then
    13/11/23, 12:54 pm - Deepansh Pandey: Ok
    13/11/23, 3:01 pm - Alka Coaching: 5 karlo
    13/11/23, 3:11 pm - Abhi Coaching: okay
    13/11/23, 4:01 pm - Alka Coaching: Bhai mere ghar me aaj kuch naatak chal raha 
    30 minutes me batata mera kya hai
    13/11/23, 4:02 pm - Abhi Coaching: haan dekh le mera bhi kuch toh ho raha
    13/11/23, 4:02 pm - Abhi Coaching: bata jaldi kaisa hai
    13/11/23, 4:05 pm - Abhi Coaching: zyada ho toh 15 ka rakh lete
    13/11/23, 4:06 pm - Deepansh Pandey: I'm busy on 15
    13/11/23, 4:07 pm - Abhi Coaching: bank?
    13/11/23, 4:07 pm - Deepansh Pandey: Kal
    13/11/23, 4:07 pm - Abhi Coaching: what about 16?
    13/11/23, 4:07 pm - Deepansh Pandey: 15 ko dooj hai
    13/11/23, 4:07 pm - Abhi Coaching: arey haan
    13/11/23, 4:07 pm - Deepansh Pandey: 17 ko ja rha.. 16 ko pack wack krne mei time ghus jayega
    13/11/23, 4:08 pm - Abhi Coaching: what about kal
    13/11/23, 4:08 pm - Deepansh Pandey: .
    13/11/23, 4:08 pm - Abhi Coaching: done kal mera fix
    13/11/23, 4:08 pm - Deepansh Pandey: Chaman... Kal bank ka kaam hai pure din
    13/11/23, 4:08 pm - Abhi Coaching: arey bc
    13/11/23, 4:09 pm - Deepansh Pandey: Chat toh pdho soordaas
    13/11/23, 4:09 pm - Abhi Coaching: aaj raat ko milega?
    13/11/23, 4:09 pm - Abhi Coaching: 😂😂
    13/11/23, 4:09 pm - Deepansh Pandey: Kamra khol k rkhna
    13/11/23, 4:10 pm - Abhi Coaching: chalo then aaj raat
    13/11/23, 4:10 pm - Abhi Coaching: ghoomna hoga toh saamne moti jheel mei bakchodi karlenge
    13/11/23, 4:10 pm - Deepansh Pandey: Decide kr lo tm doni
    13/11/23, 4:10 pm - Deepansh Pandey: Dono
    13/11/23, 4:54 pm - Alka Coaching: Kal karlo 
    Aaj guest aaye hain
    13/11/23, 4:54 pm - Abhi Coaching: okay
    13/11/23, 4:54 pm - Abhi Coaching: Deepu Bank bhi sirf 5 tak khulta hai
    13/11/23, 5:13 pm - Deepansh Pandey: Kal nhi ho payega
    13/11/23, 5:23 pm - Abhi Coaching: tum aur mai toh aaj milre hai
    13/11/23, 5:23 pm - Abhi Coaching: alka ko balcony se hi kardenge
    13/11/23, 5:25 pm - Alka Coaching: Jab aas pass ho to batana
    Agar free hua to aata Milne
    13/11/23, 5:25 pm - Abhi Coaching: agar nahi aayenge toh tu milega bas
    13/11/23, 5:26 pm - Deepansh Pandey: Bhai yha bhi mehmaan aa gaye 😅😅
    13/11/23, 5:26 pm - Deepansh Pandey: Bhai kuch n kuch krte hai thda wqt do...
    13/11/23, 5:26 pm - Deepansh Pandey: Milna toh hai hi
    13/11/23, 5:26 pm - Abhi Coaching: Abey toh raat tak toh jayenge na
    13/11/23, 5:27 pm - Abhi Coaching: warna kal raat
    13/11/23, 5:27 pm - Abhi Coaching: milenge toh hai hee
    13/11/23, 5:30 pm - Deepansh Pandey: Done done
    13/11/23, 10:10 pm - Deepansh Pandey: Pahoch gaye?
    13/11/23, 10:10 pm - Deepansh Pandey: <Media omitted>
    13/11/23, 10:10 pm - Deepansh Pandey: The only pic I got
    13/11/23, 10:11 pm - Deepansh Pandey: Abhi share kr dena tu
    13/11/23, 10:12 pm - Abhi Coaching: yesssir
    13/11/23, 10:12 pm - Abhi Coaching: <Media omitted>
    13/11/23, 10:12 pm - Abhi Coaching: <Media omitted>
    13/11/23, 10:39 pm - Deepansh Pandey: Contri kitne ki hui bata do
    13/11/23, 10:39 pm - Abhi Coaching: 200
    13/11/23, 10:39 pm - Deepansh Pandey: Bhk yha se
    13/11/23, 10:40 pm - Deepansh Pandey: Ye exclude krke bata,🤣🤣
    13/11/23, 10:40 pm - Abhi Coaching: <Media omitted>
    13/11/23, 10:42 pm - Deepansh Pandey: Moye moye
    13/11/23, 10:42 pm - Abhi Coaching: <Media omitted>
    13/11/23, 10:43 pm - Deepansh Pandey: Tu bday party kb de rha? 😂
    13/11/23, 10:44 pm - Abhi Coaching: <Media omitted>
    13/11/23, 10:45 pm - Abhi Coaching: abhi ko bhi add karle ab
    13/11/23, 10:50 pm - Deepansh Pandey: Ok
    13/11/23, 10:50 pm - You added Abhee
    13/11/23, 10:50 pm - Abhee: maqsad mt bhulna bhaiyaon!!!
    13/11/23, 10:51 pm - Abhi Coaching: <Media omitted>
    13/11/23, 10:51 pm - Deepansh Pandey: <Media omitted>
    13/11/23, 11:23 pm - Abhee: alka qr..
    13/11/23, 11:24 pm - Abhee: lekin aaj kal bada sawal ye hai ki ky abhinav urf abhii to apne paise wapas milenge...
    13/11/23, 11:24 pm - Abhi Coaching: damn abhee aate hee alka
    13/11/23, 11:24 pm - Abhee: bro alakshendra bht bada hai.
    13/11/23, 11:24 pm - Abhi Coaching: bhai bas yaad mat dila
    13/11/23, 11:24 pm - Abhee: spelling bhii ni aati meko toh
    06/12/23, 8:09 pm - Deepansh Pandey: <Media omitted>
    06/12/23, 8:09 pm - Deepansh Pandey: <Media omitted>
    07/12/23, 1:31 pm - Alka Coaching: Apna roz ka hai
    07/12/23, 1:32 pm - Abhi Coaching: alka finally back
    07/12/23, 1:32 pm - Alka Coaching: Tomorrow last test
    07/12/23, 1:32 pm - Abhi Coaching: tomorrow first test
    07/12/23, 1:33 pm - Deepansh Pandey: Day after tomorrow come meet daddy (me)
    07/12/23, 1:33 pm - Abhi Coaching: 🤝🏻
    07/12/23, 1:33 pm - Alka Coaching: Ji sir
    13/12/23, 6:38 pm - Abhi Coaching: <Media omitted>
    13/12/23, 6:57 pm - Abhi Coaching: I am happy to announce a free programming course by GeeksforGeeks to every first-year student at Galgotias University.  
    
    Key details of the program include:
    
    - Course Content: The course covers fundamental programming concepts essential for success in the ever-evolving field of computer science including all major languages (Python/JAVA/C++).     
    
    - Instructor: Sandeep Jain, the Founder and CEO of GeeksforGeeks, will guide the students through the course, providing valuable insights and expertise.
     The batch link for registration is [https://practice.geeksforgeeks.org/courses/programming-language-foundation-builder], and you can use the following coupon code for free access: GFGPLFB23.                             Also, let me know about your experience with this course.
    13/12/23, 6:58 pm - Deepansh Pandey: GFGPLFB23
    16/12/23, 12:36 am - Abhi Coaching: <Media omitted>
    16/12/23, 12:37 am - Alka Coaching: Kya baat hai bhai
    16/12/23, 12:37 am - Alka Coaching: Ye to hame bhi dekhna
    16/12/23, 12:37 am - Alka Coaching: Not the picture (just text)
    16/12/23, 12:37 am - Abhi Coaching: picture toh waise bhi save nahi ho paayi cuz WhatsApp
    16/12/23, 12:38 am - Abhi Coaching: wait
    16/12/23, 12:41 am - Alka Coaching: Pakka galti ni thi?
    16/12/23, 12:41 am - Abhi Coaching: <Media omitted>
    16/12/23, 12:41 am - Alka Coaching: Fuckkkkkkkkkkk
    16/12/23, 12:41 am - Abhi Coaching: maybe she was expecting something else
    16/12/23, 12:41 am - Abhee: bro is it what i think it is
    16/12/23, 12:41 am - Abhi Coaching: but the boys here gave wrong instructions
    16/12/23, 12:41 am - Alka Coaching: Yeah 👍🏿
    16/12/23, 12:42 am - Abhee: damnn
    16/12/23, 12:42 am - Alka Coaching: Obviously
    16/12/23, 12:42 am - Abhee: abhi jam ke add ne sikhaya tha
    16/12/23, 12:42 am - Abhee: sharing is caring
    16/12/23, 12:42 am - Abhi Coaching: what are you thinking abhee
    16/12/23, 12:42 am - Abhee: hot pic
    16/12/23, 12:42 am - Abhee: of her..
    16/12/23, 12:43 am - Abhi Coaching: arey bro WhatsApp is fucked up yaar warna pehle wahi share karta 😂
    16/12/23, 12:43 am - Abhi Coaching: ss blank ho jata yaha
    16/12/23, 12:43 am - Abhee: 😂😂
    16/12/23, 12:43 am - Abhee: screen recorder
    16/12/23, 12:43 am - Abhi Coaching: sure was bhai but the boys here took the wrong call
    16/12/23, 12:43 am - Abhi Coaching: i miss y'all
    16/12/23, 12:43 am - Abhee: fuckk bhai
    16/12/23, 12:43 am - Abhi Coaching: i tried, blank <This message was edited>
    16/12/23, 12:43 am - Alka Coaching: Lund
    16/12/23, 12:44 am - Abhi Coaching: ik you can see the proof 😂
    16/12/23, 12:44 am - Abhi Coaching: video*
    16/12/23, 12:44 am - Abhee: now only going to galgotia can fix me🥹
    16/12/23, 12:44 am - Abhi Coaching: she's not from here
    16/12/23, 12:44 am - Abhi Coaching: bataya toh school se
    16/12/23, 12:44 am - Abhee: ooh
    16/12/23, 12:44 am - Abhi Coaching: abhee bhai pay more attention to texts here
    16/12/23, 12:44 am - Abhee: behenchod barra kyu jaara tha mai🥹🥹
    16/12/23, 12:44 am - Abhi Coaching: yaha pictorial form se zyada interesting texts hote 😂
    16/12/23, 12:45 am - Alka Coaching: Kalyanpur chinaars on top :,)
    16/12/23, 12:45 am - Abhi Coaching: honestly if we met in the same school i would've been bitchless kyuki fir tumlog ke alawa kisi se baat hee nahi karta 😂
    16/12/23, 12:45 am - Abhi Coaching: side note acha hee hua baad mei mile
    16/12/23, 12:45 am - Alka Coaching: No offence abhii, tere ko pasand to ni ye
    16/12/23, 12:46 am - Alka Coaching: Ye jalwa
    16/12/23, 12:46 am - Abhee: deepu ko hai
    16/12/23, 12:46 am - Abhi Coaching: aprooved
    16/12/23, 12:46 am - Abhi Coaching: ab tu ye puchega saale?
    16/12/23, 12:46 am - Abhee: skill hai bhai achaa hua tu sikh gya
    16/12/23, 12:47 am - Abhee: key to happily 😂
    16/12/23, 12:47 am - Abhi Coaching: milne ke baad bhool bhi toh gaya 😂
    16/12/23, 12:47 am - Abhi Coaching: btw 
    welcome to bajrang dal abhee
    16/12/23, 12:47 am - Abhee: bc deepu hi krwa skta hai ni toh bc wo bhi bhagalpur mai reh reh kr
    16/12/23, 12:47 am - Abhee: bhul jayega
    16/12/23, 12:47 am - Abhi Coaching: 😂😂😂😂😂
    16/12/23, 12:48 am - Abhee: loving it here
    16/12/23, 12:48 am - Abhi Coaching: the second domain
    16/12/23, 12:48 am - Abhee: batao saala recent meetup mai sirf londo ki baatein..
    16/12/23, 12:49 am - Abhee: ya fr seniors ki
    16/12/23, 12:49 am - Abhi Coaching: mai bataunga na achi achi wait till I'm back 😂
    16/12/23, 8:45 am - Deepansh Pandey: Kids grow up... Don't be so immature yr... ! 
    Aur @917007242537  jb for once pic mile whatsapp pr.. Toh WhatsApp web pr woh pic khola kr aur fir laptop screen ki ki pic apne phone mei click kia kr..! 
    Yha laundo ke video se acha ladkiyo ke nudes share kro
    16/12/23, 8:46 am - Abhi Coaching: 😂😂😂😂
    16/12/23, 12:29 pm - Abhi Coaching changed this group's icon
    16/12/23, 7:54 pm - Deepansh Pandey: <Media omitted>
    16/12/23, 7:54 pm - Deepansh Pandey: <Media omitted>
    16/12/23, 7:54 pm - Deepansh Pandey: <Media omitted>
    16/12/23, 7:54 pm - Deepansh Pandey: <Media omitted>
    17/12/23, 3:43 am - Abhi Coaching: <Media omitted>
    17/12/23, 3:43 am - Abhi Coaching: just saving it here
    17/12/23, 10:42 am - Abhee: abe 2nd sem mai kisi ko data structures hai?
    17/12/23, 10:42 am - Abhee: @917307900795 tereko hai?
    17/12/23, 10:42 am - Deepansh Pandey: Ha
    17/12/23, 10:42 am - Abhee: algo bhi hai ky?
    17/12/23, 10:43 am - Deepansh Pandey: Dsa k andr hi ayega
    17/12/23, 10:43 am - Abhee: abe mere mai
    17/12/23, 10:43 am - Abhee: ds hai bss
    17/12/23, 10:43 am - Abhee: algo nahi hai
    17/12/23, 10:43 am - Deepansh Pandey: Uske andr hoga
    17/12/23, 10:44 am - Abhee: chaloo thikk
    17/12/23, 12:06 pm - Abhi Coaching: us moment
    17/12/23, 5:12 pm - Abhi Coaching: <Media omitted>
    24/12/23, 9:06 pm - Deepansh Pandey: <Media omitted>
    24/12/23, 9:09 pm - Deepansh Pandey: <Media omitted>
    24/12/23, 9:09 pm - Deepansh Pandey: <Media omitted>
    24/12/23, 9:09 pm - Deepansh Pandey: <Media omitted>
    24/12/23, 9:09 pm - Deepansh Pandey: <Media omitted>
    24/12/23, 9:09 pm - Deepansh Pandey: <Media omitted>
    24/12/23, 9:09 pm - Deepansh Pandey: <Media omitted>
    24/12/23, 9:09 pm - Deepansh Pandey: <Media omitted>
    24/12/23, 9:09 pm - Deepansh Pandey: <Media omitted>
    24/12/23, 9:09 pm - Deepansh Pandey: <Media omitted>
    24/12/23, 9:15 pm - Abhi Coaching: Deepu bana writer
    24/12/23, 9:16 pm - Alka Coaching: And more than that developer!!!
    24/12/23, 9:16 pm - Deepansh Pandey: Bkl main cheez mt dekh lena
    24/12/23, 9:16 pm - Abhi Coaching: alka wala toh 100% sach hai
    24/12/23, 9:16 pm - Deepansh Pandey: Pehli 3 lines meri hai baki gpt
    24/12/23, 9:16 pm - Alka Coaching: Isme link tumhare GPay ka hai?!
    24/12/23, 9:17 pm - Deepansh Pandey: Woh backend mei ata hai...
    24/12/23, 9:17 pm - Deepansh Pandey: Haven't even completed front end
    24/12/23, 9:18 pm - Abhi Coaching: isko toh g pe dunga mai
    24/12/23, 9:18 pm - Abhi Coaching: wo lag hee raha hai
    24/12/23, 9:19 pm - Alka Coaching: Bhai sexy ho rahi site 
    Yr 2 start me hi devops internship
    24/12/23, 9:20 pm - Deepansh Pandey: Are nhi yr.. DSA ho nhi rha tha😮‍💨😮‍💨 <This message was edited>
    24/12/23, 9:20 pm - Deepansh Pandey: Isliye idhr time waste kr dia
    24/12/23, 9:20 pm - Abhi Coaching: lekin site toh sexy hai
    24/12/23, 9:21 pm - Deepansh Pandey: Pay then 🥰🥰
    24/12/23, 9:21 pm - Abhi Coaching: kal aata hu
    24/12/23, 9:21 pm - Deepansh Pandey: Tomorrow I'll be out of town
    24/12/23, 9:21 pm - Deepansh Pandey: Day after rkh ke
    24/12/23, 9:21 pm - Deepansh Pandey: Le
    24/12/23, 9:28 pm - Abhi Coaching: okay
    24/12/23, 9:28 pm - Abhi Coaching: aur kisse g pe lene Jaa Raha hai
    24/12/23, 10:15 pm - Deepansh Pandey: Mandir ja rha hu balak 😊😊
    24/12/23, 10:15 pm - Abhi Coaching: konse
    24/12/23, 10:15 pm - Alka Coaching: Jai Shree Raam!!!
    24/12/23, 10:16 pm - Deepansh Pandey: Chandrika devi ji ka mandir
    24/12/23, 10:16 pm - Abhi Coaching: noiceee
    24/12/23, 10:16 pm - Deepansh Pandey: Jai shree raa🙏
    24/12/23, 10:17 pm - Deepansh Pandey: Raam*
    24/12/23, 10:17 pm - Abhi Coaching: Jai Mata di 🙏🏻
    24/12/23, 10:17 pm - Deepansh Pandey: Jai mata di
    24/12/23, 10:19 pm - Alka Coaching: Oh
    24/12/23, 10:26 pm - Abhee: radhe radhe
    24/12/23, 10:27 pm - Abhi Coaching: uthgaya Raja beta
    24/12/23, 10:27 pm - Abhee: hehehe
    24/12/23, 10:27 pm - Abhee: im getting tumbad vibess
    26/12/23, 10:12 am - Deepansh Pandey: Bithoor chale?
    26/12/23, 10:12 am - Abhee: ky krega udhr
    26/12/23, 10:13 am - Deepansh Pandey: Bhai wha amrood ki redi lagaunga
    26/12/23, 10:13 am - Abhee: as expected
    26/12/23, 10:13 am - Abhi Coaching: 😂😂😂
    26/12/23, 10:13 am - Deepansh Pandey: Tu bhi chalega?
    26/12/23, 10:14 am - Abhee: batate hain soch ke
    26/12/23, 10:14 am - Deepansh Pandey: Puch ke*
    26/12/23, 10:14 am - Abhee: abe ja
    mujhe kisi ki permission ni lgti
    26/12/23, 10:15 am - Abhee: tu hi hai nabalik
    26/12/23, 10:15 am - Deepansh Pandey: <Media omitted>
    26/12/23, 4:27 pm - Alka Coaching: <Media omitted>
    26/12/23, 4:32 pm - Alka Coaching: <Media omitted>
    26/12/23, 4:32 pm - Alka Coaching: <Media omitted>
    26/12/23, 4:32 pm - Alka Coaching: <Media omitted>
    26/12/23, 4:32 pm - Alka Coaching: <Media omitted>
    26/12/23, 4:32 pm - Alka Coaching: <Media omitted>
    26/12/23, 6:24 pm - Abhi Coaching: <Media omitted>
    26/12/23, 6:24 pm - Abhi Coaching: <Media omitted>
    26/12/23, 6:44 pm - Abhi Coaching: <Media omitted>
    26/12/23, 6:44 pm - Abhi Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:05 pm - Alka Coaching: <Media omitted>
    26/12/23, 7:11 pm - Deepansh Pandey: <Media omitted>
    26/12/23, 7:11 pm - Deepansh Pandey: <Media omitted>
    26/12/23, 7:11 pm - Deepansh Pandey: <Media omitted>
    26/12/23, 7:12 pm - Abhi Coaching: <Media omitted>
    26/12/23, 7:12 pm - Abhi Coaching: <Media omitted>
    26/12/23, 7:12 pm - Abhi Coaching: <Media omitted>
    26/12/23, 7:12 pm - Abhi Coaching: <Media omitted>
    26/12/23, 7:12 pm - Abhi Coaching: <Media omitted>
    27/12/23, 7:31 pm - Abhi Coaching: Kal bithoor chale?
    27/12/23, 7:32 pm - Alka Coaching: I’m in (bus din me rakhna)
    27/12/23, 7:32 pm - Abhi Coaching: haan raat mei thodi jayenge obviously
    27/12/23, 7:33 pm - Deepansh Pandey: Chal lo
    27/12/23, 7:33 pm - Alka Coaching: Matlab aate hue bhi shaam ni honi chahiye please
    27/12/23, 7:34 pm - Abhi Coaching: dekhlo jaisa ho
    27/12/23, 7:34 pm - Abhi Coaching: kuch hai waha ghoomne ko?
    27/12/23, 7:34 pm - Abhi Coaching: 🤔🤔
    27/12/23, 7:34 pm - Deepansh Pandey: Wait
    27/12/23, 7:34 pm - Deepansh Pandey: Join meeting
    27/12/23, 7:35 pm - Deepansh Pandey: https://meet.google.com/zsg-ntes-zju
    28/12/23, 8:37 am - Deepansh Pandey: Plan kya hai??
    28/12/23, 8:45 am - Abhi Coaching: bithoor rehene dete hai
    28/12/23, 8:46 am - Abhi Coaching: kaafi durr padega plus visibility itni kam hai wo road risky hai
    28/12/23, 10:04 am - Deepansh Pandey: Abe toh plan toh batao malik
    28/12/23, 10:25 am - Abhi Coaching: budhsen chaloge?
    28/12/23, 10:26 am - Abhi Coaching: restraunt type hai but waha momos, chat, kachori etc etc etc milta hai kafi acha lagta mujhe
    28/12/23, 10:27 am - Abhi Coaching: but that's not some place to enjoy sirf khane chalna ho toh theek hai
    28/12/23, 10:27 am - Deepansh Pandey: Bhai hum khane ka kya krnge
    28/12/23, 10:27 am - Abhi Coaching: khayenge?
    28/12/23, 10:28 am - Deepansh Pandey: 🤯🤯
    28/12/23, 10:28 am - Abhi Coaching: <Media omitted>
    28/12/23, 10:30 am - Abhi Coaching: bhai yaar jagah decide karna was never my thing 😂
    28/12/23, 10:30 am - Abhi Coaching: alka ko bulao koi
    28/12/23, 10:30 am - Deepansh Pandey: 😴
    28/12/23, 10:32 am - Deepansh Pandey: <Media omitted>
    28/12/23, 10:36 am - Abhi Coaching: 2 baje tak kuch decide nahi hua toh alka ke ghar
    28/12/23, 10:40 am - Deepansh Pandey: <Media omitted>
    28/12/23, 10:52 am - Abhee: guyss im not available today
    28/12/23, 11:05 am - Deepansh Pandey: No issues bhai... Paise bhej dena😂😂😂
    28/12/23, 11:06 am - Abhi Coaching: Deepu aaj kal sabse G pe leta hai
    28/12/23, 11:07 am - Deepansh Pandey: Its not like that.... Ur special 🥵
    28/12/23, 11:08 am - Abhi Coaching: <Media omitted>
    28/12/23, 11:09 am - Abhee: sharam kr le
    28/12/23, 11:44 am - Deepansh Pandey: 🥱🥱
    01/01/24, 12:19 am - Abhi Coaching: Happy new year bois
    01/01/24, 5:50 am - Abhi Coaching: <Media omitted>
    01/01/24, 5:52 am - Deepansh Pandey: Happy new year balak 🥳
    01/01/24, 7:27 am - Abhee: happy new year guyss!!
    01/01/24, 10:51 pm - Abhi Coaching: <Media omitted>
    06/01/24, 9:47 am - Deepansh Pandey: <Media omitted>
    06/01/24, 9:47 am - Deepansh Pandey: <Media omitted>
    06/01/24, 9:57 am - Abhi Coaching: ganga you beauty
    06/01/24, 2:36 pm - Alka Coaching: Tarr ho gay
    06/01/24, 2:36 pm - Abhee: tere campus mai road bhi ni bani abhi tk?
    06/01/24, 3:37 pm - Deepansh Pandey: Bani hai
    07/01/24, 3:19 am - Abhi Coaching: <Media omitted>
    07/01/24, 3:20 am - Abhee: avg rajisthani kids
    07/01/24, 3:21 am - Abhi Coaching: bhaii 💀
    08/01/24, 12:37 am - Abhi Coaching: <Media omitted>
    08/01/24, 12:38 am - Abhi Coaching: <Media omitted>
    12/01/24, 10:19 am - Deepansh Pandey: <Media omitted>
    12/01/24, 10:19 am - Deepansh Pandey: <Media omitted>
    12/01/24, 10:19 am - Deepansh Pandey: <Media omitted>
    12/01/24, 10:20 am - Abhee: jee baat londe🔥🔥
    12/01/24, 10:42 am - Abhi Coaching: damn deepu
    12/01/24, 10:42 am - Abhi Coaching: maal lagra
    12/01/24, 10:42 am - Abhee: pehli baaar
    12/01/24, 10:46 am - Abhi Coaching: Abey wo stud hai humesha maal lagta
    17/01/24, 12:33 am - Alka Coaching: Deepu mai chala hilaane
    17/01/24, 12:35 am - Deepansh Pandey: Are re... O hoo.... Bhaishb... Kiska reply aa gya
    17/01/24, 12:36 am - Deepansh Pandey: Are laundo aarti ki thali lao...
    17/01/24, 12:36 am - Deepansh Pandey: Ye bhaishb ki aarti utaro... Nhi toh chale jayenge
    17/01/24, 12:36 am - Alka Coaching: Baauji aa gaye
    17/01/24, 12:36 am - Abhee: 😂
    17/01/24, 12:36 am - Deepansh Pandey: <Media omitted>
    18/01/24, 12:27 am - Abhi Coaching: <Media omitted>
    18/01/24, 12:28 am - Abhi Coaching: <Media omitted>
    18/01/24, 12:29 am - Abhi Coaching: <Media omitted>
    18/01/24, 12:29 am - Abhi Coaching: today's events
    18/01/24, 12:30 am - Deepansh Pandey: 🤣🤣
    18/01/24, 12:30 am - Deepansh Pandey: 🔥
    18/01/24, 8:50 am - Abhi Coaching: bhai banda literally haath paer jod raha hai
    18/01/24, 9:02 am - Deepansh Pandey: Tu college mei hai ya university?
    18/01/24, 9:03 am - Abhi Coaching: Uni
    21/01/24, 10:37 am - Abhi Coaching: गलगोटिया यूनिवर्सिटी के  सोशियोलाजी के प्रोफेसर आदरणीय प्रदीप सिंह जी ने किया सुसाइड। ईश्वर उनकी आत्मा को अपने श्री चरणों में स्थान दें। हम सभी पुलिस जाँच की माँग करते है। #rip #justice
    21/01/24, 10:37 am - Abhi Coaching: <Media omitted>
    21/01/24, 10:37 am - Abhi Coaching: <Media omitted>
    21/01/24, 10:57 am - Deepansh Pandey: Bhai subh subh kya mst mood bna dia
    21/01/24, 10:57 am - Deepansh Pandey: Nice 👍
    21/01/24, 11:20 am - Abhi Coaching: anytime deepu
    21/01/24, 11:21 am - Abhee: khush kr ditta putr
    22/01/24, 1:00 am - Deepansh Pandey: <Media omitted>
    22/01/24, 3:02 am - Abhee: tu fr se reddit chalane laga?
    22/01/24, 10:14 am - Deepansh Pandey: Mai toh chalata hi hu
    22/01/24, 3:04 pm - Abhi Coaching: <Media omitted>
    22/01/24, 3:55 pm - Abhee: <Media omitted>
    22/01/24, 3:55 pm - Abhee: <Media omitted>
    22/01/24, 3:56 pm - Abhee: deepu ka booty king
    22/01/24, 3:56 pm - Abhee: @917307900795 kyu bsdke?
    22/01/24, 7:29 pm - Deepansh Pandey: 😂😂
    22/01/24, 7:30 pm - Deepansh Pandey: 👀👀meet session with salman
    22/01/24, 7:31 pm - Abhee: booty call bhai
    22/01/24, 7:32 pm - Abhee: tereko google meet  pe dikhata tha
    30/01/24, 11:20 pm - Alka Coaching: <Media omitted>
    30/01/24, 11:21 pm - Abhee: faak!! kisne kichi
    30/01/24, 11:21 pm - Abhi Coaching: arey BEHENCHODDDD
    30/01/24, 11:21 pm - Abhi Coaching: bhai maaal lagra hai bey
    30/01/24, 11:21 pm - Abhee: bht jada
    30/01/24, 11:21 pm - Alka Coaching: Dost ka kamera
    30/01/24, 11:21 pm - Abhi Coaching: new laptop same mere roommate ke paas hai
    30/01/24, 11:21 pm - Alka Coaching: 🥰
    30/01/24, 11:22 pm - Abhee: ab alka meri hai
    30/01/24, 11:22 pm - Abhee: 😂
    30/01/24, 11:22 pm - Alka Coaching: Yeah I told you no
    Kaafi sahi hai
    30/01/24, 11:22 pm - Abhi Coaching: for real bhai ye sala humesha underdressed ghumta hai
    30/01/24, 11:22 pm - Abhi Coaching: jaa bey
    30/01/24, 11:22 pm - Abhi Coaching: already competition tight hai <This message was edited>
    30/01/24, 11:22 pm - Alka Coaching: Bhai yahi to fayda hai 
    Zara se effort daal do
    Kaafi sahi ho jaata
    30/01/24, 11:23 pm - Alka Coaching: Dekhta hun jaise hi milti photos, I’ll send your way
    30/01/24, 11:23 pm - Abhee: ladka khel gya hai!!
    30/01/24, 11:24 pm - Abhi Coaching: tu janta nahi hai abhee issey
    30/01/24, 11:24 pm - Alka Coaching: Aayein
    30/01/24, 11:24 pm - Abhee: jald hi milte hain fr
    30/01/24, 11:24 pm - Abhi Coaching: kab ghar aa raha hai?
    30/01/24, 11:25 pm - Abhee: bhai mushkil hai bht holi pe aa paunga
    30/01/24, 11:25 pm - Abhee: probably uske baad hi jaunga
    30/01/24, 11:25 pm - Abhi Coaching: sab holi pe hee ayenge fir
    30/01/24, 11:25 pm - Abhi Coaching: mai bhi nahi jaunga ab
    30/01/24, 11:25 pm - Abhee: 🆗
    30/01/24, 11:28 pm - Abhi Coaching: <Media omitted>
    30/01/24, 11:40 pm - Deepansh Pandey: <Media omitted>
    30/01/24, 11:55 pm - Abhi Coaching: <Media omitted>
    31/01/24, 12:18 am - Deepansh Pandey: Kuch aur lagauna
    31/01/24, 12:19 am - Deepansh Pandey: Lagaunga*
    31/01/24, 12:20 am - Abhee: 😂😂
    31/01/24, 12:21 am - Abhi Coaching: <Media omitted>
    31/01/24, 4:57 pm - Abhi Coaching: <Media omitted>
    31/01/24, 4:58 pm - Alka Coaching: Bhai scary lag raha itna thanda 
    Chaai pi or coffee
    31/01/24, 4:58 pm - Abhi Coaching: kal exam hai
    31/01/24, 4:59 pm - Abhi Coaching: ikr smog abhi clear hogaya baarish ki wajeh se
    31/01/24, 4:59 pm - Abhi Coaching: warna visibility was zero
    31/01/24, 4:59 pm - Alka Coaching: Fuc
    03/02/24, 10:27 am - Deepansh Pandey: Agr alka humara saccha dost hai toh happy birthday ka msg aaj hi dalega bhabhi ko(agrima dwivedi)
    03/02/24, 10:27 am - Abhi Coaching: <Media omitted>
    03/02/24, 10:28 am - Abhi Coaching: +1
    03/02/24, 10:29 am - Deepansh Pandey: Koi BKL hi hoga ho apni dosti ke khatir ek bholi bhali ladki ko bday wish na kre
    03/02/24, 6:33 pm - Abhi Coaching: dekh saare messages ignored
    03/02/24, 6:33 pm - Abhi Coaching: 1-2 din baad dekhega aur ganda sa excuse dega
    03/02/24, 6:37 pm - Alka Coaching: Bhakk Saale
    03/02/24, 6:42 pm - Abhi Coaching: karde alex you've got a chance to make someone happy
    03/02/24, 7:12 pm - Alka Coaching: Bhai or bimaar ho jaaunga
    04/02/24, 1:38 pm - Abhee: https://meet.google.com/cvh-oasd-wbe
    04/02/24, 1:50 pm - Deepansh Pandey: Thanq bhai log...! 
    U made the day 😘
    04/02/24, 10:17 pm - Deepansh Pandey: <Media omitted>
    04/02/24, 10:17 pm - Deepansh Pandey: <Media omitted>
    04/02/24, 10:17 pm - Deepansh Pandey: <Media omitted>
    04/02/24, 10:18 pm - Deepansh Pandey: "Hum science ki trf se aaye hai"
    04/02/24, 11:58 pm - Alka Coaching: Bhai memories to aap bana rahe
    04/02/24, 11:59 pm - Abhi Coaching: for real bhai
    04/02/24, 11:59 pm - Abhi Coaching: generator ka idea bata dete bas full scene ho jata
    05/02/24, 1:23 am - Abhee: bhai ye audacity se iiitbh ki hoodie pehen kr ghusa hai??
    05/02/24, 1:23 am - Abhee: *kis
    05/02/24, 6:42 am - Deepansh Pandey: Nhi bhai jacket dusre ki pehna di thi
    05/02/24, 6:42 am - Deepansh Pandey: Bkl bihari kehte... Ayein!!?
    10/02/24, 2:22 pm - Abhi Coaching: <Media omitted>
    10/02/24, 2:35 pm - Abhee: damnnnnnnnnnn
    10/02/24, 2:35 pm - Abhee: tooo good bhaii
    10/02/24, 10:49 pm - Alka Coaching: Subah uth ke record kiya?
    Very good 
    Pink city hamara, pink sky aapka 
    Asali pink Deepu ki
    10/02/24, 10:49 pm - Abhi Coaching: haan subha 5 baje
    10/02/24, 10:50 pm - Abhi Coaching: <Media omitted>
    10/02/24, 10:50 pm - Abhi Coaching: <Media omitted>
    10/02/24, 10:51 pm - Abhi Coaching: <Media omitted>
    10/02/24, 10:51 pm - Alka Coaching: Atti sundar 
    Aap or aapki dedication
    10/02/24, 10:52 pm - Abhi Coaching: loneliness*
    10/02/24, 11:02 pm - Alka Coaching: Hum Hainn
    10/02/24, 11:02 pm - Abhi Coaching: issi ka toh sukoon hai
    13/02/24, 4:03 pm - Abhi Coaching: This message was deleted
    14/02/24, 12:50 pm - Alka Coaching: <Media omitted>
    14/02/24, 1:02 pm - Deepansh Pandey: Bhai pata nhi download nhi ho rha
    14/02/24, 1:03 pm - Abhi Coaching: same
    14/02/24, 1:03 pm - Abhi Coaching: mujhe laga mera issue hai
    14/02/24, 1:06 pm - Alka Coaching: Ruk I’ll send after editing
    14/02/24, 1:11 pm - Alka Coaching: <Media omitted>
    14/02/24, 1:41 pm - Deepansh Pandey: <Media omitted>
    14/02/24, 6:07 pm - Abhi Coaching: bhaiya ji toh chah gaye ladkiya hasse jaa rahi hai 😂
    14/02/24, 6:07 pm - Abhi Coaching: popularity at peak ayy
    14/02/24, 6:07 pm - Abhi Coaching: mujhe toh female cricket wala best laga
    14/02/24, 6:08 pm - Abhi Coaching: Jesus wala abhi acha tha
    14/02/24, 6:08 pm - Abhi Coaching: infact saare hee badhiya the <This message was edited>
    14/02/24, 6:25 pm - Alka Coaching: Thanks bhai 
    Thank you so much
    14/02/24, 6:25 pm - Alka Coaching: Love you
    14/02/24, 6:26 pm - Abhi Coaching: bhai jaldi match aaye yaar milna hai ab bahaut ho raha hai
    14/02/24, 6:28 pm - Alka Coaching: Sahi me
    14/02/24, 6:28 pm - Abhi Coaching: aaj raat group vc kare? <This message was edited>
    14/02/24, 6:28 pm - Abhi Coaching: free ho?
    14/02/24, 6:29 pm - Alka Coaching: Abhi tests chal re
    14/02/24, 6:29 pm - Abhi Coaching: kab khatam ho rahe?
    14/02/24, 6:29 pm - Abhi Coaching: mere end sems Aaj khatam huye
    14/02/24, 6:29 pm - Alka Coaching: Kal maths ka quiz hai, sabse khatarnak
    14/02/24, 6:30 pm - Abhi Coaching: all the best buddy you'll need it 😂
    15/02/24, 12:06 am - Abhi Coaching: Happy valentine's day alka 💗
    15/02/24, 12:08 am - Deepansh Pandey: Happy Valentine's Day to all 💦💦
    15/02/24, 8:20 am - Alka Coaching: Basant Panchami mubarak
    15/02/24, 9:07 am - Deepansh Pandey: Hardik shubhkamnaayein*
    15/02/24, 1:13 pm - Alka Coaching: Hard dick*
    15/02/24, 10:33 pm - Abhee: <Media omitted>
    15/02/24, 10:42 pm - Deepansh Pandey: Noice
    17/02/24, 10:57 pm - Deepansh Pandey: <Media omitted>
    17/02/24, 10:57 pm - Deepansh Pandey: <Media omitted>
    17/02/24, 10:58 pm - Deepansh Pandey: <Media omitted>
    17/02/24, 10:58 pm - Abhi Coaching: another crash?
    17/02/24, 10:58 pm - Deepansh Pandey: Yepp
    17/02/24, 10:59 pm - Abhi Coaching: demn 😂
    17/02/24, 10:59 pm - Abhi Coaching: bhai ab mai bhi karunga
    17/02/24, 10:59 pm - Deepansh Pandey: Bhai judge ki shadi thi
    17/02/24, 10:59 pm - Abhi Coaching: issi month karunga ruk
    17/02/24, 10:59 pm - Abhi Coaching: holy crap
    17/02/24, 10:59 pm - Abhi Coaching: marega saale
    17/02/24, 10:59 pm - Deepansh Pandey: Sare VVIPs the
    18/02/24, 12:24 pm - Alka Coaching: Damn bhai 
    Maare na kao kisi din
    18/02/24, 12:24 pm - Abhi Coaching: wahi mai bhi kehra
    18/02/24, 1:13 pm - Deepansh Pandey: Bhai kya bataye...papi pet karata hai ye kaam
    18/02/24, 1:18 pm - Alka Coaching: Bhai mere pass to bus pahad or gareebi hai
    18/02/24, 1:19 pm - Deepansh Pandey: <Media omitted>
    18/02/24, 3:17 pm - Alka Coaching: Sexy namo babi
    18/02/24, 3:19 pm - Abhi Coaching: This message was deleted
    18/02/24, 3:45 pm - Deepansh Pandey: Online hai yr.... Initially he was supposed to be present
    18/02/24, 4:20 pm - Alka Coaching: Damn bruh
    18/02/24, 4:23 pm - Abhi Coaching: Modi ji bhi sochne lage sala Bihar mei kya hee karunga jaa kar online hee karleta hu 😂
    18/02/24, 4:46 pm - Deepansh Pandey: Ngl... True stry
    20/02/24, 4:08 pm - Deepansh Pandey: <Media omitted>
    20/02/24, 4:10 pm - Abhi Coaching: <Media omitted>
    20/02/24, 4:10 pm - Alka Coaching: ek aad letters overcook ho gaye thoda sa
    20/02/24, 4:11 pm - Deepansh Pandey: Biggest moye moye in my life so far <This message was edited>
    20/02/24, 4:11 pm - Abhi Coaching: ye BAA konsa course hai Deepu
    20/02/24, 4:11 pm - Deepansh Pandey: Ayein!?
    20/02/24, 4:12 pm - Alka Coaching: it's only exclusive in gujarat.. it teaches "yo mom"
    20/02/24, 4:12 pm - Abhi Coaching: bad joke nvn
    20/02/24, 4:12 pm - Alka Coaching: i got it bruh
    20/02/24, 4:12 pm - Abhi Coaching: ye behen ka lauda jaha muh kholta hai...... 😂 <This message was edited>
    20/02/24, 4:13 pm - Abhi Coaching: tabhi toh meri darling hai
    20/02/24, 4:13 pm - Deepansh Pandey: Mereko smjha fir
    20/02/24, 4:13 pm - Alka Coaching: koi bkl hi hoga jo bro k liye na khole
    20/02/24, 4:13 pm - Alka Coaching: baaki colors dark ho gaye Bhagalpur me
    20/02/24, 4:14 pm - Abhi Coaching: bhai ghar kab aa raha hai I miss you 😭
    20/02/24, 4:14 pm - Alka Coaching: holi ke din rang mil jaate hai, homies ko makeout karvaate hain
    20/02/24, 4:15 pm - Deepansh Pandey: Ate woh dark nhi hai that's because of reflection
    20/02/24, 4:15 pm - Deepansh Pandey: Are*
    20/02/24, 4:15 pm - Alka Coaching: haan haan vo jox tha.... BRUH...
    20/02/24, 4:16 pm - Alka Coaching: tum log me se kisi ka first sem me vectors tha?
    20/02/24, 4:16 pm - Deepansh Pandey: Bhai jox toh ye hai ki maine jaise imagine kia tha waisa hi hai... Information aur Bhagalpur pata nhi madarchod kaha se aa gaya
    20/02/24, 4:17 pm - Deepansh Pandey: 🤚
    20/02/24, 4:17 pm - Alka Coaching: jaha se aap aaye bhaijaan
    20/02/24, 4:17 pm - Deepansh Pandey: Gote mei se?
    20/02/24, 4:17 pm - Alka Coaching: notes, assignments, q papers and answers and shit
    20/02/24, 4:17 pm - Alka Coaching: jossA
    20/02/24, 4:18 pm - Abhi Coaching: next sem mei hai ab
    20/02/24, 4:18 pm - Deepansh Pandey: Nikal doa gya tha usme se mujhe... Remember 😇😇
    20/02/24, 4:18 pm - Deepansh Pandey: Mujhse umeed na rakh
    20/02/24, 4:18 pm - Alka Coaching: fata fat bhej do jo bhi material hai, meri gand fati hai... kuch samajh ni aa raha
    20/02/24, 4:18 pm - Deepansh Pandey: +1
    20/02/24, 4:18 pm - Alka Coaching: to kisse?
    20/02/24, 4:18 pm - Alka Coaching: 8.7
    20/02/24, 4:19 pm - Deepansh Pandey: Sab moh maya hai bkl.. 
    Yha ek hafte mei paper hai aur ek akshar nhi padha
    20/02/24, 4:19 pm - Abhi Coaching: alex iss baar tereko mauka milega isse pelne ka
    20/02/24, 4:20 pm - Abhi Coaching: ache se kootna
    20/02/24, 4:20 pm - Deepansh Pandey: Hum dono mei ghodi usually woh bnta hai ... Toh pelunga mai 😘
    20/02/24, 4:20 pm - Alka Coaching: tum bhai meethe hi jalaye jaaoge saale chashni k chod
    20/02/24, 4:20 pm - Abhi Coaching: issiliye precise kiya
    20/02/24, 4:21 pm - Deepansh Pandey: Bkl alakshendra hai tera naam... Chasni nhi
    20/02/24, 4:21 pm - Abhi Coaching: alka badass hote jaa raha hai
    20/02/24, 4:21 pm - Abhi Coaching: 😂😂
    20/02/24, 4:21 pm - Deepansh Pandey: Damn thay ass😈
    20/02/24, 4:21 pm - Abhi Coaching: gay allegations just got shifted to Deepu now
    20/02/24, 4:22 pm - Alka Coaching: ye saala marte dum tak "mai gareeb, maine kuch ni padha, bhai fail" karta rahega
    20/02/24, 4:22 pm - Deepansh Pandey: Abe jaa n jaake toffee kha... Bade log baat kar rhe hau
    20/02/24, 4:22 pm - Deepansh Pandey: Hai
    20/02/24, 4:22 pm - Deepansh Pandey: Mat maan bhai ksm se yhi haal hai
    20/02/24, 4:22 pm - Abhi Coaching: avg topper instincts
    20/02/24, 4:23 pm - Abhi Coaching: <Media omitted>
    20/02/24, 4:23 pm - Deepansh Pandey: Topper hata de.. Average k sahare hu mai
    20/02/24, 4:24 pm - Alka Coaching: ye duniya agar mil bhi jaaye to kya hai
    20/02/24, 4:24 pm - Abhi Coaching: i remember this
    20/02/24, 4:25 pm - Deepansh Pandey: Kya hai?
    20/02/24, 4:25 pm - Alka Coaching: lund mera
    20/02/24, 4:26 pm - Abhi Coaching: real
    20/02/24, 4:26 pm - Abhi Coaching: bhai alex mil yaar jaldi
    20/02/24, 4:26 pm - Abhi Coaching: 😂😂😂
    20/02/24, 4:27 pm - Alka Coaching: bhai mai khud dab raha syllabus ke andar, holi pe 9-10 days ki chhutti hai
    20/02/24, 4:27 pm - Abhi Coaching: kab se kab tak?
    20/02/24, 4:27 pm - Abhi Coaching: mai 22 ko aa raha
    20/02/24, 4:27 pm - Alka Coaching: mai bhi most prolly
    20/02/24, 4:28 pm - Abhi Coaching: kab tak hai chuttiya?
    20/02/24, 4:29 pm - Alka Coaching: 22-31march
    20/02/24, 4:29 pm - Abhi Coaching: noiceee
    20/02/24, 4:30 pm - Abhi Coaching: exams kabse?
    20/02/24, 4:30 pm - Alka Coaching: 29 feb 1st
    20/02/24, 4:30 pm - Abhi Coaching: med sems hai na?
    20/02/24, 4:31 pm - Alka Coaching: yes
    20/02/24, 4:31 pm - Abhi Coaching: alright
    20/02/24, 4:31 pm - Abhi Coaching: btw forward kar dena sab
    20/02/24, 4:32 pm - Alka Coaching: meko khud chahiye... @917307900795 kisi topper friend se hi dhund valo
    20/02/24, 4:51 pm - Deepansh Pandey: Bade log 😭😭
    20/02/24, 4:51 pm - Alka Coaching: yes
    22/02/24, 6:52 pm - Abhi Coaching: https://tennews.in/apple-and-galgotias-university-forge-partnership-to-empower-future-ios-developers/
    22/02/24, 7:43 pm - Deepansh Pandey: Ja beta tujhe siri bula rhi hai
    22/02/24, 7:44 pm - Abhi Coaching: bas kuch theek thak log mil jaaye
    22/02/24, 7:44 pm - Abhi Coaching: plus ye sirf dikhawa karte hai padhana toh aata nahi
    22/02/24, 7:44 pm - Deepansh Pandey: Hr jgh ka wahi haal hai
    23/02/24, 12:36 pm - Deepansh Pandey: <Media omitted>
    23/02/24, 12:36 pm - Deepansh Pandey: <Media omitted>
    23/02/24, 12:37 pm - Abhi Coaching: competition khatam karne ki ninja technique 😂😂😂
    25/02/24, 2:02 pm - Deepansh Pandey: https://join.slickapp.co/ma5p
    25/02/24, 2:02 pm - Deepansh Pandey: Referal code : ma5p
    25/02/24, 2:03 pm - Deepansh Pandey: Bhaiyo this is the link to an app called slick
    25/02/24, 2:03 pm - Deepansh Pandey: Download kr lena and verify using ur college id and use this  referral code
    25/02/24, 2:04 pm - Deepansh Pandey: Yha college mei bakchodi bakchodi mei competition lga hua hai kaun kitne krwa payega
    25/02/24, 2:04 pm - Deepansh Pandey: So do it... Baki baad mei chaho toh delete kr dena
    25/02/24, 2:08 pm - Abhi Coaching: okay
    25/02/24, 2:08 pm - Abhi Coaching: kya kya karate rehta hai Deepu 🥱
    25/02/24, 3:03 pm - Alka Coaching: Mai already hun yaar
    25/02/24, 3:05 pm - Abhi Coaching: 💁‍♂️ Invite partners to the bot and get paid for them!
    
    Send this link to a friend:
    https://t.me/Tgbotsponsor_bot?start=5786363312
    200 ₹ for each partner you invite
    The referral is counted only after your friend has activated the bot!
    
    ◽️Users invited: 0
    ◽️Earnings: 0 ₹
    25/02/24, 3:05 pm - Abhi Coaching: ye join karo
    25/02/24, 3:06 pm - Abhi Coaching: fatafat
    25/02/24, 3:07 pm - Abhi Coaching: paisa milra issey ek senior hai wo bola hai party dega 😂
    25/02/24, 3:07 pm - Abhi Coaching: bata dena jab karlena toh
    25/02/24, 3:11 pm - Deepansh Pandey: Kr lia
    25/02/24, 4:03 pm - Abhi Coaching: okay
    26/02/24, 11:49 am - Abhi Coaching: <Media omitted>
    26/02/24, 11:53 am - Deepansh Pandey: Abe fake hoga
    26/02/24, 11:53 am - Deepansh Pandey: Nhi toh koi ek hi hogi multiple times
    11/03/24, 8:08 pm - Abhi Coaching: <Media omitted>
    11/03/24, 8:08 pm - Abhi Coaching: <Media omitted>
    11/03/24, 8:08 pm - Abhi Coaching: the crowd here
    11/03/24, 9:01 pm - Abhee: chora intelligent lage manne..
    11/03/24, 9:02 pm - Abhi Coaching: rajasthani kyu bolra
    11/03/24, 9:47 pm - Deepansh Pandey: Pedophile hai sala
    11/03/24, 9:54 pm - Abhi Coaching: Wo toh tu bhi hai
    11/03/24, 9:55 pm - Abhee: bss mann kr gya
    13/03/24, 3:47 pm - Abhi Coaching: apne apne GitHub profiles bhejo
    13/03/24, 7:05 pm - Deepansh Pandey: <Media omitted>
    13/03/24, 7:29 pm - Abhi Coaching: 😂😂
    13/03/24, 7:49 pm - Abhi Coaching: null
    13/03/24, 8:25 pm - Alka Coaching: I support
    13/03/24, 9:50 pm - Deepansh Pandey: Noice
    17/03/24, 1:10 am - Alka Coaching: <Media omitted>
    17/03/24, 1:10 am - Alka Coaching: <Media omitted>
    17/03/24, 1:10 am - Alka Coaching: <Media omitted>
    17/03/24, 1:10 am - Alka Coaching: <Media omitted>
    17/03/24, 1:10 am - Alka Coaching: <Media omitted>
    17/03/24, 1:10 am - Alka Coaching: <Media omitted>
    17/03/24, 1:10 am - Alka Coaching: <Media omitted>
    17/03/24, 1:10 am - Alka Coaching: <Media omitted>
    17/03/24, 1:10 am - Alka Coaching: <Media omitted>
    17/03/24, 1:10 am - Alka Coaching: <Media omitted>
    17/03/24, 1:10 am - Alka Coaching: <Media omitted>
    17/03/24, 1:11 am - Deepansh Pandey: 👍👍💦💦
    23/03/24, 11:59 am - Abhi Coaching: <Media omitted>
    23/03/24, 11:59 am - Abhi Coaching: ye mere class ka Muslim ladka hai Issey kisi ne color laga diya
    23/03/24, 10:34 pm - Deepansh Pandey: Shi kiye
    23/03/24, 10:41 pm - Alka Coaching: Bullah na maano, holi hai
    23/03/24, 10:42 pm - Deepansh Pandey: Bullah ki jana mai kaun
    24/03/24, 12:06 am - Deepansh Pandey: null
    24/03/24, 12:41 am - Abhi Coaching: null
    24/03/24, 9:38 am - Abhi Coaching: If you r willing to learn more about Islam try learning the biography of our beloved prophet Muhammad whose biography is learnt by Mahatma Gandhi and many more famous warriors and see what they had said about prophet Muhammad
    24/03/24, 9:38 am - Abhi Coaching: ek group hai usmei ye bhejra hai
    24/03/24, 9:38 am - Abhi Coaching: 😂😂
    24/03/24, 9:39 am - Deepansh Pandey: I have a doubt
    24/03/24, 9:41 am - Deepansh Pandey: The marriage with ayesha was consummated at the age of 9 or 11?
    24/03/24, 9:41 am - Abhi Coaching: Bhai bawal ho jayega 😂
    24/03/24, 9:42 am - Abhi Coaching: The problem is ki agar usne koi comeback diya toh lack of knowledge is wajeh se mai reply nahi de paunga acha
    24/03/24, 9:44 am - Deepansh Pandey: Acha chor ye bata ladki ke baap ko nikah-e-mutah mei kitne paise dene padenge ek raat k liye?
    24/03/24, 9:46 am - Abhi Coaching: bhai deepu is definitely the person i'm going to for any religious, historical or political disrespect I need to know 😂😂 <This message was edited>
    24/03/24, 10:08 am - Abhi Coaching: bhai ye LinkedIn bc kitna mehenga hai bey
    24/03/24, 10:09 am - Abhi Coaching: uska lowest subscription 23 days ke liye hai 1850/-
    
    aur highest 23 days ke liye 9k+
    24/03/24, 10:09 am - Deepansh Pandey: Koi nhi bhai time aane de take over kar lenge 😏
    24/03/24, 10:09 am - Deepansh Pandey: Ohh... Tu iski baat kr rha tha
    24/03/24, 10:09 am - Abhi Coaching: ek month bhi nahi 23 fucking days
    24/03/24, 10:09 am - Abhi Coaching: haan buddhu 😂🤦🏻‍♂️
    25/03/24, 11:31 am - Abhi Coaching: happy holi bhailog ♥️✨
    25/03/24, 1:41 pm - Deepansh Pandey: Happy holi bhaiyo
    25/03/24, 1:43 pm - Deepansh Pandey: <Media omitted>
    25/03/24, 1:43 pm - Deepansh Pandey: <Media omitted>
    25/03/24, 1:44 pm - Abhi Coaching: bicep flex
    25/03/24, 1:44 pm - Abhi Coaching: <Media omitted>
    25/03/24, 1:44 pm - Deepansh Pandey: Bas
    25/03/24, 1:44 pm - Deepansh Pandey: !
    25/03/24, 1:45 pm - Abhi Coaching: nai nahi aur hongi
    25/03/24, 1:45 pm - Abhi Coaching: abhi mere phone pe nahi
    25/03/24, 1:45 pm - Deepansh Pandey: Abe arya nagar nhi gaya?
    25/03/24, 1:45 pm - Abhi Coaching: bhejta hu baad mei
    25/03/24, 1:45 pm - Abhi Coaching: naa
    25/03/24, 1:45 pm - Deepansh Pandey: Abe sale
    25/03/24, 1:45 pm - Abhi Coaching: ghar pe hee khatarnak hogyi
    25/03/24, 1:45 pm - Abhi Coaching: kal gaya tha lekin alex ne fir ditch kardiya
    25/03/24, 1:46 pm - Deepansh Pandey: 😕
    02/05/24, 12:43 am - Abhi Coaching: https://x.com/TheJonyVerma/status/1785696352447705299?t=hqIQIudZs0Nh53z14gkjPQ&s=08
    02/05/24, 12:46 am - Abhi Coaching: This message was deleted
    02/05/24, 12:49 am - Abhee: dammnn bhai
    02/05/24, 12:50 am - Abhee: 😂
    02/05/24, 12:50 am - Abhee: gand fad diya reporter ne
    02/05/24, 12:52 am - Abhi Coaching: bhai bezzati
    02/05/24, 12:53 am - Abhi Coaching: aaj se tum nahi jaante mai galgotias mei hu
    02/05/24, 12:53 am - Abhi Coaching: samjhe?
    02/05/24, 12:53 am - Abhee: ky bolna hai fr
    02/05/24, 12:54 am - Abhee: abhinav kaha pdhta hai
    02/05/24, 12:55 am - Deepansh Pandey: GALGOTIYA UNIVERSITY
    Jaha apple ne ios development kab bnaya hai
    02/05/24, 12:56 am - Abhee: abhi toh mana kiye ye ni bolna hai <This message was edited>
    02/05/24, 12:56 am - Deepansh Pandey: BKL tu pogo khel jaakr.. Aur fir kapil sharma show... Tere bas ki nhi sarcasm smjhna
    02/05/24, 12:57 am - Abhi Coaching: bhai bolde drop out hai
    02/05/24, 12:57 am - Abhi Coaching: kyuki degree toh gyi maa chudane
    02/05/24, 12:57 am - Abhee: 😂
    02/05/24, 12:57 am - Abhi Coaching: bhechod
    02/05/24, 12:57 am - Abhi Coaching: 😂😂😂
    02/05/24, 12:57 am - Abhi Coaching: 😂😂
    02/05/24, 12:58 am - Abhee: gand mara laude
    02/05/24, 12:59 am - Deepansh Pandey: <Media omitted>
    02/05/24, 1:29 am - Abhi Coaching: https://x.com/dhruv_rathee/status/1785638844240412741?t=r7ZpbvCURt6QkSXYekpNfg&s=08
    02/05/24, 1:29 am - Abhi Coaching: the most awaited one
    02/05/24, 1:29 am - Abhi Coaching: finally
    02/05/24, 7:51 am - Alka Coaching: Delhi me Har jagah same hai (tu jaanta kisi ko inme?)
    02/05/24, 8:01 am - Abhi Coaching: haan 2 chutiye meri class ke
    02/05/24, 8:01 am - Abhi Coaching: ek toh cr hai mera but unn wo sirf bg mei hai
    02/05/24, 8:32 am - Alka Coaching: CR chutiye hi hote hain😊
    02/05/24, 9:07 am - Abhi Coaching: agreed
    02/05/24, 9:07 am - Abhi Coaching: deepu would now understand when i hesitate to mention my uni 😂
    02/05/24, 9:24 am - Deepansh Pandey: Once ur in it... Just bloody own it
    02/05/24, 9:25 am - Abhi Coaching: shut up Deepu maths padh jaa ke
    02/05/24, 9:48 am - Alka Coaching: take the man out of the bihar not the bihar out the man
    02/05/24, 9:51 am - Abhi Coaching: Bihar is an emotion
    02/05/24, 1:32 pm - Alka Coaching: Lose (e)motion
    02/05/24, 4:30 pm - Alka Coaching: <Media omitted>
    02/05/24, 4:40 pm - Abhi Coaching: ye kaha pe tha? 😂
    02/05/24, 4:40 pm - Alka Coaching: ethics quiz
    02/05/24, 6:47 pm - Deepansh Pandey: All ki jgh none ka misprint ho gya shud
    02/05/24, 6:47 pm - Deepansh Pandey: Shyd*
    02/05/24, 7:00 pm - Abhi Coaching: <Media omitted>
    02/05/24, 7:00 pm - Abhi Coaching: <Media omitted>
    02/05/24, 7:00 pm - Abhi Coaching: <Media omitted>
    02/05/24, 8:15 pm - Alka Coaching: kaafi brutalist photos bhai, nice @917007242537
    02/05/24, 8:18 pm - Abhi Coaching: it's not iiit bh yaha buildings are well finished 😂
    02/05/24, 8:18 pm - Abhi Coaching: tho it seems so
    08/05/24, 7:54 am - Deepansh Pandey: <Media omitted>
    08/05/24, 7:55 am - Abhi Coaching: baaki dono buildings toh theek hai ye beech wali ko Superman ka spaceship kyu bana diya
    08/05/24, 7:55 am - Alka Coaching: Chid gaya bhadwa
    08/05/24, 7:56 am - Alka Coaching: Sundar hai vaise kaafi
    08/05/24, 7:56 am - Abhi Coaching: agreed
    08/05/24, 7:56 am - Deepansh Pandey: Teri gaand iske kone pr tikane ke liye
    08/05/24, 7:56 am - Deepansh Pandey: 😈💦💦
    08/05/24, 7:57 am - Deepansh Pandey: @918299433225 Tu kb aaaa rha knp?
    08/05/24, 7:57 am - Alka Coaching: 17
    08/05/24, 7:57 am - Abhi Coaching: Bihar jaa ke badtameez hogaya hai
    08/05/24, 7:58 am - Deepansh Pandey: @917007242537 we're gonna  have sex without you 😌😌
    08/05/24, 7:58 am - Abhi Coaching: mera last exam 16 ko hai 🥲🥲
    08/05/24, 7:58 am - Abhi Coaching: midsems ka
    08/05/24, 7:59 am - Deepansh Pandey: Mahuda
    16/05/24, 12:37 pm - Abhi Coaching: shaam ko group vc hai
    16/05/24, 12:37 pm - Abhi Coaching: nahi aaye toh gay allegations on you
    16/05/24, 12:37 pm - Alka Coaching: Mai taxi ne honga
    16/05/24, 12:37 pm - Alka Coaching: Vo ton already hai
    16/05/24, 12:39 pm - Abhi Coaching: koi baat nahi
    16/05/24, 12:39 pm - Abhi Coaching: 5 min ke liye attend karlena
    16/05/24, 12:39 pm - Alka Coaching: 🫡
    16/05/24, 12:49 pm - Deepansh Pandey: Bsdk.. Allegations nhi hai woh
    16/05/24, 12:51 pm - Abhi Coaching: This message was deleted
    16/05/24, 12:51 pm - Abhi Coaching: 😂😂
    16/05/24, 12:53 pm - Abhi Coaching: saale you're not getting exempted attend karni padegi call bhale hee 5 min
    16/05/24, 12:53 pm - Deepansh Pandey: Ok
    16/05/24, 2:35 pm - Abhee: timings ky hai sir @917007242537
    16/05/24, 5:25 pm - Abhi Coaching: This message was deleted
    16/05/24, 5:25 pm - Abhi Coaching: 6 pm
    16/05/24, 6:06 pm - Abhi Coaching: null
    16/05/24, 6:08 pm - Deepansh Pandey: https://meet.google.com/tkm-kpuc-rgh
    06/06/24, 5:40 pm - Deepansh Pandey: <Media omitted>
    06/06/24, 5:45 pm - Abhee: what is this place
    06/06/24, 5:46 pm - Abhi Coaching: 😭😭😭😭😭😭
    06/06/24, 5:47 pm - Abhi Coaching: <Media omitted>
    06/06/24, 5:49 pm - Abhi Coaching: <Media omitted>
    06/06/24, 5:49 pm - Abhi Coaching: <Media omitted>
    06/06/24, 5:49 pm - Abhi Coaching: <Media omitted>
    06/06/24, 5:49 pm - Alka Coaching: Kya din tha yaar bhai vo
    06/06/24, 5:49 pm - Deepansh Pandey: <Media omitted>
    06/06/24, 5:49 pm - Abhi Coaching: you don't know abhee
    06/06/24, 5:49 pm - Abhi Coaching: 😂😂
    06/06/24, 5:49 pm - Abhi Coaching: bhai dadhi aane lagi
    06/06/24, 5:49 pm - Abhi Coaching: lessgooo
    06/06/24, 5:50 pm - Abhi Coaching: also new phone?
    06/06/24, 5:50 pm - Alka Coaching: Nahi bhai
    Reshe hain
    06/06/24, 5:50 pm - Alka Coaching: Bhai Deepu se pehle tune notice kiya
    06/06/24, 5:50 pm - Deepansh Pandey: Bhai mai abhi notice kr rha
    06/06/24, 5:51 pm - Abhi Coaching: fir bhi tu dhokha deta hai
    06/06/24, 5:51 pm - Abhi Coaching: unfair world people
    06/06/24, 5:51 pm - Alka Coaching: Kaha Bebs
    06/06/24, 5:51 pm - Deepansh Pandey: Mera bada hai
    06/06/24, 5:52 pm - Abhi Coaching: irony
    06/06/24, 5:53 pm - Abhi Coaching: chalo enjoy mai jaa raha sone
    06/06/24, 5:53 pm - Abhi Coaching: kal fir practical hai
    06/06/24, 5:53 pm - Deepansh Pandey: All the best
    06/06/24, 5:53 pm - Deepansh Pandey: Me doing practical fr
    06/06/24, 5:53 pm - Abhi Coaching: <Media omitted>
    06/06/24, 5:54 pm - Abhi Coaching: <Media omitted>
    06/06/24, 5:54 pm - Abhi Coaching: alka sirf meri hai
    13/06/24, 2:54 pm - Alka Coaching: <Media omitted>
    13/06/24, 3:08 pm - Abhee: ghar ke bade
    13/06/24, 4:22 pm - Abhi Coaching: alex aur uski mun wali bandi
    13/06/24, 4:52 pm - Deepansh Pandey: Alka khud bandi hai
    13/06/24, 4:53 pm - Alka Coaching: Bhai launde baithe
    13/06/24, 4:53 pm - Abhi Coaching: piche dekh
    13/06/24, 4:54 pm - Alka Coaching: Oh vo 
    Bhai vo apni saheli ni 😔
    13/06/24, 4:55 pm - Abhi Coaching: kyu nahi hai abhi tak?
    13/06/24, 4:56 pm - Alka Coaching: Shy launda mai🤓
    13/06/24, 4:56 pm - Abhi Coaching: jaa bey 😂
    25/06/24, 1:12 pm - Abhi Coaching: linkdin mei bhi short videos aagaye
    25/06/24, 1:12 pm - Abhi Coaching: hadd kardiye ye log
    27/06/24, 4:23 pm - Abhi Coaching: <Media omitted>
    27/06/24, 6:05 pm - Alka Coaching: Bhai dil ki baat keh di 
    Mujhe lagta sirf mujhe hi bura lagta ye overpriced tatti
    27/06/24, 6:14 pm - Deepansh Pandey: Ye desh tarakki kyu nhi kr rha  hai... ? 
    
    Yr bhadwe vande bharat ke khane ka review krna toh bn kre....
    27/06/24, 6:31 pm - Abhi Coaching: bhai that was just the review of that popcorn vande Bharat se kya relation??
    27/06/24, 6:34 pm - Alka Coaching: Tray dikh rahi photo me bhyomkesh Bakshi ko
    27/06/24, 6:35 pm - Deepansh Pandey: Laude ksm kha kr bta vande bharat ka nhi hai?
    27/06/24, 6:37 pm - Abhi Coaching: chutiye ko har jagah commentary karni hoti sala dadi kahi ka
    27/06/24, 6:37 pm - Abhi Coaching: Abey hai vande Bharat ka lekin message ka point wo nahi tha na lodu
    27/06/24, 6:38 pm - Alka Coaching: Me?🥺
    27/06/24, 7:51 pm - Abhi Coaching: back in the city bois
    28/06/24, 9:42 pm - Abhi Coaching: photos bhej
    28/06/24, 9:45 pm - Alka Coaching: <Media omitted>
    28/06/24, 9:45 pm - Alka Coaching: <Media omitted>
    28/06/24, 9:45 pm - Alka Coaching: <Media omitted>
    28/06/24, 9:45 pm - Alka Coaching: <Media omitted>
    28/06/24, 9:57 pm - Deepansh Pandey: 👍👍
    28/06/24, 9:57 pm - Deepansh Pandey: Couple goals
    28/06/24, 10:24 pm - Abhee: madard
    28/06/24, 10:24 pm - Abhee: *madar
    28/06/24, 10:24 pm - Abhee: akele akele
    28/06/24, 10:24 pm - Abhi Coaching: sudden plan
    28/06/24, 10:33 pm - Abhee: bhen ki lodi raand
    28/06/24, 10:33 pm - Abhee: raandwe ho saalon
    28/06/24, 10:41 pm - Abhi Coaching: Abey abhi firse milenge kal deepu jaa raha na
    28/06/24, 10:41 pm - Abhi Coaching: aayega toh fir chalenge dhang se kahi
    28/06/24, 10:45 pm - Abhee: kal??
    28/06/24, 10:45 pm - Abhee: kaha
    28/06/24, 10:51 pm - Abhi Coaching: family trip
    28/06/24, 10:51 pm - Abhee: papa ke bina??
    28/06/24, 10:51 pm - Abhee: surprise hai ky mere liye?
    28/06/24, 10:52 pm - Abhi Coaching: 😂😂
    28/06/24, 10:56 pm - Deepansh Pandey: Abe kal ka postpone ho gya shyd?
    29/06/24, 7:21 pm - Alka Coaching: @917307900795 darshan ho gaye?
    29/06/24, 7:24 pm - Deepansh Pandey: Na bhai
    29/06/24, 7:24 pm - Deepansh Pandey: Kal nikalne ka plan hai
    29/06/24, 7:24 pm - Deepansh Pandey: Aaj nhi nikle
    05/07/24, 10:24 pm - Abhi Coaching: Abey ye shardendu phone kyu kar raha hai raat ko
    05/07/24, 10:25 pm - Abhi Coaching: whatsapp call kiya fir normal call kiya
    05/07/24, 10:25 pm - Alka Coaching: Baat karo to ek baar… someone must
    05/07/24, 10:25 pm - Abhi Coaching: maine pick nahi kiya
    05/07/24, 10:26 pm - Abhi Coaching: bhai kya bolunga mere college toh inferior hee hai na aur wo bhadwa koi mauka nahi chorta taana maarne ka
    05/07/24, 10:51 pm - Deepansh Pandey: I wanna talk to him then😋
    05/07/24, 10:53 pm - Abhi Coaching: number du? 😂
    05/07/24, 10:55 pm - Deepansh Pandey: Bhai pgl kutta aakr tujhe kate toh smjh ata hai.... 
    BC uske paas jake katwane mei kya smjhdari
    05/07/24, 10:55 pm - Abhi Coaching: 😂😂😂
    05/07/24, 10:55 pm - Abhi Coaching: with this Deepu and his good examples and timing make a comeback <This message was edited>
    05/07/24, 10:56 pm - Alka Coaching: Bhai kisi ko to baat karni padegi
    05/07/24, 10:56 pm - Alka Coaching: Abhhi is the least meanest that’s why I guess he’s calling
    05/07/24, 10:59 pm - Deepansh Pandey: There's a reason he didn't call me
    05/07/24, 10:59 pm - Deepansh Pandey: 😂😂
    05/07/24, 11:01 pm - Abhi Coaching: well I'd definitely make him feel better but after the call what if I don't
    05/07/24, 11:01 pm - Abhi Coaching: 😵‍💫😵‍💫😵‍💫
    05/07/24, 11:02 pm - Deepansh Pandey: When things go out of hands... Call papa (me)
    05/07/24, 11:02 pm - Abhi Coaching: tell that to your son dendu
    05/07/24, 11:03 pm - Deepansh Pandey: We all know who's been referred to here 😘
    05/07/24, 11:03 pm - Abhi Coaching: shutup Deepu humesha wahi joke bhakk 😂
    05/07/24, 11:06 pm - Deepansh Pandey: Ha beta hamare jokes ab purane lagne lage 🌚
    05/07/24, 11:10 pm - Abhi Coaching: <Media omitted>
    12/07/24, 7:33 pm - Abhee: <Media omitted>
    12/07/24, 7:37 pm - Abhi Coaching: context?
    12/07/24, 7:42 pm - Abhee: deepu batayega
    12/07/24, 7:45 pm - Abhi Coaching: gotcha
    12/07/24, 7:45 pm - Abhi Coaching: mahi
    12/07/24, 7:45 pm - Abhee: tujhe pata hai?
    12/07/24, 7:46 pm - Abhi Coaching: itna obvious karega toh samjh hee jaunga na 😂
    12/07/24, 7:46 pm - Abhee: okay
    12/07/24, 7:46 pm - Abhee: kb mil ra bhai
    12/07/24, 7:46 pm - Abhee: mai chala jaunga
    12/07/24, 7:46 pm - Abhee: next week
    12/07/24, 7:47 pm - Abhi Coaching: kal milte hai subha tak confirm karta hu
    13/07/24, 10:43 am - Abhi Coaching: what's the scene mil sakte aaj 12-1 baje around?
    13/07/24, 11:31 am - Deepansh Pandey: @919580158054 ...
    13/07/24, 11:31 am - Abhee: abe dopahar mai milega?
    13/07/24, 11:36 am - Deepansh Pandey: Shaam tk kr lo fir
    13/07/24, 11:39 am - Deepansh Pandey: Woh sb chor... Rainbow 🌈 kyu dala?
    13/07/24, 11:57 am - Abhi Coaching: I'm free ussi time isliye kehra <This message was edited>
    13/07/24, 11:58 am - Abhi Coaching: 2 baje chal lo
    13/07/24, 12:09 pm - Abhi Coaching: warna fir kal rakho
    13/07/24, 12:21 pm - Deepansh Pandey: @919580158054
    13/07/24, 12:26 pm - Abhee: ky krna hai tu bata
    13/07/24, 12:27 pm - Abhee: 😂😂😂
    13/07/24, 12:27 pm - Deepansh Pandey: Mujhe nhi pata be
    13/07/24, 12:27 pm - Abhee: bata bsdke
    13/07/24, 12:27 pm - Abhee: kal rakhte hai
    13/07/24, 12:27 pm - Abhee: shaam ko?
    13/07/24, 12:28 pm - Abhi Coaching: theek
    13/07/24, 12:28 pm - Deepansh Pandey: Ok
    13/07/24, 12:28 pm - Abhi Coaching: dopeher mei kyu nahi aate tumlog? <This message was edited>
    13/07/24, 12:28 pm - Abhee: bc garmii
    13/07/24, 12:28 pm - Abhee: bhai
    13/07/24, 12:29 pm - Abhi Coaching: acha
    13/07/24, 12:30 pm - Deepansh Pandey: Ha mc tan ho jayega na
    13/07/24, 12:31 pm - Abhi Coaching: abhi ladki bulati toh sala exact 12 baje wahi khada milta 😂
    13/07/24, 12:31 pm - Abhi Coaching: fir number bhi nahi deti 🥰
    13/07/24, 12:53 pm - Abhee: pitegaa saaale
    13/07/24, 12:54 pm - Abhi Coaching: uske liye bhi toh milna padega na
    13/07/24, 12:54 pm - Abhi Coaching: 🥰🥰
    13/07/24, 12:54 pm - Abhee: aata hu rukk tu
    13/07/24, 12:54 pm - Abhee: babu bhaiya se panga leta hai tu
    13/07/24, 12:59 pm - Abhi Coaching: aa jaa
    14/07/24, 1:44 pm - Deepansh Pandey: Ha bsdk kya plan hai?
    14/07/24, 1:55 pm - Abhee: aaj ni ho payega
    14/07/24, 1:55 pm - Abhee: maasi ke ghr pe pooja hai
    14/07/24, 1:56 pm - Abhee: achaa ye batao
    14/07/24, 1:56 pm - Abhee: kitte baje se free ho?
    14/07/24, 1:56 pm - Abhee: 4 baje se pehle aana hai hmko wapas
    14/07/24, 8:18 pm - Deepansh Pandey: Thik hai
    14/07/24, 8:18 pm - Deepansh Pandey: Toh kab nikle?
    14/07/24, 9:05 pm - Abhi Coaching: bas abhi 2 ghante mei
    14/07/24, 9:06 pm - Abhee: nikal ja tu <This message was edited>
    14/07/24, 9:06 pm - Abhee: aata hu mai
    14/07/24, 9:06 pm - Abhi Coaching: mujhe 15 min lagta tum poch ke call Karo
    14/07/24, 9:25 pm - Deepansh Pandey: Abe kaha marwa rhe ho
    14/07/24, 9:25 pm - Deepansh Pandey: Wait kr rha hu jldi pohcho <This message was edited>
    14/07/24, 9:50 pm - Abhi Coaching: bas aagaya 2 min wo metro wale bhaiya ki detection machine mei kuch dikkat aagayi hai check kar rahe
    16/07/24, 5:06 pm - Abhi Coaching: yaar mummy ka eye doctor ka appointment hai
    16/07/24, 5:06 pm - Abhi Coaching: kal din mei nahi mil sakte?
    27/07/24, 6:39 pm - Deepansh Pandey: <Media omitted>
    27/07/24, 6:39 pm - Deepansh Pandey: <Media omitted>
    27/07/24, 6:51 pm - Abhi Coaching: bhai wo ajeeb sa building figure kya hai last mei?
    27/07/24, 6:52 pm - Abhee: chii bhaii
    27/07/24, 6:56 pm - Deepansh Pandey: Machuda bc <This message was edited>
    27/07/24, 6:58 pm - Alka Coaching: Bhai gajab sundar
    27/07/24, 6:59 pm - Deepansh Pandey: Bhai bas tu hi yaar hai mera
    27/07/24, 6:59 pm - Deepansh Pandey: 😘😘
    27/07/24, 6:59 pm - Alka Coaching: Road bhi pink 😏
    27/07/24, 7:00 pm - Deepansh Pandey: Galgotiya aur bvp ki sadko pr itni gadiya chalti hai ki woh ab kali ho gyi hai🌚
    27/07/24, 7:02 pm - Alka Coaching: Sarkari ni hain na sadken tumhari tarah sabki
    27/07/24, 7:02 pm - Abhi Coaching: bhai genuine question tha mera
    27/07/24, 7:03 pm - Alka Coaching: Abe hum log nikle to the bagal se jab bairaaj gaye the
    27/07/24, 7:04 pm - Abhi Coaching: lol
    27/07/24, 7:05 pm - Alka Coaching: AI centre hoga 
    Yahi karte management vaale
    27/07/24, 7:09 pm - Deepansh Pandey: Computer centre n library
    27/07/24, 7:16 pm - Abhi Coaching: reminded me of kalki ka complex
    27/07/24, 7:24 pm - Alka Coaching: Same difference 😉
    04/08/24, 10:30 am - Deepansh Pandey: <Media omitted>
    04/08/24, 10:30 am - Deepansh Pandey: <Media omitted>
    04/08/24, 10:30 am - Deepansh Pandey: You deleted this message
    04/08/24, 10:30 am - Deepansh Pandey: You deleted this message
    04/08/24, 10:31 am - Abhee: bhai hare kurte wale
    04/08/24, 10:31 am - Abhee: delete kr
    04/08/24, 10:31 am - Abhee: bhai katua lag ra.huuu
    04/08/24, 10:31 am - Deepansh Pandey: Bhaiyo parso apni marzi se chunkr koi bhi photo daal skte ho stry pe
    04/08/24, 10:31 am - Abhee: mt kr bhaiiii
    04/08/24, 10:31 am - Abhee: wo delete kr de bss
    04/08/24, 10:31 am - Abhee: hara kurta
    04/08/24, 10:32 am - Deepansh Pandey: <Media omitted>
    04/08/24, 10:32 am - Abhee: badwe
    04/08/24, 10:32 am - Deepansh Pandey: <Media omitted>
    04/08/24, 10:32 am - Deepansh Pandey: Ab thik hai 🤣🤣🤣
    05/08/24, 2:16 pm - Abhi Coaching: https://drive.google.com/file/d/10ROYdWb69m7Sas9uKAsHAQvllkQ1v2-i/view?usp=sharing
    05/08/24, 2:16 pm - Abhi Coaching: hd quality
    05/08/24, 2:16 pm - Abhi Coaching: dual audio
    05/08/24, 2:40 pm - Deepansh Pandey: 🥰
    05/08/24, 2:40 pm - Deepansh Pandey: 😘😘
    05/08/24, 3:08 pm - Abhi Coaching: near hd * <This message was edited>
    28/08/24, 8:21 pm - Abhi Coaching: https://meet.google.com/hjx-vunf-div
    28/08/24, 11:25 pm - Deepansh Pandey: bhaiyo i am sorry jldi chor di aaj ki meet
    28/08/24, 11:25 pm - Alka Coaching: Kitne bane laude
    28/08/24, 11:25 pm - Deepansh Pandey: happy birthday @918299433225 
    sorry yr bhool gya tha
    28/08/24, 11:26 pm - Deepansh Pandey: woh bhi nhi de paya , got stuck somewhere else
    28/08/24, 11:26 pm - Alka Coaching: Love you guys 
    Thanks a lot
    28/08/24, 11:26 pm - Alka Coaching: Choot
    28/08/24, 11:27 pm - Deepansh Pandey: uske chakkar mei contest thde hi chorunga beech mei
    28/08/24, 11:30 pm - Abhi Coaching: Love you too babydoll 😚
    28/08/24, 11:32 pm - Alka Coaching: Sure sure
    09/10/24, 6:13 pm - Abhi Coaching: <Media omitted>
    09/10/24, 6:31 pm - Deepansh Pandey: MC ye woh hai hi nhi!
    09/10/24, 6:31 pm - Deepansh Pandey: Us bdwale ne msg nhi likha!!
    09/10/24, 6:34 pm - Alka Coaching: SAALE NE CHUTIYA KAATA
    09/10/24, 6:35 pm - Deepansh Pandey: <Media omitted>
    09/10/24, 6:36 pm - Deepansh Pandey: Bhadwe ki complain karne ja rha mai
    09/10/24, 6:36 pm - Abhee: rukk mai call krke maa chodta hu
    09/10/24, 6:36 pm - Abhee: han mc ko line pe lee
    09/10/24, 6:36 pm - Abhee: mere ko add kr
    09/10/24, 6:36 pm - Abhee: maa ka bhosda kr dunga
    09/10/24, 6:38 pm - Deepansh Pandey: MC utha nhi rha
    09/10/24, 7:00 pm - Abhi Coaching: 😂😂😂
    09/10/24, 7:00 pm - Abhi Coaching: liyoooo
    13/10/24, 11:06 pm - Abhi Coaching: <Media omitted>
    13/10/24, 11:07 pm - Alka Coaching: Chutmari ka clones bana k hila raha
    13/10/24, 11:07 pm - Abhi Coaching: skills
    13/10/24, 11:08 pm - Abhi Coaching: and leetcode timeline dekh iski
    13/10/24, 11:08 pm - Abhee: kon hai
    13/10/24, 11:08 pm - Abhee: ye
    13/10/24, 11:08 pm - Abhee: guys??
    13/10/24, 11:08 pm - Abhi Coaching: may se lekar abhi tak everyday streak
    13/10/24, 11:08 pm - Abhi Coaching: both on leetcode and github4
    13/10/24, 11:08 pm - Abhi Coaching: hum teeno ko common irritation
    13/10/24, 11:08 pm - Abhee: elaborate
    13/10/24, 11:09 pm - Abhee: coaching ka dost ?
    13/10/24, 11:10 pm - Alka Coaching: Dost🥹
    13/10/24, 11:10 pm - Abhi Coaching: yes
    13/10/24, 11:11 pm - Abhi Coaching: more like imposter
    13/10/24, 11:11 pm - Abhee: 😂😂
    13/10/24, 11:12 pm - Abhee: alka roo di bhai😂 <This message was edited>
    13/10/24, 11:12 pm - Abhi Coaching: sabse zyada isii ko irritate karta tha na
    13/10/24, 11:12 pm - Abhee: ooooh
    13/10/24, 11:43 pm - Alka Coaching: abe bahut chaud me rehta tha
    13/10/24, 11:43 pm - Abhee: ooh
    
    


```python
 pattern = r'\d{2}/\d{2}/\d{2,4}, \d{1,2}:\d{2}\u202f[apAP][mM]\s-\s'
```


```python
messages = re.split(pattern,data)
messages
```




    ['',
     'Messages and calls are end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them. Tap to learn more.\n',
     'You created this group\n',
     "You updated the message timer. New messages will disappear from this chat 24 hours after they're sent, except when kept.\n",
     "You changed this group's icon\n",
     "Abhi Coaching changed this group's icon\n",
     'You changed the group name from "Kalra ka shukla" to "Kanpuriye"\n',
     'Abhi Coaching turned off disappearing messages.\n',
     'Alka Coaching: Never too busy for you bruh\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Abhi Coaching: send books\n',
     'Abhi Coaching: kaha mar gaye?\n',
     'Alka Coaching: Idhar hi hun\n',
     'Deepansh Pandey: Aaj ka kya plan shero?\n',
     'Deepansh Pandey: Alka reply kro baby\n',
     'Abhi Coaching: bhai alakshendra yaar\n',
     'Deepansh Pandey: Kab ka plan banaye\n',
     'Abhi Coaching: itna kya bhav khaa rahe ho reply dene mei\n',
     "Deepansh Pandey: Kal I'll be busy\n",
     'Abhi Coaching: yaha fast reply pe koi judge nai karta\n',
     'Deepansh Pandey: 🤣🤣🤣\n',
     'Deepansh Pandey: Batao alka kb ka rkhe\n',
     'Alka Coaching: Bhai mai kal hi ghum ke aaya \nMa baap bol denge itne bhi acche number ni aaye hain\n',
     'Deepansh Pandey: Ghr ka plan rkh le?\n',
     'Alka Coaching: Ghar pe kuch karne ho ga ni\n',
     'Alka Coaching: Kal parso bahar chale?\n',
     "Deepansh Pandey: Kal ka I'm not sure\n",
     'Alka Coaching: Parso?\n',
     'Abhi Coaching: bahar kya karoge?\n',
     'Deepansh Pandey: Again shyd mai na rhu\n',
     'Deepansh Pandey: But Jo bhi ho parso shyd possible ho bhi... Jaisa hoga bata denge\n',
     'Deepansh Pandey: Ye bhi hai\n',
     'Alka Coaching: Khaayenge yaar \nScenery dekhenge \nGhar pe hue to abuse bhi halke se karna padega\n',
     'Abhi Coaching: ghar pe ekdum relax rehta\n',
     'Abhi Coaching: baate toh bahar bhi karenge\n',
     'Alka Coaching: Bhai tu kal k baad kab free hai\n',
     "Deepansh Pandey: I've got something to tell guys\n",
     'Deepansh Pandey: Abhi knows a bit\n',
     'Abhi Coaching: but what we can do is ghar chalte fir khane chalenge bahar\n',
     'Deepansh Pandey: Jldi milne ka rkho bhaiyo\n',
     'Alka Coaching: Sure\n',
     'Alka Coaching: Kyun kya hua?\n',
     'Deepansh Pandey: Milkr bataunga\n',
     'Abhi Coaching: yaar fun talks can be without gaali too yk 😂\nsamjhao bhai deepansh isko\n',
     'Abhi Coaching: Saturday rakhe??\n',
     'Alka Coaching: Saturday’s okay\n',
     "Deepansh Pandey: Abe whi toh parso hai... I'm not sure n about parso\n",
     'Alka Coaching: Sunday?\n',
     'Deepansh Pandey: Shyd weekend or relatives ke yha jana pde\n',
     'Abhi Coaching: toh fir Monday ya Tuesday rakhlo\n',
     'Alka Coaching: Bhai Monday done karte?\n',
     'Abhi Coaching: kyuki Sunday is family day here\n',
     'Abhi Coaching: next week any day\n',
     'Abhi Coaching: fine by me\n',
     'Alka Coaching: Gotcha \nBandi se milne jaayega\n',
     "Deepansh Pandey: Acha lsn agr sat possible hua then I'll tell otherwise mon\n",
     'Abhi Coaching: haan wo bandi meri Nani hai\n',
     'Abhi Coaching: mast\n',
     'Alka Coaching: Done deal bhai\n',
     'Deepansh Pandey: You deleted this message\n',
     'Deepansh Pandey: You deleted this message\n',
     'Abhi Coaching: <Media omitted>\n',
     'Deepansh Pandey: You deleted this message\n',
     'Abhi Coaching changed the group name from "Kanpuriye" to "bajrang dal 🚩"\n',
     'Deepansh Pandey: You deleted this message\n',
     'Deepansh Pandey: You deleted this message\n',
     'Abhi Coaching: This message was deleted\n',
     'Abhi Coaching: This message was deleted\n',
     'Deepansh Pandey: You deleted this message\n',
     'Abhi Coaching: This message was deleted\n',
     'Abhi Coaching: This message was deleted\n',
     'Deepansh Pandey: You deleted this message\n',
     'Abhi Coaching: This message was deleted\n',
     'Deepansh Pandey: You deleted this message\n',
     'Deepansh Pandey: You deleted this message\n',
     'Abhi Coaching: This message was deleted\n',
     'Abhi Coaching: This message was deleted\n',
     'Deepansh Pandey: You deleted this message\n',
     'Abhi Coaching: This message was deleted\n',
     'Abhi Coaching: This message was deleted\n',
     'Deepansh Pandey: 😂😂\n',
     'Abhi Coaching: 😂😂\n',
     'Alka Coaching: Nice\n',
     "Deepansh Pandey: Tmhare liye hi kia hai.... I'm glad u liked it\n",
     'Alka Coaching: Shows how much you guys care:)\n',
     'Deepansh Pandey: We love you alka ❤\n',
     'Alka Coaching: Gay\n',
     'Deepansh Pandey: Tere liye 😍\n',
     'Deepansh Pandey: 🤣🤣\n',
     'Abhi Coaching: as a friend*\n',
     'Alka Coaching: Somehow that’s gayer abbhi\n',
     'Abhi Coaching: somehow all you think about is being gay why so alex\n',
     'Alka Coaching: Dunno\n',
     'Abhi Coaching: thoda toh excitement dikhaya kar bhai apni zindagii mei basss thoda sa\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Alka Coaching: Boys… kuch karne ko ni hai\n',
     'Abhi Coaching: go read your new books\n',
     'Deepansh Pandey: Call kr le\n',
     'Deepansh Pandey: Bc krte hai\n',
     'Abhi Coaching: discord pe aa jao bey teeno waha chess khel sakte, YouTube dekh sakte ya koi movie bhi\n',
     'Deepansh Pandey: Ye bhi thik hai\n',
     'Alka Coaching: Done\n',
     'Alka Coaching: Invite bhejna\n',
     'Abhi Coaching: okay bhejta hu thodi der mei\n',
     'Abhi Coaching: https://discord.gg/pewDwSZj\n',
     'Deepansh Pandey: Kal ka plan rkhe?\n',
     'Alka Coaching: Kal thoda short term hai \nAbbhi?\n',
     'Abhi Coaching: This message was deleted\n',
     'Abhi Coaching: rakhlo kal\n',
     'Abhi Coaching: waise bhi shaam ka hee rakh rahe hai\n',
     'Deepansh Pandey: Bhai agle month k kiye adv notice bhej du?\n',
     'Abhi Coaching: agar dopeher ka hota toh mai bhi bolta but since shaam ka hai toh no issues\n',
     'Deepansh Pandey: Yeah... So now alka u decide\n',
     'Abhi Coaching: keep Monday or Saturday whatever you like Alex\n',
     'Alka Coaching: Thik hai \nKal shaam ko ghar aana \nThoda thanda hote hi fir chalenge bahar\n',
     "Abhi Coaching: pacca you're fine by that na?\n",
     'Alka Coaching: 4:30ish tak aa jaiyo\n',
     'Alka Coaching: Yeah \nJust asked ma\n',
     'Deepansh Pandey: 👍👍\n',
     'Abhi Coaching: cool\n',
     'Alka Coaching: Chalo chehre dekhe aakhir\n',
     'Alka Coaching: Especially abhhi\n',
     'Abhi Coaching: Shutup yaar\n',
     'Alka Coaching: Mere Mann me to tu takla hi hai\n',
     'Deepansh Pandey: Tu fir ganja hi hai n?\n',
     'Abhi Coaching: haan yaar\n',
     'Deepansh Pandey: 😂😂\n',
     'Abhi Coaching: 😭😭😭😭\n',
     'Alka Coaching: Tabla bajayenge\n',
     'Alka Coaching: Shivaji the boss\n',
     'Deepansh Pandey: 😂😂\n',
     'Abhi Coaching: stool ka arrangement kar lena chotu\n',
     'Abhi Coaching: 😂😂😂😂\n',
     'Alka Coaching: Too far\n',
     'Abhi Coaching: far beyond your reach\n',
     'Deepansh Pandey: @918299433225  bhai mai na sehta\n',
     'Alka Coaching: You know \nThat does make sense\n',
     "Abhi Coaching: we're not anant afterall\n",
     'Alka Coaching: You wish\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Alka Coaching: Adv mat bola kar ab\n',
     'Deepansh Pandey: Mujhe bhi likhne mei ajeeb sa kaha\n',
     'Deepansh Pandey: Laga*\n',
     'Abhi Coaching: <Media omitted>\n',
     'Alka Coaching: Knew it\n',
     'Deepansh Pandey: https://www.instagram.com/reel/CtLUJWhgaj9/?igshid=MTc4MmM1YmI2Ng==\n',
     'Deepansh Pandey: Abe ye kaun hai sala chadarmod\n',
     'Abhi Coaching: tshirt nai dikhri kya\n',
     'Deepansh Pandey: Abe woh thik hai but ye... Sala 8vi nhi kiye hoga bhai\n',
     'Abhi Coaching: iska channel hai ig pe gyaan pelta hai bemtlb ka just like Praful billori\n',
     'Abhi Coaching: mba chaiwala\n',
     'Deepansh Pandey: Bhai duniya k agr ye haal hai... Toh bdne do fir global warming\n',
     'Deepansh Pandey: Ozone bhi hata do bhai fir\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: 😂😂\n',
     'Alka Coaching: It’s funny when I do it abbhi\nOtherwise you’re bullying buddy\n',
     "Abhi Coaching: it's you that's why I'm bullying\n",
     "Abhi Coaching: who doesn't bully his bestfriend huh\n",
     'Alka Coaching: I bet Anant doesn’t\n',
     "Abhi Coaching: he doesn't have one ig\n",
     'Deepansh Pandey: Are ye dekh k acha yaad aya\n',
     'Deepansh Pandey: Bhai books le ana pls\n',
     'Abhi Coaching: okay\n',
     'Abhi Coaching: <Media omitted>\n',
     "Abhi Coaching: that's the real Elon btw\n",
     'Deepansh Pandey: 😂😂\n',
     'Alka Coaching: Very hardworking \nTruly deserves to be the richest guy in the world\n',
     'Abhi Coaching: This message was deleted\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: Ye koi iski clips kato...\n',
     'Deepansh Pandey: Bht funny hai upload krnge stry pr\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: Baki I have these pics... Jo ki kahi upload krne lyk hai nhi\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Deepansh Pandey: Proper 10 min wla WhatsApp pr nhi ja rha\n',
     'Abhi Coaching: fast forward looks better\n',
     'Deepansh Pandey: Hmm\n',
     'Deepansh Pandey: Slander jaisa\n',
     'Abhi Coaching: https://myflixer.pw/movie/fast-and-furious-10-8846\n',
     'Deepansh Pandey: https://youtu.be/NG6uCHWT03w\n',
     'Deepansh Pandey: Abe lo yt pr mil gyi 🤣🤣\n',
     'Abhi Coaching: maine jaane tu jaane na dekhi thi yt pe\n',
     'Abhi Coaching: yt is a bliss to mankind jab tak paid nai hota\n',
     'Abhi Coaching: <Media omitted>\n',
     "Abhi Coaching: richest man y'all\n",
     'Deepansh Pandey: 🤣🤣\n',
     'Abhi Coaching: <Media omitted>\n',
     'Deepansh Pandey: 👍👍\n',
     'Deepansh Pandey: https://www.aznude.com/view/celeb/a/anjaliarora.html?jwsource=cl\n',
     'Abhi Coaching: abet bsdk\n',
     'Abhi Coaching: telegram bhai telegram not WhatsApp pls\n',
     'Deepansh Pandey: Laude wha koi group nhi hai\n',
     'Deepansh Pandey: Isliye yha bheja\n',
     'Abhi Coaching: Banalo\n',
     'Deepansh Pandey: Tum bhai banake wha send kr dena\n',
     'Deepansh Pandey: https://maps.app.goo.gl/oT6BT9Lu9wbsFCry7\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Deepansh Pandey: Abe aur bhejo\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Deepansh Pandey: Chutiye gandi wali bhejo\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Deepansh Pandey: Jo actual memories hai\n',
     'Abhi Coaching: <Media omitted>\n',
     'Deepansh Pandey: Ye jadoo ke grah ki pics mt bhejo\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: bhai ye saari hai\n',
     'Deepansh Pandey: Check my story\n',
     'Abhi Coaching: fuckoff yaar deepu\n',
     'Abhi Coaching: Tera phone bhool hee jana chaiye tha\n',
     'Deepansh Pandey: 😂😂😂\n',
     'Alka Coaching: https://youtu.be/LIKPbZqsb5w\n',
     'Abhi Coaching: https://youtu.be/6TG68Fg3or8\n',
     'Abhi Coaching: ye gaana sunna ek baar\n',
     'Abhi Coaching: aaj mila mujhe kaafi Acha laga\n',
     'Abhi Coaching: vibey hai kaafi\n',
     'Alka Coaching: Bhai ye bahut famous bhajan hai\n',
     'Alka Coaching: Ye remix kaafi chill hai though\n',
     "Abhi Coaching: ik ik but this one's a remix\n",
     'Deepansh Pandey: ❤❤\n',
     'Deepansh Pandey: https://youtu.be/tdch76DuAvc\n',
     'Abhi Coaching: entertaining toh tha\n',
     'Deepansh Pandey: Told u\n',
     'Alka Coaching: https://youtube.com/shorts/rWIWyfhNPsA?feature=share\n',
     'Abhi Coaching: This message was deleted\n',
     'Abhi Coaching: This message was deleted\n',
     'Deepansh Pandey: Are woh channel ka link bhejo jo bta rhe the\n',
     'Abhi Coaching: gsoc\n',
     'Deepansh Pandey: 👍\n',
     'Abhi Coaching: bhai naam nahi hai ye\n',
     'Abhi Coaching: naam wahi batayega\n',
     'Deepansh Pandey: Ok\n',
     'Abhi Coaching: https://youtube.com/shorts/l3feaOt2ZIk?feature=share\n',
     'Abhi Coaching: thapar is in Punjab na\n',
     'Alka Coaching: Yes bro\n',
     'Abhi Coaching: Bhai Delhi ho jaate tera\n',
     'Alka Coaching: Bhai chahte to hum bhi yahi\n',
     'Abhi Coaching: 10 baje tak call karte\n',
     'Abhi Coaching: dinner wagera bhi ho jayega\n',
     'Deepansh Pandey: Bhai ruk jao... Abhi thda late call kr lenge\n',
     'Abhi Coaching: nai nai hogaya\n',
     'Abhi Coaching: kal 2 baje ka decide hua\n',
     'Deepansh Pandey: Acha\n',
     'Deepansh Pandey: Okk\n',
     'Abhi Coaching: alex ke Ghar pe milenge fir kahi chalenge\n',
     'Abhi Coaching: room pe arihant hai with the broken leg\n',
     'Abhi Coaching: so yeah\n',
     'Deepansh Pandey: Okk\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: 21 Wall Street\n',
     'Alka Coaching: Baaki dominos and Pizza Hut bhi hain bagal me\n',
     'Alka Coaching: And 2 fancier places I know\n',
     'Abhi Coaching: Bhai mujhse itna nahi ho payega tum dono decide karlo\n',
     'Alka Coaching: Abe dekho bhai\n',
     'Abhi Coaching: Deepu is going\nI trust Deepu \nDeepu will decide\n',
     'Deepansh Pandey: Bhai imo around 200 hai sparkles mei... So 3 item udhr kr lenge... Round off 700 then agr chaho toh pizza Hut chl lenge udhr combo hai   400 k 4 pizza... Nhi toh ek aur hai 250 ke ke 2 ... Accordingly udhr bhi kr lenge\n',
     'Deepansh Pandey: Thik m\n',
     'Deepansh Pandey: ?\n',
     'Abhi Coaching: <Media omitted>\n',
     'Alka Coaching: 👌🏿\n',
     'Abhi Coaching: day well spent\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Abhi Coaching: yaar teri dadi actually bahaut sweet hai\n',
     'Deepansh Pandey: Ha bhai...\n',
     'Deepansh Pandey: Actually sabhi log yr\n',
     'Abhi Coaching: but especially dadi ji\n',
     'Alka Coaching: Yeah \nShe loves meeting my friends \nMere jo dost unse mile hain, vo abhi tak dost hain\n',
     'Alka Coaching: Upar se sirf mere hi dosto se milti \nArihant Anwesha ke ni\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Abhi Coaching: jo kehlo Bhai iPhone camera mei toh baap hai\n',
     'Deepansh Pandey: True that\n',
     'Alka Coaching: Bhai my photography skills yaar \nDekh ke moment liye hain\n',
     'Deepansh Pandey: Bhk\n',
     'Abhi Coaching: that was the joke\n',
     'Alka Coaching: Okay\n',
     'Deepansh Pandey: BTW guys \nCSA mei I met this sigma\n',
     'Alka Coaching: Who?\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     "Abhi Coaching: bro's buff\n",
     'Deepansh Pandey: Bhai bht badi hai\n',
     'Alka Coaching: He’s why I wanna have a mustache and wear janeu\n',
     'Deepansh Pandey: Bhai infact statue ki detailing dekh\n',
     'Deepansh Pandey: There are abs\n',
     'Alka Coaching: Piche banduk hogi\n',
     'Abhi Coaching: buff i said\n',
     'Abhi Coaching: tujhe bhai suit karegi you look better clean 😂😂\n',
     'Alka Coaching: True\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Alka Coaching changed their phone number to a new number. Tap to message or add the new number.\n',
     'Abhi Coaching: 4 seater hai?\n',
     'Deepansh Pandey: Temporary hai bhai\n',
     'Deepansh Pandey: Waise 3 seater hai yha sare\n',
     'You added Alka Coaching\n',
     'Deepansh Pandey: 9415485087 kiska hai?\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Alka Coaching: Bhai mummy ka\n',
     'Alka Coaching: Hatao ise\n',
     'You removed +91 94154 85087\n',
     'Deepansh Pandey: Done👍\n',
     'Alka Coaching: Bhai very posh hostel you’ve got\n',
     'Deepansh Pandey: Just khula hai hai n Bhai isliye\n',
     'Abhi Coaching: thapar ka bhi maal hai\n',
     'Abhi Coaching: i liked this\n',
     'Deepansh Pandey: Sbse bdiya toh uski library hai bhai\n',
     'Deepansh Pandey: Bhai ye tables hai abhi set nhi hui room mei\n',
     "Deepansh Pandey: They'll be set once we get into 3 seater\n",
     'Abhi Coaching: i thought aise hee set hai lol\n',
     'Abhi Coaching: yes yes\n',
     'Deepansh Pandey: Nhi bhai\n',
     'Abhi Coaching: wo bench wali feel aayegi\n',
     'Deepansh Pandey: Woh wali.... Na bhai 🥲\n',
     'Deepansh Pandey: We were just different\n',
     'Deepansh Pandey: Bhai 🤜🤛\n',
     'Abhi Coaching: 🤧🤧\n',
     'Abhi Coaching: senti mat kar ab firse\n',
     'Deepansh Pandey: 💦💦\n',
     'Alka Coaching: Vaha kaisi greenery bhai?\n',
     'Deepansh Pandey: Bs greenery hi baj\n',
     'Deepansh Pandey: Hai*\n',
     'Abhi Coaching: arey the rooms are good as compared to other hostels i meant\n',
     'Deepansh Pandey: But Bhai I was seriously saying... Mkc bs greenery hi hai\n',
     'Deepansh Pandey: Sb aisa hi hai\n',
     'Abhi Coaching: wo thapar ki baat kar Raha\n',
     'Alka Coaching: I meant big butts\n',
     'Abhi Coaching: teeo alag alag interpret kiye 😂\n',
     'Deepansh Pandey: Bhai yha ldkiyo ka akaal hai\n',
     'Deepansh Pandey: , 🥲\n',
     'Alka Coaching: https://youtube.com/shorts/cfFDoGLy0YM?feature=share\n',
     'Abhi Coaching: Bhai log meri bhi jaane ki dates aagayi 18 ko reporting 🫡\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Alka Coaching: Ah shit \nTime hai abhi \nBut new life now\n',
     "Abhi Coaching: yes yes acha hai na we'll meet\n",
     'Abhi Coaching: coincidence Deepu aur meri dates same\n',
     'Deepansh Pandey: Oh yeah\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: #couple goals\n',
     'Abhi Coaching: fast forward mei lagra zombie dance karre\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: This message was deleted\n',
     'Deepansh Pandey: Are bc.... Baal aa gaye 🤣🤣\n',
     'Abhi Coaching: bhai iska expression dekh\n',
     'Abhi Coaching: idk kisse but similarity lagri kisi movie character se\n',
     'Deepansh Pandey: My boys... So happy to see them again... \nProud father 🥲\n',
     'Abhi Coaching: Bhai bhelpuri wale ke paas Tera khata khulwa Diya hai jab aana toh pay kardena\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Abhi Coaching: Bhai couples dekh ke alakshendra ko tumari yaad aa rahi thi senti ho raha tha\n',
     'Deepansh Pandey: Couples dekh k meri??\n',
     'Abhi Coaching: haan tumhi toh ho humare ek laute laundiyabaz\n',
     'Abhi Coaching: 😂😂\n',
     'Deepansh Pandey: Khud ko bhul gaya sale???!\n',
     'Deepansh Pandey: Hypocrisy ki bhi seema hoti hai\n',
     'Abhi Coaching: jk hum jheel ka view dekh ke ye sochre the kaash thora aur time hota\n',
     'Abhi Coaching: fir socha Diwali mei aayenge ek week ke liye\n',
     'Abhi Coaching: tab mauj karenge\n',
     'Abhi Coaching: Bhai kabhi kabhi mera bhi Mann karta hai laundiyabaz bolne ka samjha karo\n',
     'Abhi Coaching: 😂😂😂\n',
     'Alka Coaching: Bhai deep thoughts with Deepu vibes thi Jheel kinare\n',
     'Abhi Coaching: wahi exactly\n',
     'Deepansh Pandey: Samay aane pr ye bhi kia jayega\n',
     'Alka Coaching: Inshallah\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Abhi Coaching: Perfectly dealt\n',
     "Abhi Coaching: if he was getting the same then why didn't he join us IIIT dwd better than bhagalpur?\n",
     'Alka Coaching: No it’s not \nHe’s a moron \nCse k chakkar me land college Gaya (usne saare cs waale upar rakhe honge)\n',
     'Abhi Coaching: gotcha\n',
     'Alka Coaching: Dharwad campus to hai hi ni \nAnd placements are fuckall\nAnd we all make fun of Bhagalpur for being secluded, Dharwad might as well be on moon\n',
     "Abhi Coaching: he asked you all that just cuz he wanted to see where he's at the delusional comparison\n",
     'Alka Coaching: He’s at 5’4” \nThat’s where he’s at\n',
     'Abhi Coaching: 😂😂\n',
     'Deepansh Pandey: IIIT mei kewal placements achi hoti hai.. Aur dwd mei woh bhi achi nhi hoti\n',
     'Abhi Coaching: why did he go there fir\n',
     'Abhi Coaching: uska bhai bits pilani mei hai\n',
     'Abhi Coaching: saga bhai\n',
     'Deepansh Pandey: CSE k chakkar mei\n',
     'Alka Coaching: Government college clout and cs clout \nHoga jhaat ki kuch\n',
     'Alka Coaching: Bhai bits me bhi non circuital branches ka bura haal hai\n',
     'Deepansh Pandey: And after talking to others on college... IIIT mei branch hardly matters.... Curriculum is such ki yha sbko placement thdi mil jati hai\n',
     'Alka Coaching: Kehne ko chale jaao but fir 30 lac kharch k 9-10LPA ki job\n',
     'Abhi Coaching: samjha samjha\n',
     'Alka Coaching: Bhai udhar to sirf circuital hi hoti hai na that’s why placement is best\n',
     'Abhi Coaching: btw Deepu classes kabse?\n',
     'Alka Coaching: And bits me CSE is 300 +\n',
     'Deepansh Pandey: Mon\n',
     'Abhi Coaching: love how this gc lights up\n',
     'Deepansh Pandey: There are other reasons too\n',
     'Abhi Coaching: alka is going out today\n',
     'Deepansh Pandey: Yha ki ece is way different than that in other colleges\n',
     'Abhi Coaching: basically moving out\n',
     'Deepansh Pandey: Bye bye baby\n',
     'Alka Coaching: :)\n',
     'Abhi Coaching: oye photos bhej\n',
     'Deepansh Pandey: Ha\n',
     'Deepansh Pandey: Bhej\n',
     'Alka Coaching: Bhai upload hone de\n',
     'Abhi Coaching: kithe ghante mei hogi?\n',
     'Alka Coaching: Some time\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Alka Coaching: Bhai hotel ki tarah lag raha\n',
     'Alka Coaching: Photo dekh ke aankh bhar aayi (cum se)\n',
     'Alka Coaching: Sex macha ab khub\n',
     'Abhi Coaching: tuu kab bhejra\n',
     'Alka Coaching: <Media omitted>\n',
     'Abhi Coaching: 😂😂😂\n',
     'Deepansh Pandey: Bhai mai ro dunga\n',
     'Abhi Coaching: ayy phulwa rote nahi na\n',
     'Abhi Coaching: pyar karte hai tumse\n',
     'Abhi Coaching: itna toh karenge hee na\n',
     'Deepansh Pandey: 😂😂\n',
     'Deepansh Pandey: Aur baki sb thik?\n',
     'Abhi Coaching: bhai Gand faad di idhar udhar ghuma ghuma ke\n',
     'Abhi Coaching: finally Sara official document wala kaam khatam\n',
     'Abhi Coaching: ab kal se orientation\n',
     'Deepansh Pandey: Chl bdhiya\n',
     'Deepansh Pandey: Aram kr\n',
     'Deepansh Pandey: Ab nayi life strt teri bhi\n',
     'Abhi Coaching: haan abhi orientation ho jaane do teeno baith ke randi Rona karenge\n',
     'Deepansh Pandey: Sure sure\n',
     'Alka Coaching: Bhai tu vaise hi kaafi hot ho raha aajkal, bus bandiyon se door rahiyo noch na le\n',
     'Abhi Coaching: bhai yaar mai kuch bhi nahi yaha\n',
     'Abhi Coaching: aise aise log hai na mai gayab hu\n',
     'Abhi Coaching: ladkiya ekdum fashionable ladke behenchod model Wale kapde pehente\n',
     'Abhi Coaching: plus point I have people taller than me here\n',
     'Abhi Coaching: some Nigerian international students\n',
     'Abhi Coaching: ek toh bc mujhse bhi 2-3 inch lamba tha\n',
     'Alka Coaching: Vo lund hai\n',
     'Abhi Coaching: bhai tum dono mei se kisi ke pass C ke notes hai kya\n',
     'Abhi Coaching: ho agar toh bhej diyo jab time mile\n',
     'Deepansh Pandey: Ok\n',
     'Abhi Coaching: <Media omitted>\n',
     'Alka Coaching: Sexy\n',
     'Alka Coaching: Let Us C khareed lo \nBest book \nUske questions bhi kar lena \nNotes chutiya hain\n',
     'Abhi Coaching: got it\n',
     'Abhi Coaching: i actually have that already\n',
     'Abhi Coaching: but Ghar pe padi hai bc\n',
     'Alka Coaching: Bus vahi kar and questions bhi uske karo saare\n',
     'Alka Coaching: Abe saale\n',
     'Abhi Coaching: mai mangwa leta hu\n',
     'Abhi Coaching: noted\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Abhi Coaching: 🥰🥰\n',
     'Alka Coaching: Sexy\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: bach gaya bhai\n',
     'Deepansh Pandey: Nice bhai\n',
     'Alka Coaching: Kitti bandiyon ka DM aaya ye batao\n',
     'Abhi Coaching: Bhai pela gaya hu aur kuch nahi\n',
     'Abhi Coaching: null\n',
     'Alka Coaching: Hotel jaisa hostel \nModel jaisa resident\n',
     'Abhi Coaching: Abey tute dil ka aashiq sala pichle 10 min se haaye jaa raha same song\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: ye dekho kya bakchodi karte ye hostel mei 😂😂\n',
     'Abhi Coaching: ek ladke photo click kari aur edit kardi\n',
     'Deepansh Pandey: Teri jhalak asharfee\n',
     'Abhi Coaching: bhayavah drishya bhai\n',
     'Alka Coaching: Bhai shitttt\n',
     'Abhi Coaching: iss tarah ka bully hota yaha 😂\n',
     'Alka Coaching: Bhai bahut acchi editing\n',
     'Abhi Coaching: bc upar se launda niche se patani kya kardiya\n',
     'Alka Coaching: Accha kiya\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: ye hai ladka\n',
     'Alka Coaching: Itni ladkiyan?!?!\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Abhi Coaching: 😂😂😂\n',
     'Abhi Coaching: haan bhai lekin launda inke triple the\n',
     'Abhi Coaching: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: do not use headphones\n',
     'Deepansh Pandey: 😂😂\n',
     'Abhi Coaching: <Media omitted>\n',
     'Alka Coaching: With great power cums\n',
     'Abhi Coaching: wo hawa ki power hai\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Abhi Coaching: 😂😂😂\n',
     'Abhi Coaching: badhiya Deepu ekdum mazdoor\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Alka Coaching: Deepu ho Gaya hot\n',
     'Alka Coaching: Abe zyada hi \nMai ghur raha 10 mint se\n',
     'Deepansh Pandey: Bhai isiliye bheja\n',
     'Deepansh Pandey: Hila le\n',
     'Deepansh Pandey: Woh mujhe bhej dena\n',
     'Deepansh Pandey: Bhai knp jake maine jo kaam kaha tha kr dena\n',
     'Alka Coaching: Bilkul huzoor\n',
     'Abhi Coaching: kya?\n',
     'Abhi Coaching: mujhe bhi toh batao\n',
     'Alka Coaching: Secret\n',
     'Abhi Coaching: all is well wala feel\n',
     'Deepansh Pandey: Totally\n',
     'Abhi Coaching: 🥹🥹\n',
     'Abhi Coaching: This message was deleted\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Abhi Coaching: Abey bhai mera toh aur kharab tha yaar 😭😭\n',
     'Deepansh Pandey: Bhai but mera acha tha aaj ka\n',
     'Abhi Coaching: dekhne mei bhi kaafi better lagra\n',
     'Abhi Coaching: mere mei toh machine se roti banti hai moti moti aadhi kachii\n',
     'Deepansh Pandey: Same here \nBut kal special tha\n',
     'Abhi Coaching: maze toh alka le raha hai\n',
     'Deepansh Pandey: 😒\n',
     'Alka Coaching: You know it buddy\n',
     'Abhi Coaching: pollution dekh\n',
     'Abhi Coaching: <Media omitted>\n',
     'Deepansh Pandey: Nice\n',
     'Abhi Coaching: ye pehli building is my hostel\n',
     'Deepansh Pandey: Earthquake aa gya guys\n',
     'Deepansh Pandey: 😵\u200d💫\n',
     'Abhi Coaching: haan bhai wo bhi\n',
     'Abhi Coaching: <Media omitted>\n',
     'Alka Coaching: Sojaya kar\n',
     'Abhi Coaching: bas kal thoda crazy hogaya warna usually i sleep around 1\n',
     'Deepansh Pandey: <Media omitted>\n',
     "Abhi Coaching: I'm home boys\n",
     'Alka Coaching: Welcome back brother\n',
     'Abhi Coaching: bhai kasam se itni oxygen aayi na kanpur enter karte hee\n',
     'Deepansh Pandey: Ruk aa rha mai 5 min mei\n',
     "Abhi Coaching: bhai I'm too tired ig poora time bas sounga\n",
     'Abhi Coaching: kal subha milte\n',
     'Deepansh Pandey: Mai aa rhaa.. Ghr ke bhr nikl\n',
     'Alka Coaching: Jala lo laudo\n',
     'Abhi Coaching: 😂😂😂\n',
     'Abhi Coaching: aao bey tum bhi jaldi aao\n',
     'Alka Coaching: null\n',
     'Abhi Coaching: Lolita padhne ka time kaha se milra \n\nbags toh maine bhi 2 din pehle hee pach kardiye the 😂\n',
     'Abhi Coaching: null\n',
     'Alka Coaching: On bus adda\n',
     'Abhi Coaching: aaj nikalra?\n',
     'Alka Coaching: Ji\n',
     'Abhi Coaching: lessgooo\n',
     'Abhi Coaching: kab tak aayega?\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Abhi Coaching: kya mtlb ghar jaa raha hu toh bag mei pathar aur cement le jaane ki zaroorat nahi\n',
     'Alka Coaching: Kal subah\n',
     "Deepansh Pandey: Daddy's home bitch\n",
     'Alka Coaching: Pranaam\n',
     'Alka Coaching: null\n',
     'Abhi Coaching: pardesi ghar aaya\n',
     'You started a call\n',
     'Abhi Coaching: Diwali mein आपको मुंह से लेकर पिछवाड़े तक सुख समृधि दे; कोई भोसड़ी का आपकी झाट का बाल ना उखाड़ सके; आप सफलता की ऐसी माँ चोदे; कि सबकी फट जाये; आप पर आने वाले दुखों की बहन चुद जाये; कामयाबी हमेशा आपकी गांड में घुसी रहे। Diwali ki गांड फाड़ बधाई। 😎Bhai😝 Ki Taraf Se 😝 अब मत कहना\xa0कि\xa0बधाई\xa0नही\xa0दी।शुभ दीपावली\n',
     'Abhi Coaching: boys hostel\n',
     'Deepansh Pandey: Shaam ka kya scene?\n',
     'Abhi Coaching: alka batao\n',
     'Alka Coaching: Bhai ghar pe thodi dikkat coz vahi log vaala scene \nBut shaam ko bahar chalte \nAnd ghar pe bhi mummy papa se mil lena\n',
     'Alka Coaching: Sham ko chalna kidhar vo aap log batayen\n',
     'Abhi Coaching: haan wo toh theek hai kaha chalre ye bata\n',
     'Alka Coaching: Tum dekho kuch \nMai bata ek do dhundh k\n',
     'Abhi Coaching: dekhta hu mai bhi\n',
     'Deepansh Pandey: 4??\n',
     'Abhi Coaching: pehle jagah toh dekh bhosdu\n',
     'Abhi Coaching: time toh ho hee jayega 😂\n',
     'Deepansh Pandey: Woh tu dekh\n',
     'Deepansh Pandey: Party teri pending hai🤣🤣\n',
     'Abhi Coaching: Abey yaar hum yahi nautanki karte at the end scooty ride karke aise hee kahi khaa ke aa jate 😂\n',
     'Abhi Coaching: raat gyi baat gyi 😂\n',
     'Deepansh Pandey: Chlega\n',
     'Abhi Coaching: done!\n',
     "Abhi Coaching: it's 4 then\n",
     'Deepansh Pandey: Ok\n',
     'Alka Coaching: 5 karlo\n',
     'Abhi Coaching: okay\n',
     'Alka Coaching: Bhai mere ghar me aaj kuch naatak chal raha \n30 minutes me batata mera kya hai\n',
     'Abhi Coaching: haan dekh le mera bhi kuch toh ho raha\n',
     'Abhi Coaching: bata jaldi kaisa hai\n',
     'Abhi Coaching: zyada ho toh 15 ka rakh lete\n',
     "Deepansh Pandey: I'm busy on 15\n",
     'Abhi Coaching: bank?\n',
     'Deepansh Pandey: Kal\n',
     'Abhi Coaching: what about 16?\n',
     'Deepansh Pandey: 15 ko dooj hai\n',
     'Abhi Coaching: arey haan\n',
     'Deepansh Pandey: 17 ko ja rha.. 16 ko pack wack krne mei time ghus jayega\n',
     'Abhi Coaching: what about kal\n',
     'Deepansh Pandey: .\n',
     'Abhi Coaching: done kal mera fix\n',
     'Deepansh Pandey: Chaman... Kal bank ka kaam hai pure din\n',
     'Abhi Coaching: arey bc\n',
     'Deepansh Pandey: Chat toh pdho soordaas\n',
     'Abhi Coaching: aaj raat ko milega?\n',
     'Abhi Coaching: 😂😂\n',
     'Deepansh Pandey: Kamra khol k rkhna\n',
     'Abhi Coaching: chalo then aaj raat\n',
     'Abhi Coaching: ghoomna hoga toh saamne moti jheel mei bakchodi karlenge\n',
     'Deepansh Pandey: Decide kr lo tm doni\n',
     'Deepansh Pandey: Dono\n',
     'Alka Coaching: Kal karlo \nAaj guest aaye hain\n',
     'Abhi Coaching: okay\n',
     'Abhi Coaching: Deepu Bank bhi sirf 5 tak khulta hai\n',
     'Deepansh Pandey: Kal nhi ho payega\n',
     'Abhi Coaching: tum aur mai toh aaj milre hai\n',
     'Abhi Coaching: alka ko balcony se hi kardenge\n',
     'Alka Coaching: Jab aas pass ho to batana\nAgar free hua to aata Milne\n',
     'Abhi Coaching: agar nahi aayenge toh tu milega bas\n',
     'Deepansh Pandey: Bhai yha bhi mehmaan aa gaye 😅😅\n',
     'Deepansh Pandey: Bhai kuch n kuch krte hai thda wqt do...\n',
     'Deepansh Pandey: Milna toh hai hi\n',
     'Abhi Coaching: Abey toh raat tak toh jayenge na\n',
     'Abhi Coaching: warna kal raat\n',
     'Abhi Coaching: milenge toh hai hee\n',
     'Deepansh Pandey: Done done\n',
     'Deepansh Pandey: Pahoch gaye?\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: The only pic I got\n',
     'Deepansh Pandey: Abhi share kr dena tu\n',
     'Abhi Coaching: yesssir\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Deepansh Pandey: Contri kitne ki hui bata do\n',
     'Abhi Coaching: 200\n',
     'Deepansh Pandey: Bhk yha se\n',
     'Deepansh Pandey: Ye exclude krke bata,🤣🤣\n',
     'Abhi Coaching: <Media omitted>\n',
     'Deepansh Pandey: Moye moye\n',
     'Abhi Coaching: <Media omitted>\n',
     'Deepansh Pandey: Tu bday party kb de rha? 😂\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: abhi ko bhi add karle ab\n',
     'Deepansh Pandey: Ok\n',
     'You added Abhee\n',
     'Abhee: maqsad mt bhulna bhaiyaon!!!\n',
     'Abhi Coaching: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Abhee: alka qr..\n',
     'Abhee: lekin aaj kal bada sawal ye hai ki ky abhinav urf abhii to apne paise wapas milenge...\n',
     'Abhi Coaching: damn abhee aate hee alka\n',
     'Abhee: bro alakshendra bht bada hai.\n',
     'Abhi Coaching: bhai bas yaad mat dila\n',
     'Abhee: spelling bhii ni aati meko toh\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Alka Coaching: Apna roz ka hai\n',
     'Abhi Coaching: alka finally back\n',
     'Alka Coaching: Tomorrow last test\n',
     'Abhi Coaching: tomorrow first test\n',
     'Deepansh Pandey: Day after tomorrow come meet daddy (me)\n',
     'Abhi Coaching: 🤝🏻\n',
     'Alka Coaching: Ji sir\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: I am happy to announce a free programming course by GeeksforGeeks to every first-year student at Galgotias University.  \n\nKey details of the program include:\n\n- Course Content: The course covers fundamental programming concepts essential for success in the ever-evolving field of computer science including all major languages (Python/JAVA/C++).     \n\n- Instructor: Sandeep Jain, the Founder and CEO of GeeksforGeeks, will guide the students through the course, providing valuable insights and expertise.\n The batch link for registration is [https://practice.geeksforgeeks.org/courses/programming-language-foundation-builder], and you can use the following coupon code for free access: GFGPLFB23.                             Also, let me know about your experience with this course.\n',
     'Deepansh Pandey: GFGPLFB23\n',
     'Abhi Coaching: <Media omitted>\n',
     'Alka Coaching: Kya baat hai bhai\n',
     'Alka Coaching: Ye to hame bhi dekhna\n',
     'Alka Coaching: Not the picture (just text)\n',
     'Abhi Coaching: picture toh waise bhi save nahi ho paayi cuz WhatsApp\n',
     'Abhi Coaching: wait\n',
     'Alka Coaching: Pakka galti ni thi?\n',
     'Abhi Coaching: <Media omitted>\n',
     'Alka Coaching: Fuckkkkkkkkkkk\n',
     'Abhi Coaching: maybe she was expecting something else\n',
     'Abhee: bro is it what i think it is\n',
     'Abhi Coaching: but the boys here gave wrong instructions\n',
     'Alka Coaching: Yeah 👍🏿\n',
     'Abhee: damnn\n',
     'Alka Coaching: Obviously\n',
     'Abhee: abhi jam ke add ne sikhaya tha\n',
     'Abhee: sharing is caring\n',
     'Abhi Coaching: what are you thinking abhee\n',
     'Abhee: hot pic\n',
     'Abhee: of her..\n',
     'Abhi Coaching: arey bro WhatsApp is fucked up yaar warna pehle wahi share karta 😂\n',
     'Abhi Coaching: ss blank ho jata yaha\n',
     'Abhee: 😂😂\n',
     'Abhee: screen recorder\n',
     'Abhi Coaching: sure was bhai but the boys here took the wrong call\n',
     "Abhi Coaching: i miss y'all\n",
     'Abhee: fuckk bhai\n',
     'Abhi Coaching: i tried, blank <This message was edited>\n',
     'Alka Coaching: Lund\n',
     'Abhi Coaching: ik you can see the proof 😂\n',
     'Abhi Coaching: video*\n',
     'Abhee: now only going to galgotia can fix me🥹\n',
     "Abhi Coaching: she's not from here\n",
     'Abhi Coaching: bataya toh school se\n',
     'Abhee: ooh\n',
     'Abhi Coaching: abhee bhai pay more attention to texts here\n',
     'Abhee: behenchod barra kyu jaara tha mai🥹🥹\n',
     'Abhi Coaching: yaha pictorial form se zyada interesting texts hote 😂\n',
     'Alka Coaching: Kalyanpur chinaars on top :,)\n',
     "Abhi Coaching: honestly if we met in the same school i would've been bitchless kyuki fir tumlog ke alawa kisi se baat hee nahi karta 😂\n",
     'Abhi Coaching: side note acha hee hua baad mei mile\n',
     'Alka Coaching: No offence abhii, tere ko pasand to ni ye\n',
     'Alka Coaching: Ye jalwa\n',
     'Abhee: deepu ko hai\n',
     'Abhi Coaching: aprooved\n',
     'Abhi Coaching: ab tu ye puchega saale?\n',
     'Abhee: skill hai bhai achaa hua tu sikh gya\n',
     'Abhee: key to happily 😂\n',
     'Abhi Coaching: milne ke baad bhool bhi toh gaya 😂\n',
     'Abhi Coaching: btw \nwelcome to bajrang dal abhee\n',
     'Abhee: bc deepu hi krwa skta hai ni toh bc wo bhi bhagalpur mai reh reh kr\n',
     'Abhee: bhul jayega\n',
     'Abhi Coaching: 😂😂😂😂😂\n',
     'Abhee: loving it here\n',
     'Abhi Coaching: the second domain\n',
     'Abhee: batao saala recent meetup mai sirf londo ki baatein..\n',
     'Abhee: ya fr seniors ki\n',
     "Abhi Coaching: mai bataunga na achi achi wait till I'm back 😂\n",
     "Deepansh Pandey: Kids grow up... Don't be so immature yr... ! \nAur @917007242537  jb for once pic mile whatsapp pr.. Toh WhatsApp web pr woh pic khola kr aur fir laptop screen ki ki pic apne phone mei click kia kr..! \nYha laundo ke video se acha ladkiyo ke nudes share kro\n",
     'Abhi Coaching: 😂😂😂😂\n',
     "Abhi Coaching changed this group's icon\n",
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: just saving it here\n',
     'Abhee: abe 2nd sem mai kisi ko data structures hai?\n',
     'Abhee: @917307900795 tereko hai?\n',
     'Deepansh Pandey: Ha\n',
     'Abhee: algo bhi hai ky?\n',
     'Deepansh Pandey: Dsa k andr hi ayega\n',
     'Abhee: abe mere mai\n',
     'Abhee: ds hai bss\n',
     'Abhee: algo nahi hai\n',
     'Deepansh Pandey: Uske andr hoga\n',
     'Abhee: chaloo thikk\n',
     'Abhi Coaching: us moment\n',
     'Abhi Coaching: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Abhi Coaching: Deepu bana writer\n',
     'Alka Coaching: And more than that developer!!!\n',
     'Deepansh Pandey: Bkl main cheez mt dekh lena\n',
     'Abhi Coaching: alka wala toh 100% sach hai\n',
     'Deepansh Pandey: Pehli 3 lines meri hai baki gpt\n',
     'Alka Coaching: Isme link tumhare GPay ka hai?!\n',
     'Deepansh Pandey: Woh backend mei ata hai...\n',
     "Deepansh Pandey: Haven't even completed front end\n",
     'Abhi Coaching: isko toh g pe dunga mai\n',
     'Abhi Coaching: wo lag hee raha hai\n',
     'Alka Coaching: Bhai sexy ho rahi site \nYr 2 start me hi devops internship\n',
     'Deepansh Pandey: Are nhi yr.. DSA ho nhi rha tha😮\u200d💨😮\u200d💨 <This message was edited>\n',
     'Deepansh Pandey: Isliye idhr time waste kr dia\n',
     'Abhi Coaching: lekin site toh sexy hai\n',
     'Deepansh Pandey: Pay then 🥰🥰\n',
     'Abhi Coaching: kal aata hu\n',
     "Deepansh Pandey: Tomorrow I'll be out of town\n",
     'Deepansh Pandey: Day after rkh ke\n',
     'Deepansh Pandey: Le\n',
     'Abhi Coaching: okay\n',
     'Abhi Coaching: aur kisse g pe lene Jaa Raha hai\n',
     'Deepansh Pandey: Mandir ja rha hu balak 😊😊\n',
     'Abhi Coaching: konse\n',
     'Alka Coaching: Jai Shree Raam!!!\n',
     'Deepansh Pandey: Chandrika devi ji ka mandir\n',
     'Abhi Coaching: noiceee\n',
     'Deepansh Pandey: Jai shree raa🙏\n',
     'Deepansh Pandey: Raam*\n',
     'Abhi Coaching: Jai Mata di 🙏🏻\n',
     'Deepansh Pandey: Jai mata di\n',
     'Alka Coaching: Oh\n',
     'Abhee: radhe radhe\n',
     'Abhi Coaching: uthgaya Raja beta\n',
     'Abhee: hehehe\n',
     'Abhee: im getting tumbad vibess\n',
     'Deepansh Pandey: Bithoor chale?\n',
     'Abhee: ky krega udhr\n',
     'Deepansh Pandey: Bhai wha amrood ki redi lagaunga\n',
     'Abhee: as expected\n',
     'Abhi Coaching: 😂😂😂\n',
     'Deepansh Pandey: Tu bhi chalega?\n',
     'Abhee: batate hain soch ke\n',
     'Deepansh Pandey: Puch ke*\n',
     'Abhee: abe ja\nmujhe kisi ki permission ni lgti\n',
     'Abhee: tu hi hai nabalik\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Alka Coaching: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: Kal bithoor chale?\n',
     'Alka Coaching: I’m in (bus din me rakhna)\n',
     'Abhi Coaching: haan raat mei thodi jayenge obviously\n',
     'Deepansh Pandey: Chal lo\n',
     'Alka Coaching: Matlab aate hue bhi shaam ni honi chahiye please\n',
     'Abhi Coaching: dekhlo jaisa ho\n',
     'Abhi Coaching: kuch hai waha ghoomne ko?\n',
     'Abhi Coaching: 🤔🤔\n',
     'Deepansh Pandey: Wait\n',
     'Deepansh Pandey: Join meeting\n',
     'Deepansh Pandey: https://meet.google.com/zsg-ntes-zju\n',
     'Deepansh Pandey: Plan kya hai??\n',
     'Abhi Coaching: bithoor rehene dete hai\n',
     'Abhi Coaching: kaafi durr padega plus visibility itni kam hai wo road risky hai\n',
     'Deepansh Pandey: Abe toh plan toh batao malik\n',
     'Abhi Coaching: budhsen chaloge?\n',
     'Abhi Coaching: restraunt type hai but waha momos, chat, kachori etc etc etc milta hai kafi acha lagta mujhe\n',
     "Abhi Coaching: but that's not some place to enjoy sirf khane chalna ho toh theek hai\n",
     'Deepansh Pandey: Bhai hum khane ka kya krnge\n',
     'Abhi Coaching: khayenge?\n',
     'Deepansh Pandey: 🤯🤯\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: bhai yaar jagah decide karna was never my thing 😂\n',
     'Abhi Coaching: alka ko bulao koi\n',
     'Deepansh Pandey: 😴\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Abhi Coaching: 2 baje tak kuch decide nahi hua toh alka ke ghar\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Abhee: guyss im not available today\n',
     'Deepansh Pandey: No issues bhai... Paise bhej dena😂😂😂\n',
     'Abhi Coaching: Deepu aaj kal sabse G pe leta hai\n',
     'Deepansh Pandey: Its not like that.... Ur special 🥵\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhee: sharam kr le\n',
     'Deepansh Pandey: 🥱🥱\n',
     'Abhi Coaching: Happy new year bois\n',
     'Abhi Coaching: <Media omitted>\n',
     'Deepansh Pandey: Happy new year balak 🥳\n',
     'Abhee: happy new year guyss!!\n',
     'Abhi Coaching: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Abhi Coaching: ganga you beauty\n',
     'Alka Coaching: Tarr ho gay\n',
     'Abhee: tere campus mai road bhi ni bani abhi tk?\n',
     'Deepansh Pandey: Bani hai\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhee: avg rajisthani kids\n',
     'Abhi Coaching: bhaii 💀\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Abhee: jee baat londe🔥🔥\n',
     'Abhi Coaching: damn deepu\n',
     'Abhi Coaching: maal lagra\n',
     'Abhee: pehli baaar\n',
     'Abhi Coaching: Abey wo stud hai humesha maal lagta\n',
     'Alka Coaching: Deepu mai chala hilaane\n',
     'Deepansh Pandey: Are re... O hoo.... Bhaishb... Kiska reply aa gya\n',
     'Deepansh Pandey: Are laundo aarti ki thali lao...\n',
     'Deepansh Pandey: Ye bhaishb ki aarti utaro... Nhi toh chale jayenge\n',
     'Alka Coaching: Baauji aa gaye\n',
     'Abhee: 😂\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     "Abhi Coaching: today's events\n",
     'Deepansh Pandey: 🤣🤣\n',
     'Deepansh Pandey: 🔥\n',
     'Abhi Coaching: bhai banda literally haath paer jod raha hai\n',
     'Deepansh Pandey: Tu college mei hai ya university?\n',
     'Abhi Coaching: Uni\n',
     'Abhi Coaching: गलगोटिया यूनिवर्सिटी के  सोशियोलाजी के प्रोफेसर आदरणीय प्रदीप सिंह जी ने किया सुसाइड। ईश्वर उनकी आत्मा को अपने श्री चरणों में स्थान दें। हम सभी पुलिस जाँच की माँग करते है। #rip #justice\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhi Coaching: <Media omitted>\n',
     'Deepansh Pandey: Bhai subh subh kya mst mood bna dia\n',
     'Deepansh Pandey: Nice 👍\n',
     'Abhi Coaching: anytime deepu\n',
     'Abhee: khush kr ditta putr\n',
     'Deepansh Pandey: <Media omitted>\n',
     'Abhee: tu fr se reddit chalane laga?\n',
     'Deepansh Pandey: Mai toh chalata hi hu\n',
     'Abhi Coaching: <Media omitted>\n',
     'Abhee: <Media omitted>\n',
     ...]




```python
dates= re.findall(pattern,data)
dates
```




    ['26/04/23, 11:01\u202fam - ',
     '26/04/23, 11:01\u202fam - ',
     '26/04/23, 11:01\u202fam - ',
     '26/04/23, 11:19\u202fam - ',
     '27/04/23, 3:20\u202fpm - ',
     '06/06/23, 1:27\u202fpm - ',
     '07/06/23, 5:08\u202fpm - ',
     '07/06/23, 6:04\u202fpm - ',
     '07/06/23, 6:11\u202fpm - ',
     '07/06/23, 6:20\u202fpm - ',
     '07/06/23, 11:06\u202fpm - ',
     '07/06/23, 11:44\u202fpm - ',
     '08/06/23, 7:58\u202fam - ',
     '08/06/23, 1:33\u202fpm - ',
     '08/06/23, 1:33\u202fpm - ',
     '08/06/23, 1:33\u202fpm - ',
     '08/06/23, 1:33\u202fpm - ',
     '08/06/23, 1:33\u202fpm - ',
     '08/06/23, 1:33\u202fpm - ',
     '08/06/23, 1:33\u202fpm - ',
     '08/06/23, 1:35\u202fpm - ',
     '08/06/23, 1:35\u202fpm - ',
     '08/06/23, 1:35\u202fpm - ',
     '08/06/23, 1:36\u202fpm - ',
     '08/06/23, 1:36\u202fpm - ',
     '08/06/23, 1:36\u202fpm - ',
     '08/06/23, 1:36\u202fpm - ',
     '08/06/23, 1:36\u202fpm - ',
     '08/06/23, 1:36\u202fpm - ',
     '08/06/23, 1:37\u202fpm - ',
     '08/06/23, 1:37\u202fpm - ',
     '08/06/23, 1:37\u202fpm - ',
     '08/06/23, 1:37\u202fpm - ',
     '08/06/23, 1:37\u202fpm - ',
     '08/06/23, 1:37\u202fpm - ',
     '08/06/23, 1:37\u202fpm - ',
     '08/06/23, 1:37\u202fpm - ',
     '08/06/23, 1:37\u202fpm - ',
     '08/06/23, 1:38\u202fpm - ',
     '08/06/23, 1:38\u202fpm - ',
     '08/06/23, 1:38\u202fpm - ',
     '08/06/23, 1:38\u202fpm - ',
     '08/06/23, 1:38\u202fpm - ',
     '08/06/23, 1:38\u202fpm - ',
     '08/06/23, 1:39\u202fpm - ',
     '08/06/23, 1:39\u202fpm - ',
     '08/06/23, 1:39\u202fpm - ',
     '08/06/23, 1:39\u202fpm - ',
     '08/06/23, 1:39\u202fpm - ',
     '08/06/23, 1:39\u202fpm - ',
     '08/06/23, 1:39\u202fpm - ',
     '08/06/23, 1:39\u202fpm - ',
     '08/06/23, 1:39\u202fpm - ',
     '08/06/23, 1:39\u202fpm - ',
     '08/06/23, 1:40\u202fpm - ',
     '08/06/23, 1:40\u202fpm - ',
     '08/06/23, 1:40\u202fpm - ',
     '08/06/23, 1:40\u202fpm - ',
     '08/06/23, 1:40\u202fpm - ',
     '08/06/23, 1:40\u202fpm - ',
     '08/06/23, 1:41\u202fpm - ',
     '08/06/23, 1:41\u202fpm - ',
     '08/06/23, 1:41\u202fpm - ',
     '08/06/23, 1:41\u202fpm - ',
     '08/06/23, 1:42\u202fpm - ',
     '08/06/23, 1:42\u202fpm - ',
     '08/06/23, 1:42\u202fpm - ',
     '08/06/23, 1:42\u202fpm - ',
     '08/06/23, 1:42\u202fpm - ',
     '08/06/23, 1:43\u202fpm - ',
     '08/06/23, 1:43\u202fpm - ',
     '08/06/23, 1:43\u202fpm - ',
     '08/06/23, 1:44\u202fpm - ',
     '08/06/23, 1:44\u202fpm - ',
     '08/06/23, 1:45\u202fpm - ',
     '08/06/23, 1:45\u202fpm - ',
     '08/06/23, 1:46\u202fpm - ',
     '08/06/23, 1:46\u202fpm - ',
     '08/06/23, 1:46\u202fpm - ',
     '08/06/23, 1:47\u202fpm - ',
     '08/06/23, 1:47\u202fpm - ',
     '08/06/23, 2:39\u202fpm - ',
     '08/06/23, 4:19\u202fpm - ',
     '08/06/23, 6:00\u202fpm - ',
     '08/06/23, 6:13\u202fpm - ',
     '08/06/23, 6:27\u202fpm - ',
     '08/06/23, 6:28\u202fpm - ',
     '08/06/23, 6:28\u202fpm - ',
     '08/06/23, 9:44\u202fpm - ',
     '08/06/23, 11:18\u202fpm - ',
     '09/06/23, 2:26\u202fam - ',
     '09/06/23, 8:53\u202fam - ',
     '09/06/23, 8:53\u202fam - ',
     '09/06/23, 9:32\u202fam - ',
     '09/06/23, 11:44\u202fam - ',
     '09/06/23, 11:46\u202fam - ',
     '09/06/23, 11:47\u202fam - ',
     '09/06/23, 11:47\u202fam - ',
     '09/06/23, 11:47\u202fam - ',
     '09/06/23, 11:47\u202fam - ',
     '09/06/23, 12:57\u202fpm - ',
     '09/06/23, 12:57\u202fpm - ',
     '09/06/23, 12:57\u202fpm - ',
     '09/06/23, 1:40\u202fpm - ',
     '09/06/23, 9:32\u202fpm - ',
     '09/06/23, 9:41\u202fpm - ',
     '09/06/23, 9:41\u202fpm - ',
     '09/06/23, 9:42\u202fpm - ',
     '09/06/23, 9:42\u202fpm - ',
     '09/06/23, 9:43\u202fpm - ',
     '09/06/23, 9:47\u202fpm - ',
     '09/06/23, 9:49\u202fpm - ',
     '09/06/23, 10:04\u202fpm - ',
     '09/06/23, 10:05\u202fpm - ',
     '09/06/23, 10:06\u202fpm - ',
     '09/06/23, 10:06\u202fpm - ',
     '09/06/23, 10:06\u202fpm - ',
     '09/06/23, 10:06\u202fpm - ',
     '09/06/23, 10:06\u202fpm - ',
     '09/06/23, 10:06\u202fpm - ',
     '09/06/23, 10:07\u202fpm - ',
     '09/06/23, 10:07\u202fpm - ',
     '09/06/23, 10:07\u202fpm - ',
     '09/06/23, 10:07\u202fpm - ',
     '09/06/23, 10:07\u202fpm - ',
     '09/06/23, 10:07\u202fpm - ',
     '09/06/23, 10:07\u202fpm - ',
     '09/06/23, 10:07\u202fpm - ',
     '09/06/23, 10:07\u202fpm - ',
     '09/06/23, 10:07\u202fpm - ',
     '09/06/23, 10:08\u202fpm - ',
     '09/06/23, 10:08\u202fpm - ',
     '09/06/23, 10:08\u202fpm - ',
     '09/06/23, 10:08\u202fpm - ',
     '09/06/23, 10:08\u202fpm - ',
     '09/06/23, 10:08\u202fpm - ',
     '09/06/23, 10:09\u202fpm - ',
     '09/06/23, 10:09\u202fpm - ',
     '09/06/23, 10:09\u202fpm - ',
     '09/06/23, 10:10\u202fpm - ',
     '09/06/23, 10:11\u202fpm - ',
     '09/06/23, 10:11\u202fpm - ',
     '09/06/23, 10:11\u202fpm - ',
     '09/06/23, 10:11\u202fpm - ',
     '09/06/23, 10:13\u202fpm - ',
     '09/06/23, 10:13\u202fpm - ',
     '09/06/23, 10:14\u202fpm - ',
     '09/06/23, 10:15\u202fpm - ',
     '09/06/23, 10:16\u202fpm - ',
     '09/06/23, 10:16\u202fpm - ',
     '09/06/23, 10:17\u202fpm - ',
     '09/06/23, 10:17\u202fpm - ',
     '09/06/23, 11:20\u202fpm - ',
     '09/06/23, 11:21\u202fpm - ',
     '10/06/23, 1:28\u202fam - ',
     '10/06/23, 1:30\u202fam - ',
     '10/06/23, 1:30\u202fam - ',
     '10/06/23, 1:31\u202fam - ',
     '10/06/23, 1:33\u202fam - ',
     '10/06/23, 6:59\u202fam - ',
     '10/06/23, 6:59\u202fam - ',
     '10/06/23, 9:45\u202fam - ',
     '10/06/23, 10:32\u202fam - ',
     '10/06/23, 10:32\u202fam - ',
     '10/06/23, 10:35\u202fam - ',
     '10/06/23, 1:05\u202fpm - ',
     '10/06/23, 4:21\u202fpm - ',
     '10/06/23, 9:53\u202fpm - ',
     '10/06/23, 9:53\u202fpm - ',
     '10/06/23, 9:54\u202fpm - ',
     '10/06/23, 9:54\u202fpm - ',
     '10/06/23, 9:54\u202fpm - ',
     '10/06/23, 9:54\u202fpm - ',
     '10/06/23, 9:54\u202fpm - ',
     '10/06/23, 9:54\u202fpm - ',
     '10/06/23, 9:54\u202fpm - ',
     '11/06/23, 9:13\u202fam - ',
     '11/06/23, 9:15\u202fam - ',
     '11/06/23, 9:30\u202fam - ',
     '11/06/23, 9:34\u202fam - ',
     '11/06/23, 9:41\u202fam - ',
     '11/06/23, 9:41\u202fam - ',
     '12/06/23, 8:47\u202fpm - ',
     '12/06/23, 8:52\u202fpm - ',
     '12/06/23, 8:53\u202fpm - ',
     '12/06/23, 8:54\u202fpm - ',
     '12/06/23, 8:54\u202fpm - ',
     '12/06/23, 8:56\u202fpm - ',
     '12/06/23, 8:57\u202fpm - ',
     '12/06/23, 9:13\u202fpm - ',
     '14/06/23, 2:07\u202fpm - ',
     '14/06/23, 2:36\u202fpm - ',
     '11/07/23, 10:03\u202fam - ',
     '11/07/23, 10:03\u202fam - ',
     '11/07/23, 10:03\u202fam - ',
     '11/07/23, 10:05\u202fam - ',
     '11/07/23, 10:05\u202fam - ',
     '11/07/23, 10:05\u202fam - ',
     '11/07/23, 10:05\u202fam - ',
     '11/07/23, 5:22\u202fpm - ',
     '11/07/23, 9:47\u202fpm - ',
     '11/07/23, 9:47\u202fpm - ',
     '11/07/23, 9:47\u202fpm - ',
     '11/07/23, 9:47\u202fpm - ',
     '11/07/23, 9:47\u202fpm - ',
     '11/07/23, 9:47\u202fpm - ',
     '11/07/23, 9:47\u202fpm - ',
     '11/07/23, 9:47\u202fpm - ',
     '11/07/23, 9:48\u202fpm - ',
     '11/07/23, 9:51\u202fpm - ',
     '11/07/23, 9:52\u202fpm - ',
     '11/07/23, 9:52\u202fpm - ',
     '11/07/23, 9:52\u202fpm - ',
     '11/07/23, 9:52\u202fpm - ',
     '11/07/23, 9:52\u202fpm - ',
     '11/07/23, 9:52\u202fpm - ',
     '11/07/23, 9:52\u202fpm - ',
     '11/07/23, 9:52\u202fpm - ',
     '11/07/23, 9:52\u202fpm - ',
     '11/07/23, 9:53\u202fpm - ',
     '11/07/23, 9:53\u202fpm - ',
     '11/07/23, 9:53\u202fpm - ',
     '11/07/23, 9:53\u202fpm - ',
     '11/07/23, 9:53\u202fpm - ',
     '11/07/23, 9:53\u202fpm - ',
     '11/07/23, 9:54\u202fpm - ',
     '11/07/23, 9:54\u202fpm - ',
     '11/07/23, 9:54\u202fpm - ',
     '11/07/23, 9:54\u202fpm - ',
     '11/07/23, 9:54\u202fpm - ',
     '11/07/23, 9:54\u202fpm - ',
     '11/07/23, 9:54\u202fpm - ',
     '11/07/23, 9:54\u202fpm - ',
     '11/07/23, 9:55\u202fpm - ',
     '11/07/23, 9:56\u202fpm - ',
     '11/07/23, 10:01\u202fpm - ',
     '11/07/23, 10:01\u202fpm - ',
     '11/07/23, 10:04\u202fpm - ',
     '12/07/23, 2:28\u202fpm - ',
     '12/07/23, 2:34\u202fpm - ',
     '12/07/23, 2:34\u202fpm - ',
     '12/07/23, 2:35\u202fpm - ',
     '12/07/23, 2:35\u202fpm - ',
     '12/07/23, 5:48\u202fpm - ',
     '12/07/23, 5:48\u202fpm - ',
     '12/07/23, 5:49\u202fpm - ',
     '12/07/23, 6:00\u202fpm - ',
     '13/07/23, 6:19\u202fpm - ',
     '14/07/23, 12:29\u202fpm - ',
     '14/07/23, 1:17\u202fpm - ',
     '15/07/23, 11:13\u202fam - ',
     '15/07/23, 1:39\u202fpm - ',
     '15/07/23, 1:39\u202fpm - ',
     '15/07/23, 6:46\u202fpm - ',
     '15/07/23, 6:46\u202fpm - ',
     '15/07/23, 6:47\u202fpm - ',
     '15/07/23, 6:47\u202fpm - ',
     '15/07/23, 6:47\u202fpm - ',
     '15/07/23, 7:28\u202fpm - ',
     '20/07/23, 5:31\u202fpm - ',
     '20/07/23, 5:31\u202fpm - ',
     '20/07/23, 6:26\u202fpm - ',
     '20/07/23, 6:27\u202fpm - ',
     '20/07/23, 6:38\u202fpm - ',
     '14/08/23, 8:46\u202fpm - ',
     '14/08/23, 8:46\u202fpm - ',
     '14/08/23, 9:29\u202fpm - ',
     '14/08/23, 9:30\u202fpm - ',
     '14/08/23, 9:30\u202fpm - ',
     '14/08/23, 9:30\u202fpm - ',
     '14/08/23, 9:30\u202fpm - ',
     '14/08/23, 9:30\u202fpm - ',
     '14/08/23, 9:30\u202fpm - ',
     '14/08/23, 9:30\u202fpm - ',
     '14/08/23, 9:30\u202fpm - ',
     '14/08/23, 11:19\u202fpm - ',
     '14/08/23, 11:19\u202fpm - ',
     '14/08/23, 11:19\u202fpm - ',
     '14/08/23, 11:19\u202fpm - ',
     '14/08/23, 11:19\u202fpm - ',
     '14/08/23, 11:19\u202fpm - ',
     '14/08/23, 11:19\u202fpm - ',
     '14/08/23, 11:19\u202fpm - ',
     '14/08/23, 11:19\u202fpm - ',
     '14/08/23, 11:19\u202fpm - ',
     '14/08/23, 11:19\u202fpm - ',
     '14/08/23, 11:19\u202fpm - ',
     '14/08/23, 11:20\u202fpm - ',
     '14/08/23, 11:20\u202fpm - ',
     '14/08/23, 11:24\u202fpm - ',
     '14/08/23, 11:37\u202fpm - ',
     '14/08/23, 11:39\u202fpm - ',
     '15/08/23, 6:17\u202fam - ',
     '15/08/23, 6:18\u202fam - ',
     '15/08/23, 6:18\u202fam - ',
     '15/08/23, 8:16\u202fam - ',
     '15/08/23, 9:56\u202fam - ',
     '15/08/23, 7:43\u202fpm - ',
     '15/08/23, 7:43\u202fpm - ',
     '15/08/23, 7:43\u202fpm - ',
     '15/08/23, 7:43\u202fpm - ',
     '15/08/23, 7:43\u202fpm - ',
     '15/08/23, 7:43\u202fpm - ',
     '15/08/23, 7:43\u202fpm - ',
     '15/08/23, 7:43\u202fpm - ',
     '15/08/23, 7:43\u202fpm - ',
     '15/08/23, 7:43\u202fpm - ',
     '15/08/23, 7:43\u202fpm - ',
     '15/08/23, 7:43\u202fpm - ',
     '15/08/23, 7:43\u202fpm - ',
     '15/08/23, 7:43\u202fpm - ',
     '15/08/23, 8:05\u202fpm - ',
     '15/08/23, 8:05\u202fpm - ',
     '15/08/23, 8:05\u202fpm - ',
     '15/08/23, 8:05\u202fpm - ',
     '15/08/23, 8:05\u202fpm - ',
     '15/08/23, 8:05\u202fpm - ',
     '15/08/23, 8:05\u202fpm - ',
     '15/08/23, 8:25\u202fpm - ',
     '15/08/23, 8:28\u202fpm - ',
     '15/08/23, 8:28\u202fpm - ',
     '15/08/23, 8:35\u202fpm - ',
     '15/08/23, 8:46\u202fpm - ',
     '15/08/23, 8:47\u202fpm - ',
     '15/08/23, 8:52\u202fpm - ',
     '15/08/23, 8:52\u202fpm - ',
     '15/08/23, 8:52\u202fpm - ',
     '15/08/23, 8:52\u202fpm - ',
     '15/08/23, 8:52\u202fpm - ',
     '15/08/23, 8:52\u202fpm - ',
     '15/08/23, 8:52\u202fpm - ',
     '15/08/23, 8:52\u202fpm - ',
     '15/08/23, 8:52\u202fpm - ',
     '15/08/23, 8:52\u202fpm - ',
     '15/08/23, 8:52\u202fpm - ',
     '15/08/23, 8:52\u202fpm - ',
     '15/08/23, 8:52\u202fpm - ',
     '15/08/23, 8:52\u202fpm - ',
     '15/08/23, 8:52\u202fpm - ',
     '15/08/23, 8:52\u202fpm - ',
     '15/08/23, 8:52\u202fpm - ',
     '15/08/23, 8:52\u202fpm - ',
     '15/08/23, 8:52\u202fpm - ',
     '15/08/23, 8:52\u202fpm - ',
     '15/08/23, 8:52\u202fpm - ',
     '15/08/23, 8:56\u202fpm - ',
     '15/08/23, 8:56\u202fpm - ',
     '15/08/23, 9:00\u202fpm - ',
     '15/08/23, 9:01\u202fpm - ',
     '15/08/23, 9:01\u202fpm - ',
     '15/08/23, 9:01\u202fpm - ',
     '15/08/23, 9:01\u202fpm - ',
     '15/08/23, 9:01\u202fpm - ',
     '15/08/23, 9:02\u202fpm - ',
     '15/08/23, 9:02\u202fpm - ',
     '15/08/23, 9:02\u202fpm - ',
     '15/08/23, 9:02\u202fpm - ',
     '15/08/23, 9:02\u202fpm - ',
     '15/08/23, 9:03\u202fpm - ',
     '15/08/23, 9:04\u202fpm - ',
     '15/08/23, 9:04\u202fpm - ',
     '15/08/23, 9:04\u202fpm - ',
     '15/08/23, 9:05\u202fpm - ',
     '15/08/23, 9:05\u202fpm - ',
     '15/08/23, 9:08\u202fpm - ',
     '19/08/23, 6:22\u202fpm - ',
     '19/08/23, 6:22\u202fpm - ',
     '19/08/23, 6:22\u202fpm - ',
     '19/08/23, 6:22\u202fpm - ',
     '19/08/23, 6:22\u202fpm - ',
     '19/08/23, 6:22\u202fpm - ',
     '19/08/23, 6:22\u202fpm - ',
     '19/08/23, 6:22\u202fpm - ',
     '19/08/23, 6:35\u202fpm - ',
     '19/08/23, 6:45\u202fpm - ',
     '19/08/23, 7:40\u202fpm - ',
     '19/08/23, 7:40\u202fpm - ',
     '19/08/23, 8:19\u202fpm - ',
     '19/08/23, 8:20\u202fpm - ',
     '19/08/23, 8:21\u202fpm - ',
     '19/08/23, 8:21\u202fpm - ',
     '19/08/23, 8:21\u202fpm - ',
     '19/08/23, 8:21\u202fpm - ',
     '19/08/23, 8:21\u202fpm - ',
     '19/08/23, 8:21\u202fpm - ',
     '19/08/23, 8:21\u202fpm - ',
     '19/08/23, 8:21\u202fpm - ',
     '19/08/23, 8:21\u202fpm - ',
     '19/08/23, 8:21\u202fpm - ',
     '19/08/23, 8:21\u202fpm - ',
     '19/08/23, 8:22\u202fpm - ',
     '19/08/23, 8:23\u202fpm - ',
     '19/08/23, 8:24\u202fpm - ',
     '19/08/23, 8:25\u202fpm - ',
     '19/08/23, 8:26\u202fpm - ',
     '19/08/23, 8:26\u202fpm - ',
     '19/08/23, 8:26\u202fpm - ',
     '19/08/23, 8:27\u202fpm - ',
     '19/08/23, 8:27\u202fpm - ',
     '19/08/23, 8:27\u202fpm - ',
     '19/08/23, 8:27\u202fpm - ',
     '19/08/23, 8:27\u202fpm - ',
     '19/08/23, 8:28\u202fpm - ',
     '19/08/23, 8:28\u202fpm - ',
     '19/08/23, 8:28\u202fpm - ',
     '19/08/23, 8:30\u202fpm - ',
     '19/08/23, 8:30\u202fpm - ',
     '19/08/23, 8:40\u202fpm - ',
     '19/08/23, 8:55\u202fpm - ',
     '19/08/23, 9:54\u202fpm - ',
     '19/08/23, 9:54\u202fpm - ',
     '19/08/23, 9:55\u202fpm - ',
     '19/08/23, 10:08\u202fpm - ',
     '19/08/23, 10:08\u202fpm - ',
     '19/08/23, 10:09\u202fpm - ',
     '19/08/23, 10:16\u202fpm - ',
     '19/08/23, 10:16\u202fpm - ',
     '20/08/23, 5:00\u202fam - ',
     '20/08/23, 5:01\u202fam - ',
     '20/08/23, 4:09\u202fpm - ',
     '20/08/23, 9:29\u202fpm - ',
     '20/08/23, 10:07\u202fpm - ',
     '20/08/23, 10:41\u202fpm - ',
     '20/08/23, 10:42\u202fpm - ',
     '20/08/23, 10:43\u202fpm - ',
     '20/08/23, 10:43\u202fpm - ',
     '30/08/23, 10:18\u202fam - ',
     '30/08/23, 10:18\u202fam - ',
     '30/08/23, 10:22\u202fam - ',
     '30/08/23, 7:49\u202fpm - ',
     '30/08/23, 7:50\u202fpm - ',
     '30/08/23, 7:51\u202fpm - ',
     '30/08/23, 7:51\u202fpm - ',
     '30/08/23, 7:51\u202fpm - ',
     '30/08/23, 7:51\u202fpm - ',
     '30/08/23, 7:53\u202fpm - ',
     '30/08/23, 7:54\u202fpm - ',
     '30/08/23, 7:56\u202fpm - ',
     '30/08/23, 8:12\u202fpm - ',
     '30/08/23, 8:13\u202fpm - ',
     '30/08/23, 8:13\u202fpm - ',
     '30/08/23, 8:13\u202fpm - ',
     '30/08/23, 8:14\u202fpm - ',
     '30/08/23, 8:14\u202fpm - ',
     '30/08/23, 8:14\u202fpm - ',
     '30/08/23, 8:14\u202fpm - ',
     '30/08/23, 8:14\u202fpm - ',
     '30/08/23, 8:14\u202fpm - ',
     '30/08/23, 8:14\u202fpm - ',
     '30/08/23, 8:15\u202fpm - ',
     '30/08/23, 8:16\u202fpm - ',
     '30/08/23, 9:59\u202fpm - ',
     '01/09/23, 3:36\u202fpm - ',
     '01/09/23, 3:36\u202fpm - ',
     '01/09/23, 3:37\u202fpm - ',
     '01/09/23, 3:39\u202fpm - ',
     '01/09/23, 3:40\u202fpm - ',
     '01/09/23, 3:41\u202fpm - ',
     '01/09/23, 3:41\u202fpm - ',
     '01/09/23, 3:41\u202fpm - ',
     '01/09/23, 3:41\u202fpm - ',
     '01/09/23, 3:42\u202fpm - ',
     '01/09/23, 3:43\u202fpm - ',
     '01/09/23, 3:45\u202fpm - ',
     '01/09/23, 3:45\u202fpm - ',
     '01/09/23, 3:45\u202fpm - ',
     '01/09/23, 3:45\u202fpm - ',
     '01/09/23, 3:45\u202fpm - ',
     '01/09/23, 3:45\u202fpm - ',
     '01/09/23, 3:46\u202fpm - ',
     '01/09/23, 3:46\u202fpm - ',
     '01/09/23, 3:46\u202fpm - ',
     '01/09/23, 3:46\u202fpm - ',
     '01/09/23, 3:47\u202fpm - ',
     '01/09/23, 3:47\u202fpm - ',
     '01/09/23, 3:48\u202fpm - ',
     '01/09/23, 3:48\u202fpm - ',
     '01/09/23, 3:48\u202fpm - ',
     '01/09/23, 3:48\u202fpm - ',
     '01/09/23, 3:48\u202fpm - ',
     '01/09/23, 3:48\u202fpm - ',
     '01/09/23, 3:48\u202fpm - ',
     '01/09/23, 3:49\u202fpm - ',
     '24/09/23, 1:56\u202fpm - ',
     '24/09/23, 2:16\u202fpm - ',
     '24/09/23, 2:16\u202fpm - ',
     '24/09/23, 11:07\u202fpm - ',
     '24/09/23, 11:33\u202fpm - ',
     '25/09/23, 6:23\u202fpm - ',
     '29/09/23, 6:29\u202fpm - ',
     '29/09/23, 6:31\u202fpm - ',
     '29/09/23, 6:35\u202fpm - ',
     '29/09/23, 6:35\u202fpm - ',
     '29/09/23, 6:35\u202fpm - ',
     '29/09/23, 6:35\u202fpm - ',
     '29/09/23, 6:41\u202fpm - ',
     '29/09/23, 6:44\u202fpm - ',
     '29/09/23, 6:52\u202fpm - ',
     '29/09/23, 6:54\u202fpm - ',
     '29/09/23, 6:54\u202fpm - ',
     '29/09/23, 6:54\u202fpm - ',
     '29/09/23, 6:54\u202fpm - ',
     '29/09/23, 6:54\u202fpm - ',
     '29/09/23, 6:55\u202fpm - ',
     '29/09/23, 6:55\u202fpm - ',
     '29/09/23, 6:55\u202fpm - ',
     '29/09/23, 6:55\u202fpm - ',
     '29/09/23, 6:55\u202fpm - ',
     '29/09/23, 6:55\u202fpm - ',
     '29/09/23, 7:00\u202fpm - ',
     '29/09/23, 7:25\u202fpm - ',
     '30/09/23, 1:43\u202fam - ',
     '30/09/23, 5:05\u202fam - ',
     '30/09/23, 5:05\u202fam - ',
     '30/09/23, 5:06\u202fam - ',
     '30/09/23, 5:06\u202fam - ',
     '30/09/23, 5:06\u202fam - ',
     '30/09/23, 5:06\u202fam - ',
     '30/09/23, 5:17\u202fpm - ',
     '01/10/23, 10:13\u202fam - ',
     '01/10/23, 10:14\u202fam - ',
     '01/10/23, 10:15\u202fam - ',
     '01/10/23, 10:26\u202fam - ',
     '01/10/23, 12:06\u202fpm - ',
     '01/10/23, 12:07\u202fpm - ',
     '01/10/23, 12:53\u202fpm - ',
     '01/10/23, 12:53\u202fpm - ',
     '01/10/23, 12:53\u202fpm - ',
     '01/10/23, 12:54\u202fpm - ',
     '01/10/23, 12:54\u202fpm - ',
     '01/10/23, 12:54\u202fpm - ',
     '01/10/23, 12:54\u202fpm - ',
     '01/10/23, 12:57\u202fpm - ',
     '01/10/23, 1:05\u202fpm - ',
     '01/10/23, 3:28\u202fpm - ',
     '09/10/23, 10:48\u202fpm - ',
     '09/10/23, 10:48\u202fpm - ',
     '09/10/23, 10:48\u202fpm - ',
     '09/10/23, 10:57\u202fpm - ',
     '09/10/23, 10:57\u202fpm - ',
     '09/10/23, 11:27\u202fpm - ',
     '12/10/23, 2:46\u202fpm - ',
     '12/10/23, 2:47\u202fpm - ',
     '12/10/23, 2:47\u202fpm - ',
     '15/10/23, 1:47\u202fpm - ',
     '15/10/23, 1:48\u202fpm - ',
     '15/10/23, 1:48\u202fpm - ',
     '15/10/23, 1:48\u202fpm - ',
     '15/10/23, 1:48\u202fpm - ',
     '15/10/23, 1:48\u202fpm - ',
     '15/10/23, 1:49\u202fpm - ',
     '15/10/23, 1:49\u202fpm - ',
     '15/10/23, 1:49\u202fpm - ',
     '15/10/23, 1:50\u202fpm - ',
     '15/10/23, 1:50\u202fpm - ',
     '15/10/23, 1:50\u202fpm - ',
     '15/10/23, 1:51\u202fpm - ',
     '15/10/23, 1:51\u202fpm - ',
     '15/10/23, 1:54\u202fpm - ',
     '15/10/23, 1:54\u202fpm - ',
     '16/10/23, 7:47\u202fpm - ',
     '16/10/23, 7:59\u202fpm - ',
     '16/10/23, 7:59\u202fpm - ',
     '16/10/23, 7:59\u202fpm - ',
     '16/10/23, 8:00\u202fpm - ',
     '16/10/23, 8:01\u202fpm - ',
     '16/10/23, 8:15\u202fpm - ',
     '16/10/23, 8:15\u202fpm - ',
     '20/10/23, 12:16\u202fam - ',
     '20/10/23, 12:18\u202fam - ',
     '20/10/23, 12:18\u202fam - ',
     '21/10/23, 12:15\u202fam - ',
     '21/10/23, 12:15\u202fam - ',
     '21/10/23, 12:16\u202fam - ',
     '21/10/23, 12:17\u202fam - ',
     '21/10/23, 12:19\u202fam - ',
     '21/10/23, 12:19\u202fam - ',
     '21/10/23, 12:19\u202fam - ',
     '21/10/23, 12:19\u202fam - ',
     '21/10/23, 12:21\u202fam - ',
     '21/10/23, 12:22\u202fam - ',
     '21/10/23, 12:33\u202fam - ',
     '21/10/23, 12:33\u202fam - ',
     '21/10/23, 12:33\u202fam - ',
     '21/10/23, 12:34\u202fam - ',
     '21/10/23, 12:34\u202fam - ',
     '21/10/23, 12:34\u202fam - ',
     '21/10/23, 12:40\u202fam - ',
     '24/10/23, 9:51\u202fpm - ',
     '24/10/23, 10:11\u202fpm - ',
     '24/10/23, 10:44\u202fpm - ',
     '25/10/23, 9:36\u202fam - ',
     '25/10/23, 9:36\u202fam - ',
     '25/10/23, 9:47\u202fam - ',
     '25/10/23, 10:51\u202fam - ',
     '25/10/23, 11:03\u202fam - ',
     '25/10/23, 12:37\u202fpm - ',
     '03/11/23, 11:57\u202fpm - ',
     '03/11/23, 11:57\u202fpm - ',
     '03/11/23, 11:57\u202fpm - ',
     '04/11/23, 12:00\u202fam - ',
     '04/11/23, 12:02\u202fam - ',
     '04/11/23, 12:02\u202fam - ',
     '04/11/23, 12:02\u202fam - ',
     '06/11/23, 3:24\u202fam - ',
     '06/11/23, 8:45\u202fam - ',
     '06/11/23, 10:06\u202fam - ',
     '06/11/23, 3:41\u202fpm - ',
     '09/11/23, 7:32\u202fam - ',
     '09/11/23, 7:33\u202fam - ',
     '09/11/23, 7:36\u202fam - ',
     '09/11/23, 9:47\u202fam - ',
     '09/11/23, 10:39\u202fam - ',
     '09/11/23, 10:39\u202fam - ',
     '09/11/23, 11:01\u202fam - ',
     '09/11/23, 12:50\u202fpm - ',
     '09/11/23, 7:55\u202fpm - ',
     '09/11/23, 7:55\u202fpm - ',
     '09/11/23, 8:08\u202fpm - ',
     '09/11/23, 8:09\u202fpm - ',
     '09/11/23, 8:10\u202fpm - ',
     '09/11/23, 8:41\u202fpm - ',
     '09/11/23, 8:41\u202fpm - ',
     '09/11/23, 8:42\u202fpm - ',
     '09/11/23, 8:45\u202fpm - ',
     '09/11/23, 8:45\u202fpm - ',
     '09/11/23, 9:02\u202fpm - ',
     '09/11/23, 9:04\u202fpm - ',
     '09/11/23, 9:14\u202fpm - ',
     '10/11/23, 7:54\u202fam - ',
     '10/11/23, 8:11\u202fam - ',
     '10/11/23, 9:49\u202fam - ',
     '10/11/23, 9:51\u202fam - ',
     '11/11/23, 3:32\u202fpm - ',
     '12/11/23, 12:19\u202fam - ',
     '12/11/23, 12:19\u202fam - ',
     '13/11/23, 11:59\u202fam - ',
     '13/11/23, 12:42\u202fpm - ',
     '13/11/23, 12:43\u202fpm - ',
     '13/11/23, 12:43\u202fpm - ',
     '13/11/23, 12:44\u202fpm - ',
     '13/11/23, 12:45\u202fpm - ',
     '13/11/23, 12:45\u202fpm - ',
     '13/11/23, 12:51\u202fpm - ',
     '13/11/23, 12:51\u202fpm - ',
     '13/11/23, 12:52\u202fpm - ',
     '13/11/23, 12:52\u202fpm - ',
     '13/11/23, 12:52\u202fpm - ',
     '13/11/23, 12:53\u202fpm - ',
     '13/11/23, 12:53\u202fpm - ',
     '13/11/23, 12:54\u202fpm - ',
     '13/11/23, 12:54\u202fpm - ',
     '13/11/23, 12:54\u202fpm - ',
     '13/11/23, 12:54\u202fpm - ',
     '13/11/23, 3:01\u202fpm - ',
     '13/11/23, 3:11\u202fpm - ',
     '13/11/23, 4:01\u202fpm - ',
     '13/11/23, 4:02\u202fpm - ',
     '13/11/23, 4:02\u202fpm - ',
     '13/11/23, 4:05\u202fpm - ',
     '13/11/23, 4:06\u202fpm - ',
     '13/11/23, 4:07\u202fpm - ',
     '13/11/23, 4:07\u202fpm - ',
     '13/11/23, 4:07\u202fpm - ',
     '13/11/23, 4:07\u202fpm - ',
     '13/11/23, 4:07\u202fpm - ',
     '13/11/23, 4:07\u202fpm - ',
     '13/11/23, 4:08\u202fpm - ',
     '13/11/23, 4:08\u202fpm - ',
     '13/11/23, 4:08\u202fpm - ',
     '13/11/23, 4:08\u202fpm - ',
     '13/11/23, 4:08\u202fpm - ',
     '13/11/23, 4:09\u202fpm - ',
     '13/11/23, 4:09\u202fpm - ',
     '13/11/23, 4:09\u202fpm - ',
     '13/11/23, 4:09\u202fpm - ',
     '13/11/23, 4:10\u202fpm - ',
     '13/11/23, 4:10\u202fpm - ',
     '13/11/23, 4:10\u202fpm - ',
     '13/11/23, 4:10\u202fpm - ',
     '13/11/23, 4:54\u202fpm - ',
     '13/11/23, 4:54\u202fpm - ',
     '13/11/23, 4:54\u202fpm - ',
     '13/11/23, 5:13\u202fpm - ',
     '13/11/23, 5:23\u202fpm - ',
     '13/11/23, 5:23\u202fpm - ',
     '13/11/23, 5:25\u202fpm - ',
     '13/11/23, 5:25\u202fpm - ',
     '13/11/23, 5:26\u202fpm - ',
     '13/11/23, 5:26\u202fpm - ',
     '13/11/23, 5:26\u202fpm - ',
     '13/11/23, 5:26\u202fpm - ',
     '13/11/23, 5:27\u202fpm - ',
     '13/11/23, 5:27\u202fpm - ',
     '13/11/23, 5:30\u202fpm - ',
     '13/11/23, 10:10\u202fpm - ',
     '13/11/23, 10:10\u202fpm - ',
     '13/11/23, 10:10\u202fpm - ',
     '13/11/23, 10:11\u202fpm - ',
     '13/11/23, 10:12\u202fpm - ',
     '13/11/23, 10:12\u202fpm - ',
     '13/11/23, 10:12\u202fpm - ',
     '13/11/23, 10:39\u202fpm - ',
     '13/11/23, 10:39\u202fpm - ',
     '13/11/23, 10:39\u202fpm - ',
     '13/11/23, 10:40\u202fpm - ',
     '13/11/23, 10:40\u202fpm - ',
     '13/11/23, 10:42\u202fpm - ',
     '13/11/23, 10:42\u202fpm - ',
     '13/11/23, 10:43\u202fpm - ',
     '13/11/23, 10:44\u202fpm - ',
     '13/11/23, 10:45\u202fpm - ',
     '13/11/23, 10:50\u202fpm - ',
     '13/11/23, 10:50\u202fpm - ',
     '13/11/23, 10:50\u202fpm - ',
     '13/11/23, 10:51\u202fpm - ',
     '13/11/23, 10:51\u202fpm - ',
     '13/11/23, 11:23\u202fpm - ',
     '13/11/23, 11:24\u202fpm - ',
     '13/11/23, 11:24\u202fpm - ',
     '13/11/23, 11:24\u202fpm - ',
     '13/11/23, 11:24\u202fpm - ',
     '13/11/23, 11:24\u202fpm - ',
     '06/12/23, 8:09\u202fpm - ',
     '06/12/23, 8:09\u202fpm - ',
     '07/12/23, 1:31\u202fpm - ',
     '07/12/23, 1:32\u202fpm - ',
     '07/12/23, 1:32\u202fpm - ',
     '07/12/23, 1:32\u202fpm - ',
     '07/12/23, 1:33\u202fpm - ',
     '07/12/23, 1:33\u202fpm - ',
     '07/12/23, 1:33\u202fpm - ',
     '13/12/23, 6:38\u202fpm - ',
     '13/12/23, 6:57\u202fpm - ',
     '13/12/23, 6:58\u202fpm - ',
     '16/12/23, 12:36\u202fam - ',
     '16/12/23, 12:37\u202fam - ',
     '16/12/23, 12:37\u202fam - ',
     '16/12/23, 12:37\u202fam - ',
     '16/12/23, 12:37\u202fam - ',
     '16/12/23, 12:38\u202fam - ',
     '16/12/23, 12:41\u202fam - ',
     '16/12/23, 12:41\u202fam - ',
     '16/12/23, 12:41\u202fam - ',
     '16/12/23, 12:41\u202fam - ',
     '16/12/23, 12:41\u202fam - ',
     '16/12/23, 12:41\u202fam - ',
     '16/12/23, 12:41\u202fam - ',
     '16/12/23, 12:42\u202fam - ',
     '16/12/23, 12:42\u202fam - ',
     '16/12/23, 12:42\u202fam - ',
     '16/12/23, 12:42\u202fam - ',
     '16/12/23, 12:42\u202fam - ',
     '16/12/23, 12:42\u202fam - ',
     '16/12/23, 12:42\u202fam - ',
     '16/12/23, 12:43\u202fam - ',
     '16/12/23, 12:43\u202fam - ',
     '16/12/23, 12:43\u202fam - ',
     '16/12/23, 12:43\u202fam - ',
     '16/12/23, 12:43\u202fam - ',
     '16/12/23, 12:43\u202fam - ',
     '16/12/23, 12:43\u202fam - ',
     '16/12/23, 12:43\u202fam - ',
     '16/12/23, 12:43\u202fam - ',
     '16/12/23, 12:44\u202fam - ',
     '16/12/23, 12:44\u202fam - ',
     '16/12/23, 12:44\u202fam - ',
     '16/12/23, 12:44\u202fam - ',
     '16/12/23, 12:44\u202fam - ',
     '16/12/23, 12:44\u202fam - ',
     '16/12/23, 12:44\u202fam - ',
     '16/12/23, 12:44\u202fam - ',
     '16/12/23, 12:44\u202fam - ',
     '16/12/23, 12:45\u202fam - ',
     '16/12/23, 12:45\u202fam - ',
     '16/12/23, 12:45\u202fam - ',
     '16/12/23, 12:45\u202fam - ',
     '16/12/23, 12:46\u202fam - ',
     '16/12/23, 12:46\u202fam - ',
     '16/12/23, 12:46\u202fam - ',
     '16/12/23, 12:46\u202fam - ',
     '16/12/23, 12:46\u202fam - ',
     '16/12/23, 12:47\u202fam - ',
     '16/12/23, 12:47\u202fam - ',
     '16/12/23, 12:47\u202fam - ',
     '16/12/23, 12:47\u202fam - ',
     '16/12/23, 12:47\u202fam - ',
     '16/12/23, 12:47\u202fam - ',
     '16/12/23, 12:48\u202fam - ',
     '16/12/23, 12:48\u202fam - ',
     '16/12/23, 12:48\u202fam - ',
     '16/12/23, 12:49\u202fam - ',
     '16/12/23, 12:49\u202fam - ',
     '16/12/23, 8:45\u202fam - ',
     '16/12/23, 8:46\u202fam - ',
     '16/12/23, 12:29\u202fpm - ',
     '16/12/23, 7:54\u202fpm - ',
     '16/12/23, 7:54\u202fpm - ',
     '16/12/23, 7:54\u202fpm - ',
     '16/12/23, 7:54\u202fpm - ',
     '17/12/23, 3:43\u202fam - ',
     '17/12/23, 3:43\u202fam - ',
     '17/12/23, 10:42\u202fam - ',
     '17/12/23, 10:42\u202fam - ',
     '17/12/23, 10:42\u202fam - ',
     '17/12/23, 10:42\u202fam - ',
     '17/12/23, 10:43\u202fam - ',
     '17/12/23, 10:43\u202fam - ',
     '17/12/23, 10:43\u202fam - ',
     '17/12/23, 10:43\u202fam - ',
     '17/12/23, 10:43\u202fam - ',
     '17/12/23, 10:44\u202fam - ',
     '17/12/23, 12:06\u202fpm - ',
     '17/12/23, 5:12\u202fpm - ',
     '24/12/23, 9:06\u202fpm - ',
     '24/12/23, 9:09\u202fpm - ',
     '24/12/23, 9:09\u202fpm - ',
     '24/12/23, 9:09\u202fpm - ',
     '24/12/23, 9:09\u202fpm - ',
     '24/12/23, 9:09\u202fpm - ',
     '24/12/23, 9:09\u202fpm - ',
     '24/12/23, 9:09\u202fpm - ',
     '24/12/23, 9:09\u202fpm - ',
     '24/12/23, 9:09\u202fpm - ',
     '24/12/23, 9:15\u202fpm - ',
     '24/12/23, 9:16\u202fpm - ',
     '24/12/23, 9:16\u202fpm - ',
     '24/12/23, 9:16\u202fpm - ',
     '24/12/23, 9:16\u202fpm - ',
     '24/12/23, 9:16\u202fpm - ',
     '24/12/23, 9:17\u202fpm - ',
     '24/12/23, 9:17\u202fpm - ',
     '24/12/23, 9:18\u202fpm - ',
     '24/12/23, 9:18\u202fpm - ',
     '24/12/23, 9:19\u202fpm - ',
     '24/12/23, 9:20\u202fpm - ',
     '24/12/23, 9:20\u202fpm - ',
     '24/12/23, 9:20\u202fpm - ',
     '24/12/23, 9:21\u202fpm - ',
     '24/12/23, 9:21\u202fpm - ',
     '24/12/23, 9:21\u202fpm - ',
     '24/12/23, 9:21\u202fpm - ',
     '24/12/23, 9:21\u202fpm - ',
     '24/12/23, 9:28\u202fpm - ',
     '24/12/23, 9:28\u202fpm - ',
     '24/12/23, 10:15\u202fpm - ',
     '24/12/23, 10:15\u202fpm - ',
     '24/12/23, 10:15\u202fpm - ',
     '24/12/23, 10:16\u202fpm - ',
     '24/12/23, 10:16\u202fpm - ',
     '24/12/23, 10:16\u202fpm - ',
     '24/12/23, 10:17\u202fpm - ',
     '24/12/23, 10:17\u202fpm - ',
     '24/12/23, 10:17\u202fpm - ',
     '24/12/23, 10:19\u202fpm - ',
     '24/12/23, 10:26\u202fpm - ',
     '24/12/23, 10:27\u202fpm - ',
     '24/12/23, 10:27\u202fpm - ',
     '24/12/23, 10:27\u202fpm - ',
     '26/12/23, 10:12\u202fam - ',
     '26/12/23, 10:12\u202fam - ',
     '26/12/23, 10:13\u202fam - ',
     '26/12/23, 10:13\u202fam - ',
     '26/12/23, 10:13\u202fam - ',
     '26/12/23, 10:13\u202fam - ',
     '26/12/23, 10:14\u202fam - ',
     '26/12/23, 10:14\u202fam - ',
     '26/12/23, 10:14\u202fam - ',
     '26/12/23, 10:15\u202fam - ',
     '26/12/23, 10:15\u202fam - ',
     '26/12/23, 4:27\u202fpm - ',
     '26/12/23, 4:32\u202fpm - ',
     '26/12/23, 4:32\u202fpm - ',
     '26/12/23, 4:32\u202fpm - ',
     '26/12/23, 4:32\u202fpm - ',
     '26/12/23, 4:32\u202fpm - ',
     '26/12/23, 6:24\u202fpm - ',
     '26/12/23, 6:24\u202fpm - ',
     '26/12/23, 6:44\u202fpm - ',
     '26/12/23, 6:44\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:05\u202fpm - ',
     '26/12/23, 7:11\u202fpm - ',
     '26/12/23, 7:11\u202fpm - ',
     '26/12/23, 7:11\u202fpm - ',
     '26/12/23, 7:12\u202fpm - ',
     '26/12/23, 7:12\u202fpm - ',
     '26/12/23, 7:12\u202fpm - ',
     '26/12/23, 7:12\u202fpm - ',
     '26/12/23, 7:12\u202fpm - ',
     '27/12/23, 7:31\u202fpm - ',
     '27/12/23, 7:32\u202fpm - ',
     '27/12/23, 7:32\u202fpm - ',
     '27/12/23, 7:33\u202fpm - ',
     '27/12/23, 7:33\u202fpm - ',
     '27/12/23, 7:34\u202fpm - ',
     '27/12/23, 7:34\u202fpm - ',
     '27/12/23, 7:34\u202fpm - ',
     '27/12/23, 7:34\u202fpm - ',
     '27/12/23, 7:34\u202fpm - ',
     '27/12/23, 7:35\u202fpm - ',
     '28/12/23, 8:37\u202fam - ',
     '28/12/23, 8:45\u202fam - ',
     '28/12/23, 8:46\u202fam - ',
     '28/12/23, 10:04\u202fam - ',
     '28/12/23, 10:25\u202fam - ',
     '28/12/23, 10:26\u202fam - ',
     '28/12/23, 10:27\u202fam - ',
     '28/12/23, 10:27\u202fam - ',
     '28/12/23, 10:27\u202fam - ',
     '28/12/23, 10:28\u202fam - ',
     '28/12/23, 10:28\u202fam - ',
     '28/12/23, 10:30\u202fam - ',
     '28/12/23, 10:30\u202fam - ',
     '28/12/23, 10:30\u202fam - ',
     '28/12/23, 10:32\u202fam - ',
     '28/12/23, 10:36\u202fam - ',
     '28/12/23, 10:40\u202fam - ',
     '28/12/23, 10:52\u202fam - ',
     '28/12/23, 11:05\u202fam - ',
     '28/12/23, 11:06\u202fam - ',
     '28/12/23, 11:07\u202fam - ',
     '28/12/23, 11:08\u202fam - ',
     '28/12/23, 11:09\u202fam - ',
     '28/12/23, 11:44\u202fam - ',
     '01/01/24, 12:19\u202fam - ',
     '01/01/24, 5:50\u202fam - ',
     '01/01/24, 5:52\u202fam - ',
     '01/01/24, 7:27\u202fam - ',
     '01/01/24, 10:51\u202fpm - ',
     '06/01/24, 9:47\u202fam - ',
     '06/01/24, 9:47\u202fam - ',
     '06/01/24, 9:57\u202fam - ',
     '06/01/24, 2:36\u202fpm - ',
     '06/01/24, 2:36\u202fpm - ',
     '06/01/24, 3:37\u202fpm - ',
     '07/01/24, 3:19\u202fam - ',
     '07/01/24, 3:20\u202fam - ',
     '07/01/24, 3:21\u202fam - ',
     '08/01/24, 12:37\u202fam - ',
     '08/01/24, 12:38\u202fam - ',
     '12/01/24, 10:19\u202fam - ',
     '12/01/24, 10:19\u202fam - ',
     '12/01/24, 10:19\u202fam - ',
     '12/01/24, 10:20\u202fam - ',
     '12/01/24, 10:42\u202fam - ',
     '12/01/24, 10:42\u202fam - ',
     '12/01/24, 10:42\u202fam - ',
     '12/01/24, 10:46\u202fam - ',
     '17/01/24, 12:33\u202fam - ',
     '17/01/24, 12:35\u202fam - ',
     '17/01/24, 12:36\u202fam - ',
     '17/01/24, 12:36\u202fam - ',
     '17/01/24, 12:36\u202fam - ',
     '17/01/24, 12:36\u202fam - ',
     '17/01/24, 12:36\u202fam - ',
     '18/01/24, 12:27\u202fam - ',
     '18/01/24, 12:28\u202fam - ',
     '18/01/24, 12:29\u202fam - ',
     '18/01/24, 12:29\u202fam - ',
     '18/01/24, 12:30\u202fam - ',
     '18/01/24, 12:30\u202fam - ',
     '18/01/24, 8:50\u202fam - ',
     '18/01/24, 9:02\u202fam - ',
     '18/01/24, 9:03\u202fam - ',
     '21/01/24, 10:37\u202fam - ',
     '21/01/24, 10:37\u202fam - ',
     '21/01/24, 10:37\u202fam - ',
     '21/01/24, 10:57\u202fam - ',
     '21/01/24, 10:57\u202fam - ',
     '21/01/24, 11:20\u202fam - ',
     '21/01/24, 11:21\u202fam - ',
     '22/01/24, 1:00\u202fam - ',
     '22/01/24, 3:02\u202fam - ',
     '22/01/24, 10:14\u202fam - ',
     '22/01/24, 3:04\u202fpm - ',
     '22/01/24, 3:55\u202fpm - ',
     '22/01/24, 3:55\u202fpm - ',
     ...]




```python
print("Length of messages:", len(messages))
print("Length of dates:", len(dates))
min_length = min(len(messages), len(dates))
messages = messages[:min_length]
dates = dates[:min_length]


```

    Length of messages: 1618
    Length of dates: 1617
    


```python
df = pd.DataFrame({'user_message': messages, 'message_date': dates})
# Remove non-breaking space characters (Unicode \u202f) and strip the trailing " -"
df['message_date'] = df['message_date'].str.replace('\u202f', ' ').str.strip(' -')

# Convert 'message_date' to datetime with the correct format
df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M %p')

# Rename column for consistency
df.rename(columns={'message_date': 'date'}, inplace=True)

# Display the DataFrame
print(df.head())

```

                                            user_message                date
    0                                                    2023-04-26 11:01:00
    1  Messages and calls are end-to-end encrypted. N... 2023-04-26 11:01:00
    2                           You created this group\n 2023-04-26 11:01:00
    3  You updated the message timer. New messages wi... 2023-04-26 11:19:00
    4                    You changed this group's icon\n 2023-04-27 15:20:00
    


```python
import re

# Initialize lists to store users and messages
user = []
message_text = []  # Renamed to avoid conflict with the 'message' variable in the loop

# Iterate over the 'user_message' column
for msg in df['user_message']:
    entry = re.split('([\w\W]+?):\s', msg)
    
    if entry[1:]:  # If there is a valid split, meaning a user and a message
        user.append(entry[1])
        message_text.append(entry[2])
    else:  # If the message doesn't follow the expected format
        user.append('group_notification')
        message_text.append(entry[0])

# Add the extracted 'user' and 'message' columns to the DataFrame
df['user'] = user
df['message'] = message_text

# Drop the original 'user_message' column
df.drop(columns=['user_message'], inplace=True)

# Display the updated DataFrame
df.head()

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>user</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2023-04-26 11:01:00</td>
      <td>group_notification</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>2023-04-26 11:01:00</td>
      <td>group_notification</td>
      <td>Messages and calls are end-to-end encrypted. N...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2023-04-26 11:01:00</td>
      <td>group_notification</td>
      <td>You created this group\n</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2023-04-26 11:19:00</td>
      <td>group_notification</td>
      <td>You updated the message timer. New messages wi...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2023-04-27 15:20:00</td>
      <td>group_notification</td>
      <td>You changed this group's icon\n</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Extract year, month name, day, hour, and minute from the 'date' column
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month_name()
df['day'] = df['date'].dt.day
df['hour'] = df['date'].dt.hour
df['minute'] = df['date'].dt.minute

```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>user</th>
      <th>message</th>
      <th>year</th>
      <th>month</th>
      <th>day</th>
      <th>hour</th>
      <th>minute</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2023-04-26 11:01:00</td>
      <td>group_notification</td>
      <td></td>
      <td>2023</td>
      <td>April</td>
      <td>26</td>
      <td>11</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2023-04-26 11:01:00</td>
      <td>group_notification</td>
      <td>Messages and calls are end-to-end encrypted. N...</td>
      <td>2023</td>
      <td>April</td>
      <td>26</td>
      <td>11</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2023-04-26 11:01:00</td>
      <td>group_notification</td>
      <td>You created this group\n</td>
      <td>2023</td>
      <td>April</td>
      <td>26</td>
      <td>11</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2023-04-26 11:19:00</td>
      <td>group_notification</td>
      <td>You updated the message timer. New messages wi...</td>
      <td>2023</td>
      <td>April</td>
      <td>26</td>
      <td>11</td>
      <td>19</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2023-04-27 15:20:00</td>
      <td>group_notification</td>
      <td>You changed this group's icon\n</td>
      <td>2023</td>
      <td>April</td>
      <td>27</td>
      <td>15</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>




```python
f = 
```
