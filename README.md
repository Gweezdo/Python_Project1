# Python_Project1
edx assignment - adding_report() function

| Some Assignment Requirements |
|:-------------------------------|
|This program requires the use of<ul><li>**`while`** loop</li><li>**`if, elif, else`**</li><li>**`if,else`** (nested)</li><li>**casting** of type,  between strings and numbers</li></ul><br/>The program should **only** use code syntax covered in modules 1 - 4.<br/><br/>The program must result in print output using the numeric input, similar to that shown in the samples displaying "Items" and "Total".  |


## Program: `adding_report()` function  
This program calls the adding_report() function which repeatedly takes positive integer input until the user quits and then sums the integers and prints a "report".    
The **adding_report()** function has 1 string parameter which indicates the type of report:  
- "A" used as the argument to adding_report() results in printing of all of the input integers and the total  
- "T" used as the argument results in printing only the total   

#### Sample input and output:  
call adding_report() with "A" as argument (print all the integers entered and the total)  
```
Input an integer to add to the total or "Q" to quit
Enter an integer or "Q"): 3
Enter an integer or "Q"): 6
Enter an integer or "Q"): 24
Enter an integer or "Q"): 17
Enter an integer or "Q"): 61
Enter an integer or "Q"): nine
nine is invalid input
Enter an integer or "Q"): q

Items
3
6
24
17
61

Total
 111
```  

call with "T"(print only the total)  
```
Input an integer to add to the total or "Q" to quit
Enter an integer or "Q": 5
Enter an integer or "Q": 7
Enter an integer or "Q": Quit

Total
 12
```  

### The forever (while True) loop diagram  
This diagram represents only part of the assignment - it is the loop and nested if statements inside the function.  The code will enter at the while True loop after initializing variables.  

![image of while True Loop with nested if statements described in bulleted text above](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/adding_report_loop_sketch.png)

### Additional Details
  
- initialize `total` variable which will sum integer values entered  
- initialize `items` variable which will build a string of the integer inputs separated with a *new line character*  
- define the `adding_report` function with one parameter `report` that will be a string with default of "T"  
- inside the function build a forever loop (infinite while loop) and inside the loop complete the following  
  - use a variable to gather input (integer or "Q")  
  - check if the input string is a digit (integer) and if it is...  
    - add input iteger to total  
    - if report type is "A" add the numeric character(s) to the item string seperated by a new line  
  - if not a digit, check if the input string is "Q" or starts with a "Q", **if "Q"** then...  
    - if the report type is "A" print out all the integer items entered and the sum total  
    - if report type is "T" then print out the sum total only  
    - `break` out of while loop to end the function after printing the report ("A" or "T") 
  - if not a digit and if not a "Q" then print a message that the "input is invalid"  

- Call the `adding_report` function with "A" and then with "T" report parameters  
- Run and test your code before submitting