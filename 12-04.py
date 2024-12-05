meeting = "sain bnuu"
print(meeting)

a = str(input("neree oruulna uu!"))
b = int(input("nasaa oruulna uu!"))
c = float(input("unduruu oruulna uu!"))
jin = float(input("jingee oruulah!"))
er_huis = "er"
em_huis = "em"
bmi_index = jin/c**2

if bmi_index <= 18.4:
    status = 'underweight'
elif bmi_index > 18.5 and bmi_index <24.9:
    status = 'Normal'
elif bmi_index > 25.0 and bmi_index < 39.9:
    status = 'overweight'
else:
    status = 'Obese'

print(f"my name is {a}, I am {b} years old, and I am {c} undur nuruutai, minii index: {bmi_index}, minii index status:{status}")

huis = str(input("ta huisiin medeellee oruulna uu:"))
if huis == 'er':
    print("bid tand mashin uguy")
else:
    print("bid tand LV tsunh uguy")

