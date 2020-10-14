# Python_Exercises
## Programs Motive


## ***Program1.py***

   Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list



## ***Program2.py***

   Convert two equal length lists into a dictionary


## ***Program3.py***

   **Leetcode :- First Program**
   
   Given an array of integers nums and and integer target, return the indices of the two numbers such that they add up to target.You may assume that each input would have exactly one solution, and you may not use the same element twice.You can return the answer in any order.
 
>Examples:

     Example 1:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Output: Because nums[0] + nums[1] == 9, we return [0, 1]
     Example 2:
        Input: nums = [3,2,4], target = 6
        Output: [1,2]
     Example 3:
        Input: nums = [3,3], target = 6
        Output: [0,1]
 
>Constraints:

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.


## ***Program4.py***

   competition between user & system generated numbers to conculde who's winner among the random numbers which generates by user , system .
   
   
## ***Program5.py***

   Program is to display least/minimum number which randomly generated by a system . 
   
   
## ***Program6.py***

   Program will display the count of value which is present in a list/array.
   
## ***Program7.py***

   **Program motive :-** There is a saying that "Data scientists spend 80% of their time cleaning data, and 20% of their time complaining about cleaning data." Let's see if you can write a function to help clean US zip code data. Given a string, it should return whether or not that string represents a valid zip code. For our purposes, a valid zip code is any string consisting of exactly 5 digits.

## ***outlook_mail_send_automation***
   **Program motive :-** Sending an automatic mail via outlook app in windows platform

   **Pre-requisite things :**
   - outlook application with email id
 
   **Program execution :** 
   - dispatching the outlook application
   - create items based on request 
   - make the receiver id (To item)
   - have the subject line for the mail initiation 
   - Write the body for the mail automation 
   - if needed any attachment you can add it 
   - then final option is to send 


## ***Masking_user_password***
   **Program motive :-** Mask the user password which user enters on screen
   
   **Pre-requisite things :**
   - pip install getpass
   - pip install stdiomask
   
   **Program Description :**
   - Masking the user password we have 2 methods which can be implemented by using the 2 packages/modules :
     * getpass
       - Where getpass module will not echo's any password which being entered by user.
     * stdiomask
       - Where stdiomask will prompts the user password as asterix or '*'.
     
  
## ***Python_package_installation_over_cmd***
   **Program motive :-** Installing the required packages automatically via command prompt 
  
   **Pre-requisite things :**
   - Prerequisite file is package_files from another PC who has installed python on his/her system & with some extra packages/modules .
to get the all lists of packages list into a text file , just type " pip freeze > 'file_name.txt' " on your cmd/terminal.

   **Program Description :** 
   - Importing OS module , to run cmd with each package_name which is stored in a <python_packages.txt> file, os.system(command) #which results into a cmd with command
  
   **Useful commands of pip:**
    pip is a package manager for Python packages. When we install pip, it is added to the system as a command line program which can be run from the command line. We not only use pip to install and uninstall Python packages, it is rather a great tool to create Python virtual environment.
    
    - pip search <package_name>
            The above command useful to search a details/content about particular package which is installed on our machine. 
            
    - pip install <package_name>
            The above command useful to install new package onto our machine.
                     
    - pip install --no-cache-dir <package_name> 
            The above command will do the installation from the python package server , not from cache storage which is present on our machine.
         
    - pip show <package_name>
            The above command is usefull when we wanted to know the full info about a specific installed package.
            
    - pip uninstall <package_name>
            The above command useful to uninstall the installed package from our machine.
           
    - pip list
            The above command will list out all installed packages which is present at our machine.
            
    - pip freeze 
            The above command is also does the similar action as pip list does.
           
    - pip install -r <path_to_file>
            The above command will do the installation of each package & version from the file which user will specifies <path_to_file>.
     
   ![Difference of show and search](/Python_package_installation_over_cmd/Capture.PNG)**   
    

## ***FizzBuzz***

   **Program Description :** 
   - Program has to print 'Fizz' for the multiple of 3's , and should print 'Buzz' for the multiple of 5's
and if a number which is multiple of both 3&5 then it should print 'FizzBuzz'.
if not the program has to print number itself .

## ***Daily_coding_problems***

   **daily_coding_1.py**
   - Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
   
   **daily_coding_2.py**
   - Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6]
   
   **daily_coding_4.py**
   - Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, 
find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3


## ***reverse_number_verification or palindrome checks***

The program will ask user to enter a integer number , and will check the reverse of it is same as original or not.

## ***Swap list***

The program will do the swapping of 2 lists which is been provided by user .
   
## ***factorial_calculation***
   
Program will ask user to give input integer number to get a its equivalent factorial number .

## ***switch_case_implementation*** 

Switch_case_statement implemention as like as in C. 

using dictionary , we can declare 'n' number of operation or condition 
& we can use it as like a swicth case statement which C language & other language supports.
        
    Parameters
    ----------
    operator : TYPE -> String
        DESCRIPTION -> with help of operator the function will returns its operation. 
    num1 : TYPE -> int
        DESCRIPTION -> a integer number to do all mathematical operations
    num2 : TYPE -> int
        DESCRIPTION -> a integer number to do all mathematical operations

    Returns
    -------
            the function returns the expresions/operations from 2 input numbers with help of operator variable.
            

## ***integer_to_roman_conversion*** 

Program will do the conversion of real integers to equivalent roman numerals:
- it will ask user to enter the integer number.
- it will display its equivalent roman numerals


## ***quick_sort_algorithm***

Program will do the sorting algorithm on the list with out using an inbuilt 'list.sort()' method.

- it will ask the number of elemnents  to be present in a list 
- it will ask you enter the elements till hits the count of final (*step 1 result)
- program will displays the list before & after sorting algorthim .

## ***max_out_of_integers***

program will ask the user to enter one integer number & also ask user to enter one more digit number . 
where the second user input digit will be inserting into each start + end position of digits in the first user input number , prints out the max one .

>Example:

     input = 1234 
     given number = 9 
     output= 12349 , 12394, 12934, 19234,91234
     max_output = 91234
   

## ***student_ranking_series***

- The first python file is 'input_file_creation.py' will creates a student database by getting all required information fro user , if user doesnot know the name of a student & his/her subjects , then it will consider the defaults names into a 'student_database.txt' file.

- So after execution of 'input_file_creation.py' will get 'student_database.txt' file in this way:

   Student_name-[series],subject_name-[marks],subject_name-[marks],subject_name-[marks]
  
- Then we will use the above 'student_database.txt' file to create 'student_database_ranking.txt' file by using 'output_file_creation.py' file.
- So after execution of 'output_file_creation.py' will get 'student_database_ranking.txt' file in this way:

   Student_name-[series],subject_name-[marks],subject_name-[marks],subject_name-[marks],Total_marks-[total_score],Rank-[rankseries]

     **One more assumption that user have one input.txt file which contains students name , and his/her marks of 3 subjects , program has to find out his/her total marks & his/her rank series among all the other students.**

***Things:***
* main program is :- rank_series_calculation.py
* input file is :- input.txt
* output file is :-  output.txt

input.txt file looks like below :

![input_txt file](/student_ranking_series/input_txt.PNG) 




output.txt file should looks like below:

![output_txt file](/student_ranking_series/output_txt.PNG)




    
    
