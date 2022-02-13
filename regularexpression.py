import re

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
# print(lst)

message = 'The price is $10'
findm = re.findall('\$+S', message)
print(findm)