import gn_lib3.jolse_parser as parser
import gn_lib3.save_to_file as saver

file = open("./jolse_01.html")

result = parser.parse(file.read())
print("=>",result)
print(len(result))

saver.saveToFile(result, "./jolse_01.csv")
