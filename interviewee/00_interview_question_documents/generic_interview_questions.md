Reference:
https://www.atlassian.com/agile/software-development/code-reviews
https://www.atlassian.com/continuous-delivery/software-testing
https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment

1. What exactly is code review?
- When a developer is finished wokring on a piece of code, another developer looks in the same code to identify:
a. Are there any obvious logical errors in the code?
b. Looking at the requirement, are all the cases fully implemented?
c. Are the new automated tests sufficient for the new code?
d. Does the new code adheres to existing standards and guidelines?
***

2. What are the advantages of code review for an Agile team?
- Code reviews share knowledge
- Code reviews help in reaching better estimates
- Code reviews enable time off
- Code reviews can help with mentoring newer engineers
***

3. What are some code review best practices?
- Share the laod
- Manual review gate before merging code changes to production
- Use peer pressure to your advantage
***

4. How is code coverage calculated?
- Function coverage
- Statement coverage
- Branches coverage
- Condition coverage
- Line coverage
***

5. What is the difference between CI, CD (Continuous Delivery) and CD (Continuous Deployment)?
[1] Continuous Integration (CI):
- Developers merge the changes back to the main branch as often as possible
- Changes are validated by creating a build and running automated tests against the build
- CI puts a great emphasis on testing automation to check that the application is not broken whenever new commits are integrated into the main branch

[2] Continuous Delivery (CD):
- Extension of CI since it automatically deploys the code changes to a testing and production environment after the build stage
- Automated release process - deploys code changes to testing/production environment after the build stage
- We can have periodic (eg: daily, weekly, monthly) release cycles

[3] Continuous Deployment (CD):
- Goes one step further Continuous Deployment - every changes that passes all the stages of production pipeline is released to the customers
- There is no human intervention, except, in case of failure
- Excellent way to accelerate feedback loop with the customers and take pressure off the team

![](https://wac-cdn.atlassian.com/dam/jcr:b2a6d1a7-1a60-4c77-aa30-f3eb675d6ad6/ci%20cd%20asset%20updates%20.007.png?cdnVersion=176)
***

6. SOLID Design Principles
- (S)ingle Responsibility Principle: A class should have one and only one reason to change
- (O)pen Closed Principle: Software entities should be open for extension but closed for modification
- (L)iskov Substitution Principle (LSP): Subtypes must be substitutable for their base types
- (I)nterface Segregation Principle (ISP): The dependency of one class on another should depend on the smallest possible interface
- (D)ependency Inversion Principle (DIP): Depend upon abstractions (interfaces) not upon concrete classes
