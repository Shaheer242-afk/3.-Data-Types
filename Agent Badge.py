name = input("Please enter your name: ")
gadget = input("Please enter your Gadget: ")

agent_number = 10
speed_rating = 9
mission_count = 17
height = 1.97
is_active = True

print("Name:", name, "-> Type:", type(name))
print("Gadget:", gadget, "-> Type:", type(gadget))
print("Agent Number:", agent_number, "-> Type:", type(agent_number))
print("Speed Rating:", speed_rating, "-> Type:", type(speed_rating))
print("Mission Count:", mission_count, "-> Type:", type(mission_count))
print("Height:", height, "-> Type:", type(height))
print("Is active?:", is_active, "-> Type:", type(is_active))

agent_number_text = str(agent_number)
speed_rating_text = str(speed_rating)
mission_count_text = str(mission_count)
is_active_text = str(is_active)
print("\n\nAfter type casting\n")

print("Agent Number as Text", agent_number_text, "-> Type:",
type(agent_number_text))
print("Speed Rating as Text", speed_rating_text, "-> Type:",
type(speed_rating_text))
print("Mission Count as Text", mission_count_text, "-> Type:",
type(mission_count_text))
print("Is Active as Text", is_active_text, "-> Type:",
type(is_active_text))

first_three = name[0:3]
last_letter = name[-1:]
code_name= first_three + last_letter
print("First three letter:", first_three)
print("Last Letter:", last_letter)
print("Secret Code Name:", code_name)

reversed_gadget = gadget[::-1]
print("Reversed Gadget Name:", reversed_gadget)

badge_line_1 = "AGENT " + code_name.upper()
badge_line_2 = "ID: " + agent_number_text + " | MISSIONS:" + mission_count_text
badge_line_3 = "SPEED: " + speed_rating_text + " | ACTIVE:" + is_active_text
badge_line_4 = "SECRET GADGET CODE: " + agent_number_text + reversed_gadget.upper()

print("")
print("====== SECRET AGENT BADGE =====")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print("===============================")