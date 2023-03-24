# attendance Program
total_class=int(input("Enter total No. of Class"))
no_of_cls_attended=int(input("Enter classes attended "))
att_per= (no_of_cls_attended/total_class)*100
print("Your attendance % is",att_per)
if att_per<75:
    print("Not Allowed for Exam ,Your are Condonation")
else:
    print("Eligible for Exam")
