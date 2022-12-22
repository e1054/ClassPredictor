from typing import Any

import data
from Student import *
from StudentClass import *
import user_input
import random as r


def fill_class_list():
    """Fill the classes list with all the classes in random block"""

    data.class_list.clear()
    # Loop through each total class and assign it to a block and an id
    for id in range(data.total_classes):
        open_block = False
        random_block = -1
        while not open_block:
            random_block = r.randint(0, 7)
            open_block = check_open_block(random_block)
        data.class_list.append(StudentClass(id, random_block))

def check_open_block(block:int) -> bool:
    """Check how many classes is in a specific block and if block is open"""
    amount = 0
    # loop through each class and check if block is used
    for c in data.class_list:
        if c.id == block:
            amount += 1.
        if amount >= data.total_classes//10:
            return False
    return not amount >= data.total_classes//10

def assign_classes():
    """Assigns 8 random classes to all the students (random for each student)"""
    for student in data.student_list:
        student.classes.clear() # Clear old data from last trial
        for block in range(8):
            # Make sure the block the class is given to is empty and give the class
            valid_block = False
            while not valid_block:
                c = r.choice(data.class_list)
                valid_block = c.block == block
            student.classes.append(c)

def check_simular_classes():
    """Run through all students and check if they have simular classes with other students"""

    student_list_copy = data.student_list.copy()
    # Run while there is students left
    while len(student_list_copy) > 0:
        student = student_list_copy[0] # Student in which will be checked

        # Loop through all other students to check against initial student
        for i in range(len(student_list_copy)-1):
            # Initial Variables
            student_to_compare = student_list_copy[i+1]
            simulate_classes = 0
            simulate_with_level_classes = 0
            language_found = False
            none_language_found = False
            same_Level = True

            # Loop through each students 8 blocks per day
            for block in range(8):

                # Get each student's class in that specific bock
                class1:StudentClass = get_class(block, student)
                class2:StudentClass = get_class(block, student_to_compare)
                if class1 is None or class2 is None:
                    continue

                # If it is the same class that the students are in.
                if class1.id == class2.id:
                    simulate_with_level_classes += 1
                    # Check if the class is a language class. (Only once for each 8 blocks)
                    if not language_found and (class1.classid >= total_classes-total_languages):
                        data.simular_list["Simular Language"] += 1
                        language_found = True
                    if not none_language_found and (class1.classid < total_classes-total_languages):
                        data.simular_list["Simular None Language"] += 1
                        none_language_found = True
                # Check if class is the same level.
                # (To check if a students has classes with the same level all day in the same blocks)
                if not (class1.classlevel == class2.classlevel and class1.classid == class2.classid):
                    same_Level = False
                else:
                    simulate_classes += 1

            # Record data
            data.simular_list["Simular With Level " + (str(simulate_classes))] += 1
            data.simular_list["Simular " + (str(simulate_with_level_classes))] += 1
            if same_Level:
                data.simular_list["Same Level"] += 1
            else:
                data.simular_list["Not Same Level"] += 1

        # Remove current student and begin with next until none left
        student_list_copy.remove(student)
    pass

def get_class(block:int, student:Student) -> Any | None:
    """Get the class of a student in a specie block or None if no class is found"""

    for c in student.classes:
        if c.block == block:
            return c
    return None



def simulate():
    """Simulate one trial"""

    # Setup class list variables
    fill_class_list()

    # Assign classes to students
    assign_classes()

    # Run and record one simulation with the set variables
    check_simular_classes()
    
    pass

def display_DataFrame():
    """Print final data after all trials"""
    print(data.simular_list)
    pass

def main():
    """Start of program...!"""

    try:
        # Get basic information for the simulation
        i: int = user_input.get_int_positiv("Please enter the amount of trials to run: ")
        students_amount: int = user_input.get_int_positiv("Please enter the amount of students in each trial: ")
        default_settings: bool = user_input.get_boolean("Do you wish to use default settings in the simulation: ")
        if not default_settings:
            data.set_settings() # Let user pick all the settings

    except:
        return
    run(i, students_amount) # Start the simulation

def run(epochs: int, students_amount:int):
    """Run the simulation a set amount of times"""

    # Initialze Baker Objects
    for i in range(students_amount):
        data.student_list.append(Student(i))

    # Run each Simulation
    for i in range(1, epochs+1):
        # % Program Finished
        print(str(i) + " | " + "{:.2f}".format((i/epochs)*100) + "%")
        # Run one simulation (Saves output globally)
        simulate()

    # Display data for all the simulations
    display_DataFrame()


if __name__ == '__main__':
    main()