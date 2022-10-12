#Dependencies (things needed to run csv function)
import csv

'''
with is the part that closes the open function because if you don't
    close it, then it will remain open
open is the open function from csv (hence why we import it)
First parameter is the file path
    The . is needed in front of the file path because it refers to the 
    current folder. So to create a relative file path, you need it
Second parameter is what we are doing to the csv file
    the r is reading it, the w is writing, and there are others
as csvfile is the varaible that we use to read the headers and lines
the function returns a custom csv datatype (not a string or integar,
it is its own datatype)
'''
with open(".\Resources\election_data.csv", "r") as csvfile:
    s = csvfile.readlines()
    # for i in range(len(s)):
    #     if i < 10:
    #         print(i)
    #     else:
    #         break
    print(csvfile)