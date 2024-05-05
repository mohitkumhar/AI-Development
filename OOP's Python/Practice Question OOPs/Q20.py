# 20. Create a class `Email` with attributes `sender`, `recipient`, and `content`. Add a method `send` to send the email and print a confirmation message.

class Email:
    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content
    
    def send(self):
        print(f"From: {self.sender}")
        print(f"To: {self.recipient}")
        print(f"Content: {self.content}")
        print()
        print("This Mail Has Successfully Been Send")
    
e1 = Email("mohitmolela@gmail.com", "write2mohitkumhar@hotmail.com", "Hey! I Hope This Message Finds You Well")

e1.send()
        
        


