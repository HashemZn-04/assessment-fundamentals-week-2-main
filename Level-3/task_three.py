from datetime import date


class Trainee:
    def __init__(self, name: str, email: str, date_of_birth: date):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = []

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

    def get_assessment_of_type(self, type: str) -> list[Assessment]:
        """
        Returns a list of all assessments matching the type specified in this
        function's position arg.
        """
        if not isinstance(type, str):
            raise TypeError('You must enter a string!')
        elif type != "multiple-choice" and type != "presentation" and type != "technical":
            raise ValueError(
                'You must enter either multiple-choice, presentation, or technical for assessment types!')

        assessment_type_list = []
        for assessment in self.assessments:
            if assessment.type == type:
                assessment_type_list.append(assessment)
        return assessment_type_list


class Assessment:
    def __init__(self, name: str, type: str, score: float):
        self.name = name
        self.type = type
        self.score = score

        if not isinstance(self.score, float) and not isinstance(self.score, int):
            raise TypeError("You must enter a float for assessment score!")
        if self.type != "multiple-choice" and self.type != "presentation" and self.type != "technical":
            raise ValueError(
                "You must choose either multiple-choice, presentation or technical for assessment type.")

    def calculate_score(self):
        """Calculates the score of an assessment based on its given weighting."""
        if not isinstance(self.score, float) and not isinstance(self.score, int):
            raise TypeError('You must enter an float for score!')
        return self.score * self.weighting


class MultipleChoiceAssessment(Assessment):
    def __init__(self, name: str, score: float):
        super().__init__(name, "multiple-choice", score)
        self.weighting = 0.7


class PresentationAssessment(Assessment):
    def __init__(self, name: str, score: float):
        super().__init__(name, "presentation", score)
        self.weighting = 0.6


class TechnicalAssessment(Assessment):
    def __init__(self, name: str, score: float):
        super().__init__(name, "technical", score)
        self.weighting = 1


class Question:

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer


class Quiz:

    def __init__(self, questions: list, name: str, type: str):
        self.questions = questions
        self.name = name
        self.type = type


class Marking:

    def __init__(self, quiz: Quiz) -> None:
        self._quiz = quiz

    def mark(self) -> int:
        self.trainee_score = 0
        self.total_score = len(self._quiz.questions)
        for question in self._quiz.questions:
            if question.chosen_answer == question.correct_answer:
                self.trainee_score += 1
        self.percentage_score = self.trainee_score / self.total_score * 100
        return int(self.percentage_score)

    def generate_assessment(self) -> Assessment:
        return Assessment(self._quiz.name, self._quiz.type, self.mark())


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
