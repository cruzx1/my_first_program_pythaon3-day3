from sys import argv

# read the filename
script, filename = argv  
# to open the file
txt = open(filename)
#print and format the file 
print(f"Here's your file {filename}:")
#called the function of txt nameed read
print(txt.read())

# print("Type the filename again:")
# file_again = input("> ")

# txt_again = open(file_again)

# print(txt_again.read())
