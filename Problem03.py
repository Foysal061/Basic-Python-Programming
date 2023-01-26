# Suppose, in a company , here are some employee salaries in an array
#     [35000, 25000, 28000, 32500, 44000, 32800]
#     Write a method to find out the 3rd highest salary

salary_list = [35000, 25000, 28000, 32500, 44000, 32800]
salary_list.sort(reverse = True)
print("Third highest salary: ",salary_list[2])