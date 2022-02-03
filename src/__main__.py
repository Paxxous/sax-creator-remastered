import playsound, readfile


# Main, where commands are processed
if __name__ == "__main__":
  whatAnswer = input("Would you like to create (1), edit (2), or play (3) a file?\n")

  # create file
  if whatAnswer == "1":
    # get name of the file to create and create it
    nameOfFile = input("What would you like the name of your file to be?\n")
    
    newFile = open(nameOfFile, 'w')
    newFile.close()
  
  # editing mode
  elif whatAnswer == "2":

    while True:
      # Get the name of the file to open and open it if it exists
      whatFileToOpen = input("What is the name of the file that you would like to open?\n")

      # open the file to write
      try:
        open(whatFileToOpen, 'r')
        
        
        while True:
          appendTheFile = open(whatFileToOpen, 'a')

          theNote = input("Type note to add (ctrl + c to stop): ")

          # append the new note to the file
          appendTheFile.write(theNote + ",")



      except FileNotFoundError:
        print("Seems that file doesn't exist...")

      except KeyboardInterrupt:
        print("Stopping editing mode...")
        break

  # elif whatAnswer == "3":

