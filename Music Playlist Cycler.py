#!/usr/bin/python3

#Written by Antonio Vasquez.


# Imports:
import re
import random
import fileinput
import time


 # File variables:
CruiseFile = "C:\\Users\\Tony\\Desktop\\Music Playlist Cycler\\Cruise.txt"
RideFile = "C:\\Users\\Tony\\Desktop\\Music Playlist Cycler\\Ride.txt"
LaunchFile = "C:\\Users\\Tony\\Desktop\\Music Playlist Cycler\\Launch.txt"


#  The following function is designed to specify:
# - A message to the user.
# - A prompt for user input.
# - A list of acceptable answers.
# - A custom error message if the user input is invalid.
# You can specify each in their respective variable before calling the function.
# Afterwards, you can make a custom variable that will be equal to whatever the user
# entered and be used outside of the function by simply making it equal the "Input" variable.

def Input_Check():
    while True:
        global Message
        global Prompt
        global Input_List
        global Error_Message
        global Input
        print(Message)
        Input = input(Prompt)
        if Input in Input_List:
            break
        else:
            print(Error_Message)
            time.sleep(1)


# Copy and paste the following in order to customize the "Input_Check_Function":

#Message = (""" """)
#Prompt = "\n>"
#Input_List = [""]
#Error_Message = ""
#Input_Check_Function()
#"" = Input



def Counter_Reset():
    global ResetTarget
    
    with fileinput.FileInput(ResetTarget, inplace = True) as Overwrite:
        for OneCheck in Overwrite:
            if "[0]" in OneCheck:
                print(OneCheck.replace("[0]","[-1]"), end ='')
            elif "[1]" in OneCheck:
                print(OneCheck.replace("[1]","[0]"), end ='')
            else:
                print(OneCheck, end ='')


def Play_Counter():
    global UnplayedCounter

    for Song in SongSelection:
        UnplayedCounter += 1
        CounterCheck = int(re.search(r'^\[(.+|\d+)\]', Song).group(1))
        if CounterCheck == 0:
            UnplayedList.append(Song)
        elif CounterCheck == 1:
            UnplayedCounter -= 1
        elif CounterCheck < 0:
            UnplayedCounter -= 1


def Random_Song():
    global CurrentSong

    RandomSong = random.choice(UnplayedList)
    CurrentSong = (RandomSong[4:])

    for Song in SongSelection:
        if "[-1]" in Song:
            CurrentSong = (Song[5:])
            with fileinput.FileInput(ResetTarget, inplace = True) as Overwrite:
                for ZeroCheck in Overwrite:
                    if "[-1]" in ZeroCheck:
                        print(ZeroCheck.replace("[-1]","[0]"), end ='')
                    else:
                        print(ZeroCheck, end ='')

    with fileinput.FileInput(ResetTarget, inplace = True) as Overwrite:
         for ZeroCheck in Overwrite:
            if CurrentSong in ZeroCheck:
                print(ZeroCheck.replace("[0]","[1]"), end ='')
            else:
                print(ZeroCheck, end ='')



# Prompt for music category:
#1 = Cruise
#2 = Ride
#3 = Launch
Message =("""
How will we be driving this time?
    
    1) We're just cruising.
    2) Let's go for a ride.
    3) We've got somewhere to be NOW.""")
Prompt = "\n>"
Input_List = ["1", "2", "3"]
Error_Message = "Mmm, try again."
Input_Check()
MusicCategory = Input


# The following functions sets conditional actions depending on the music category choice:

