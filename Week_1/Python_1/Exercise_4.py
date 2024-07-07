midterm_score = input("Type your midterm score : ")
final_score = input("Type your final score : ")
homework_score = input("Type your homework score : ")
total_score = (float(midterm_score)*0.4 + float(final_score)*0.5 + float(homework_score)*0.1)

print(f"Total score is {total_score}")