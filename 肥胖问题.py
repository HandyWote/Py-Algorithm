m,h = map(float,input().split())
bmi = m/(h**2)
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24:    
    print("Normal")
elif 24 <= bmi:
    print("{:.6g}".format(bmi))
    print("Overweight")
