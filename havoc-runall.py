#!/usr/bin/env python
# -*- coding: utf-8 -*-

from havoc import Demon, RegisterCommand, RegisterModule, GetDemons

lastDemon : Demon = None

# you can use a callback function to parse output 
# and print everything to the same console
# a good example of this is the bofbelt module
# see here: https://github.com/HavocFramework/Modules/blob/main/Bofbelt/bofbelt.py
def callback( demonID, TaskID, worked, output, error ):
    global lastDemon

    demon : Demon = None
    demon = Demon(demonID)

    # if this isnt the main demon
    # also print to the other demon console
    if demonID != lastDemon.DemonID:
        demon.ConsoleWrite( demon.CONSOLE_INFO, f"cback: {demonID} | {TaskID} | {worked} | {output} | {error}" )

    lastDemon.ConsoleWrite( lastDemon.CONSOLE_INFO, f"cback: {demonID} | {TaskID} | {worked} | {output} | {error}" )
    
    return True

# This doesnt work that well... it wont output everything and the buffer is stuck until there is other callbacks that are called
# will revisit this in the future after the rewrite...
def callback_print_curr_console( demonID, TaskID, worked, output, error ):
    global lastDemon

    lastDemon.ConsoleWrite( lastDemon.CONSOLE_INFO, f"[!!!] cback: {demonID} | {TaskID} | {worked}" )

    if output: 
        lastDemon.ConsoleWrite( lastDemon.CONSOLE_INFO, f"\tOutput:")
        for l in output.split("\n"):
            lastDemon.ConsoleWrite( lastDemon.CONSOLE_INFO, "\t" + l)

    if error: 
        lastDemon.ConsoleWrite( lastDemon.CONSOLE_INFO, f"\tError:")
        for l in error.split("\n"):
            lastDemon.ConsoleWrite( lastDemon.CONSOLE_INFO, "\t" + l)

    return True
    

# cmd callback is defined differently
# idk why
# nvm it actually doesnt get called?
# weird behaviour
def callback_cmd( output ):
    global lastDemon

    lastDemon.ConsoleWrite( lastDemon.CONSOLE_INFO, f"Output:" )

    if output:
        for l in output.split("\n"):
            lastDemon.ConsoleWrite( lastDemon.CONSOLE_INFO, f"\t{l}" )

    return True

def runall_example( demonID, *param ):
    global lastDemon

    TaskID : str = None

    demon_ids = GetDemons()
    d_count = len(demon_ids)

    demon : Demon = None

    # this is the one we ran things from
    mainDemon = Demon(demonID)
    lastDemon = mainDemon

    TaskID = mainDemon.ConsoleWrite(mainDemon.CONSOLE_TASK, f"Running funny bof on all active demons... Total demons: {d_count}. Active: idk..." )


    for i, d in enumerate(demon_ids):
        demon = Demon(d)
        # ipconfig crashes the client, dont do it
        # whoami too idk why

        # You can run command as such which will run on all Demons
        # some commands will crash the client.. dont ask me why.. idk.
        demon.Command(TaskID, "checkin")
        demon.Command(TaskID, "pwd")

        # You can also run bofs and use a callback function to see which demons are active
        demon.InlineExecuteGetOutput( callback, "go", "enumpwshhist.o", b'')


    # return True so that we also print consoleWrite messages
    # otherwise it defaults to only printing demon.CONSOLE_TASK
    return TaskID

def runall_sw( demonID, *params):
    global lastDemon

    TaskID : str = None

    demon_ids = GetDemons()
    d_count = len(demon_ids)

    demon : Demon = None

    # this is the one we ran things from
    mainDemon = Demon(demonID)
    lastDemon = mainDemon
    
    cmd = " ".join(params)

    TaskID = mainDemon.ConsoleWrite(mainDemon.CONSOLE_TASK, f"Attempting to run bof on all demons with output to this window: {cmd}" )

    for i, d in enumerate(demon_ids):
        demon = Demon(d)
        demon.CommandGetOutput( TaskID, cmd, callback_cmd )

    return TaskID


def runall( demonID, *params):
    global lastDemon

    TaskID : str = None

    demon_ids = GetDemons()
    d_count = len(demon_ids)

    demon : Demon = None

    # this is the one we ran things from
    mainDemon = Demon(demonID)
    lastDemon = mainDemon
    
    cmd = " ".join(params)

    TaskID = mainDemon.ConsoleWrite(mainDemon.CONSOLE_TASK, f"Attempting to run cmd on all demons: {cmd}" )

    for i, d in enumerate(demon_ids):
        demon = Demon(d)
        demon.Command(TaskID, cmd)

    return TaskID

def getalive( demonID, *param ):
    global lastDemon
    TaskID : str = None

    demon_ids = GetDemons()
    d_count = len(demon_ids)

    demon : Demon = None

    mainDemon = Demon(demonID)
    lastDemon = mainDemon

    TaskID = mainDemon.ConsoleWrite(mainDemon.CONSOLE_TASK, f"Finding alive beacons" )

    for i, d in enumerate(demon_ids):
        demon = Demon(d)
        # run a dummy command so we can see who is alive
        # the GetOutput for the Command function is shit so we'll use a dummy bof instead
        # demon.CommandGetOutput( TaskID, "ls", callback_cmd )

        demon.InlineExecuteGetOutput( callback, "go", "getalivebof/getalivebof.o", b'')

    return TaskID

RegisterCommand( runall, "", "runall", "Run a command on all beacons", 0, "", "" )

RegisterCommand( getalive, "", "getalive", "Find all alive beacons", 0, "", "" )

