# Requirements, Acceptance Criteria, Test Cases

# Test Plan

## Index
1. [Requirements](#requeriments)
    1. [Process Requirements](#process-requirements)
    2. [Functional Requirements](#functional-requirements)
    3. [Non-Functional Requirements](#non-functional-requirements)
2. [Acceptance Criteria](#acceptance-criteria)
3. [Test Cases](#test-cases)
    1. [End-To-End Testing](#end-to-end-testing)
    2. [Unit Testing](#unit-testing)

## Requirements

### Process Requirements

* **Proc-Req-1:** The software shall be developed using Python 3.10.4.

* **Proc-Req-2:** The software shall be tested using unittest module.

### Functional Requirements

* **Func-Req-1:** The software must convert arabic numbers to roman numerals.

* **Func-Req-2:** The software must ask to the user for a number after giving a welcome message.

* **Func-Req-3:** If the input is not an arabic number, the software must tell the user the problem and to ask them to try again.

* **Func-Req-4:** If the input is an arabic number, the software must be able to convert it into roman numeral and tell the user *< arabic number > = < roman number >*

### Non-Functional Requirements

* **NF-Req-1:** The software must work on Linux Ubuntu 22.

* **NF-Req-2:** The software learning time must be inmediately.

* **NF-Req-3:** The software must execute one conversion at a time.

## Acceptance Criteria

The software must comply with the roman numerals rules, which are:

* **Cri-1:** The letters must be in upper case.

* **Cri-2:** A letter should not repeat itselft more than three times.

* **Cri-3:** When a letter is followed by another one of less than or equal value, these values must be added.

* **Cri-4:** When a letter (except V, L and D) is followed by another one of greater value, these values must be subtracted.

* **Cri-5:** The roman numeral values are multiplied by 1000 when is followed by a mid dash.

## Test Cases

### End-To-End Testing

* **ETE-TC-1:** 

  1. Execute the software.
  2. Write *5*.
  3. Press *Enter*.
  4. When it tells you 5 = V and it asks you if you want to exit the application, the test has passed.

### Unit Testing

* **UT-TC-1:**

  1. 333 = CCCXXXIII
  2. 444 = CDXLIV

* **UT-TC-2:**

  1. 2.5 = Not an arabic number. Try again.
  2. *Text* = Not an arabic number. Try again.

* **UT-TC-3:**

  1. 45000 = XLV-
  2. 50000 = L-