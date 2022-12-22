import user_input

student_list = [] # List of students
class_list = []   # List of classes

# Data recorded
simular_list = {"Simular 0": 0, "Simular 1": 0, "Simular 2": 0, "Simular 3": 0, "Simular 4": 0,
                "Simular 5": 0, "Simular 6": 0, "Simular 7": 0, "Simular 8": 0,
                "Simular With Level 0": 0, "Simular With Level 1": 0, "Simular With Level 2": 0, "Simular With Level 3": 0, "Simular With Level 4": 0,
                "Simular With Level 5": 0, "Simular With Level 6": 0, "Simular With Level 7": 0, "Simular With Level 8": 0,
                "Simular Language": 0, "Simular None Language": 0,
                "Same Level": 0, "Not Same Level": 0}

total_classes = 76
# Math
total_math_cp = 4
total_math_e = 4
total_math_h = 4
# Science
total_science_cp = 4
total_science_e = 4
total_science_h = 4
# English
total_english_cp = 6
total_english_h = 6
# History
total_history = 12
# Gym
total_gym = 12
# Spanish
total_spanish_cp = 3
total_spanish_h = 3
# French
total_french_cp = 1
total_french_h = 1
# Chinese
total_chinese_cp = 1
total_chinese_h = 1
# Latin
total_latin_cp = 1
total_latin_h = 1

def get_total_languages() -> int:
    return total_spanish_cp + total_spanish_h + total_french_cp + total_french_h + total_chinese_cp+total_chinese_h+total_latin_cp+total_latin_h

def set_settings():
    total = 0
    # Classes
    total_classes = user_input.get_int_positiv("How many classes should there be? ")
    # MATH
    total_math_cp = user_input.get_int_positiv("1/18 | Please enter amount of CP Math classes ("+str(total)+"/"+str(total_classes)+")")
    total += total_math_cp
    total_math_e = user_input.get_int_positiv("2/18 | Please enter amount of Enriched Math classes (" + str(total) + "/" + str(total_classes) + ")")
    total += total_math_e
    total_math_h = user_input.get_int_positiv("3/18 | Please enter amount of Honors Math classes (" + str(total) + "/" + str(total_classes) + ")")
    total += total_math_h
    # Science
    total_science_cp = user_input.get_int_positiv("4/18 | Please enter amount of CP Science classes (" + str(total) + "/" + str(total_classes) + ")")
    total += total_science_cp
    total_science_e = user_input.get_int_positiv("5/18 | Please enter amount of Enriched Science classes (" + str(total) + "/" + str(total_classes) + ")")
    total += total_science_e
    total_science_h = user_input.get_int_positiv("6/18 | Please enter amount of Honors Science classes (" + str(total) + "/" + str(total_classes) + ")")
    total += total_science_h
    # English
    total_english_cp = user_input.get_int_positiv("7/18 | Please enter amount of CP English classes (" + str(total) + "/" + str(total_classes) + ")")
    total += total_english_cp
    total_english_h = user_input.get_int_positiv("8/18 | Please enter amount of Honors English classes (" + str(total) + "/" + str(total_classes) + ")")
    total += total_english_h
    # History
    total_history = user_input.get_int_positiv("9/18 | Please enter amount of History classes (" + str(total) + "/" + str(total_classes) + ")")
    total += total_history
    # Gym
    total_gym = user_input.get_int_positiv("10/18 | Please enter amount of Gym classes (" + str(total) + "/" + str(total_classes) + ")")
    total += total_gym
    # Spanish
    total_spanish_cp = user_input.get_int_positiv("11/18 | Please enter amount of CP Spanish classes (" + str(total) + "/" + str(total_classes) + ")")
    total += total_spanish_cp
    total_spanish_h = user_input.get_int_positiv("12/18 | Please enter amount of Honors Spanish classes (" + str(total) + "/" + str(total_classes) + ")")
    total += total_spanish_h
    # French
    total_french_cp = user_input.get_int_positiv("13/18 | Please enter amount of CP French classes (" + str(total) + "/" + str(total_classes) + ")")
    total += total_french_cp
    total_french_h = user_input.get_int_positiv("14/18 | Please enter amount of Honors French classes (" + str(total) + "/" + str(total_classes) + ")")
    total += total_french_h
    # Chinese
    total_chinese_cp = user_input.get_int_positiv("15/18 | Please enter amount of CP Chinese classes (" + str(total) + "/" + str(total_classes) + ")")
    total += total_chinese_cp
    total_chinese_h = user_input.get_int_positiv("16/18 | Please enter amount of Honors Chinese classes (" + str(total) + "/" + str(total_classes) + ")")
    total += total_chinese_h
    # Latin
    total_latin_cp = user_input.get_int_positiv("17/18 | Please enter amount of CP Latin classes (" + str(total) + "/" + str(total_classes) + ")")
    total += total_latin_cp
    total_latin_h = user_input.get_int_positiv("18/18 | Please enter amount of Honors Latin classes (" + str(total) + "/" + str(total_classes) + ")")
    total += total_latin_h