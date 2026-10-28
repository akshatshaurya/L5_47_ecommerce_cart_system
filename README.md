# Lab 5 — Static Code Analysis: E-Commerce Cart System

## Files
- `ecommerce_cart_system.py` — corrected cart program.
- `issues.md` — issue table with original line references, impact, and fixes.
- `reflection.md` — four reflection answers aligned with the lab's learning outcomes.
- `reports/` — before/after report placeholders that clearly state the analyzers were not executable in the preparation environment.

## Generate genuine before reports
The original file is preserved in Git commit `baseline: add supplied program and report notes`. To analyze the original version, check out that commit, then run:

```bash
python -m pip install pylint bandit flake8
pylint ecommerce_cart_system.py > reports/pylint_before.txt
bandit -r ecommerce_cart_system.py > reports/bandit_before.txt
flake8 ecommerce_cart_system.py > reports/flake8_before.txt
```

Save those authentic outputs, then return to the latest commit.

## Generate genuine after reports
From the final version, run:

```bash
pylint ecommerce_cart_system.py > reports/pylint_after.txt
bandit -r ecommerce_cart_system.py > reports/bandit_after.txt
flake8 ecommerce_cart_system.py > reports/flake8_after.txt
```

Review each report, fix any remaining findings, and rerun the tools. The lab handout asks for a Pylint score above 9.5 and for Bandit and Flake8 findings to be addressed. No score or clean report is claimed until the tools are actually run.

## Git commits
The repository contains three focused fix commits:
1. Pylint/code-quality and reliability improvements.
2. Bandit/security improvements.
3. Flake8/style and final cleanup.

To review: `git log --oneline`.
