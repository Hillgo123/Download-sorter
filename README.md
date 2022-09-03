# Download-sorter
 This is a python sorter that takes the files from your downloads and sorts them into folders based on the file type.

 In order to add more file types add 
 File_Handler.create(r"C:\Downloads\{folder name}/")
 and
 File_Handler.move("{file type}", r"C:\Downloads\{file name}/")
 to the update function within the file handler class.