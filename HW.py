name = input("Please enter your name: ")
club_name = input("Please enter your Club Name: ")

ID_number = 7864
clubs_joined = 4


print("Name:", name, "-> Type:", type(name))
print("Club Name:", club_name, "-> Type:", type(club_name))
print("Clubs Joined:", clubs_joined, "-> Type:", type(clubs_joined))
print("ID Number:", ID_number, "-> Type:", type(ID_number))


ID_number_text = str(ID_number)
clubs_joined_text = str(clubs_joined)
print("\n\nAfter type casting\n")

print("Name: ", name, "-> Type:",
type(name))
print("Club Name: ", club_name, "-> Type:",
type(club_name))
print("Clubs Joined: ", clubs_joined, "-> Type:",
type(clubs_joined_text))
print("ID Number: ", ID_number, "-> Type:",
type(ID_number_text))

first_three = name[0:3]
last_letter = name[-1:]
club_code_name= first_three + last_letter
print("First three letter:", first_three)
print("Last Letter:", last_letter)
print("Club Code:", club_code_name)

badge_line_1 = " " + club_code_name.upper()
badge_line_2 = "ID: " + ID_number_text
badge_line_3 = "Clubs Joined:" + clubs_joined_text
badge_line_4 = "Club Name: " + club_name

print("")
print("====== CLUB BADGE =====")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print("=======================")