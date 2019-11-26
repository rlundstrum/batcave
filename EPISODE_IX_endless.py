#             EPISODE IX
# CALCULATING DATES WITH IF STATEMENTS

import os, time, random
from datetime import date, timedelta, datetime
from random import randint
from colorama import init, Fore, Back, Style
init(convert=True)#dont forget this init line. Don't know what it means, though....

while True: #start loop to run forever
    episodeIX = datetime(2019, 12, 20, 8, 0)
    rightNow = datetime.now()
    daysLeft = episodeIX - rightNow
    oneDay = episodeIX - timedelta(days=1)
    rebelScum = os.getlogin()
    quoteList = ['I am one with the force, the force is with me. - Chirrut Imwe',
                 'I love you. - Leia    I know. - Han',
                 'You have disappointed me for the last time. - Vader',
                 "It's a trap!! - Admiral Ackbar",
                 'Do. Or do not. There is no try. - Yoda',
                 'In my experience there is no such thing as luck. - Obi-Wan Kenobi',
                 "I've got a bad feeling about this. - basically everyone",
                 'Stay on target. - Gold Five',
                 '*Nods* - Boba Fett',
                 'Why, you stuck-up, half-witted, scruffy-looking nerf herder! - Leia Organa',
                 "There's always a bigger fish. - Qui-Gon Jinn",
                 "You can't stop the change, any more than you can stop the suns from setting. - Shmi Skywalker",
                 'Fear is the path to the dark side. Fear leads to anger; anger leads to hate; hate leads to suffering. I sense much fear in you. - Yoda',
                 "I hate sand. - (We'd rather forget)",
                 "Don't try it, I have the high ground! - Obi-Wan Kenobi",
                 'Luminous beings are we, not this crude matter. - Yoda',
                 'Maclurky! - Greedo (seriously, WTF George Lucas...)',
                 "Don't be too proud of this technological terror you've constructed. The ability to destroy a planet is insignificant next to the power of the Force. - Vader",
                 'And I thought they smelled bad on the outside. - Han Solo']
    if rightNow == episodeIX:
        print ('You are not at the theater? I find your lack of commitment disturbing.')
    elif rightNow == oneDay:
        print ('Lord ', rebelScum,'I have a good feeling about this.', 
        daysLeft.days,'day left!')
    elif rightNow < episodeIX:
        print (Style.BRIGHT + Fore.YELLOW + random.choice(quoteList)+ Style.RESET_ALL)
        print ('Patience, young', rebelScum,' ', daysLeft, ', you have.')
    else:
        print ('Maclurky! You missed it!')
    time.sleep(5)
#May The Force be with you.