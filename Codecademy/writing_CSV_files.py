access_log = [
{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'},
{'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, 
{'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, 
{'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, 
{'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, 
{'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, 
{'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, 
{'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, 
{'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, 
{'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}
]



import csv

#write to a CSV file 
with open("logger.csv", "w") as logger_csv:                  # open a ne csv file in write mode
  fields = ['time', 'address', 'limit']                      #define the headers of the csv file from the dict keys
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields) #instantiate our CSV writer object and pass two arguments
                                                             #we can start adding lines to the CSV file itself!
  log_writer.writeheader()                                   #writes all the fields passed to fieldnames as the (headers) first row in our file
  for item in access_log:                                    #iterate through our list of data.
    log_writer.writerow(item)                                #We call output_writer.writerow() with the item dictionaries which writes each line to the CSV file.

#read the CSV file
with open("logger.csv", "r") as logger_csv:
  read = logger_csv.read()
print(read)
