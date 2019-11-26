#             EPISODE IX
# CALCULATING DATES WITH IF STATEMENTS
import os, time, arcpy, random
from datetime import date, timedelta, datetime
from random import randint
#while True: #start loop to run forever
for R in range(5):
    #episodeIX = datetime(2019, 12, 21, 8, 0, 
    episodeIX = arcpy.GetParameter(0) #get the input date parameter from the geoprocessing window
    rightNow = datetime.now()
    daysLeft = episodeIX - rightNow
    oneDay = episodeIX - timedelta(days=1)
    rebelScum = os.getlogin() #get the computer username
    # fc is a point feature class
    randomX = randint(-19000000, 19000000)#in meters somewhere on earth
    randomY = randint(-19000000, 19000000)
    fc = "C:/Users/russe/Documents/ArcGIS/Projects/EPISODE_IX/EpisodeIX.gdb/Stars"
    #build list of quotes, maybe use table later?
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
                 "Don't be too proud of this technological terror you've constructed. The ability to destroy a planet is insignificant next to the power of the Force. - Vader"]
    rowValue = (random.choice(quoteList) + " (" + str(daysLeft) + " left you have.)",(randomX, randomY))#stuff to enter into the new point record
    cursor = arcpy.da.InsertCursor(fc,["Label", "SHAPE@XY"])
    if rightNow < episodeIX: #many days leading up to screening day
        arcpy.AddMessage(random.choice(quoteList))
        arcpy.AddMessage('::Patience young padawan ' + str(daysLeft) + ' left you have.')
        arcpy.AddMessage('.')
        cursor.insertRow(rowValue) #add random point to the map
    elif rightNow > oneDay: #one day away special message
        arcpy.AddMessage( 'Lord ' + rebelScum + ', ' + str(daysLeft) + ' left, I have a good feeling about this.')
    elif rightNow == episodeIX: #movie day!
        arcpy.AddMessage('You are not at the theater? I find your lack of commitment disturbing.')
    else: #everyday after
        arcpy.AddMessage(random.choice(quoteList))
        arcpy.AddMessage('Maclurky! You missed it!')
    del cursor
    time.sleep(5) #every 5 seconds run it again















