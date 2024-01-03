
# Docs

 - this will define the different rules / actions and their syntax
 
 - The syntax for all commands is as follows:

 - To get the executable name for a process go to the details tab on Task Manager
{Rule} {arguments} {Action} {arguments}
e.g. start chrome.exe kill chrome.exe

# Rules:

# start

Description:
Will change the process when the specified process starts up.

Usage:
start {process}

Example:
start chrome.exe kill chrome.exe

# stop

Description:
Will change the process when the specified process stops.

Usage:
stop {process}

Example:
stop chrome.exe kill firefox.exe


# Actions:

# kill

Description:
Will kill the specified process

Usage: 
kill {process}

Example:
kill chrome.exe

# priority

Description:
Will change the priority of the specified process

priorities:
realtime
high
above
normal
below
low

Usage:
priority {process} {priority}

Example:
priority chrome.exe low

# start_process

Description:
Start the specified file with the specified priority

Usage:
start_process {path to file} {priority}

Example
start_process "C:Path/To/File/Here" high

