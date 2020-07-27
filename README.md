# Arithmetic-Formatter
* It is a function named solve which takes a required parameter and an optional parameter.
* The required parameter named problems is a list of arithmetic problems (only addition and subtraction).
* The optional parameter named choice is a boolean. If True, the function prints answers to the problems otherwise not.
* The problems are not more than 5. 
* The operands are not more than 4 digits long and consist of digits only.
* This function arranges the problems in a vertical format and prints them (With answers if choice is True).
```
solve(["23 + 456","4589 - 568","45 + e5"])
OUTPUT: Error: Numbers must only contain digits.

solve(["23 + 456","4589 - 568","4545 + 5"])
OUTPUT: 
  23	  4589	4545
  +456	-568	+5
  -----	-----	-----

solve(["23 + 456","4589 - 568","4545 + 5"],True)
OUTPUT:
  23	  4589	4545
  +456	-568	+5
-----	-----	-----
  479	  4021	4550
```
