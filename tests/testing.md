# ✅ Testing Guide

This project includes unit tests for the data cleaning functions, ensuring correctness in email validation, country standardization, and age imputation.

## 🧪 Test Location

📁 All tests are placed in the `tests/` folder.  

```
tests/
└── test_cleaning.py   # Unit tests for cleaning functions
```

## ▶️ How to Run Tests

1. Make sure you have `pytest` installed. You can install it via pip if you don’t have it yet:

```bash
pip install pytest
```
2. Run tests from the root directory of the project:

```bash
pytest
```

3. To run a specific test file, use:

```bash
pytest tests/test_cleaning.py
```


## 🧹 What is Tested?

The tests cover important cleaning functions such as:

- **Email validation**: ensures only valid emails pass.
- **Country standardization**: maps various country name variants to a standard name.
- **Age imputation**: fills missing ages with the median and converts to integers.

## 💡 Why Use Tests?

- To ensure your data cleaning logic is working correctly.
- To avoid regressions when you modify or extend your code.
- To increase confidence in your pipeline’s robustness.

## ➕ How to Add More Tests?

- Create additional test functions inside the `tests/test_cleaning.py` or separate files under `tests/`.
- Use descriptive test names starting with `test_`.
- Test edge cases and invalid inputs as well.

---

Happy testing! 🚀
