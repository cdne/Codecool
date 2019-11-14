def import_calendar(file_name):
  with open(file_name, 'r') as file:
    content = file.read()
  return content

print(import_calendar('calendar.txt'))
