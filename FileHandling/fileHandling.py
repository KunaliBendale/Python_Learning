#with open("sample.txt","a") as file1:
#   file1.write("Appended text")

# WAP that checks if file exists or not. If it exists, print "file exists" else print "file does not exist
# "
# import os 

# if os.path.exists("mis.txt"):
#     print("file exists")
# else:
#     print("file does not exist")
    
    
    
# WAP to open missing_file.txtin read mode , if file doesn't exists print file not found.

# try:
#     with open("missing_file.txt", "r") as file:
#         content = file.read()
#         print(content)
        
# except FileNotFoundError:
#     print("file not found")
    
    
# WAP that merges content of multiple files in a file merge.txt , maintaining order of file

# files=["sample.txt","sample2.txt"]
# with open("merge.txt","w")as mgd:
#         for file in files:
#             try:
#                 with open(file,"r")as f:
#                     data=f.read()
#                     mgd.write(data)
#                     mgd.write("\n")
#             except FileNotFoundError:
#                 print(f"{file} not found")  
                
    
# WAP that compares content of two files and print files are same if content is same and files are different if 
#content is different

# with open("sample.txt","r") as file1, open("sample2.txt","r") as file2:
#     content1=file1.read()
#     content2=file2.read()
    
#     if content1==content2:
#         print("files are same")
#     else:
#         print("files are different")


#WAP that opens file in read ans write mode(r+) reads thr first line and add 
# "updated content" to beginning of file

# with open("sample.txt", "r+") as file:
#     line=file.readline()
#     print(line)
#     file.seek(0,1) 
#     file.write("updated content")


#WAP that checks if file sample.txt exists before opening it in read mode. 
# If file does not exists, print "file not found"

# import os

# if os.path.exists("sample3.txt"):
#     with open("sample.txt","r")as file:
#         content=file.read()
#         print(content)
# else:
#     print("file not found")
    

# WAP open file sample.txt in r+ mode . read the content and replace the word "old" with "new" 
# and write the updated content back to file

# with open("sample.txt","r+") as file:
#     content=file.read()
#     print(content)
#     content=content.replace("old","new")
#     file.seek(0)
#     file.write(content)
    

# WAP opens file in "w" mode ,if file exists ,overwrite content with "report generated successfully.."

# with open("sample.txt","w")as file:
#     file.seek(0)
#     file.write("report generated successfully..")
    
    
# WAP to take input string from user and writr that content with w mode. 
# if file exists, overwrite content with user input string

st1=input("Enter string to write in file: ")
with open("sample.txt","w")as file:
    file.write(st1)