from data import *


class StudentClass:
    def __init__(self, id, block):
        """Student Class to simulate each class"""
        self.id = id
        self.block = block
        self.classid = self.getClassID(id)
        self.classlevel = self.getClassLevel(id)

    def getClassID(self, id: int) -> int:
        """Get the class id"""

        i = 1
        total = 0
        total += total_math_cp
        if id > total:  # Math CP
            i += 1
        total += total_math_e
        if id > total:  # Math E
            i += 1
        total += total_math_h
        if id > total:  # Math H
            i += 1
        total += total_science_cp
        if id > total:  # Science CP
            i += 1
        total += total_science_e
        if id > total:  # Science E
            i += 1
        total += total_science_h
        if id > total:  # Science H
            i += 1
        total += total_english_cp
        if id > total:  # English CP
            i += 1
        total += total_english_h
        if id > total:  # English H
            i += 1
        total += total_history
        if id > total:  # US History
            i += 1
        total += total_gym
        if id > total:  # Gym
            i += 1
        total += total_spanish_cp
        if id > total:  # Spanish - CP
            i += 1
        total += total_spanish_h
        if id > total:  # Spanish - H
            i += 1
        total += total_french_cp
        if id > total:  # French - CP
            i += 1
        total += total_french_h
        if id > total:  # French - H
            i += 1
        total += total_chinese_cp
        if id > total:  # Chinese - CP
            i += 1
        total += total_chinese_h
        if id > total:  # Chinese - H
            i += 1
        total += total_latin_cp
        if id > total:  # Latin - CP
            i += 1
        total += total_latin_h
        if id > total:  # Latin - H
            i += 1
        return i

    def getClassLevel(self, id: int) -> str:
        """Get the class level (CP, Enriched[E], Honors[H])"""

        total = total_classes
        total -= total_latin_h
        if id > total:  # Latin - H
            return 'H'
        total -= total_latin_cp
        if id > total:  # Latin - CP
            return 'CP'
        total -= total_chinese_h
        if id > total:  # Chinese - H
            return 'H'
        total -= total_chinese_cp
        if id > total:  # Chinese - CP
            return 'CP'
        total -= total_french_h
        if id > total:  # French - H
            return 'H'
        total -= total_french_cp
        if id > total:  # French - CP
            return 'CP'
        total -= total_spanish_h
        if id > total:  # Spanish - H
            return 'H'
        total -= total_spanish_cp
        if id > total:  # Spanish - CP
            return 'CP'
        total -= total_gym
        if id > total:  # Gym
            return 'GYM'
        total -= total_history
        if id > total:  # History
            return 'HISTORY'
        total -= total_english_h
        if id > total:  # English H
            return 'CP'
        total -= total_english_cp
        if id > total:  # English CP
            return 'CP'
        total -= total_science_h
        if id > total:  # Science H
            return 'H'
        total -= total_science_e
        if id > total:  # Science E
            return 'E'
        total -= total_science_cp
        if id > total:  # Science CP
            return 'CP'
        total -= total_math_h
        if id > total:  # Math H
            return 'H'
        total -= total_math_e
        if id > total:  # Math E
            return 'E'
        total -= total_math_cp
        if id > total:  # Math CP
            return 'CP'

        return 'CP'
