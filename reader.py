import sys

input_file, output_file, variables = sys.argv[1], sys.argv[2], sys.argv[3:]

user_input = sys.argv[3:]
if not user_input:
    print("Error: Value is required.")

elif user_input:
    operation_list = []
    with open('input.csv', mode='r+') as file_stream:

        input_date = file_stream.read()
        input_date = input_date.split("\n")
        for element in input_date:
            element = element.split(",")
            operation_list.append(element)


    for operation in variables:
        row, column, value = operation.split(",")
        row = int(row)
        column = int(column)
        operation_list[row][column] = value


    with open('output.csv', mode="w") as file_stream:
        #output_file = file_stream.write(f"{input_date} \n")
        for line in operation_list:
            file_stream.write(",".join(line) + "\n")
            print(",".join(line))

#python reader.py in.csv out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0
