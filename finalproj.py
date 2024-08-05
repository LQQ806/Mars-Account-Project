# Final Project: Human Mission to Mars Account Setup
# Date:  6/10/2024
# Class: DEV108 44480
# Name: Hengmeng Ly

import csv
import random
import string
import time
MAX_SIZE = 20

# csv file
mainfile = "humandata.csv"

# Function to get their full name
def add_human_first():
    while True:
        firstname = input("Enter your first name: ").strip()
        return firstname
def add_human_last():
    while True:
        lastname = input("Enter your last name: ").strip()
        return lastname
    
# Function to get their age
def get_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            return age
        except ValueError:
            print("Invalid Input!")
            continue

# ID Number Function
def get_idnumber():
    id_number = random.randint(1001,9999)
    return id_number

# Email Function
def get_email(id_number,firstname,lastname):
    if " " in firstname or lastname:
        firstname.replace(" ","_")
        lastname.replace(" ","_")
    email = firstname+lastname+str(id_number)+"@gmail.com"
    return email

# Password Function
def get_password():
    length = 8
    # Variable to combine everything together
    passwordcharacter = [string.ascii_letters, string.digits, string.punctuation]
    password = ""

    # For loop to fill out password until it is 8 characters long
    for i in range(length):
        passwordrandom = random.choice(passwordcharacter)
        password += random.choice(passwordrandom)
    return password

# Living pod Function
def living_pod():
    # Variable for the building number and letter
    buildingletter = ["A","B","C","D","E"]
    randomletter = random.choice(buildingletter)
    digits = random.randint(1,10)
    pod_id = randomletter + str(digits)
    return pod_id

def random_note():
    randomnotes = [
        "Schizophrenic",
        "Very energetic",
        "A Normal Being",
        "Adventerous",
        "A very random person",
        "Batman?"
    ]
    generated_note = random.choice(randomnotes)
    return generated_note
# A search function
def search_command(datas):
    query = input("Search by their last name: ")
    results = []
    for row in datas:
        if query.lower() == row[1].lower():
            results.append(row)    
 
    if len(results) < 1:
        print("There is no one containing that last name.") 
    else:   
        print("Here are the name people who contains the name " + query)
        print()
        clean_list(results, False, True, False)

# Pod search command
def pod_search_command(datas):
    pod = input("Enter the Pod ID: ")
    count = 0
    for row in datas:
        if pod.upper() == row[5]:
            count += 1

    max_count = MAX_SIZE - count
    if max_count > 1:
        print(f"There are {max_count} pods left in {pod.upper()}")
    elif max_count:
        print(f"There is 1 pod left in {pod.upper()}")
    elif max_count < 1:
        print(f"There are no pods left in {pod.upper()}")

