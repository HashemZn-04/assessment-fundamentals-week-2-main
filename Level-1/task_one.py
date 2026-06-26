from datetime import date


class Trainee:
    """
    Trainee subclass that contains all trainee information,
    this includes returning age in years, adding an assessment
    to the trainee's list of assessments, and a method get_assessment()
    that returns a specified assessment from its assessment list.
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


class Assessment:  # pylint: disable=too-few-public-methods
    """
    Assessment class containing assessment type, its name, and score.
    """

    def __init__(self, name: str, assessment_type: str, score: float):
        self.name = name
        self.assessment_type = assessment_type
        self.score = score

        if not isinstance(self.score, float) and not isinstance(self.score, int):
            raise TypeError("You must enter a float for assessment score!")
        if self.score < 0 or self.score > 100:
            raise ValueError("You must enter a score between 0 and 100!")
        if self.assessment_type not in ('multiple-choice', 'presentation', 'technical'):
            raise ValueError(
                "You must choose either multiple-choice, presentation"
                " or technical for assessment assessment_type.")

    def __str__(self):
        return f"{self.assessment_type} assessment, with a score of {self.score}"


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(Assessment(
        "Python Basics", "multiple-choice", 90.1))
    trainee.add_assessment(Assessment(
        "Python Data Structures", "technical", 67.4))
    trainee.add_assessment(Assessment("Python OOP", "multiple-choice", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
