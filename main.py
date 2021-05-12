# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
heights_sum = 0
num_students = 0
for student_height in student_heights:
  heights_sum += student_height
  num_students += 1

average_height = round(heights_sum / num_students)

print(average_height)

