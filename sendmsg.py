from messaging_library import send_message

def send_class_message(sender, recipients, message):
  """
  Sends a message to a group of students in a class.

  Args:
    sender: The teacher's ID or username.
    recipients: A list of student IDs or usernames.
    message: The message content.
  """
  for recipient in recipients:
    send_message(sender, recipient, message)

# Example usage
teacher_id = "teacher123"
students = ["student456", "student789", "student101"]
message_content = "Hello students! Today's lesson is on..."

send_class_message(teacher_id, students, message_content)
