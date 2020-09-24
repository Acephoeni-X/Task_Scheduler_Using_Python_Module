# Task_Scheduler_Using_Python_Module
A program which shows how can we use a Python Module "Schedule " to schedule everyday task

## Image
![Task Schedular](https://github.com/Rishi-Sharma2002/Task_Scheduler_Using_Python_Module/blob/master/screenshots/Web%201920%20%E2%80%93%201.png)

## How to use this program:-
1. Clone this repository to the desired directory.
2. Open Schedule.py file in the editor.
3. Change the link in the webbrowser function like this:-
   webbrowser.open("  __YOUR_DESIRED_LINK___     ")
   
4. Change the timinings in the schedule function like this:-
    schedule.every().monday.at("__Set_Your_Time__").do(monlecture_1)
    
5. Now you can run the file directly or you can make exe using python module Pyinstaller.

### Use Pyinstaller to create exe file:-
1. If you already have python installed, just open cmd and type :
    ```
    pip install pyinstaller /  pip3 install pyinstaller
    ```
2. Head to the directory where Schedule.py file is located, and open cmd.
3. In cmd type:-
    ```
    pyinstaller Schedule.py
    ```
    and hit enter.
    
4. A file name "dist" will be created from where you can use the "Schedule.exe" to run the task.

###### For more details on pyinstaller, schedule, and webbrowser visit link 
[PyInstaller!](https://pyinstaller.readthedocs.io/en/stable/usage.html)
[Schedule!](https://docs.python.org/3/library/sched.html)
[Webbrowser!](https://docs.python.org/3/library/webbrowser.html?highlight=webbrowser)


## If you like this content rate it pls!
[Ask me anything on LinkedIn !](https://www.linkedin.com/in/rishi-sharma-5602ba199/)
