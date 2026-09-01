# EGN 321 — Module 1 Defect Report

## Student Information
- **Name:**Renato Jacinto
- **Student ID:**RJ05348
- **Date:**09/01/26

## Workbook Reviewed
- **Workbook:** `TANK_FILL_rev4.xlsx`
- **Worksheet(s) Reviewed:**

## 1. Workbook Purpose
Explain what the workbook appears to calculate, its inputs, and its final output.

## 2. Defect Summary

| # | Location | Defect | Correct Behavior | Impact | Confidence |
|---|---|---|---|---|---|
| 1 |  |  |  |  | High / Medium / Low |
| 2 |  |  |  |  | High / Medium / Low |
| 3 |  |  |  |  | High / Medium / Low |

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
The values now are clear without leaving a doubt when calculating

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
If it were fix, the TOTAL RECORDED VOLUME will be different

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
30.0 ft
### Impact on the Result
The values now are clear without leaving a doubt when calculating

### Estimated Age of the Defect
Unknown; the defect is present in the current inherited rev4 workbook, but its exact age cannot be determined.

### Verification
Calculating 2.5ft * 12

## 6. Additional Suspected Defects
### Location
- **Worksheet:** Field Notes
- **Cell/Range:** C3-E3

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
Confirm that the measurement cells are numeric using ISNUMBER(C4). It should return TRUE after correction.

## 7. Overall Assessment
Would you trust this workbook for a real engineering decision? Explain.
I would use this workbook only as an unverified draft. Before relying on it, I would correct the formulas and units, reconcile the data with the original field measurements, document the conversions, and have another engineer independently review the calculations.


## 8. What Should Become a Python Test?
1.
2.
3.
