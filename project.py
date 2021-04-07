def swapFile():
    fileOne = input("Enter the File Name.")
    fileTwo = input("Enter the File Name.")
    file = open(fileOne,'r')
    file = open(fileTwo,'w')
    file.write(file)
    
swapFile()