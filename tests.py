from functions.write_file import write_file as write 

print(write("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

print(write("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

print(write("calculator", "/tmp/temp.txt", "this should not be allowed"))


