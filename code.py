def swapFiles():
     file1 = open("file1.txt", 'r')
     file2 = open("file2.txt", 'r')

     file1Text = file1.read()
     file2Text = file2.read()

     file1.close()
     file2.close()

     file1 = open("file1.txt", 'w')
     file2 = open("file2.txt", 'w')

     file1.write(file2Text)
     file2.write(file1Text)
     

swapFiles()