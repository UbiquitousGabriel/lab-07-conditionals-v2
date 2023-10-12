currHour = input("What is the current hour in military time? 0-23")
floatCurrHour = float(currHour)

if (floatCurrHour <= 5):
    print("It's early. You should be sleeping!");
elif (floatCurrHour <= 7):
    print("Wake up, brew that coffee, get that mile run in, and get that breakfast…");
elif (floatCurrHour <= 9):
    print("Time to go to work.");
elif (floatCurrHour <= 12):
    print("You should be working!");
elif (floatCurrHour <= 13):
    print("Take your lunch break!");
elif (floatCurrHour <= 17):
    print("Do you feel that afternoon lull?");
elif (floatCurrHour <= 19):
    print("Time to hit the gym…");
elif (floatCurrHour <= 21):
    print("Gotta eat that dinner.");
elif (floatCurrHour <= 23):
    print("Get that SLEEP. And rePEAT!");
else:
    print("You didn’t type an acceptable value! (0-23)");
