import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("nehasparks2@gmail.com", "sparks@2")

# message to be sent
message = "nothing bro"

# sending the mail
s.sendmail("nehasparks2@gmail.com", "nehasparks2@gmail.com", message)

# terminating the session
s.quit()