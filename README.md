Katas in Python

### Considerations when writing a new test

* Test should test **one thing only**

* **Triangulate** by adding new tests that force you code to **pivot**

* Give tests **meaningful names (behavior/goal-oriented)** names that express your **business domain**

  - Avoid technical names like `myMethodReturns5`

  - Avoid leaking implementation information like `myTestReturnsFalse`

  - Avoid writing technical tests; you should test behaviours, not the technicality of components

* Make sure tests **fail for the right reason**

* Ensure you have **meaningful feedback from the failing** test

* Organize your unit tests to **reflect your production code**

### The Transformation Priority Premise

When we test drive an algorithm, the code usually changes from specific to generic; from stupid to intelligent.
We don't want to implement the whole algorithm all at once as there is a high chance to get stuck (**impasse**), 
distracted or tired, and by the time you implement the production code, you feel so drained 
you don't want to write any tests, delivering an implementation not supported by automated tests,
with a high chance to contain bugs (or unexpected use cases).

The Transformation Priority Premise is one of the technical terms introduced by Uncle Bob to 
formalize the phenomenon we experiment when test-driving production code, and it brings a sequence of
common changes from simple to complex that we unconsciously make through the process and
they can guide you when test-driving your code.

Note that the motivation for these transformations is always to make the code meet more generic specifications. 
They are very different from **refactors**, where you want to change the structure of the code to make it easier
to read or more simple without modifying the behavior.

### Avoid the impasse (or getting stuck)
Some problems are hard to solve all at once and it is very common for beginners to try to solve the whole problem with
a generic solution that ends up in a big buggy unmanageable chunk of code. It overloads your brain and there is a point
where you need to rewrite the whole implementation. 

The premise is that if you choose the tests and implementations that use transformations that are higher on the list, 
you will avoid the impasse. 
 
### The sequence of transformations

1 (() –> None) no code at all->code that employs None
2 (None -> constant)
3 (constant->constant+) a simple constant to a more complex constant
4 (constant->scalar) replacing a constant with a variable or an argument
5 (statement->statements) adding more unconditional statements.
6 (unconditional->if) splitting the execution path
7 (scalar->list)
8 (list->container)
9 (statement->recursion)
10 (if->while)
11 (expression->function) replacing an expression with a function or algorithm
12 (variable->assignment) replacing the value of a variable.


### An example in Python 

To validate this premise I want to put it into practice by resolving a Kata. The most used
Kata to illustrate this premise is "Roman Numerals" but I have solved this kata several times already and I would
like to use a different one: ** The bowling kata ** The requirements of this kata are very well explained in this
[Katalist by Codurance](https://katalyst.codurance.com/bowling).

#### 1. First baby step - First roll, zero pins:

One could start by implementing a new function returning None as first step, which
is the top value in the transformation sequence:

```python
def score_for(all_rolls):
    return None
```

And implement a failing tests for a simple use case:

```python
def test_no_pins_first_roll():
    """
    Given no pins were knocked down on the first roll
    The score should be zero
    """
    assert score_for(all_rolls="0") == 0
```

For simplicity, I'm using a string type to represent a sequence of rolls.
This hides the concept of frame, but I am not worried about that yet because
I don't need to introduce that concept for now.

When there were no pins knocked down, we don't have any score point, and we are representing
that with a zero. (Note: this is a design decision that is open to interpretation and the fact that
we are writing tests makes it much more easier to change our code if the decision has to be modified)

>
> Note how I am using the 'business' language right from the first test.
> This is important because it allows to bridge the communication, from the beginning, between
> you, the developer, and any other domain expert (a bowling player or bowl center owner)
>

The test is failing ❌ and this is great! We always want to start with a failing test
that fails for the right reason and ensures our test cycle is healthy:

![img](bowling/screenshots/step_1.png)

### 2. Fake it - Make it pass

We now want to make that test pass by faking the implementation. That is as simple as:

```python
def score_for(all_rolls):
    return 0
```

And we're now in transformation level two (constant) and our test is passing ✅:

![img](bowling/screenshots/step_2.png)


### 3. Second roll any amount under 10

We know that if we test for two rolls with no pins `all_rolls="00"` the test will automatically pass so there
is no point on testing that, we need to find the next simplest case that fails ❌ and that could be `all_rolls="01"`


```python
def test_one_pin_second_roll():
    """
    Given one pin was knocked down on the second roll
    The score should be one
    """
    assert score_for(all_rolls="01") == 1
```

And we can make this test pass ✅ by simply converting the string into an int, so that we'll be in transformation
 number 5) statement :

```python
def score_for(all_rolls):
    """
    Given a set of bowling frames
    It returns the total score accumulated
    :param all_rolls: string
    :return: int
    """
    return sum([int(n) for n in list(all_rolls)])
```

We know this case will work for any combination of numbers which sum is below 10, i.e: 
"11", "35", "90", "09"...etc So, once again, there is no point in testing those and we can say we have
covered one dimension (or use case) of our code.

### 4. Strike on first roll

The maximum number of pins in a frame is 10. We can reach that number by rolling a strike on the first roll and
we can consider this to be the next special case. In order to differentiate 1,0 from 10, we'll use the 'X' notation
for a strike on the first roll of a frame.

> Note: Here I am making another design decision: when the first roll is a strike
> the score could stay unchanged, waiting for the next two rolls, but instead
> I am going to return the accumulated score which could be
> a wrong decision but because we are using TDD, we are safe to change behavior
> later if we find out the implementation doesnt the stakeholder needs

> I don't care about the future, **I feel safe**, all of this can be easily changed thanks to 
> the automated tests supporting my code.

```python
def test_strike_on_first_roll():
    """
    Given 10 pins were knocked down on the first roll
    The score should be 10
    """
    assert score_for(all_rolls="X") == 10
```

And, of course, this test fails and we make sure it does. To make it pass we'll move to the 6th level 
of transformation, conditional. Where the **fake it** solution is:

```python
def score_for(all_rolls):
   return sum([int(n) for n in list(all_rolls)]) if all_rolls != 'X' else 10
```

The last case in the dimension of a first frame would be a spare, which we could represent by any number under 10 plus
a backslash, i.e: "3/"

```python
def test_spare_on_second_roll():
    """
    Given the 10 pins were knocked down on the second roll
    The score should be 10
    """
    assert score_for(all_rolls="3/") == 10
```

Once we are in level 6, we stay using if statements until the code gets too complex. The **obvious implementation**
would be:

```python
def score_for(all_rolls):
    """
    Given a set of bowling frames
    It returns the total score accumulated
    :param all_rolls: string
    :return: int
    """
    if all_rolls == 'X' or '/' in all_rolls:
        return 10
    else:
        return sum([int(n) for n in list(all_rolls)])
```

And our test is passing now. Is this a fraud? Well, it is passing for a first frame, which means the implementation
is working for a subset of scenarios which is the pure essence of Agile development :-D


