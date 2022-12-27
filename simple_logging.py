

# Example from java logger
#Sun Dec 25 00:17:06 PST 2022 WarningMessageCB: Sensor tripped. Name: FamilyMot, MOTION

from datetime import datetime

curr_log = -1

def log(s):
    # Generate the log string
    # strftime quick reference: strftime.org
    result = datetime.now().strftime('%a %b %d %H:%M:%S %Z %Y') + ' '
    result+=str(s)

    # Determine which log to write to
    today = int(datetime.now().strftime('%w'))  # weekday as a decimal. 0 is Sun, 6 is Sat
    global curr_log
    if curr_log == -1:
        # LATER: Make this smarter where it checks the log for what day it is
        # For now, I'll just append just in case
        curr_log = today
        log = open('log' + str(curr_log) + '.txt', 'a')
    elif curr_log != today:
        # Set curr_log to today
        curr_log = today
        # And open the log file for writing (not append) to erase the contents
        log = open('log' + str(curr_log) + '.txt', 'w')
    else:
        # Just open the current log for appending
        log = open('log' + str(curr_log) + '.txt', 'a')

    # Write the message
    log.write(result)
    log.write('\r\n')
    log.close()

