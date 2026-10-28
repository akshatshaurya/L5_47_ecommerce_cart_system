# Reflection Questions — Static Code Analysis

**Note:** The supplied lab handout explains the reflection requirement but does not print the four questions themselves. The answers below address four standard reflection prompts aligned with the handout's stated learning outcomes.

### 1. What is static code analysis, and why is it useful?
Static code analysis examines source code without running the program. It helps identify likely bugs, security risks, and style problems early, before the code reaches users. Pylint focuses on code quality and likely errors, Bandit checks common security weaknesses, and Flake8 checks Python style and formatting.

### 2. Which issues were most important, and why?
The highest-priority issue was `eval()` on a supplied expression because it could execute arbitrary code. The hard-coded gateway secret and shell command construction were also serious security concerns. The predictable PIN generator and weak MD5 hashing were improved, while the mutable default argument and broad exception handling were corrected to prevent confusing behavior and hidden failures.

### 3. How did the tools complement one another?
The tools have overlapping but different goals. Pylint helps identify design, naming, unused-code, and maintainability issues. Bandit focuses on risky security patterns. Flake8 catches formatting and style violations that make code harder to read and maintain. Using all three provides broader coverage than relying on one tool.

### 4. What did you learn, and what are the limitations of static analysis?
I learned that code can appear to work while still containing security, reliability, and maintainability problems. Safer APIs, explicit validation, context managers, and clear naming reduce risk. Static analysis cannot prove that a program is correct or replace runtime tests, code review, or security testing; its warnings must be reviewed in context. For this submission, the analyzer packages could not be installed in the execution environment, so the included report notes are explicitly not genuine tool output. The commands in the README should be run in a network-enabled local environment to produce the required authentic reports.
