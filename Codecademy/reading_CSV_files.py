import csv

#reading CSV Files - comma separated
with open("cool_csv.csv", newline='') as cool_csv: # opens file, newline so that we don't mistake linebreak for new row 
    cool_csv_dict = csv.DictReader(cool_csv) # converts each row into OrderedDict with 1st row as keys
    for birthday in cool_csv_dict: # iterates through each OrderedDict
        print(birthday["Cool Birthday"]) #prints values for specified key


#reading different types of CSV files
with open("books.csv") as books_csv:
  #print(books_csv.read())
  books_reader = csv.DictReader(books_csv, delimiter="@")
  isbn_list = [isbn_num["ISBN"] for isbn_num in books_reader]
  print(isbn_list)