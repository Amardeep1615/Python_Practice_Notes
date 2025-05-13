principal = float(input("Enter the Principal value: " ))
rate = float(input("Enter the rate value: "))
time = float(input("Enter the time "))

def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    print("\nCalcultor Details")
    print(f"principal: {principal}")
    print(f"rate: {rate}%")
    print(f" time: {time} years")
    print(f" /n SimpleInterest: {interest}")
    print(f"total amount: {principal+interest}")
calculate_interest (principal, rate, time)
