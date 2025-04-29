def Append_Data_to_the_File(filename):

    with open('filename', "w") as file:
        user_input = file.write(input('Enter text to write to the file: ') +"\n")
        print(f'Data successfully written to {filename}.\n')

    with open('filename', "a") as file:
        user_input2 = file.write(input('Enter additional text to append: ') +"\n")
        print('Data successfully appended.\n')

    with open('filename', "r") as file:
        print(f'Final Content of the {filename}:')
        print(file.read())

# Calling the function
Append_Data_to_the_File('output.txt')