# Write it into the CSV file
def write_trip(data):
  with open(mainfile, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(data)

# Read the data from the functions
def read_trips():
  datas = []
  with open(mainfile, newline="") as file:
    reader = csv.reader(file)
    for row in reader:
      datas.append(row)
    return datas
  
# List Human Function
def clean_list(datas, listaccess, searchaccess, adminaccess):
  if listaccess:
    print("Firstname\t" + "Lastname\t" + "Age\t\t" + "Email\t\t\t" + "Pod Num\t")
    print()
    for data in datas:
      print(str(data[0]) + "\t\t" + str(data[1]) + "\t\t"  + str(data[2]) + "\t" + str(data[4]) + "\t\t" + str(data[5]))
      print()    
    # Check for the search command
  elif searchaccess:
    print("Firstname\t" + "Lastname\t" + "Age\t\t" + "Pod Num\t\t" + "Notes")
    print()
    for data in datas:
      print(str(data[0]) + "\t\t" + str(data[1]) + "\t\t"  + str(data[2]) + "\t\t" + str(data[5]) + "\t" + str(data[7]))
      print()
    # Check for the admin access
  elif adminaccess:
    print("Firstname\t" + "Lastname\t" + "Age\t" + "ID\t\t" + "Email\t\t\t" + "Password\t" + "Pod Num\t\t" + "Notes")
    print()
    for data in datas:
      print(str(data[0]) + "\t\t" + str(data[1]) + "\t\t"  + str(data[2]) + "\t" + str(data[3]) + "\t" + str(data[4]) + "\t" + str(data[6]) + "\t" + str(data[5]) + "\t" + str(data[7]))
      print()

# Delete function command
def delete_command(datas):
    try:
        delete = int(input("DELETION! Enter the ID of the account: "))
        for index, row in enumerate(datas):
            if delete == int(row[3]):
                del datas[index]
                break
    except ValueError:
        print("Invalid Input!")

# Admin access function
def adminstrator(datas):
    admin_access = input("Enter the admin password:")
    if admin_access == "Crytoisdabest":
        print()
        print("Admin Acess Granted!")
        clean_list(datas, False, False, True)
    else:
        print("Incorrect Password. Admin Access Denied!")
        print()
        
# Mission Function
def mission(datas):
    print("--------- PLANET EXPLORATION ---------")
    counter = 0
    mission_check = False
    while mission_check == False:
        choice = input ("This mission is dangerous! Would you like to proceed (y/n): ")
        randomnumber = random.sample(datas, random.randint(2,4))
        selected = []
        for i in randomnumber:
            selected.append(random.choice(datas)[0])
        
        if choice.lower() == "y":
            available_planets = ["Teyvat", "Solaris-3"]
            randomplanet = random.choice(available_planets)
            if randomplanet == available_planets[0]:
                print("You," + ", ".join(selected) + " have joined a mission towards Teyvat.")
                teyvat()
                mission_check == True
                break
            elif randomplanet == available_planets[1]:
                print("You," + ", ".join(selected) + " have joined a mission towards Solaris-3.")
                solaris3()
                mission_check == True
                break
        elif choice.lower() == "n":
            randommessage = ["Oh! I guess you aren't that adventurous.",
                                            "Cmon! A new planet is such an interesting journey.",
                                            "May this journey lead us starward.",
                                            "Across the multiverse, You shall be one with us",
                                            "Weakkk! Why not join with us?",
                                            "You sure are afraid of death eh?",
                                            "Cmon why aren't you fun :(",
                                            ]
            print(random.choice(randommessage))
            break
        else:
            print("Invalid Input! Please try again!")

# Function for Teyvat Mission
def teyvat():
    dialogue1 = False
    dialogue2 = False
    dialogue3 = False
    print()
    print("Teyvat is a world different from what Earth or Mars is and located 5 light years away from Mars.")
    time.sleep(1.5)
    print("This world is considered a fantasy across the galaxy and a majority of people have the power of the element.")
    time.sleep(1.5)
    print("According to the information that the ISS gathered, there is a city called Mondstadt that you can visit.")
    time.sleep(1.5)
    print()
    print("You and your friends decided to visit Mondstadt, a city of freedom and the region of Anemo (Air).")
    time.sleep(1.5)
    print("You were excited to explore the city to its root and you suddenly met a stunning woman.")
    time.sleep(1.5)
    print("The woman introduced herself and calls herself, Jean.")
    print()
    time.sleep(1.5)
    print("Jean: Hello, I am Jean, Acting Grand Master of the Knights of Favonius. It seems you are new here, Traveller.")
    time.sleep(1.5)
    print("A. Hello Jean! I am here to explore this world and it seems really intriguing.\n"
                "B. This is such a nice city that you have built.")
    while dialogue1 != True:
        dialogue1 = input("Enter your choice: ")
        if dialogue1.upper() == "A":
            print()
            print("Jean: Exploring? I guess calling you a traveller is correct.")
            time.sleep(1.5)
        elif dialogue1.upper() == "B":
            print()
            print("Jean: Oh! I didn't built this city, my ancestor built it and it is such an incredible thing that has ever happened.")
            print()
            time.sleep(1.5)
        else:
            print("Invalid Input! Please try again.")
            continue
        dialogue1 = True
        print("Jean: So, how do you like this cit---")
        time.sleep(1.5)
        print("Before Jean could finish her question, a loud bang echoed across the city.")
        time.sleep(1.5)
        print("Jean: Don't tell me those hilichurls are attacking the front gate of the city.")
        time.sleep(1.5)
        print("Before you could speak, Jean dashed out to the front gate where the hilichurls are attacking.")
        time.sleep(1.5)
        print("A. Go help Jean and defend the city")
        print("B. Run away and leave this planet.")
        while dialogue2 != True:
            dialogue2 = input("Enter your choice:")
            print()
            if dialogue2.upper() == "A":
                print("You rushed behind Jean and help her in battle, you saw alot of hilichurls and decided to unseathe your sword and attack them.")
                time.sleep(1.25)
                print("A. You use 'Dimension Slash'")
                print("B. You use 'Accelaration Precise Slash' ")
                dialogue2 = True
                while dialogue3 != True:
                    dialogue3 = input("Enter your choice: ")
                    print()
                    if dialogue3.upper() == "A":
                        print("You sliced all of the hilichurls in half in a split of a second.")
                    elif dialogue3.upper() == "B":
                        print("You moved so fast that you killed every hilichurls before the other soliders could even blink once.")
                    else:
                        print("Invalid Input! Try again.")
                        continue
                    time.sleep(1.25)
                    print("After the battle, everyone on the battlefield was amazed by your ability")
                    time.sleep(1.25)
                    print("Jean: This ability you used is too dangerous, you need to get out of here now!")
                    time.sleep(1.25)
                    print("Jean: The Abyss will come get you, if you don't get out")
                    time.sleep(1.25)
                    print("As danger approaches, You and your friend decides to leave the planet once and for all")
                    time.sleep(1.25)
                    print("During the stay, you have learnt abit about this world and you think of coming again in the future")
                    time.sleep(1.25)
                    print()
                    print("Mission Complete.....")
                    dialogue3 = True
            elif dialogue2.upper() == "B":
                print("You and your friends ditched and left the planet forever......")
                dialogue2 = True
            else:
                print("Invalid Input! Try again.")
                continue

# Function for the mission
def solaris3():
    dialogue1 = False
    dialogue2 = False
    dialogue3 = False
    dialogue4 = False
    print()
    time.sleep(1.5)
    print("A world similar to Earth, the terrain itself has been changed completely because of the sudden rise of Echoes, monster that are made out of frequency.")
    time.sleep(1.5)
    print("According to the information that the ISS gathered, there is a city called Jinzhou that you can visit.")
    time.sleep(1.5)
    print()
    print("You and your friends decided to visit Jinzhou, the youngest province in Huanglong.")
    time.sleep(1.5)
    print("You began exploring the city, it is filled with crowds and seems well managed with a defense mechanism around the city.")
    time.sleep(1.5)
    print("You and your friends were impressed of their technology and the locals are very kind too.")
    time.sleep(2.0)
    print()
    print("While you are exploring the city glory, a woman came up to you. She looks majestic and stared into your eyes.")
    time.sleep(1.5)
    print("You know she is a big deal with her stance and white hair and eyes, you can't fathom or grasps her beauty. You stood there in shock...")
    time.sleep(1.5)
    print("Until she speaks out, that is when you gained back your sense and reality.")
    time.sleep(1.5)
    print()
    print("Jinshi: Hello there, I am Jinshi, Magistrate of Jinzhou or the President in your world.")
    print("A. Wait so you know we are not from around here?\n"
                "B. Hey there, majestic lady (with a smirky face).")
    while dialogue1 != True:
        dialogue1 = input("Enter your choice: ")
        if dialogue1.upper() == "A":
            print()
            print("Jinshi: Well, the moment your ship entered the atmosphere, our defend system detected and we were prepared by your arrival.")
            time.sleep(2.25)
        elif dialogue1.upper() == "B":
            print()
            print("Jinshi: Look at you, flirting at me, aren't you a little cheeky person?")
            time.sleep(1.5)
        else:
            print("Invalid Input! Please try again.")
            continue
        dialogue1 = True
        print()
        print("Jinshi: Anyways, what brings you here, 'Rover'?")
        time.sleep(1.5)
        print("A. Just wanted to explore this interesting planet on our list.")
        print("B. We wanted to get some food and we heard it is a good planet for good food. ")
        while dialogue2 != True:
            dialogue2 = input("Enter your choice: ")
            if dialogue2.upper() == "A":
                print("Jinshi: You got a whole list of planets you want to visit,? Adventerous, aren't you?")
            elif dialogue2.upper() == "B":
                print("Jinshi: That is interesting way to come to a new planet.")
            else:
                print("Invalid Input! Try again.")
                continue
            dialogue2 = True
            print()
            print("The moment she said that, her cellphone beeped loudly.")
            time.sleep(1.5)
            print("Jinshi: Well, I would love to tour everyone here, but there seems to be some trouble, You care to join with me?")
            time.sleep(1.5)
            print("A. You decide to go with Jinshi to deal with the danger.")
            print("B. Stay back and continue exploring.")
        while dialogue3 != True:
            dialogue3 = input("Enter your choice: ")
            if dialogue3.upper() == "A":
                print("You follow Jinshi to the front gate of the city and saw alot of monsters called Echoes.")
            elif dialogue3.upper() == "B":
                print("You continue to explore and enjoy their food and return back to Mars.")
                break
            else:
                print("Invalid Input! Try again.")
            dialogue3 = True
            print()
            time.sleep(1.5)
            print("Many soldiers attack Echoes and as well as Jinshi helping out.")
            time.sleep(1.5)
            print("While battling, an elite class Echo appeared and began killing every soldiers, you decide to jump in and help.")
            time.sleep(1.5)
            print("A. You use 'Divine Departure'.")
            print("B. You use 'Imperior Slash' ")
            while dialogue4 != True:
                dialogue4 = input("Enter your choice: ")
                if dialogue4.upper() == "A":
                    print("You slashed the Elite class Echo and killed all the little ones.")
                elif dialogue4.upper() == "B":
                    print("You effortlessly killed the Echos and severely slashed the Elite class Echo.")
                else:
                    print("Invalid Input! Try again.")
                    continue
                print()
                time.sleep(1.9)
                print("Before the Echoes die, it muttered something.")
                time.sleep(1.5)
                print("Echo: Greeting Rover, y-you soon be dinner for our k-king.")
                time.sleep(1.5)
                print("You were terrified after hearing what it said to you.")
                print()
                time.sleep(1.5)
                print("Jinshi: Rover, you and your friends must get out of this planet now immediately.")
                time.sleep(1.5)
                print("You and your friends leave the planet in a hurry to avoid anymore danger.")
                time.sleep(1.5)
                print("Mission Complete.")
                dialogue4 = True
                break
# Display all human information upon creating a new account
def information(firstname, lastname, age, id_number, email, password, podid, notes):
    print("------------ Account Information ------------")
    print("Full Name: " + firstname + " " +  lastname)
    print("Age: " + str(age))
    print("ID Number: " + str(id_number))
    print("Pod ID: " + podid)
    print("Email: " + email)
    print("Password: " + password)
    print("Random Note: " + notes)
    print("--------------------------------------------------")
# Main function
def main():
    while True:
        datas = read_trips()
        
        # A Dupe Variable to prevent a dupe when reading data
        prevent_dupe = False
        print()
        print("Human Mission to Mars Menu")
        print()
        print("1. Add a human.")
        print("2. Lists of all humans")
        print("3. Search")
        print("4. Living Pod Search")
        print("5. Delete")
        print("6. Administrator Access")
        print("7. Missions")
        print("8. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                firstname = add_human_first()
                lastname = add_human_last()
                age = get_age()
                id_number = get_idnumber()
                email = get_email(id_number,firstname,lastname)
                podid = living_pod()
                password = get_password()
                notes = random_note()
                information(firstname, lastname, age, id_number, email, password, podid,notes)
                prevent_dupe = False
            elif choice == 2:
                prevent_dupe = True
                clean_list(datas, True, False, False)
            elif choice == 3:
                prevent_dupe = True
                data = search_command(datas)
            elif choice == 4:
                prevent_dupe = True
                count = pod_search_command(datas)
            elif choice == 5:
                prevent_dupe = True
                delete = delete_command(datas)
                write_trip(datas)
            elif choice == 6:
                prevent_dupe = True
                admin = adminstrator(datas)
            elif choice == 7:
                prevent_dupe = True
                speicalmission = mission(datas)
            elif choice == 8:
                prevent_dupe = True
                print("Thank for using our program!")
                break
            if prevent_dupe == False:
                data = []

                data.append(firstname)
                data.append(lastname)
                data.append(age)
                data.append(id_number)
                data.append(email)
                data.append(podid)
                data.append(password)
                data.append(notes)

                write_trip(data)
                prevent_dupe = True

        except ValueError or UnboundLocalError:
            print("Invalid Input. Please try again!")
if "__main__" == __name__:
     main()