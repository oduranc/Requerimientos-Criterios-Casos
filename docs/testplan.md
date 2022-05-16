# Requirements, Acceptance Criteria, Test Cases

## Requirements

### Process Requirements

* **Proc-Req-1:** The software shall be developed using C# .NET Core.

* **Proc-Req-2:** The software shall be tested using MSTest.

### Functional Requirements

* **Func-Req-1:** The software must convert arabic numbers to roman numerals.

* **Func-Req-2:** The software must ask to the user for a number.

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

