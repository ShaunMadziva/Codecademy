#reading a file 'with' will close the file. We used to use .close() before
with open('grid.py') as text_file: #reads the contents of a file and returns it as a string
  text_data = text_file.read()
#print(text_data)

#reading a file line by line by iterating over the lines
with open('grid.py') as lines_doc:
    #print("****", lines_doc.readlines()) #prints a list of lines in doc
    for line in lines_doc.readlines(): #loops through the list of lines
        print(line)

# reading a file one line at a time
with open('grid.py') as first_line_doc:
  first_line = first_line_doc.readline()
  second_line = first_line_doc.readline()
  print("1.",first_line)
  print("2.",second_line)

#writing to a new files
with open("bad_bands.txt", "w") as bad_bands_doc:
  bad_bands_doc.write("the greatfull dead")
  #print("read",bad_bands_doc.read()) #not readable



#append to an exiting file
with open("bad_bands.txt", "a") as bad_bands_doc:
  bad_bands_doc.write("\nAir Buddy")
  print(bad_bands_doc) # prints the object not the file












#The with keyword invokes something called a context manager 
# for the file that we’re calling open() on. 
#This context manager takes care of opening the file when we call open()
#and then closing the file after we leave the indented block.