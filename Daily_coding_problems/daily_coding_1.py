'''

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

'''

print("Enter the list elements with space : ")
input_list  = list(map(int, input().split()))
Target = int(input("Enter the target number : "))
flag = bool
for i in input_list:
    
    temp = Target-i
    if(temp in input_list):
        flag = True
        break
    else:
        flag = False
        continue
  
print(flag)