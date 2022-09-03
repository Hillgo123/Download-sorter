import os, shutil, sched, time



class file_handler():
    def __init__(self, dir):
        self.dir = dir
        self.schedule = sched.scheduler(time.time, time.sleep)

    #Creating files to sort into
    def create(self, dir_name):
        if not os.makedirs(dir_name, exist_ok = True): #Check if directory already exist
            os.makedirs(dir_name, exist_ok = True)

    def move(self, type, destination):
        #Moving files
        for file_name in os.listdir(self.dir):
            #Where you move files from
            src = self.dir + file_name

            #Sorter for different file types
            if file_name.lower().endswith(type):
                moved = destination + file_name
                shutil.move(src, moved)
                print(moved)

    #Moving filetypes not mentiond into a seperate "other" folder
    def other(self, destination):

        for file_name in os.listdir(self.dir):
            src = self.dir + file_name
            moved = destination + file_name
            shutil.move(src, moved)
            print(moved)


    def update(self):
        #Creating directories
        File_Handler.create(r"C:\Downloads\text/")
        File_Handler.create(r"C:\Downloads\word/")
        File_Handler.create(r"C:\Downloads\installers/")
        File_Handler.create(r"C:\Downloads\pdf/")
        File_Handler.create(r"C:\Downloads\zip/")
        File_Handler.create(r"C:\Downloads\images/")
        File_Handler.create(r"C:\Downloads\other/")



        #Activating the move function for different file types
        File_Handler.move(".txt", r"C:\Downloads\text/")
        File_Handler.move(".docx", r"C:\Downloads\word/")
        File_Handler.move(".exe", r"C:\Downloads\installers/")
        File_Handler.move(".pdf", r"C:\Downloads\pdf/")
        File_Handler.move(".zip", r"C:\Downloads\zip/")
        File_Handler.move(".cvc", r"C:\Downloads\cvc/")
        File_Handler.move(".png", r"C:\Downloads\images/")
        File_Handler.move(".jpg", r"C:\Downloads\images/")
        File_Handler.other(r"C:\Downloads\other/")

        self.schedule.enter(10, 1, File_Handler.update())

        

    def run(self):
        #Run code in the background to continually update
        self.schedule.enter(10, 1, File_Handler.update())
        self.schedule.run()

                      

        
File_Handler = file_handler(r"C:\Users\leo.bergqvist1\Downloads/") #selecting where to take files from

def main():
    File_Handler.run()
            

#Run code
if __name__ == "__main__":
    main()