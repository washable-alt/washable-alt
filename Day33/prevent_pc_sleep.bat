Set objShell = CreateObject("WScript.Shell")

' Prevent PC from going to sleep
objShell.Run "powercfg -change -standby-timeout-ac 0", 0, True
objShell.Run "powercfg -change -hibernate-timeout-ac 0", 0, True

' Keep the display on
objShell.Run "powercfg -change -monitor-timeout-ac 0", 0, True

' Loop to keep the script running and prevent the PC from sleeping
Do
    WScript.Sleep(60000)  ' Wait for 60 seconds before loop repeats
Loop