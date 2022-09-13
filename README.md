# Download-sorter
 This is a python sorter that takes the files from your downloads and sorts them into folders based on the file type.

 In order to add more file types add 
 r"C:\Downloads\{folder name}/" to the self.directories list (line 6)
 and
 File_Handler.move("{file type}", r"C:\Downloads\{file name}/")
 to the update function within the file handler class. (line 49)

 In order to run automatically https://www.youtube.com/watch?v=OjykudimEqc (on windows)

 It stores data on the files moved (File Name, File Type and File Size) in the tracker.xlsx file