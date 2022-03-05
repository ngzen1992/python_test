def arithmetic_arranger(problems, get_answer = None): 
    count_of_problems = len(problems)

    ### Rule 1 Limit of problem is 5
    if count_of_problems > 5:
        return 'Error: Too many problems.'

    ### Rule 2 Problem can only accept + or -
    for problem in problems:
        if problem.split(' ')[1] == '+' or problem.split(' ')[1] == '-':
            pass
        else:
            return "Error: Operator must be '+' or '-'."

    ### Rule 3 Operands can only contain digit
    for problem in problems:
        if (problem.split(' ')[0]).isdigit() and (problem.split(' ')[2]).isdigit():
            pass
        else:
            return 'Error: Numbers must only contain digits.'
            
    ### Rule 4 Operand can only be 4 digits max
    for problem in problems:
        if len(problem.split(' ')[0]) < 5 and len(problem.split(' ')[2]) < 5 :
            pass
        else:
            return 'Error: Numbers cannot be more than four digits.'

    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''

    for problem in problems:
        largest_operator_len = 0
        if len(problem.split(' ')[0]) > largest_operator_len:
            largest_operator_len = len(problem.split(' ')[0])
        if len(problem.split(' ')[2]) > largest_operator_len:
            largest_operator_len = len(problem.split(' ')[2])
        expected_len = largest_operator_len + 2
        first_line = first_line + ((problem.split(' ')[0]).rjust(expected_len)) + '    '
        second_line = second_line + (problem.split(' ')[1] + (problem.split(' ')[2]).rjust(expected_len - 1)) + '    '
        empty_string = ""
        third_line = third_line + empty_string.rjust(expected_len, '-') + '    '
        
        ### Perform arithmetic operation
        answer = ""
        if problem.split(' ')[1] == '+':
            answer = int(problem.split(' ')[0]) + int(problem.split(' ')[2])
        else:
            answer = int(problem.split(' ')[0]) - int(problem.split(' ')[2])

        fourth_line = fourth_line + str(answer).rjust(expected_len) + '    '

    first_line = first_line.rstrip()
    second_line = second_line.rstrip()
    third_line = third_line.rstrip()
    fourth_line = fourth_line.rstrip()

    if get_answer: 
        return first_line + '\n' + second_line + '\n' + third_line + '\n' + fourth_line
    else:
        return first_line + '\n' + second_line + '\n' + third_line

print(arithmetic_arranger(["32 + 698", "2 - 3801", "45 + 43", "123 + 49"], True))