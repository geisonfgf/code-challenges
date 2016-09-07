Author: Geison Felipe Goes Flores - geisonfgf@gmail.com

Installation:

- To run this application you will need:
	- Python 2.7

Running the application:

- If you're running Linux, MacOS X or any flavour of Unix, you can run the following steps:

  ```> chmod +x financial_guide.rb```

  ```> ./intergalactic_money_conversor.py test_input.txt```

  If you don't have permission to run chmod, you can just run as follows:

  ```> python intergalactic_money_conversor.py test_input.txt```

- If you're running Windows, please install Python 2.7 from https://www.python.org/downloads/windows/ and run the command:

  ```> python intergalactic_money_conversor.py test_input.txt```

Running the tests:

- roman converter tests  
  ```> python lib/tests/roman_converter_tests.py```

- alien converter tests  
  ```> python lib/tests/alien_converter_tests.py ```

- input process tests  
  ```> python lib/tests/input_processor_tests.py```

Project Structure:

intergalactic_money_conversor  
--lib  
------__init__.py  
------intergalatic_translator.py  
------roman_converter.py
------alien_converter.py
------tests  
----------intergalatic_translator_tests.py  
----------roman_converter_tests.py
----------alien_converter_tests.py  
--intergalactic_money_conversor.py  
--README.MD  
--test_input.txt

Design:

I divided the problem presented in 4 parts:

- Convert Roman numeral to Arabic numerals
- Convert Alien numerals to Roman and so to Arabic
- Parse talk statements
- The main program responsible for read the input and print the results

I follow the S.O.L.I.D principals in all the solution, principally the Single Responsability Principle in order to easily test all parts and decouple everything.