
# Project 1: Real-Time Mean Tracker (Data Streaming)
# Kyun banayein: AI engineers ko continuously aane wale data (sensors, logs) ka average nikalna padta hai bina system ko roke.

# Aapka Task: Ek aisa program likho jo user se continuously numbers mangta rahe. Har naye number ke baad, ab tak daale gaye saare numbers ka Average (Mean) calculate karke print kare.

# Rules:

# Ek while True loop lagana hai.

# User input ko track karne ke liye do variables pehle hi bana lene hain: ek total sum ke liye, aur ek count (kitne numbers daale) ke liye.

# Agar user number ki jagah exit type kare, toh loop break ho jana chahiye aur final average print hona chahiye.

# Expected Output Flow:

# Enter number: 10
# Current Average: 10.0
# Enter number: 20
# Current Average: 15.0
# Enter number: exit
# # Program Stopped. Final Average is 15.0

total_sum = 0.0
count = 0

print("Live Data Stream Tracker")
print("Type 'exit' to stop the loop.")

while True:
    user_input = input("Enter a data point (number): ")
    
    if user_input == "exit":
        print("Exiting tracker...")
        break
        
    # User input ko float (decimal) mein convert kar rahe hain
    data_point = float(user_input)
    
    # Sum aur count update karo
    total_sum = total_sum + data_point
    count = count + 1
    
    # Mean calculate karke print karo
    current_mean = total_sum / count
    print("Current Mean (Average):", current_mean)
    print("--- Data Points Processed:", count)


