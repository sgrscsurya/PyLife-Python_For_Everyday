""" First, Lets Understand the Code Logic and what is the main Objective to code this Program """

""" It is clear that, The arithmetic_arranger function takes a list of arithmetic problems and formats them according to specific rules. It validates the input, arranges the problems vertically with proper spacing, and optionally displays the answers. The formatted result is then returned. The main.py file demonstrates how to use this function and print the formatted problems """

# So, Now First Let's Proceed with the arithmatic_arranger function
# This function takes two parameters, 
""" 1st Parameter : problems: a list of strings, where each string represents an arithmetic problem """
""" 2nd Parameter : display_answers (optional my interest): a boolean flag indicating whether to display the answers """

def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    """ RULES ERROR - 1 : Too Many Problems Checking:
Checks if the number of problems is more than 5. If it is, it returns an error message """ # ( Given in Rules )
  
    arranged_problems = ""
    top_line = ""
    bottom_line = ""
    dashes_line = ""
    answers_line = ""

    # Now here we check for Errors by Spliting each term in Problems (i.e one problem) as Operand1, operator and Operand2.
  
    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        """ RULES ERROR - 2 : Valid Operators Checking:
Checks if the operator is either '+' or '-'. If not, it returns an error message """

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        """ RULES ERROR - 3 : Numbers Contain Digits Checking:
Checks if operands contain only digits. If not, it returns an error message """

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        """ RULES ERROR - 4 : Number Digits Check:
Checks if the number of digits in each operand is not more than 4. If it is, it returns an error message """

# All the Four Error Rules are satisfied using the if condition.
# Now, Lets Proceed with the FORMATTING THE PROBLEMS :

        """ Here, We have four Things/ Lines to Understand the Formatting,
            1. top_line
            2. bottom_line
            3. dashes_line and
            4. answers_line """

# Here, First we Calculate the maximum width needed for formatting (based on the length of operands (+ & -) and operator).
      
# The below is the main code used to give max.width, Go through the format for better understanding.
        width = max(len(operand1), len(operand2)) + 2 
# We first find the length Maximum operands and then we can observe there is a gap of two spaces after every Operators, hence we do +2 at the last. Hope you Understood.


# Next, Let's Right-aligns operand1 and operand2, and add them to top_line and bottom_line respectively as given in Output.
        top_line += operand1.rjust(width) + '    '
        bottom_line += operator + operand2.rjust(width - 1) + '    '

# The both Operands end with a dashed Line as shown in Output, So Let's create a dashed line with the calculated width and add it to dashes_line variable as shown below,
        dashes_line += '-' * width + '    '
      
        """ That's all. almost there. Now Let's Display the answers and Return the result to the main.py file """

# IF it's an addition(i.e "+" operator), Let's add up both the Operands and give it as an answer.
# ELSE means it's the complementary of Addition, means if it's an subtraction(i.e "-" operator), Let's subtract down both the Operands and give it as an answer.
# That's what the display_answers Function does.

        if display_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))

# The last line we need is answers_lines which comes right after dashes_line, This gives the total output with or without Answers as per given Rules and conditions.

# Here, we won't be getting the answer of addition of Operands/substraction of Operands because,
            """ print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))""" # " The coder who provided us this Code is not expecting answers from us, but he needs is the format of the problems only, Hence this printed arithmatic_arranger is given in the main.py file itself, which shouldn't be changed. Hence we won't be obtaining any answers in the Output "

            answers_line += answer.rjust(width) + '    '

            """ *** Finally, The Main code to arrange the problems in a Fixed format using right alignment of top_line, bottom_line and dashes_line is given as arranged_problems *** """
          
    arranged_problems = top_line.rstrip() + '\n' + bottom_line.rstrip() + '\n' + dashes_line.rstrip()

  # IF display_answers which was initially given as False, becomes True. We need to return this arranged_problems function back to the main.py file and then Run the code to get an successful Output.

    if display_answers:
        arranged_problems += '\n' + answers_line.rstrip()

    return arranged_problems

    """ SUCCESSFULLY EXECUTED ARITHMATIC FORMATTER """
