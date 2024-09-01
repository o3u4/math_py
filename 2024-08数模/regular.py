import re

input_str = "2013.11"
pattern2 = r'(\d+).(\d+)'
item_matches = re.findall(pattern2, input_str)
print(item_matches[0])
