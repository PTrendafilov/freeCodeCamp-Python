def arithmetic_arranger(problems, display_solutions=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    output = ''
    problems_dict = {'first_numbers': [], 'second_numbers': [], 'operator': [], 'space_of_the_problem': []}

    for problem in problems:
        problem = problem.split(' ')

        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        if problem[1] != '+' and problem[1] != '-':
            return "Error: Operator must be '+' or '-'."

        for symbol in problem[0]:
            if symbol > '9' or symbol < '0':
                return 'Error: Numbers must only contain digits.'

        for symbol in problem[2]:
            if symbol > '9' or symbol < '0':
                return 'Error: Numbers must only contain digits.'

        problem_space = max(len(problem[0]), len(problem[2])) + 2

        problems_dict['first_numbers'].append(problem[0])
        problems_dict['second_numbers'].append(problem[2])
        problems_dict['operator'].append(problem[1])
        problems_dict['space_of_the_problem'].append(problem_space)

    first_line = ''
    for i in range(len(problems_dict['first_numbers'])):
        spaces = problems_dict['space_of_the_problem'][i] - len(problems_dict['first_numbers'][i])
        first_line += ' ' * spaces
        first_line += problems_dict['first_numbers'][i]
        first_line += ' ' * 4

    second_line = ''
    for i in range(len(problems_dict['second_numbers'])):
        spaces = problems_dict['space_of_the_problem'][i] - len(problems_dict['second_numbers'][i]) - 1
        second_line += problems_dict['operator'][i]
        second_line += ' ' * spaces
        second_line += problems_dict['second_numbers'][i]
        second_line += ' ' * 4

    third_line = ''
    for i in range(len(problems_dict['space_of_the_problem'])):
        third_line += problems_dict['space_of_the_problem'][i] * '-'
        third_line += ' ' * 4

    output += first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + third_line.rstrip()

    if display_solutions:
        solutions_line = ''
        for i in range(len(problems)):
            first_number = int(problems_dict['first_numbers'][i])
            second_number = int(problems_dict['second_numbers'][i])
            operator = problems_dict['operator'][i]

            if operator == '+':
                solution = first_number + second_number
            else:
                solution = first_number - second_number

            spaces = problems_dict['space_of_the_problem'][i] - len(str(solution))
            solutions_line += ' ' * spaces + str(solution) + ' ' * 4

        output += '\n' + solutions_line.rstrip()

    return output