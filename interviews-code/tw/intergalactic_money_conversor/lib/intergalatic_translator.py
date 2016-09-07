"""Parse an Intergalactic Talk"""

import re
from roman_converter import roman_to_numeral
from alien_converter import AlienConverter, InvalidAlienNumeralError

class IntergalaticTranslator:

    NO_IDEA = "I have no idea what you are talking about"

    def __init__(self, alien_converter=None):
        """Construct a new 'AlienConverter' object."""
        self.sentences = []
        if alien_converter is None:
            self.alien_converter = AlienConverter()

    def evaluate(self):
        """Evaluate a Intergalactic talk."""
        result = IntergalaticTranslator.NO_IDEA
        for sentence in self.sentences:
            if self.__sentence_is_a_alien_numeral_definition(sentence):
                result = self.__define_alien_numeral_value(sentence)
            elif self.__sentence_is_a_value_material_definition(sentence):
                result = self.__define_material_value(sentence)
            elif self.__sentence_is_a_question(sentence):
                result = self.__answer_question(sentence)
            else:
                result = IntergalaticTranslator.NO_IDEA 
        return result

    def __define_alien_numeral_value(self, sentence):
        alien_numeral = re.match(r"^\w+", sentence).group()
        roman_numeral = re.match(r"^\w+", re.sub(r"^\w+ is ", "", sentence)).group()
        self.alien_converter.alien_numerals[alien_numeral] = {'roman': roman_numeral,
                                              'arabic': roman_to_numeral(roman_numeral)}
    
    def __define_material_value(self, sentence):
        alien_numerals = self.__extract_alien_numerals(sentence)
        try:
            alien_numerals_value = self.alien_converter.sum_alien_numerals(alien_numerals)
        except InvalidAlienNumeralError:
            return IntergalaticTranslator.NO_IDEA
        material = re.search(r"(Silver|Gold|Iron)", sentence).group()
        if material is None:
            return IntergalaticTranslator.NO_IDEA
        credit = re.search(
            r"\d+", re.sub(r"^(\w+ )+(Silver|Gold|Iron)", "", sentence)).group()
        self.alien_converter.materials[material] = float(credit) / float(alien_numerals_value)
        
    def __extract_alien_numerals(self, sentence):
        sentence_words = sentence.split()
        alien_numerals = []
        alien_numerals_pattern = r"^(" + "|".join(self.alien_converter.alien_numerals.keys()) + ")"
        for word in sentence_words:
            if re.match(alien_numerals_pattern, word) is not None:
                alien_numerals.append(re.match(alien_numerals_pattern, word).group())
        return alien_numerals
    
    def __answer_question(self, sentence):
        alien_numerals = self.__extract_alien_numerals(sentence)
        answer = " ".join(alien_numerals)
        try:
            alien_numerals_value = self.alien_converter.sum_alien_numerals(alien_numerals)
        except InvalidAlienNumeralError:
            return IntergalaticTranslator.NO_IDEA
        if self.__question_is_how_much(sentence):
            answer = "{0} is {1}".format(answer, alien_numerals_value)
            return answer
        elif self.__question_is_how_many(sentence):
            material = re.search(r"(Silver|Gold|Iron)", sentence).group()
            if material is None:
                return IntergalaticTranslator.NO_IDEA
            answer = "{0} {1} is {2} Credits".format(
                answer, material,
                int(self.alien_converter.materials[material] * alien_numerals_value))
            return answer
        else:
            return IntergalaticTranslator.NO_IDEA
    
    def __question_is_how_much(self, sentence):
        return re.match(r"^how much is ", sentence)

    def __question_is_how_many(self, sentence):
        return re.match(r"^how many +(Credits|Silver) is ", sentence)
    
    def __sentence_is_a_alien_numeral_definition(self, sentence):
        return re.match(r"^\w+ is [IVXLCDM]$", sentence)
    
    def __sentence_is_a_value_material_definition(self, sentence):
        return re.match(r"^(\w+ )+(Silver|Gold|Iron) is \d+ Credits$", sentence)
    
    def __sentence_is_a_question(self, sentence):
        return re.match(r"^how (much|many Credits)? is (\w+ )+(Silver |Gold |Iron )?\?$", sentence)
