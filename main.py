file = open("password.txt")
file_read = file.readlines()
number = 0
#for q in file_read:
  #  test = file_read[number].splitlines()
   # print(test)
    #number += 1

while number < len(file_read):
    test = file_read[number].splitlines()
    print(test)
    number +=1

def main():
    file = open("password.txt", 'w+')
    name = input("Name: ")
    surname = input("Surname: ")
    day_of_birthday = input("Day of birthday: ")
    moons_of_birthday = input("Moons of birthday: ")
    year_of_birthday = input("Year of birthday: ")
    test = name + surname + str(day_of_birthday) + str(moons_of_birthday) + str(year_of_birthday)
    array_n = [name, surname, day_of_birthday, moons_of_birthday, year_of_birthday]
    testm = [1]
    password = []
    passwords = []
    for i in testm:
        password.append(array_n[0].capitalize() + array_n[1].capitalize())
        password.append(array_n[1].capitalize() + array_n[0].capitalize())
        password.append(str(array_n[0].capitalize()) + str(array_n[1].capitalize()) + str(array_n[2]) + str(array_n[3]) + str(array_n[4]))
        password.append(str(array_n[1].capitalize()) + str(array_n[0].capitalize()) + str(array_n[2]) + str(array_n[3]) + str(array_n[4]))
        password.append(str(array_n[0].capitalize()) + str(array_n[1]) + str(array_n[2]) + str(array_n[3]) + str(array_n[4] ))
        password.append(str(array_n[0]) + str(array_n[1].capitalize()) + str(array_n[2]) + str(array_n[3]) + str(array_n[4]))
        password.append(str(array_n[2]) + str(array_n[3]) + str(array_n[4]))
        password.append(str(array_n[4]) + str(array_n[2]) + str(array_n[3]))
        password.append(str(array_n[1]) + str(array_n[2]) + str(array_n[3]))
        password.append(str(array_n[1].capitalize()) + str(array_n[2]) + str(array_n[3]))
        password.append(str(array_n[1]) + str(array_n[2]) + str(array_n[3]) + str(array_n[4]))
        password.append(str(array_n[1]).capitalize() + str(array_n[2]) + str(array_n[3]) + str(array_n[4]))
        password.append((str(array_n[0]) + str(array_n[2]) + str(array_n[3]) + str(array_n[4])))
        password.append((str(array_n[0].capitalize()) + str(array_n[2]) + str(array_n[3]) + str(array_n[4])))
        print("Succes! saved to password.txt")
    file.write("\n".join(password))
    file.close()



if __name__ == "__main__":
    main()