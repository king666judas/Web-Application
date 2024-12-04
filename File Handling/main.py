"""
#  Create File
with open('batch03.py',"w") as myFile:
    myFile.write("print('Hello')")
"""


"""
# Reading from a File
with open("batch03.text","r") as myFile:
    content= myFile.read()
    print(content)
"""



"""
#  Renaming a File
import os
os.rename("batch03.text","python03.text")
"""


"""
#  Delete a File
import os
os.remove("python03.text")
"""


# Folder Creating
import os
os.mkdir("2024")
os.mkdir("2024/11")
with open('2024/11/rabbil.png',"w") as myFile:
    myFile.write("")


"""
import os
os.mkdir("ostad")
os.mkdir("ostad/boys")
os.mkdir("ostad/girls")
"""


"""
# Renaming a Directory
import os
os.rename("2024/11","2024/nov")
"""

"""
# Deleting a Directory
import os
os.rmdir("batch03")
"""


"""
# How to make zip from a Directory
import shutil
shutil.make_archive("2024_new",'zip','2024')
"""

"""
# How to extract
import zipfile
with zipfile.ZipFile("2024_new.zip","r") as MyZipFile:
    MyZipFile.extractall()
"""




# How to Make CSV File From List
"""
import csv
data = [
    ["Name", "Salary", "Designation", "Department", "Location"],
    ["Alice", 70000, "Software Engineer", "IT", "New York"],
    ["Bob", 85000, "Data Scientist", "Data", "San Francisco"],
    ["Charlie", 60000, "System Administrator", "IT", "Chicago"],
    ["David", 95000, "Product Manager", "Product", "Boston"],
    ["Eve", 72000, "UX Designer", "Design", "Los Angeles"]
]

with open("employee.csv",mode="w",newline='') as csvFile:
    csvFileWriter = csv.writer(csvFile)
    csvFileWriter.writerow(data)

"""


# How to Read a CSV File
import csv
with open("employee.csv",mode="r") as myFile:
    myFileReader=csv.reader(myFile)
    for row in myFileReader:
        print(row)





# Error Handling -> Catching All Exceptions
try:
    with open("abc.text", "r") as file:
        content = file.read()
        num = 10/0

    with open("abc.text", "r") as file:
        content1 = file.read()
        num2 = 10/0

    with open("abc.text", "r") as file:
        content2 = file.read()
        num3 = 10/0


except Exception as e:
     print(f"My Error is {e}")
     # LOG->

finally:
    print("Something Went Wrong ! Please Try Again Later")
    print("Loader animation off")
































