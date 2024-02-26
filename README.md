# Check Uploads Microservice 
This microservice, checkupload.py, incrementally checks the "uploads" folder and updates a message to checkupload.txt that indicates the presence of a .csv file. There are two possible outputs in the text file: "No files found in uploads folder." and "File(s) found in uploads folder." 

# How to Request & Receive Data from the Check Uploads Microservice
As this microservice primarily communicates via checkupload.txt, a program must open and read the contents of checkupload.txt to receive outputted data about the "uploads" folder. An example implementation of this is seen in convertrubric.py:
``
import os
import time

def can_convert(path):
    f=open("checkupload.txt", "r")
    content = f.read()
    if content == "No files found in uploads folder.":  
        print(content + " We can't convert the rubric.")
    elif content == "File(s) found in uploads folder.":
        print(content + " Now we can convert the rubric.")
    else:
        print("There's nothing in the text file yet.")

    f.close()

def main():
    path = "checkupload.txt"
    poll_interval = 5 # seconds

    while True:
        if os.path.exists(path):
            while True:
                can_convert(path)
                time.sleep(poll_interval)
        else:
            print("Waiting for Upload Checker microservice to begin..")
            time.sleep(10)

if __name__ == "__main__":
    main()
``
In this example, convertrubric.py is opening and reading checkupload.txt every 5 seconds before determining whether rubric conversions on the .csv file can begin.

# UML Sequence Diagram
<img src="readme/uml.png">