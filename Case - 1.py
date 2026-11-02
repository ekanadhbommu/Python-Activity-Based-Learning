aggregate=86
subjects=(78,64,91)
attendance=88
income=240000
eligible=aggregate>=80 and min(subjects)>=60 and attendance>=75 and income<=300000
print('Eligible' if eligible else 'Not eligible')
print('Rank score:', aggregate, 'Attendance:', attendance)
