# Chimba-Calculator
basic calculator made in Python

Autors:
  -Kevin Jaimes     - 1152245
  -Evelin Bermudez  - 1152278

the present proyect done in Python, basically is an aritmethic calculator. Which is divided into 2 classes, for a better understanding of the project one for the calculator's own logic (logic.py) and another in charge of the visualization or interface (interfaz.py)

![image](https://github.com/user-attachments/assets/63a125b0-2b15-4e9d-a0c4-815720fd6809)

# logic.py
This class, as we have indicated, contains the logic that allows the calculator to function as expected.

![image](https://github.com/user-attachments/assets/d3691385-300b-4f7f-9f82-307d38bbd7c7)

The "button_click" method, as understood by the name, is the one that defines the number or function pressed on a respective button, excluding the operation signs since its behavior is different

![image](https://github.com/user-attachments/assets/746c304b-ac22-4f51-8a2c-3697680fc036)

The "clear_all" method used when the "AC" button is pressed is expected to clear the result of the last operation, clearing the fields where we show the user said value in the last one.

As well as "calcula_result" which makes use of the method that py contains within itself "value()", but before calling it, we make sure to send it a correct value format, correcting possible symbols that can be misinterpreted as "x" in the case of multiplication, all in a try-catch to avoid failures, in possible exceptions

![image](https://github.com/user-attachments/assets/86e2ad46-cec1-4ec0-a512-5c33bdb98234)

"insert_text" is the missing piece or complement to what "button_click" does, it verifies that erroneous entries of leading zeros such as "0002" or "validate_numb" are not entered, which does not allow a different symbol than those of arithmetic operations allowed.


# interfaz.py
This class, as we have indicated, contains the graphic settings that allow the correct visualization of our "Chimba-Calculator"

![image](https://github.com/user-attachments/assets/da7678bd-f17f-46d6-8257-a23e0d949691)

We made use of the Tkinter library for the development of the graphic components, so the first thing would be to import it along with the class that contains the program logic, and define the most important method in our consideration, which are the buttons. with both functional and aesthetic parameters

![image](https://github.com/user-attachments/assets/12daf006-9f8b-4d4d-a0bc-097d348419cf)

Next we create our window with a default resolution of 600x400, and we create 2 main labels, one for the display and another for the buttons.

![image](https://github.com/user-attachments/assets/24ce1e15-42c3-46b5-bc4e-5e0cde02ca5d)

We added a text box that will serve as a "screen" to show the entered and response data respectively

![image](https://github.com/user-attachments/assets/073a1cfb-f6be-4fb8-b942-01df4dd880dc)

To create the buttons, we played with 2 3x3 arrangements to group them in some way and make the code easier to implement. Of course, certain specific conditions were added to the second arrangement since it contained a last digit and functional buttons.

![image](https://github.com/user-attachments/assets/a3012f71-64cd-4dbe-a017-a0a3da7108db)

Launch


# Screenshots
![image](https://github.com/user-attachments/assets/d5d34653-846e-429f-9234-c5f7b3cc4b66)
# 
![image](https://github.com/user-attachments/assets/785a7254-81ba-46bc-9d64-2221e705cd2f)
# 

