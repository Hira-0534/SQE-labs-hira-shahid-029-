# Software Quality Engineering (SQE) - Lab

## Student Information
* **Name:** Hira Shahid
* **Roll No:** FA23-BSE-029
* **Section:** A
* **Semester:** 6th (2023-2027)
* **Task:** Lab 01 - Unit Testing & Code Coverage

---

## Week 1: Unit Testing with Pytest

### Project Overview
This week focuses on setting up a professional Python testing environment and implementing unit tests for a basic calculator module. The goal was to ensure software reliability through comprehensive test cases.

### Tasks Completed
* **Environment Setup:** Created a Virtual Environment (`.venv`) to manage project-specific dependencies.
* **Tooling:** Installed and configured `pytest` for testing and `coverage.py` for quality metrics.
* **Development:** Implemented `calculator.py` with core arithmetic operations and utility functions.
* **Testing:** Developed `test_calculator.py` including 17 test cases to handle positive, negative, floating-point, and edge cases.

### Test Coverage Results
The project achieved **100% code coverage**, ensuring every logical branch was tested.

![Test Execution & Coverage Report](image.png)

| Module | Statements | Missed | Coverage |
| :--- | :---: | :---: | :---: |
| `calculator.py` | 14 | 0 | 100% |
| `test_calculator.py` | 37 | 0 | 100% |
| **Total** | **51** | **0** | **100%** |

---

### How to Run Locally
1. **Activate Virtual Environment:**
   ```powershell
   .\.venv\Scripts\activate