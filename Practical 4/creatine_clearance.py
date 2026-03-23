# Step 1: input variables
try:
    age = int(input("Please enter age (years): "))
    weight = float(input("Please enter weight (kg): "))
    cr = float(input("Please enter creatinine concentration (μmol/l): "))
except ValueError:
    print("Error: age, weight, and creatinine concentration must be numeric values!")
    exit()

# Gender selection (1 = male, 2 = female)
gender_input = input("Please select gender (1 = male, 2 = female): ")

# Convert to gender string
if gender_input == "1":
    gender = "male"
elif gender_input == "2":
    gender = "female"
else:
    gender = "invalid"

# Step 2: validity check
is_valid = True
error_message = "Variables to correct: "

if age >= 100:
    is_valid = False
    error_message += "age (must be < 100), "

if weight <= 20 or weight >= 80:
    is_valid = False
    error_message += "weight (must be 20 < weight < 80), "

if cr <= 0 or cr >= 100:
    is_valid = False
    error_message += "creatinine concentration (must be 0 < Cr < 100), "

if gender == "invalid":
    is_valid = False
    error_message += "gender (must be 1 or 2), "

# Step 3: error output
if not is_valid:
    error_message = error_message[:-2]
    print(error_message)

# Step 4: calculate CrCl
else:
    if gender == "female":
        crcl = ((140 - age) * weight) / (72 * cr) * 0.85
    else:
        crcl = ((140 - age) * weight) / (72 * cr)

    # Step 5: output result
    print("Creatinine Clearance (CrCl):", round(crcl, 2), "ml/min")