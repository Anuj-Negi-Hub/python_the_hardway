"""
Create a program that prompts for your age and your resting heart rate.
Use the Karvonen formula to determine the target heart rate based on a range of intensities from 55% to 95%.
Generate a table with the results as shown in the example output. 
The formula is TargetHeartRate = (((220 - age) - restingHR) x intensity) + restingHR

Example Output
Resting Pulse: 65 Age: 22
Intensity | Rate
-------------|--------
55% | 138 bpm
60% | 145 bpm
65% | 151 bpm
: : (extra lines omitted)
85% | 178 bpm
90% | 185 bpm
95% | 191 bpm
"""

age = int(input("Type your age: "))
rest_pulse = int(input("Type the resting pulse: "))
exer_inten = int(input("Type the intensities between 55 to 95: "))
# exact_inten = exer_inten / 100

#formula to calculate targett heart rate
# heart_rate = (((220 - age) - rest_pulse) * exact_inten) + rest_pulse


print("Intensity | Rate")
print("----------|--------")

if exer_inten >= 55 and exer_inten <= 95:
    while exer_inten >= 55 and exer_inten <= 95:
        exact_inten = exer_inten / 100
        #formula to calculate target heart rate
        heart_rate = (((220 - age) - rest_pulse) * exact_inten) + rest_pulse
        print(f"{exer_inten}%       |     {heart_rate:.0f} bpm")
        exer_inten += 5
else:
    print("Type the correct intensity value.")

# print(heart_rate)