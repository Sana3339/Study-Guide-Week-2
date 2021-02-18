class Student(object):
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        print(self.question)
        user_input=input("Enter your answer here: ")
        if user_input ==self.correct_answer:
            return True
        else:
            return False


class Exam(object):
    def __init__(self, name):
        self.questions = []
        self.name = name

    def add_question(self,question, correct_answer):

        question_and_answer = Question(question,correct_answer)
        self.questions.add(question_and_answer)
        return self.questions

    def administer(self,questions):

        correct_answer_tally = 0

        for question in questions:
            self.ask_and_evaluate()
            if self.ask_and_evaluate() == True:
                correct_answer_tally += 1
        
        print(float(correct_answer_tally))



# breakpoint()
# def add_nums(num1,num2):
#     sum = num1 + num2
#     return sum

# total = 0
# num1 = input("Provide the first number: ")
# num1 = int(num1)# num2 = input("Provide the second number: ")
# total = add_nums(num1,num2)
# print(total)
