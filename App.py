import os

class App:
    def __init__(self, path, subject, topic) -> None:
        self.path = path
        self.subject = subject
        self.topic = topic
        os.chdir(self.path)
        print(os.getcwd())
    
    def createFile(self):
        try:
            self.newFile = open(self.path+"\\"+self.topic+".txt", "a")
            print(f"File: {self.topic} create at the location {self.path}")
        except Exception as E:
            print("Could not create a new file. Something went wrong!")
            print(E)

    def takeNotes(self):
        # os.system("clear")
        try:
            print("Start taking notes. Press Enter to save the line, type 'exit' to save the work and close the application.")
            while True:
                note = input((">>> "))
                if note.lower() == "exit":
                    self.newFile.close()
                    exit(0)
                else:
                    self.newFile.writelines("\n>>> "+note.capitalize() + "\n")

        except Exception as E:
            print("Something went wrong!")
            print(E)

