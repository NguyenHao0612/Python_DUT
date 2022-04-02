#-----------------------------------------------------
#                   Debugging                        |
#-----------------------------------------------------

# Describe Problem
# Hàm sẽ chạy i tới 19 và thoát ko in dòng " You got it"
# Để fix thì thay điều kiện vòng for (1,21)
def my_function():
    # for i in range(1, 20):
    for i in range(1, 21):
        if i == 20:
            print("You got it")
my_function()

# Reproduce the Bug
# Lỗi tại mảng chạy từ 0 tới 5 nhưng randint từ 1 tới 6
# Nên ko có giá trị dice_imgs[6] => Lỗi
# Để fix thay randiant(0, 5) random chạy từ 0 tới 5
from random import randint
dice_imgs = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(1, 6)
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# Play Computer                    
# Lỗi tại year = 1994 sẽ ko có trường hợp nào    
# Để fix Thêm điều kiện = 1994
year = int(input ("What's your year of birth?"))
if year > 1980 and year < 1994:
    print ("You are a millenial.")
#elif year > 1994:
elif year >= 1994:
    print ("You are a Gen Z.")

# Fix the Errors
# Lỗi không hiện giá trị tuổi vì có f"   "
# Để fix thêm f " {age}"
age = int(input("How old are you?"))
if age > 18:
    # print("You can drive at age {age}.")
    print(f"You can drive at age {age}.")
      
#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input ("Number of pages: "))
word_per_page = int(input ("Number of words per page: "))
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}")
print(total_words)
                
#Use a Debugger
# Vòng lặp chạy tới khi item = 13 , nhân 2 thành 26 
# hàm append sẽ thêm 26 vào mảng b
# Để fix tab dòng b_list.append(new_item)
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    #b_list.append(new_item)
    print(b_list)

mutate( [1,2,3,5,8,13])

# Take a Break, Ask a friend, Run Often,
# Ask Stackoverflow, 

#-----------------------------------------------------
#                   Debug Odd or Even                |
#-----------------------------------------------------
number = int(input("Which number do you want to check?"))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

#-----------------------------------------------------
#                   Debug Leap Year                  |
#-----------------------------------------------------
year = int(input("Which year do you want to check?"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

#-----------------------------------------------------
#                   Debug Fizz Buzz                  |
#-----------------------------------------------------
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0 :
        print("Fizzbuzz")
    elif number % 3 == 0 :
        print("Fizz")
    elif number % 5 == 0 :
        print("Buzz")
    else:
        print(number)
