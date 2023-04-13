# Notes Taken from the 'Obey the Testing Goat'

## Technicalities

### Create Django Project

`django-admin.py startproject <project_name>`

### Running the Django Dev Server

Use python and make sure you're in the right folder (look for `manage.py` that Django created within the folder, it's a good hint that you're in the right spot):

`python manage.py runserver`

## Functional Tests

Functional tests let us see how te application *functions* from the user's point of view, hence the name &ndash; functional tests.
As a result, functional tests (FT) can be a sort of a specification for the application you're building.

There are some varying ways of naming these tests, so: functional_tests == acceptance_tests == end-to-end_tests == black_box_tests. These tests look at how the whole application functions from the outside.

Minimum viable app &ndash; what's the simplest thing that we can build that is still useful?

&ndash; We have a word for comments. We call them lies!

## Python's `unittest`

Tests are organized into classes which inherit from `unittest.TestCase`.

Any method whose name starts with `test` will be run by the test runner.
Nice, descriptive names are a good idea.

`setUp` and `tearDown` are special methods, run before and after each test. They're a bit like `try/except` &ndash; `tearDown` will run even if there's an error during the test itself. `tearDown` doesn't run if you hit an exception during `setUp`.

## Django's Apps: One Project &ndash; Many Apps

Django encourages you to structure your code into *apps* &ndash; one project can have many apps, from different sources.

## Unit Tests

### Running Unit Tests

`python manage.py test`

Real-world boundaries between functional tests and unit tests can get a bit blurry, but the main distinction is that:

1. functional tests test the application from the outside &ndash; from the outlook of the user,
2. unit tests test the app from the inside &ndash; from the outlook of the programmer.

Both types of tests can be used on a single application/product to guide its development.
The workflow looks like this:

1. Start with a *functional test*, describing the new functionality from the user's point of view.
2. Once you have a functional test that fails, start thinking about how to write code that can get it to pass.
3. Then use one or more *unit tests* to define how we want our code to behave. The idea &ndash; every line of production code should be tested by (at least) one of our unit tests.
4. Once we have a failing unit test, we write the smallest amount of *application code*, just enough to get the unit test to pass.
5. Re-run the functinoal tests and see if they pass.

Functional tests drive what we do at a high level, while unit tests drive what we do at a low level.

Functional tests should help build an application with the right functionality and guarantee you never accidentally break it.
Unit tests should help write code that's clean and bug-free.

The unit test is driven by the functional test, but it's also much closer to the actual code.

## Unit-Test/Code Cycle

1. Run the unit tests in the terminal and see how they fail.
2. Make a minimal code change in the editor to address the current test failure.
3. Repeat.

The more nervous we are about getting our code right, the smaller and more minimal we make each code change &ndash; the idea is to be absolutely sure that each bit of code is justified by a test.
