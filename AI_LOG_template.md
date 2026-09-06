# AI Usage Log

## EGN 321 — Module 1

AI was used after the workbook inspection to help organize the Python rebuild, tests, and documentation.

## Interaction 1

* Tool: ChatGPT
* Date: 09/06/26
* Prompt: After completing my manual audit of `TANK_FILL_rev4.xlsx`, help me plan a pure Python rebuild with named constants, validation, pytest tests, documentation, and meaningful Git commits.
* What the tool returned: The tool suggested using a pure calculation function, named constants for the conversion factors, validation for invalid measurements, pytest reference tests, a regression test for the incorrect total formula, and documentation for units and limitations.
* What I used: I used the suggested project structure, function organization, test categories, and documentation topics.
* What I changed: I used my own workbook evidence, including rows R-101 and R-113. I also used the defects I identified: unexplained conversion constants, the incorrect G25 total formula, and the R-108 unit inconsistency.
* Why I changed it: The AI suggestions were general. I changed the examples and expected results to match the actual workbook.
* How I verified it: I compared the expected values with the workbook formulas and cached results. I also ran `pytest` and reviewed the source code manually.

## Verification Statement

AI did not replace the manual workbook inspection. The workbook formulas, units, defects, and expected values were checked against the original workbook before being used in the Python tests.
