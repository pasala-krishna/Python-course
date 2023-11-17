class Student:
    def __init__(self, name, scores=[]):
        self.name = name
        self.scores = scores

    def add_score(self, score):
        self.scores.append(score)

    def calculate_average_score(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

# Example usage:
student1 = Student("Krishna", [90, 85, 95, 88])
student2 = Student("Saravan", [78, 92, 87, 80])

# Add more scores
student1.add_score(93)
student2.add_score(89)

# Calculate and display average scores
average_score1 = student1.calculate_average_score()
average_score2 = student2.calculate_average_score()

print(f"{student1.name}'s average score: {average_score1}")
print(f"{student2.name}'s average score: {average_score2}")
