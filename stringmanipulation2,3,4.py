# 2. Write a program to fill in a letter template given below with name and date. 
# letter = '''  
# Dear <|Name|>, 
# You are selected! 
# <|Date|> 
# '''
letter = '''  
Dear   <|Name|>, 
You are  selected! 
<|Date|>   
''' 
b=letter.replace("<|Name|>","Aditya").replace("<|Date|>","7th january 2026")
print(b)

# 3. Write a program to detect double space in a string.
print(letter.count("  "))

# 4. Replace the double space from problem 3 with single spaces. 
print(letter.replace("  "," "))