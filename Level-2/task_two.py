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


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(MultipleChoiceAssessment(
        "Python Basics", 90.1))
    trainee.add_assessment(TechnicalAssessment(
        "Python Data Structures", 67.4))
    trainee.add_assessment(MultipleChoiceAssessment("Python OOP", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
