import datetime
latest= [(datetime.datetime(2018, 5, 27, 18, 29, 59), 'RT @StarSportsIndia: C for Comeback\nC for Champions\nC for #CSK\n \nCongratulations, @ChennaiIPL - the #VIVOIPL 2018 winners! \xf0\x9f\x91\x91\n\n#WorldsToughe\xe2\x80\xa6'), (datetime.datetime(2018, 5, 27, 18, 29, 59), 'RT @TheSevenLife_: This is it! A dream comeback as @chennaiipl win the #VIVOIPL Trophy for the third time. #CSKvSRH https://t.co/Ea442LDIU1'), (datetime.datetime(2018, 5, 27, 18, 29, 58), '@Ajith_tweets @cricbuzz @bhogleharsha @ImZaheer @gauravkapur @joybhattacharj @Sdoull @DanishSait @MichaelVaughan\xe2\x80\xa6 https://t.co/W8OdDXdtui'), (datetime.datetime(2018, 5, 27, 18, 29, 58), 'RT @BORN4WIN: Which team has lifts the #IPL2018 trophy beaten by #SRH?\n- #ChennaiSuperKings\n\nWho gets the #OrangeCap in #IPL2018 for hittin\xe2\x80\xa6'), (datetime.datetime(2018, 5, 27, 18, 29, 58), 'RT @IPL: Chennai are Super Kings. A fairytale comeback as @ChennaiIPL beat #SRH by 8 wickets to seal their third #VIVOIPL Trophy \xf0\x9f\x8f\x86\xf0\x9f\x8f\x86\xf0\x9f\x8f\x86. This\xe2\x80\xa6'), (datetime.datetime(2018, 5, 27, 18, 29, 54), 'RT @ChennaiIPL: Another #ChinnaThala grab in the Finals to extend his record of 5 catches in #VIVOIPL Finals. Champion strikes, Shakib walk\xe2\x80\xa6'), (datetime.datetime(2018, 5, 27, 18, 29, 54), 'RT @StarSportsIndia: 117*(57) in the #WorldsToughestFinal.\n\nAge is just a number, after all.\n\nTake a bow, @ShaneRWatson33! \n\n#CSKvSRH #VIVO\xe2\x80\xa6'), (datetime.datetime(2018, 5, 27, 18, 29, 53), 'RT @erinvholland: Wishing I was with my @StarSportsIndia family for the epic #VIVOIPL final tonight! Cannot thank STAR enough for having me\xe2\x80\xa6'), (datetime.datetime(2018, 5, 27, 18, 29, 53), "RT @IPL: It's time for the big #Final as the two teams are here at the Wankhede.\n\n#VIVOIPL #Final #CSKvSRH https://t.co/I6MgDfV94t"), (datetime.datetime(2018, 5, 27, 18, 29, 52), 'RT @RCBTweets: Many congratulations @ChennaiIPL \xf0\x9f\x91\x8f Deserved winners of #VIVOIPL 2018. Watto was absolutely sensational \xf0\x9f\x94\xa5 @ShaneRWatson33\n#Pl\xe2\x80\xa6')]
# latest=[(str(a[0]),a[1].decode().encode('utf-8')) for a in latest]
latest=[(str(a[0]),a[1]) for a in latest]
for a in latest:
	print unicode(a[1], "utf8").encode("utf-8")
