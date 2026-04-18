# Take file name with extension from user
file_name = input("Enter file name with extension: ")

# Remove the last 4 characters (dot + 3-letter extension)
name_without_ext = file_name[:-4]

# Display result
print("File name without extension:", name_without_ext)
