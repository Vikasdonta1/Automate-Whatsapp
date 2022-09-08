# importing the module
import pywhatkit

# using Exception Handling to avoid
# unprecedented errors

pywhatkit.sendwhatmsg("+91xxxxxxxxxx",
						"Hello from Vikas",
						14, 15)
print("Successfully Sent!")


# handling exception
# and printing error message
print("An Unexpected Error!")
