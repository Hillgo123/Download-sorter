import os
import shutil
from datetime import date
import pandas as pd


class file_handler():
    def __init__(self, dir):
        self.dir = dir
        self.directories = [
            r'C:\Users\leo.bergqvist1\Downloads\pdf/',
            r'C:\Users\leo.bergqvist1\Downloads\word/',
            r'C:\Users\leo.bergqvist1\Downloads\installers/',
            r'C:\Users\leo.bergqvist1\Downloads\pdf/',
            r'C:\Users\leo.bergqvist1\Downloads\zip/',
            r'C:\Users\leo.bergqvist1\Downloads\images/',
            r'C:\Users\leo.bergqvist1\Downloads\cvc/',
            r'C:\Users\leo.bergqvist1\Downloads\other/'
        ]
        # Creates dictionary to keep track of downloaded files
        self.excel = {'File Name': [],
                      'File Type': [],
                      'File Size (kilobytes)': []
                      }

    # Creating files to sort into
    def create(self, dir_name):
        if not os.makedirs(dir_name, exist_ok=True):  # Check if directory already exist
            os.makedirs(dir_name, exist_ok=True)

    def move(self, type, destination):
        # Moving files
        for file_name in os.listdir(self.dir):
            # Where you move files from
            src = self.dir + file_name

            # Sorter for different file types
            # Makes sure it dosen't move the directories for downloaded files
            if not os.path.isdir(self.dir + file_name):
                if file_name.lower().endswith(type):
                    moved = destination + file_name

                    # Appends information about the moved file to the dictionary
                    self.excel['File Name'].append(str(file_name))
                    self.excel['File Type'].append(str(type))
                    self.excel['File Size (kilobytes)'].append(
                        str(os.stat(src).st_size / 1000))

                    shutil.move(src, moved)  # Moves file
                    print(moved)

    # Converts the dictionary filled with file information to an excel file
    def to_excel(self):
        df = pd.DataFrame(self.excel)

        with pd.ExcelWriter('tracker.xlsx', if_sheet_exists='new', mode='a') as writer:
            df.to_excel(writer, sheet_name=date.today().strftime('%B %d, %Y'))

    # Moving filetypes not mentiond into a seperate "other" folder
    def other(self, destination):
        for file_name in os.listdir(self.dir):
            # Makes sure it dosen't move the directories for downloaded files
            if not os.path.isdir(self.dir + file_name):
                src = self.dir + file_name
                moved = destination + file_name
                shutil.move(src, moved)
                print(moved)

    def update(self):
        # Creating directories
        for dir in self.directories:
            File_Handler.create(dir)

        # Activating the move function for different file types
        File_Handler.move('.docx', r'C:\Users\leo.bergqvist1\Downloads\word/')
        File_Handler.move('.exe', r'C:\Users\leo.bergqvist1\Downloads\installers/')
        File_Handler.move('.pdf', r'C:\Users\leo.bergqvist1\Downloads\pdf/')
        File_Handler.move('.zip', r'C:\Users\leo.bergqvist1\Downloads\zip/')
        File_Handler.move('.cvc', r'C:\Users\leo.bergqvist1\Downloads\cvc/')
        File_Handler.move('.png', r'C:\Users\leo.bergqvist1\Downloads\images/')
        File_Handler.move('.jpg', r'C:\Users\leo.bergqvist1\Downloads\images/')
        File_Handler.other(r'C:\Users\leo.bergqvist1\Downloads\other/')

        print('Files successfully moved!')
        self.to_excel()


# Defining the file handler
# selecting where to take files from
File_Handler = file_handler(r'C:\Users\leo.bergqvist1\Downloads/')


def main():
    File_Handler.update()


# Run code
if __name__ == '__main__':
    main()
