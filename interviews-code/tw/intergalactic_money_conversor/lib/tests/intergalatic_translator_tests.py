import unittest, os.path as path, sys
from inspect import getsourcefile
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from intergalatic_translator import IntergalaticTranslator
sys.path.pop(0)


class TestInputProcessorSimpleNewValues(unittest.TestCase):
    
    def setUp(self):
        self.intergalatic_translator = IntergalaticTranslator()
        self.intergalatic_translator.sentences.append("hmga is C")
        self.intergalatic_translator.sentences.append("mpor is D")
    
    def test_hmga_should_be_100(self):
        self.intergalatic_translator.sentences.append("how much is hmga ?")
        self.assertEqual(self.intergalatic_translator.evaluate(), "hmga is 100")

    def test_mpor_should_be_500(self):
        self.intergalatic_translator.sentences.append("how much is mpor ?")
        self.assertEqual(self.intergalatic_translator.evaluate(), "mpor is 500")

class TestInputProcessorSimpleValues(unittest.TestCase):
    
    def setUp(self):
        self.intergalatic_translator = IntergalaticTranslator()
        self.intergalatic_translator.sentences.append("grok is I")

    def test_grok_should_be_1(self):
        self.intergalatic_translator.sentences.append("how much is grok ?")
        self.assertEqual(self.intergalatic_translator.evaluate(), "grok is 1")

    def test_grok_grok_should_be_2(self):
        self.intergalatic_translator.sentences.append("how much is grok grok ?")
        self.assertEqual(self.intergalatic_translator.evaluate(), "grok grok is 2")

    def test_grok_grok_grok_should_be_3(self):
        self.intergalatic_translator.sentences.append("how much is grok grok grok ?")
        self.assertEqual(self.intergalatic_translator.evaluate(), "grok grok grok is 3")

    def test_grok_grok_grok_grok_is_not_a_valid_sentence(self):
        self.intergalatic_translator.sentences.append("how much is grok grok grok grok ?")
        self.assertEqual(self.intergalatic_translator.evaluate(), "I have no idea what you are talking about")

    def test_ruby_is_not_a_valid_material_in_a_sentence(self):
        self.intergalatic_translator.sentences.append("glob glob Ruby is 34 Credits ?")
        self.assertEqual(self.intergalatic_translator.evaluate(), "I have no idea what you are talking about")

    def test_wut_is_not_a_valid_sentence(self):
        self.intergalatic_translator.sentences.append("wut is not a valid sentence")
        self.assertEqual(self.intergalatic_translator.evaluate(), "I have no idea what you are talking about")


class TestInputProcessorComplexValues(unittest.TestCase):
    
    def setUp(self):
        self.intergalatic_translator = IntergalaticTranslator()
        self.intergalatic_translator.sentences.append("glob is I")
        self.intergalatic_translator.sentences.append("prok is V")
        self.intergalatic_translator.sentences.append("pish is X")
        self.intergalatic_translator.sentences.append("tegj is L")
        self.intergalatic_translator.sentences.append("glob glob Silver is 34 Credits")
        self.intergalatic_translator.sentences.append("glob prok Gold is 57800 Credits")
        self.intergalatic_translator.sentences.append("pish pish Iron is 3910 Credits")

    def test_pish_tegj_glob_glob_should_be_42(self):
        self.intergalatic_translator.sentences.append("how much is pish tegj glob glob ?")
        self.assertEqual(self.intergalatic_translator.evaluate(), "pish tegj glob glob is 42")
    
    def test_glob_prok_Silver_should_be_68_Credits(self):
        self.intergalatic_translator.sentences.append("how many Credits is glob prok Silver ?")
        self.assertEqual(self.intergalatic_translator.evaluate(), "glob prok Silver is 68 Credits")
    
    def test_glob_prok_Gold_should_be_57800_Credits(self):
        self.intergalatic_translator.sentences.append("how many Credits is glob prok Gold ?")
        self.assertEqual(self.intergalatic_translator.evaluate(), "glob prok Gold is 57800 Credits")
    
    def test_glob_prok_Iron_should_be_782_Credits(self):
        self.intergalatic_translator.sentences.append("how many Credits is glob prok Iron ?")
        self.assertEqual(self.intergalatic_translator.evaluate(), "glob prok Iron is 782 Credits")

    def test_glob_Gold_should_be_850_Silvers(self):
        self.intergalatic_translator.sentences.append("how many Silver is glob Gold ?")
        self.assertEqual(self.intergalatic_translator.evaluate(), "glob Gold is 850 Silver")

    def test_how_much_wood_could_a_woodchuck_chuck_if_a_woodchuck_could_chuck_wood_cannot_be_understood(self):
        self.intergalatic_translator.sentences.append("how much wood could a woodchuck chuck if a woodchuck could chuck wood")
        self.assertEqual(self.intergalatic_translator.evaluate(), self.intergalatic_translator.NO_IDEA)


if __name__ == '__main__':
    unittest.main()
