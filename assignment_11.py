filename =''
filename = input('\nenter filename: ').strip()

#main_program
index = len(filename) - filename.index('.')
extension = filename[-(index - 1):]

filename_without_extension = filename[:-(index)]



print('\nExtension:')
print(extension)
print('\nFilename:')
print(filename_without_extension)
