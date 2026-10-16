file_read=open("abc.txt", "r")
print("File in read mode:")
print(file_read.read())
file_read.close()

file_write=open("abc.txt", "w")
print("File in write mode:")
file_write.write("apples")
file_write.close()

file_append=open("abc.txt", "a")
print("File in append mode:")
file_append.write("\noranges")
file_append.close()