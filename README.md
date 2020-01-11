Katas in Python

### Considerations when writing a new test

* Test should test one thing only

* Triangulate by adding new tests that force you code to pivot

* Give tests meaningful names (behavior/goal-oriented) names that express your business domain

  - Avoid technical names like `myMethodReturns5`

  - Avoid leaking implementation information like `myTestReturnsFalse`

  - Avoid writing technical tests; you should test behaviours, not the technicality of components

* Make sure tests fail for the right reason

* Ensure you have meaningful feedback from the failing test

* Organize your unit tests to reflect your production code
