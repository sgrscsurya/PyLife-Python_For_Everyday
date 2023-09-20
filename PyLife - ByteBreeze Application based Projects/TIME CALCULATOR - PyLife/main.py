# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("11:06 PM", "2:02"))
print("\nLET'S CHECK OUT MORE EXAMPLES : \n")
print(add_time("8:16 PM", "466:02"))
print(add_time("11:59 PM", "24:05"))
print(add_time("2:44 PM", "554:08"))
print(add_time("4:00 AM", "5:00"))
print(add_time("12:00 PM", "12:00"))
print("\nThat's all! The \"Time Calculator\" is Sucessfully executed")


# Run unit tests automatically
main(module='test_module', exit=False)