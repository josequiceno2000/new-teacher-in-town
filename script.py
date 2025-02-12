from roster import student_roster
from classroom_organizer import ClassroomOrganizer

student_roster_iterator = iter(student_roster)

for i in range(10):
    next_item = next(student_roster_iterator)
    print(next_item)

classroom = ClassroomOrganizer()
table_combos = classroom.table_combinations()

for combo in table_combos:
    print(combo)