def Set_Music_Category():
    global MusicCategory
    global SongSelection
    global ResetTarget
    global UnplayedList
    global UnplayedCounter

    # Selected "Cruise" mode:
    if MusicCategory in "1":

        SongSelection = open(CruiseFile).read().splitlines()
        ResetTarget = CruiseFile
        UnplayedList = []
        UnplayedCounter = 0

        Play_Counter()
        
        if UnplayedCounter == 1:
            Counter_Reset()
            SongSelection = open(CruiseFile).read().splitlines()
            ResetTarget = CruiseFile
            UnplayedList = []
            UnplayedCounter = 0
            Play_Counter()
            Random_Song()
        else:
            Random_Song()


    # Selected "Ride" mode:
    elif MusicCategory in "2":

        SongSelection = open(RideFile).read().splitlines()
        ResetTarget = RideFile
        UnplayedList = []
        UnplayedCounter = 0

        Play_Counter()
        
        if UnplayedCounter == 1:
            Counter_Reset()
            SongSelection = open(RideFile).read().splitlines()
            ResetTarget = RideFile
            UnplayedList = []
            UnplayedCounter = 0
            Play_Counter()
            Random_Song()
        else:
            Random_Song()


    # Selected "Ride" mode:
    elif MusicCategory in "3":

        SongSelection = open(LaunchFile).read().splitlines()
        ResetTarget = LaunchFile
        UnplayedList = []
        UnplayedCounter = 0

        Play_Counter()
        
        if UnplayedCounter == 1:
            Counter_Reset()
            SongSelection = open(LaunchFile).read().splitlines()
            ResetTarget = LaunchFile
            UnplayedList = []
            UnplayedCounter = 0
            Play_Counter()
            Random_Song()
        else:
            Random_Song()


Set_Music_Category()


# Prompt for secondary actions after music category is selected:
while True:
    Message = (f"""
{CurrentSong}

    1) Select mood.
    2) We're here.""")
    Prompt = "\n>"
    Input_List = ["1", "2"]
    Error_Message = "Nooo. Again."
    Input_Check()
    SecondaryAction = Input

        # Prompt for selecting "Select mood." in "Cruise" mode:
    if MusicCategory in "1" and SecondaryAction in "1":
        Message = (f"""
{CurrentSong}

    1) Speed up a little.
    2) TAKE OFF!
    3) Never mind.""")
        Prompt = "\n>"
        Input_List = ["1", "2", "3"]
        Error_Message = "Pay a little more attention?"
        Input_Check()
        MusicCategorySwitch = Input
        if MusicCategorySwitch in "1":
            MusicCategory = "2"
            Set_Music_Category()
        elif MusicCategorySwitch in "2":
            MusicCategory = "3"
            Set_Music_Category()
        elif MusicCategorySwitch in "3":
            continue

    # Prompt for selecting "Select mood." in "Ride" mode:
    elif MusicCategory in "2" and SecondaryAction in "1":
        Message = (f"""
{CurrentSong}

    1) Slow it down.
    2) TAKE OFF!
    3) Never mind.""")
        Prompt = "\n>"
        Input_List = ["1", "2", "3"]
        Error_Message = "Come again?"
        Input_Check()
        MusicCategorySwitch = Input
        if MusicCategorySwitch in "1":
            MusicCategory = "1"
            Set_Music_Category()
        elif MusicCategorySwitch in "2":
            MusicCategory = "3"
            Set_Music_Category()
        elif MusicCategorySwitch in "3":
            continue

    # Prompt for selecting "Select mood." in "Launch" mode:
    elif MusicCategory in "3" and SecondaryAction in "1":
        Message = (f"""
{CurrentSong}    
        
    1) Slow it waaay down.
    2) Slow it down a little.
    3) Never mind.""")
        Prompt = "\n>"
        Input_List = ["1", "2", "3"]
        Error_Message = "Hmmm..."
        Input_Check()
        MusicCategorySwitch = Input
        if MusicCategorySwitch in "1":
            MusicCategory = "1"
            Set_Music_Category()
        elif MusicCategorySwitch in "2":
            MusicCategory = "2"
            Set_Music_Category()
        elif MusicCategorySwitch in "3":
            continue

    # Action for selecting "We're here." at any point.
    # Will end the script, and perform an extra write to the persistent files:
    else:
        if SecondaryAction in "2":
            print("""
    See you soon!
            - Lexi <3""")
            time.sleep(1)
            quit()





### NOTES ###

## Ctrl+F "#!!" to find marked changes so you don't forget them!

## Look for a method to clean up text after an input. What about "self.clearinputs()"?
## import os
## os.system("cls")  ???