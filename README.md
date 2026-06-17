# QA Automation Test Task

## Task 1: Algorithm
The implementation of the algorithms can be found in the `main.py` file. It handles single numbers, specific names, and numeric arrays dynamically (according to the given requirements).

---

## Task 2: Bracket Sequence Analysis

**Given sequence:** `[((())()(())]]`

### 1. Can this sequence be considered correct?
**No**, this sequence is incorrect (unbalanced).

### 2. What needs to be changed to make it correct?
The internal round brackets `((())()(()))` are balanced and correct. The sequence fails because of the outer square brackets: it opens with a single `[` but closes with a double `]]`. 

To make it correct, you can apply one of the following two options:

* **Correction Option 1 (Remove the extra character):** Remove one closing square bracket from the very end to match the single opening bracket.
    * **Corrected format:** `[((())()(()))]`

* **Correction Option 2 (Add the missing character):** Add an opening square bracket at the very beginning to match the double closing brackets at the end.
    * **Corrected format:** `[[((())()(()))]]`
