# Pseudocode: Creatinine Clearance (CrCl) Calculator
# 1. Define input variables: age, weight (kg), gender, creatinine concentration (Cr, μmol/l)
# 2. Input validity check rules:
#    - Age < 100 years old
#    - Weight: 20kg < weight < 80kg
#    - Creatinine concentration: 0 < Cr < 100 μmol/l
#    - Gender: only "male" or "female" (lowercase)
# 3. Validation logic: Check each variable against rules one by one, 
#    print error message if any variable is invalid (specify which one needs correction)
# 4. If all inputs are valid, calculate CrCl based on gender
# 5. Output the final CrCl result

# Actual code: Define test variables (modify values to test valid/invalid scenarios)
try:
    age = int(input("Please enter age (years): "))
    weight = float(input("Please enter weight (kg): "))
    Cr = float(input("Please enter creatinine concentration (μmol/l): "))
except ValueError:
    print("Error: Age/weight/Cr must be numeric values!")
    exit()

# Get gender input
gender = input("Please enter gender (male/female): ").lower()  # Convert to lowercase automatically

# Initialize error flag
is_invalid = False
error_msg = "Variables to correct: "

# Validity check
if age >= 100:
    is_invalid = True
    error_msg += "age (must be < 100), "
if weight <= 20 or weight >= 80:
    is_invalid = True
    error_msg += "weight (must be 20 < weight < 80), "
if Cr <= 0 or Cr >= 100:
    is_invalid = True
    error_msg += "creatinine concentration (must be 0 < Cr < 100), "
if gender not in ["male", "female"]:
    is_invalid = True
    error_msg += "gender (only 'male' or 'female' allowed), "

if is_invalid:
    # Remove the last comma and space
    error_msg = error_msg[:-2]
    print(error_msg)
else:
    # Calculate CrCl using Cockcroft-Gault formula
    if gender == "female":
        crcl = ((140 - age) * weight) / (72 * Cr) * 0.85
    else:
        crcl = ((140 - age) * weight) / (72 * Cr)
    # Output result with 2 decimal places
    print(f"Creatinine Clearance (CrCl): {crcl:.2f} ml/min")