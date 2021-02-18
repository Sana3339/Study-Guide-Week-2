class Student(object):
    """Student."""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    """A question in an exam."""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Ask a question and evaluate accuracy.

        Poses a question to a user, determines if the answer matches
        the stored correct answer and returns True/False."""

        print(self.question)
        user_input=input("Enter your answer here: ")
        if user_input ==self.correct_answer:
            return True
        else:
            return False


class Exam(object):
    """An exam consisting of multiple questions"""

    def __init__(self, name):
        self.questions = []
        self.name = name

    def add_question(self,question, correct_answer):
        """Adds a question to the exam"""

        question_and_answer = Question(question,correct_answer)
        self.questions.append(question_and_answer)

    def administer(self):
        """Asks questions and prints grade.

        Asks user all of the questions in the exam and
        at the end, provides a percentage grade."""

        correct_answer_tally = 0
        num_of_questions_asked = 0

        for question in self.questions:
            num_of_questions_asked += 1
            if question.ask_and_evaluate():
                correct_answer_tally += 1

        print(float(correct_answer_tally/num_of_questions_asked)*100)