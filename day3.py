#functions

# def max():
#     print("hello")
#     print("Lavhanya")
# max()

# passing inputs

# def call(name):
#     print(f"Hello {name} ")
# call("Lavhanya")

# def life_in_weeks(age):
#     x=90-age
#     y=52*(x)
#     print(f"You have {y} weeks left.")
# life_in_weeks(12)

# def calculate_love_score(name1, name2):
#     combined_names = name1 + name2
#     lower_names = combined_names.lower()
    
#     t = lower_names.count("t")
#     r = lower_names.count("r")
#     u = lower_names.count("u")
#     e = lower_names.count("e")
#     first_digit = t + r + u + e
    
#     l = lower_names.count("l")
#     o = lower_names.count("o")
#     v = lower_names.count("v")
#     e = lower_names.count("e")
#     second_digit = l + o + v + e
    
    
#     score = str(first_digit) + str(second_digit)
#     print(score)
    
# calculate_love_score("Kanye West", "Kim Kardashian")

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
 
# # Create an empty dictionary to collect the new values.
# student_grades = {}
 
# # Loop through each key in the student_scores dictionary
# for student in student_scores:
 
#     #Get the value (student score) by using the key each time.
#     score = student_scores[student]
 
#     #Check what grade the score would get, then add it to student_grades
#     if score >= 91:
#         student_grades[student] = 'Outstanding'
#     elif score >= 81:
#         student_grades[student] = 'Exceeds Expectations'
#     elif score >= 71:
#         student_grades[student] = 'Acceptable'
#     else:
#         student_grades[student] = 'Fail'
# Blind Auction Program

# bids = {}
# more_bidders = True

# while more_bidders:
#     name = input("Enter your name: ")
#     bid = int(input("Enter your bid: $"))
#     bids[name] = bid
    
#     more = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
#     if more != 'yes':
#         more_bidders = False

# # Find the highest bid
# winner = max(bids, key=bids.get)
# highest_bid = bids[winner]

# print(f"The winner is {winner} with a bid of ${highest_bid}")

# def collect_bids():
#     bids = {}
#     more_bidders = True
#     while more_bidders:
#         name = input("Enter your name: ")
#         bid = int(input("Enter your bid: $"))
#         bids[name] = bid

#         more = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
#         if more != 'yes':
#             more_bidders = False
#     return bids

# def find_winner(bids):
#     highest_bid = 0
#     winner = ''
#     for name in bids:
#         if bids[name] > highest_bid:
#             highest_bid = bids[name]
#             winner = name
#     return winner, highest_bid

# # Main program
# bids = collect_bids()
# winner, highest_bid = find_winner(bids)
# print(f"The winner is {winner} with a bid of ${highest_bid}")

# Bid auction program ---original
# def find_highest_bidder(bidding_dictionary):
#     highest_bid = 0
#     winner = ""

#     for bidder in bidding_dictionary:
#         bid_amount = bidding_dictionary[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder

#     print(f"The winner is {winner} with a bid of ${highest_bid}.")


# bids = {}
# continue_bidding = True

# while continue_bidding:
#     name = input("What is your name?: ")
#     price = int(input("What is your bid?: $"))
#     bids[name] = price

#     should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")

#     if should_continue == "no":
#         continue_bidding = False
#         find_highest_bidder(bids)
#     elif should_continue == "yes":
#         print("\n" * 20)

#return keyword using

# def x(f_name,l_name):
#     f1=f_name.title()
#     l1=l_name.title()
#     return f"Hello {f1} {l1}"

# print(x("Lavhanya","KOTHA"))

# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def outer_function(a, b):
#     def inner_function(c, d):
#         return c + d
#     return inner_function(a, b) # output of the outer_function is becoming the inputs of the inner_function
 
# result = outer_function(5, 10)
# print(result)