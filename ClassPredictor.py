from typing import Any

from Student import *
from StudentClass import *
import random as r

student_list = []
class_list = []

simular_list = {"Simular 0": 0, "Simular 1": 0, "Simular 2": 0, "Simular 3": 0, "Simular 4": 0,
                                 "Simular 5": 0, "Simular 6": 0, "Simular 7": 0, "Simular 8": 0,
                "Simular With Level 0": 0, "Simular With Level 1": 0, "Simular With Level 2": 0, "Simular With Level 3": 0, "Simular With Level 4": 0,
                                 "Simular With Level 5": 0, "Simular With Level 6": 0, "Simular With Level 7": 0, "Simular With Level 8": 0,
                                 "Simular Language": 0, "Simular None Language": 0,"Same Level": 0, "Not Same Level": 0}

def fill_class_list():
    class_list.clear()
    for id in range(76):
        open_block = False
        while not open_block:
            random_block = r.randint(0, 7)
            open_block = check_open_block(random_block)
        class_list.append(StudentClass(id, random_block))

def check_open_block(block:int) -> bool:
    amount = 0
    for c in class_list:
        if c.id == block:
            amount += 1.
        if amount >= 10:
            return False
    return not amount >= 10

def assign_classes():
    for student in student_list:
        student.classes.clear()
        for block in range(8):
            valid_block = False
            while not valid_block:
                c = r.choice(class_list)
                valid_block = c.block == block
            student.classes.append(c)

def check_simular_classes():
    student_list_copy = student_list.copy()
    while len(student_list_copy) > 0:
        student = student_list_copy[0]
        for i in range(len(student_list_copy)-1):
            student_to_comapre = student_list_copy[i+1]
            simulate_classes = 0
            simulate_with_level_classes = 0
            language_found = False
            none_language_found = False
            same_Level = True
            for block in range(8):
                class1:StudentClass = get_class(block, student)
                class2:StudentClass = get_class(block, student_to_comapre)
                if class1 is None or class2 is None:
                    continue

                if class1.id == class2.id:
                    simulate_with_level_classes += 1
                    if not language_found and (class1.classid > 10):
                        simular_list["Simular Language"] += 1
                        language_found = True
                    if not none_language_found and (class1.classid < 10):
                        simular_list["Simular None Language"] += 1
                        none_language_found = True

                if not (class1.classlevel == class2.classlevel and class1.classid == class2.classid):
                    same_Level = False
                else:
                    simulate_classes += 1
            simular_list["Simular With Level " + (str(simulate_classes))] += 1
            simular_list["Simular " + (str(simulate_with_level_classes))] += 1
            if same_Level:
                simular_list["Same Level"] += 1
            else:
                simular_list["Not Same Level"] += 1
        student_list_copy.remove(student)
    pass

def get_class(block:int, student:Student) -> Any | None:
    for c in student.classes:
        if c.block == block:
            return c
    return None



def simulate():
    fill_class_list()
    assign_classes()

    check_simular_classes()
    
    pass

def display_DataFrame():
    print(simular_list)
    pass

def main():
    """Start of program...!"""
    try:
        i: int = int(input("Please enter the amount of trials to run: "))
        students_amount: int = int(input("Please enter the amount of students in each trial: "))
    except:
        return
    run(i, students_amount)


def run(epochs: int, students_amount:int):
    """Run the simulation a set amount of times"""

    # Initialze Baker Objects
    for i in range(students_amount):
        student_list.append(Student(i))

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