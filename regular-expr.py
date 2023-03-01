import re

query = input("Send your query: ")
search_tag = input("Enter product tag: ")

# Query
compile = re.compile(query)
string = "Do you sell any cosmetic product in your shop?"
check_match = compile.match(string)
check_find_all = compile.findall(string)
print(check_match)
print(check_find_all)

# Tag
keyword = ['cosmetics', 'organics']
compile_kw = re.compile(keyword[0])
check_kw = compile_kw.match(search_tag)
print(check_kw)
