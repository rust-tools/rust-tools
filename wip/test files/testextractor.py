def search(file_path, id_type, item_name):
    with open(file_path, 'r') as file:
      if id_type != ("items" or "buildingBlocks" or "other"):
        print("Invalid id_type")
    

def searchData(file_path, search_string):
  with open(file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
      if search_string in line:
        return line_number
  return -1


def printFullData(file_path, line_number, num_lines_before, num_lines_after):
  with open(file_path, 'r') as file:
    lines = file.readlines()
    start_line = max(0, line_number - num_lines_before - 1)
    end_line = min(len(lines), line_number + num_lines_after)
    for line in lines[start_line:end_line]:
      print(line.strip())


file_path = "test.json"
search_string = "-295829489"
line_number = searchData(file_path, search_string)
if line_number != -1:
  print(f"The search ID '{search_string}' is found at line number: {line_number}")
  print("The full ID data is: ")
  printFullData(file_path, line_number, 3, 8)
else:
  print(f"The search ID '{search_string}' is not found.")