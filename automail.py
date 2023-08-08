import os
import yagmail

receiver = "anmolverma2410@gmail.com"  # receiver email address
body = "Attendence File"  # email body
i=os.listdir("FRAS/Attendance")
filename = "FRAS/Attendance"+os.sep+i[0]  # attach the file


# mail information
yag = yagmail.SMTP("clutterproj1732@gmail.com", "glmqgsdkwudboqmh")

# sent the mail
yag.send(
    to=receiver,
    subject="Attendance Report",  # email subject
    contents=body,  # email body
    attachments=filename,  # file attached
)
print("Mail Sent Successfully")
os.remove(filename)