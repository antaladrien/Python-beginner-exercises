def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  f"Result: {formated_f_name} {formated_l_name}"

formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)

print(format_name(input("What is your first name? "), input("What is your last name? ")))

length = len(formatted_name)

def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Result: {formated_f_name} {formated_l_name}"

