from App import App

def greetings():
    print("+------------------------------------------------------+")
    print("\t WELCOME TO THE NOTES TAKING APP ")
    print("+------------------------------------------------------+")
greetings()

# Getting the inital data for creating the app object

directory = int(input("""
Choose A Subject From The Given Options
1. Report Writing
2. Fundamentals Of Programming
3. Professional IT practices
4. Applied Physics For Eng.
5. Discrete Structures

>>> """))
path = ""
subject = ""

if directory == 1:
    path = "D:\\Study-Material\\Report-Writing\\notes\\"
    subject = "Report Writing"

elif directory == 2:
    path = "D:\\Study-Material\\Fundamentals-Of-Programming\\notes\\"
    subject = "Fundamentals Of Programming"

elif directory == 3:
    path = "D:\\Study-Material\\Prof-IT-Practices\\notes\\"
    subject = "Professional IT Practices"

elif directory == 4:
    path = "D:\\Study-Material\\Applied-Physics\\notes\\"
    subject = "Applied Physics"

elif directory == 5:
    path = "D:\\Study-Material\\Discrete-Structures\\notes\\"
    subject = "Discrete Structures"

topic = input(f"What is the today's topic for {subject}?  ")


app = App(path=path, subject=subject, topic=topic)
app.createFile()
app.takeNotes()