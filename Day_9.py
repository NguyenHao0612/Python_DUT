#----------------------------------------------------
# Dictionaries & Nesting (Từ điển và lồng nhau)
# ---------------------------------------------------
# Dictionaries
from copyreg import add_extension


programing_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    
}
# retrieving items from dictionary ( Lấy items từ dictionary)
# print(programing_dictionary["Function"])
# Adding new items to dictionary (Thêm các items mới vào dictionary)
programing_dictionary["Loop"] = "The action of doing something over and over again."
print(programing_dictionary)

# Create an empty dictionary. (Tạo dictionary rỗng)
empty_dictionary = {}

# wipe an existing dictionary
programing_dictionary = {}
print(programing_dictionary)

# Edit an item in a dictionary
programing_dictionary["Bug"] = "A moth in your computer."

# Loop through a dictionanry
for key in programing_dictionary:
    print(key)
    print(programing_dictionary[key])

#-----------------------------------------------------------
# Grading Program Exercise (Chương trình chấm điểm)

student_score = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62,
}

student_grades = {}
for student in student_score:
    score = student_score[student]
    if score > 90 :
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)

#-----------------------------------------------------
# Nesting

capitals = {
    "France" : "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary (Lồng 1 list trong dictionary)
# {
#     Key : [List],
#     Key2 : {Dict},
# }
travel_log = {
    "France" : {"cities_visited" : ["Paris", "Lille", "Dijion"], "total_vissits" : 12},
    "Germany" : {"cities_visited" : ["Berlin", "Hamburg","Stuttgart"] , "total_vissits" : 5},
}

# Nesting Dictionary in a List
travel_log = [ 
    {
        "country" : "France",
        "cities_visited" : ["Paris", "Lille", "Dijion"], 
        "total_visits" : 12
    },
    {
        "country" : "Germany",
        "cities_visited" : ["Berlin", "Hamburg","Stuttgart"] , 
        "total_visits" : 5
    },
]

#-------------------------------------------------------------
# Dictionary in List Exercise
travel_log = [ 
    {
        "country" : "France",
        "cities_visited" : ["Paris", "Lille", "Dijion"], 
        "visits" : 12
    },
    {
        "country" : "Germany",
        "cities_visited" : ["Berlin", "Hamburg","Stuttgart"] , 
        "visits" : 5
    },
]
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country("Rusia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

#--------------------------------------------------------
#
from art import logo
#print(logo)
print("Welcome to the secret auction program\n")
bids = {}
bidding_finished = False
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What is your bid? : $"))
    bids[name]= price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("-------- Clear --------\n")

