#---------------#
import re

print("It for re.search()")
text = "I am a good boy"
pattern = r"good"
search = re.search(pattern, text)

if search:
    print("Match found:", search.group()) #returns the actual matched text from the string
else:
    print("Pattern Not Found")

#------------------#
import re

print("it is for re.match()")
text = "quick The brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")

#-------------------#
import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)

#------------------#
import re

text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)
