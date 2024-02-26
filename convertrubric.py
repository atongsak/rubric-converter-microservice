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