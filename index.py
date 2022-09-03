import sched, os, time, shutil



class file_handler():

    def move(self):
        #Moving files
        for filename in os.listdir(r"C:\Users\leo.bergqvist1\Downloads"):
            #Where you move files from
            src = r"C:\Users\leo.bergqvist1\Downloads/" + filename

            #Sorter for different file types

            if filename.lower().endswith("txt"):
                moved = r"C:\Downloads\text/" + filename
                shutil.move(src, moved)
                print(moved)

            elif filename.lower().endswith("docx"):
                moved = r"C:\Downloads\word/" + filename
                shutil.move(src, moved)
                print(moved)

            elif filename.lower().endswith("exe"):
                moved = r"C:\Downloads\installers/" + filename
                shutil.move(src, moved)
                print(moved)

            elif filename.lower().endswith("pdf"):
                moved = r"C:\Downloads\pdf/" + filename
                shutil.move(src, moved)
                print(moved)

            elif filename.lower().endswith("zip"):
                moved = r"C:\Downloads\zip/" + filename
                shutil.move(src, moved)
                print(moved)

            elif filename.lower().endswith("cvc"):
                moved = r"C:\Downloads\cvc/" + filename
                shutil.move(src, moved)
                print(moved)

            elif filename.lower().endswith("png") or filename.lower().endswith("jpg") or filename.lower().endswith("tiff"):
                moved = r"C:\Downloads\images/" + filename
                shutil.move(src, moved)
                print(moved)

            else:
                moved = r"C:\Downloads\other/" + filename
                shutil.move(src, moved)
                print(moved)
            

            

            


File_Handler = file_handler()

def main():
    File_Handler.move()
            


if __name__ == "__main__":
    main()

