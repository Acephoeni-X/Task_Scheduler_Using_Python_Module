import schedule
import webbrowser
import time
import subprocess
import os

def monlecture_1():
    print("\n\n1st Lecture")
    webbrowser.open("https://meet.google.com/1stclass")
def monlecture_2():
    print("\n\n2nd Lecture")
    webbrowser.open("https://meet.google.com/2ndclass")
def monlecture_3():
    print("\n\n3rd Lecture")
    webbrowser.open("https://meet.google.com/3rdclass")
def monlecture_4():
    print("\n\n4th Class")
    webbrowser.open("https://meet.google.com/4thclass")

schedule.every().monday.at("08:59").do(monlecture_1)
schedule.every().monday.at("10:44").do(monlecture_2)
schedule.every().monday.at("11:59").do(monlecture_3)
schedule.every().monday.at("13:59").do(monlecture_4)

def tuelecture_1():
    print("\n\n1st Lecture")
    webbrowser.open("https://meet.google.com/1stclass")
def tuelecture_2():
    print("\n\n2nd Lecture")
    webbrowser.open("https://meet.google.com/2ndclass")
def tuelecture_3():
    print("\n\n3rd Lecture")
    webbrowser.open("https://meet.google.com/3rdclass")


schedule.every().tuesday.at("08:59").do(tuelecture_1)
schedule.every().tuesday.at("11:59").do(tuelecture_2)
schedule.every().tuesday.at("13:59").do(tuelecture_2)

def wedlecture_1():
    print("\n\n1st Lecture")
    webbrowser.open("https://meet.google.com/1stclass")
def wedlecture_2():
    print("\n\n2nd Lecture")
    webbrowser.open("https://meet.google.com/2ndclass")
def wedlecture_3():
    print("\n\n3rd Lecture")
    webbrowser.open("https://meet.google.com/3rdclass")
def wedlecture_4():
    print("\n\n4th Lecture")
    webbrowser.open("https://meet.google.com/4thclass")
    
schedule.every().wednesday.at("08:59").do(wedlecture_1)
schedule.every().wednesday.at("10:46").do(wedlecture_2)
schedule.every().wednesday.at("11:59").do(wedlecture_3)
schedule.every().wednesday.at("13:59").do(wedlecture_4)


def thruslecture_1():
    print("\n\n1st Lecture")
    webbrowser.open("https://meet.google.com/1stclass")
def thruslecture_2():
    print("\n\n2nd Lecture")
    webbrowser.open("https://meet.google.com/2ndclass")
def thruslecture_3():
    print("\n\n3rd Lecture")
    webbrowser.open("https://meet.google.com/3rdclass")
def thruslecture_4():
    print("\n\n4th Lecture")
    webbrowser.open("https://meet.google.com/4thclass")
    
schedule.every().thursday.at("08:59").do(thruslecture_1)
schedule.every().thursday.at("10:44").do(thruslecture_2)
schedule.every().thursday.at("11:59").do(thruslecture_3)
schedule.every().thursday.at("13:59").do(thruslecture_4)

def frilecture_1():
    print("\n\n1st Lecture")
    webbrowser.open("https://meet.google.com/1stclass")
def frilecture_2():
    print("\n\n2nd Lecture")
    webbrowser.open("https://meet.google.com/2ndclass")
def frilecture_3():
    print("\n\n3rd Lecture")
    webbrowser.open("https://meet.google.com/3rdclass")
def frilecture_4():
    print("\n\n4th Lecture")
    webbrowser.open("https://meet.google.com/4thclass")
    

schedule.every().friday.at("08:59").do(frilecture_1)
schedule.every().friday.at("10:44").do(frilecture_2)
schedule.every().friday.at("11:59").do(frilecture_3)
schedule.every().friday.at("13:59").do(frilecture_4)

def satlecture_1():
    print("\n\n1st Lecture")
    webbrowser.open("https://meet.google.com/lookup/1stclass")
def satlecture_2():
    print("\n\n2nd Lecture")
    webbrowser.open("https://meet.google.com/lookup/2ndclass")
def satlecture_3():
    print("\n\n3rd Lecture")
    webbrowser.open("https://meet.google.com/lookup/3rdclass")

schedule.every().saturday.at("08:59").do(satlecture_1)
schedule.every().saturday.at("10:44").do(satlecture_2)
schedule.every().saturday.at("13:59").do(satlecture_3)




if __name__ == "__main__":

    os.system("cls")
    print("\t\t$$$$$$$$$	$$$$$$$$$$$		$$$$$$$$$ ")
    print("\t\t$$$$$$$$$	$$$$$$$$$$$		$$$$$$$$$ ")
    print("\t\t$$		$$			$	  ")
    print("\t\t$$		$$$$$$$$$$$		$$$$$$$$$ ")
    print("\t\t$$ 			 $$		$	  ")
    print("\t\t$$$$$$$$$	$$$$$$$$$$$		$$$$$$$$$ ")
    print("\t\t$$$$$$$$$   	$$$$$$$$$$$		$$$$$$$$$ ")
    print("\n\n\t\t>>[         Program has started.....        ]<<")
    print("\n\n  # whenever their will be class it will automatically open in your browser")
    print("\n    # Do Not Close this Application Otherwise It will not work")
    print("\n\n")
    while True:
        schedule.run_pending()
        time.sleep(10)
