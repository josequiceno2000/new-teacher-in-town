from roster import student_roster

student_roster_iterator = iter(student_roster)

for i in range(10):
    next_item = next(student_roster_iterator)
    print(next_item)