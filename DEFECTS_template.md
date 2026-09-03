# EGN 321 — Module 1 Defect Report

## Student Information
- **Name:**Renato Jacinto
- **Student ID:**RJ05348
- **Date:**09/01/26

## Workbook Reviewed
- **Workbook:** `TANK_FILL_rev4.xlsx`
- **Worksheet(s) Reviewed:** Tank Fill and Field Notes

## 1. Workbook Purpose
Explain what the workbook appears to calculate, its inputs, and its final output.

The workbook records tank measurements and calculates the tank volume in U.S. gallons. The inputs include tank length and width in feet and depth readings in inches. The Tank Fill worksheet converts the depth from inches to feet, calculates cubic feet, converts the result to U.S. gallons, and reports individual volumes and the total recorded volume.

## 2. Defect Summary
| # | Location         | Defect                                                          | Correct Behavior                                 | Impact                                                                         | Confidence |
| - | ---------------- | --------------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------ | ---------- |
| 1 | Tank Fill!G6:G23 | Hard-coded conversion factors are not labeled or documented.    | Use labeled conversion cells or named constants. | No immediate numerical error, but auditing and maintenance are more difficult. | Medium     |
| 2 | Tank Fill!G25    | Formula sums only G6:G17.                                       | Formula should be `=SUM(G6:G23)`.                | The total excludes the volumes in G18:G23.                                     | High       |
| 3 | Field Notes!E11  | Depth is entered as 2.5 ft while other depth values use inches. | Store the value as numeric 30.0 inches.          | Creates unit inconsistency and possible conversion errors.                     | High       |

## 3. Defect 1
### Location
- **Worksheet:** Tank Fill
- **Cell/Range:** G6-G23

### Existing Formula or Value
"/12" "7.48052"

### Problem Identified
The formulas in Tank Fill!G6:G23 contain the hard-coded values 12 and 7.48052. The value 12 represents the number of inches in one foot, and 7.48052 represents US gallons per cubic foot. The calculation is mathematically correct, but these conversion factors should be documented or stored in labeled cells so the formula is easier to audit.

### Why This Is a Defect
When somebody try to figure out the values, it does't undertood the calculation or convertion 

### Correct Formula, Value, Range, or Unit
depth_ft = depth_in / 12
US gallons = cubic_ft * 7.48052 
### Impact on the Result
The current calculation does not produce an immediate numerical error. However, the hard-coded conversion factors make the workbook more difficult to audit and increase the risk of future editing or interpretation errors.

### Estimated Age of the Defect
Unknown; the defect is present in the current inherited rev4 workbook, but its exact age cannot be determined.

### Verification
Manually verify one row: 10 × 6 × (8 ÷ 12) × 7.48052 = 299.2208 gallons, which matches cell G6.

## 4. Defect 2
### Location
- **Worksheet:** Tank Fill
- **Cell/Range:** G25

### Existing Formula or Value
=SUM(G6:G17)

### Problem Identified
The formula don't covert all values calculated previously.

### Why This Is a Defect
It is a defect because the TOTAL RECORDED VOLUME should be the sum of every value.

### Correct Formula, Value, Range, or Unit
This formula excludes the calculated values in G18:G23. The correct formula is:
=SUM(G6:G23)
### Impact on the Result
The total recorded volume is understated by the sum of the values in G18:G23 because those six calculated volumes are excluded.

### Estimated Age of the Defect
Unknown; the defect is present in the current inherited rev4 workbook, but its exact age cannot be determined.

### Verification
Confirm that G25 contains =SUM(G6:G23) and compare the result with a manual sum of cells G6:G23.

## 5. Defect 3
### Location
- **Worksheet:** Field Notes
- **Cell/Range:** E11

### Existing Formula or Value
2.5 ft

### Problem Identified
Field Notes!E11 contains 2.5 ft, while the other depth readings use inches. Since 2.5 ft equals 30.0 in

### Why This Is a Defect
You cannot enter two different values ​​in the same column, knowing that the column already has a specific unit.

### Correct Formula, Value, Range, or Unit
30.0 in
### Impact on the Result
The values now are clear without leaving a doubt when calculating

### Estimated Age of the Defect
Unknown; the defect is present in the current inherited rev4 workbook, but its exact age cannot be determined.

### Verification
Calculating 2.5 ft * 12

## 6. Additional Suspected Defects
### Location
- **Worksheet:** Field Notes
- **Cell/Range:** Field Notes!C3:E21

### Existing Formula or Value
Length | Width | Depth Reading

### Problem Identified
Measurements such as "10.0 ft", "6.0 ft" and "8.0 in" are stored as text with the unit included, instead of numeric values.

### Why This Is a Defect
These cells cannot be used directly in calculations. A program or formula must first separate the number from the unit, which increases the risk of conversion errors like R-108.

### Correct Formula, Value, Range, or Unit
Store the number separately and keep the unit in the header:
Length (ft) : 10.0
Width (ft) : 6.0
Depth:(in) : 30.0
### Impact on the Result
More reliable calculations and easier automated analysis.

### Estimated Age of the Defect
Unknown; the defect is present in the current inherited rev4 workbook, but its exact age cannot be determined.

### Verification
Because the depth column uses inches, E11 should contain the numeric value 30.0, with the unit specified in the header. The conversion is:

2.5 ft × 12 in/ft = 30.0 in.

## 7. Overall Assessment
Would you trust this workbook for a real engineering decision? Explain.
I would use this workbook only as an unverified draft. Before relying on it, I would correct the formulas and units, reconcile the data with the original field measurements, document the conversions, and have another engineer independently review the calculations.


## 8. What Should Become a Python Test?
### 1. Volume calculation test
Python should independently calculate the expected gallons for every row in Tank Fill!G6:G23:

expected = length_ft * width_ft * (depth_in / 12) * 7.48052
assert actual_volume == expected

For G6:

assert 299.2208 == 10 * 6 * (8 / 12) * 7.48052

### 2. Total volume test
Python should verify that G25 includes all calculated volumes from G6:G23:

volumes = [value_g6, value_g7, value_g8, ......., value_g23]  
expected_total = sum(volumes)
assert total_G25 == expected_total
assert formula_G25 == "=SUM(G6:G23)"

The test should fail if the formula only sums G6:G17.

### 3. Unit and data-type test
Python should verify that depth values are numeric and stored in inches:

e11_inches = 2.5 * 12
assert e11_inches == 30.0
assert unit == "in"

The test should pass only when Field Notes!E11 is stored as numeric 30.0 inches, not as "2.5 ft".

In Python, assert means: if the condition is true, the test passes; if it is false, the test identifies a defect.
