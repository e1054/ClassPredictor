from typing import Any

import data
from Student import *
from StudentClass import *
import user_input
import random as r


def fill_class_list():
    data.class_list.clear()
    for id in range(data.total_classes):
        open_block = False
        random_block = -1
        while not open_block:
            random_block = r.randint(0, 7)
            open_block = check_open_block(random_block)
        data.class_list.append(StudentClass(id, random_block))

def check_open_block(block:int) -> bool:
    amount = 0
    for c in data.class_list:
        if c.id == block:
            amount += 1.
        if amount >= data.total_classes//10:
            return False
    return not amount >= data.total_classes//10

def assign_classes():
    for student in data.student_list:
        student.classes.clear()
        for block in range(8):
            valid_block = False
            while not valid_block:
                c = r.choice(data.class_list)
                valid_block = c.block == block
            student.classes.append(c)

def check_simular_classes():
    student_list_copy = data.student_list.copy()
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
                        data.simular_list["Simular Language"] += 1
                        language_found = True
                    if not none_language_found and (class1.classid < 10):
                        data.simular_list["Simular None Language"] += 1
                        none_language_found = True

                if not (class1.classlevel == class2.classlevel and class1.classid == class2.classid):
                    same_Level = False
                else:
                    simulate_classes += 1
            data.simular_list["Simular With Level " + (str(simulate_classes))] += 1
            data.simular_list["Simular " + (str(simulate_with_level_classes))] += 1
            if same_Level:
                data.simular_list["Same Level"] += 1
            else:
                data.simular_list["Not Same Level"] += 1
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
    print(data.simular_list)
    pass

def main():
    """Start of program...!"""
    try:
        i: int = user_input.get_int_positiv("Please enter the amount of trials to run: ")
        students_amount: int = user_input.get_int_positiv("Please enter the amount of students in each trial: ")
        default_settings: bool = user_input.get_boolean("Do you wish to use default settings in the simulation: ")
        if not default_settings:
            data.set_settings()

    except:
        return
    run(i, students_amount)

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