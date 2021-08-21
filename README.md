# computer_db_test
This is a Behavioral Driven Development (BDD) test package for Computers Database Portal.
In it you will find tests, test implementations and a Page Object Model library (normally, the POM library would live
in a separate package, but for simplification purposes, it is bundled here).
Core framework depenendies are:
* behave - Python BDD framework
* selenium - Python selenium web driver library

The package has 3 main components (and directories):
* `computer_db_pom` - Computer DB Page Object Model library
* `features` - collection of Feature Files, containing Scenarios to capture portal functional requirements
* `features/steps` - Scenario step implementations to carry out use cases in automated runs

## Environment Setup
This package was created and executed on a single Windows 10 machine with a specific set of environment prerequisites
(listed below). It is possible the package runs in other environment setups, but that is out of scope for this setup
guide.

To run this package, there are several pre-requisites that need to be met:
* Python 3.9 runtime environment - users should install the latest Python 3.9 interpreter
* Python libraries (install manually using `pip install <library>`):
  * behave == 1.2.6
  * selenium
* Chrome browser version 92 - the bundled Chrome webdriver is confirmed working for Chrome browser version 92.


## What is BDD?
Behavioral Driven Development methodology calls for modeling test suites (known as Feature Files)
and test cases (Scenarios) around product behavior. Each Scenario describes a use case capturing functionality for a
particular feature or component. Related Scenarios are bundled under a single Feature File, and the product functional
requirements are captured in the Feature Files themselves. Scenarios are comprised of 1 or more steps, each step
executing a single set of instructions to setup the environment, perform an action, or validate results.

BDD frameworks adopt a high level language called Gherkin, written in plain human-readable language, allowing anyone to
write Scenarios and Feature Files.

## How do I run tests?
### Run all implemented tests
From the root package directory, run all implemented steps with the following command:
* `behave`

### Running tests using tags
Feature Files and Scenarios make use of user-defined tags to break down tests into different groups.
Users can execute runs targeting a specific tag or tags, thereby running only those tests labeled with those tags:
* `behave -t <tag_name>`
#### Available tags:
* `sanity` - subset of tests marked for sanity test runs, validating basic functionality
* `search` - subset of tests for Search Computers functionality
* `add`    - subset of tests for Add Computer functionality
* `SAN[0-9][0-9]` - specific Scenario tagging for Sanity Feature File Scenarios
* `SEA[0-9][0-9]` - specific Scenario tagging for Search Computers Feature File Scenarios
* `ADD[0-9][0-9]` - specific Scenario tagging for Add Computer Feature File Scenarios

#### Examples
* Running sanity tests: `behave -t sanity`
* Running single search Scenario (second Scenario): `behave -t SEA02`

#### @skip tag
Feature Files and Scenarios marked with reserved tag `@skip` will be skipped during test execution.
Skipped tests will not count as failed tests.
