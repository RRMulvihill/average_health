"""
AVERAGE HEALTH
written by Riley Mulvihill

Average Health is a data analysis program
That generates random data and calculates averages
A csv file would traditionally be provided for the user
but for testing purposes, a data list will be created dynamically.
"""
#Imports
from math import pow
from random import randint
#an object that represent a person and their data
class Person:
   

    def __init__(self, name, sex, age, height, weight):
        '''Varables:name=str,sex=str('male' or 'female')age=int,height=int,weight=int'''
        self.name = name
        self.sex = sex
        self.age = age
        self.height = height
        self.weight = weight

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex
    
    def get_age(self):
        return self.age
    
    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight
    
    #Function calculates person's body mass index and classification
    def get_bmi(self):
        bmi = round(self.weight/pow(self.height,2)*703,1)
        status = "status error"
        if (bmi <= 18.5):
            status = "underweight"
        elif (bmi <= 25):
            status = "normal weight"
        elif (bmi <= 30):
            status = "overweight"
        else:
            status = "obese"
        result = "BMI: " + str(bmi) + ", " + self.name + " is " + status
        return result

#Function calculates data averages
def averages(people_list, bmi_boolean = False):
    '''varaibles:people_list=list(Person objects)'''
    males = 0
    females = 0
    average_age = 0
    average_height = 0
    average_weight = 0
    
    for person in people_list:
        if person.get_sex() == "male":
            males += 1
        else:
            females += 1
            
        average_age += person.get_age()
        average_height += person.get_height()
        average_weight += person.get_weight()

        #Prints BMI data (not encouraged for large data sets)
        if(bmi_boolean == True):
            print(person.get_bmi())
        
    #format data
    males = str(round(males/len(people_list)*100))
    females = str(round(females/len(people_list)*100))
    average_age = round(average_age/len(people_list),1)
    average_height = round(average_height/len(people_list),1)
    average_weight = round(average_weight/len(people_list),1)
    
    #Print data
    print("\n\nAVERAGES:")
    print("Total people: " + str(len(people_list)))
    print("Sex: Males: " + males + "% Females: " + females + "%")
    print("Age: " + str(average_age))
    print("Height(in): " + str(average_height))
    print("Weight(lb): " + str(average_weight))

# Function generates a random collection of data for testing purposes
def generate_data(size):
    '''Size = integer, number of people to populate data from
       Returns = List of People objects
    '''

    #Names and sex are assigned randomly and may not coincide as expected
    names_list = ("Adam","Abby","Bruce","Beth","Carol","Damian","Dave","Sam","Joe","Jose","Martha","Nicole","Lee","Yolanda","Zeke") 
    sex_dict = {0:"male",1:'female'}
    people_list = []
    
    #Loop for person creation 
    for i in range(size):
        name = names_list[randint(0,(len(names_list)-1))]
        sex = sex_dict[randint(0,1)]
        age = randint(18,80)
        height = randint(48,84)
        weight = randint(90,200)
        new_person = Person(name,sex,age,height,weight)
        people_list.append(new_person)
    return people_list

#Runs program
def main():
    run = True
    print("AVERAGE HEALTH\n   by Riley Mulvihill\n\nAverage Health is a data analysis program\nThat generates random data and calculates averages\n\n")
    while(run):
        print("")
        size = input("Specify Test Size (integer):")
        try:
            size = int(size)
        except:
            print("invalid imput")
            return
        bmi_boolean = input("Include BMI Data? (y/n)")
        if bmi_boolean == "y":
            bmi_boolean = True
        elif bmi_boolean == "n":
            bmi_boolean = False
        else:
            print("Invalid input")
            return
        people_list = generate_data(size)
        averages(people_list,bmi_boolean)
        run_boolean = input("Run Again? (y/n):")
        if run_boolean == "y":
            run = True
        elif run_boolean == "n":
            run = False
        else:
            print("Invalid input")

main()
print("\nThank you for using Average Health\nHit 'Enter' to close")
input()
