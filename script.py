from roster import student_roster
from classroom_organizer import ClassroomOrganizer
import itertools

student_roster_iterator = iter(student_roster)

for i in range(10):
    next_item = next(student_roster_iterator)
    print(next_item)

classroom = ClassroomOrganizer()
table_combos = classroom.table_combinations()

for combo in table_combos:
    print(combo)

math_students = classroom.get_students_with_subject("Math")
science_students = classroom.get_students_with_subject("Science")

math_and_science_students = itertools.chain(math_students, science_students)

afterschool_combos = itertools.combinations(math_and_science_students, 4)

for combo in afterschool_combos:
    print(combo)