print("type in a message, and I'll display it five times.")

message = input("Message: ")
print()

n = 0 
while n < 5:
    print(f"{n + 1}. {message}") 
    n +=1
