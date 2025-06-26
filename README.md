# Thoughtful FDE Technical Screen – Package Sorter

## Problem Statement

Implement a Python function to sort packages into the correct stack based on their dimensions and mass, following these rules:
- A package is **bulky** if its volume (Width x Height x Length) is ≥ 1,000,000 cm³ or any dimension is ≥ 150 cm.
- A package is **heavy** if its mass is ≥ 20 kg.
- **STANDARD**: Not bulky or heavy.
- **SPECIAL**: Bulky or heavy (but not both).
- **REJECTED**: Both bulky and heavy.

## Solution Approach

The `sort` function takes four arguments (width, height, length in cm, and mass in kg), validates input, and applies the rules above. It uses clear logic and a ternary operator as required. Edge cases and invalid input are handled robustly, and the function is fully tested.

## How to Run

1. Clone this repository.
2. (Optional) Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install pytest
   ```
4. Use the `sort` function in `sort.py` as needed.

## How to Test

Run all tests with:
```sh
pytest -v
```
All tests should pass.

## File Structure

- `sort.py` – Main function implementation.
- `test_sort.py` – Automated tests using pytest.

## Assumptions & Edge Cases

- All dimensions and mass must be positive numbers.
- The function raises `ValueError` for invalid input (non-numeric or non-positive values).
- Edge cases (thresholds, invalid input) are covered by tests.

---

For any questions or feedback, please contact the repository owner. 