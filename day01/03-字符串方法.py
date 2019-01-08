string01 = "hello world"
string02 = "HELLO"

print(string01.capitalize())
print(string02.casefold())
print(string02.lower())
print(string02.center(20, "*"))
print(string02.center(20))
print(string02.ljust(20, "*"))
print(string02.rjust(20, "*"))
print(string02.zfill(20))
print(string01.count("l"))
print(string01.count("l", 3))
print(string01.count("l", 3, 8))
print(string01.endswith("d"))
print(string01.startswith(string02))
print(string01.find("l", 4))

string03 = "I love {fruit}!"
string04 = string03.format(fruit="mongo")
print(string04)

string05 = "my name is {name}, age {age}"
string06 = string05.format_map({"name": "ksm", "age": 18})
print(string06)

print(string01.index("e"))

string07 = "hello123_"
print(string07.isalnum())

string08 = "username\temail\tpassworld\nksm\tksm@163.com\t123456\nksm\tksm@163.com\t123456\nksm\tksm@163.com\t123456\n"
string09 = string08.expandtabs(20)
print(string09)

string10 = "abcdef"
string11 = "abcde6"
string12 = "123456"
string13 = "二"
print(string10.isalpha())
print(string11.isalnum())
print(string12.isdecimal())
print(string12.isdigit())
print(string13.isnumeric())

string14 = "abcd\tef"
print(string14.isprintable())
string15 = "  "
print(string15.isspace())
string16 = "Process finished with exit code"
print(string16.istitle())
string17 = string16.title()
print(string17)
print(string17.istitle())

string18 = "你是风儿我是沙"
print(" ".join(string18))

string19 = "Kasumy"
print(string19.islower())
print(string19.lower())
print(string19.isupper())
print(string19.upper())

string20 = "\nkasumy\t"
print(string20.strip())
print(string20.lstrip())
print(string20.rstrip())

string21 = "wo jiu sui bian xie le yi ju hua"
string22 = str.maketrans("aeiou", "12345")
string23 = string21.translate(string22)
print(string23)

string24 = string21.partition("i")
print(string24)
string25 = string21.rpartition("i")
print(string25)
string26 = string21.split("i")
print(string26)
string27 = string21.rsplit("i")
print(string27)
string28 = string21.rsplit("i", 1)
print(string28)

string29 = "fdsa\nadfhlsh\nhdfsal"
res01 = string29.splitlines()
print(res01)
res02 = string29.splitlines(True)
print(res02)

string30 = "version 1.1.1"
res03 = string30.startswith("ver")
print(res03)
res04 = string30.endswith("1.1")
print(res04)

string31 = "Ksm"
res05 = string31.swapcase()
print(res05)

string32 = "ksmksmksmksm";
res06 = string32.replace("s", "y", 3)
print(res06)

############ 6个基本的 ############
# join
# split
# find
# strip
# upper
# lower
# replace
