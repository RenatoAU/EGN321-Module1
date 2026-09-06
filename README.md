# EGN 321 — Module 1 Repository

## Student
- **Name:**Renato Jacinto
- **Student ID:**RJ05348

## Project
Module 1 — The Inherited Workbook

## Repository Structure
```text
EGN321-Module1/
├── README.md
├── DEFECTS.md
├── AI_LOG.md
├── original/
│   └── TANK_FILL_rev4.xlsx
├── src/
└── tests/
```

## Module 1 Status
- [x] Manual workbook inspection complete
- [x] `DEFECTS.md` complete
- [x] Original artifact preserved
- [x] Python rebuild started
- [x] Tests added
- [x] AI use documented where applicable

## Commits
git add README.md DEFECTS.md AI_LOG.md requirements.txt
git commit -m "Document workbook evidence and project scope"

git add src/tank_fill.py
git commit -m "Implement named-constant tank volume functions"

git add tests/test_tank_fill.py
git commit -m "Add workbook reference and regression tests"

python -m pip install -r requirements.txt
pytest

git add README.md DEFECTS.md AI_LOG.md
git commit -m "Document verification assumptions and limitations"
