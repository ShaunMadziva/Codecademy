class Message:
  def __init__(self, sender, recipient, text):
    self.sender = sender
    self.recipient = recipient
    self.text = text

class User:
  def __init__(self, username):
    self.username = username
    
  def edit_message(self, message, new_text):
    if message.sender == self.username:
      message.text = new_text

#Override User‘s .edit_message() method so that an Admin can edit any messages.
class Admin(User):
 def edit_message(self, message, new_text):
   message.text = new_text

   