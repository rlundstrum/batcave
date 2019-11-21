while True:
    try:
        from datetime import date
        episodeIX = date(2019, 12, 20)
        rightNow = date.today()
        stillTooLong = episodeIX - rightNow
        print ('Patience.', stillTooLong.days, 
        'days, you have.')
        break
    except SystemError:
        print ('Maclunky')
#May The Force be with you.