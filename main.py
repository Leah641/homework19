# homework19

# ask for the base and the power
x=int(input("what is the base x?"))
b=int(input("what is the power b?"))

# set the message which will be printed
message = ""

for n in range(1,b+1):
    message += str(x)+ "X"

answer = x**b
message += "="+ str(answer)

message = message.replace("X=","=")
print(message)

quit()
