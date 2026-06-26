"""
Level 3 task, this extends on level 2 and implements the 
Marking, Quiz, and Question classes, which result in the returning
of performance in a given quiz of an assessment assessment_type.
"""
from datetime import date


class Trainee:  # pylint: disable=too-few-public-methods
    """
    Trainee subclass that contains all trainee information,
    this includes returning age in years, adding an assessment
    to the trainee's list of assessments, and a method get_assessment()
    that returns a specified assessment from its assessment list. Finally,
    a method that also returns assessments matching a specified assessment_type.
    """

    def __init__(self, name: str, email: str, date_of_birth: date):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = []

    def __str__(self):
        return f"Trainee {self.name} (email: {self.email}) born: {
            self.date_of_birth.strftime("%d/%m/%Y")}"

    def get_age(self) -> int:
        """Returns their age in years as an int."""
        today = date.today()
        str_dob = self.date_of_birth.strftime("%d-%m-%Y")
        day, month, year = map(int, str_dob.split("-"))
        age = today.year - year - ((today.month, today.day) < (month, day))
        return age

    def add_assessment(self, assessment: Assessment) -> None:
        """
        Appends the given assessment in the add_assessment 
        arg to the assessments list.
        """
        if not isinstance(assessment, Assessment):
            raise TypeError("You must enter an Assessment object!")
        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment | None:
        """
        Loops through the assessment list and returns the assessment
        matching the name in the arg, else None is returned.
        """
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment

    def get_assessment_of_type(self, assessment_type: str) -> list[Assessment]:
        """
        Returns a list of all assessments matching the assessment_type 
        specified in this
        function's position arg.
        """
        if not isinstance(assessment_type, str):
            raise TypeError('You must enter a string!')

        if assessment_type not in ('multiple-choice', 'presentation', 'technical'):
            raise ValueError(
                "You must enter either multiple-choice, presentation"
                ", or technical for assessment types!")

        assessment_type_list = []
        for assessment in self.assessments:
            if assessment.assessment_type == assessment_type:
                assessment_type_list.append(assessment)
        return assessment_type_list


class Assessment:  # pylint: disable=too-few-public-methods
    """
    Assessment superclass that passes off inheritance to the subclasses:
    Multiple-choice, presentation, and technical. It also has the 
    calculate_score() method for returning the score of an assessment
    multiplied by the weighting of the given assessment assessment_type.
    """

    def __init__(self, name: str, assessment_type: str, score: float):
        self.name = name
        self.assessment_type = assessment_type
        self.score = score

        if not isinstance(self.score, float) and not isinstance(self.score, int):
            raise TypeError("You must enter a float for assessment score!")
        if self.assessment_type not in ('multiple-choice', 'presentation', 'technical'):
            raise ValueError(
                "You must choose either multiple-choice, presentation"
                " or technical for assessment assessment_type.")

    def calculate_score(self):
        """Calculates the score of an assessment based on its given weighting."""
        if not isinstance(self.score, float) and not isinstance(self.score, int):
            raise TypeError('You must enter an float for score!')
        return self.score * self.weighting


class MultipleChoiceAssessment(Assessment):
    """"
    Multiple choice subclass for multiple choice
    based questions.
    """

    def __init__(self, name: str, score: float):
        super().__init__(name, "multiple-choice", score)
        self.weighting = 0.7


class PresentationAssessment(Assessment):
    """
    Presentation subclass for presentation
    based questions.
    """

    def __init__(self, name: str, score: float):
        super().__init__(name, "presentation", score)
        self.weighting = 0.6


class TechnicalAssessment(Assessment):
    """
    Technical Assessment subclass for technical
    based questions.
    """

    def __init__(self, name: str, score: float):
        super().__init__(name, "technical", score)
        self.weighting = 1


class Question:
    """
    Question class that holds each question within
    a quiz along with the correct and chosen answer.
    """

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer

    def __str__(self):
        return f"Question: {self.question}: "


class Quiz:
    """
    Quiz class that holds the list of questions, along
    with assessment assessment_type and assessment name.
    """

    def __init__(self, questions: list, name: str, assessment_type: str):
        self.questions = questions
        self.name = name
        self.assessment_type = assessment_type

    def __str__(self):
        return f"This is a {self.name} and is a {self.assessment_type} assessment."


class Marking:
    """
    Marking class that is responsible for returning 
    the marking of a given quiz as a percentage score
    integer.
    """

    def __init__(self, quiz: Quiz) -> None:
        self._quiz = quiz
        self.trainee_score = 0
        self.total_score = len(self._quiz.questions)
        self.percentage_score = 0

    def mark(self) -> int:
        """
        Returns a total percentage score of correct chosen answers
        in a given quiz.
        """
        self.trainee_score = 0
        self.total_score = len(self._quiz.questions)
        if self.total_score == 0:
            return 0
        for question in self._quiz.questions:
            if question.chosen_answer == question.correct_answer:
                self.trainee_score += 1
        self.percentage_score = self.trainee_score / self.total_score * 100
        return int(self.percentage_score)

    def generate_assessment(self) -> Assessment:
        """
        Returns the correct Assessment subclass
        based on properties of self._quiz.
        """
        assessment = None
        if self._quiz.assessment_type == "multiple-choice":
            assessment = MultipleChoiceAssessment(
                self._quiz.name, self.mark())
        elif self._quiz.assessment_type == "presentation":
            assessment = PresentationAssessment(
                self._quiz.name, self.mark())
        elif self._quiz.assessment_type == "technical":
            assessment = TechnicalAssessment(
                self._quiz.name, self.mark())
        return assessment


if __name__ == "__main__":
    # Example questions and quiz
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")

    # Add an implementation for the Marking class below to test your code
    marking = Marking(quiz)
    print(marking.mark())
