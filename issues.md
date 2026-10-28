# Static Analysis Issue Documentation

Line numbers refer to the supplied original `ecommerce_cart_system.py`; they may differ in the corrected file.

| Issue | Type / Severity | Original line(s) | Description | Fix approach |
|---|---|---:|---|---|
| Dynamic `eval()` | Security / High | 42–45 | Evaluating a caller-supplied expression can execute arbitrary Python code. | Replaced expression evaluation with a numeric `discount_rate` constrained to 0–1. |
| Hard-coded gateway secret | Security / High | 71–80 | A live-looking secret is embedded in source and printed, risking credential disclosure. | Removed the secret entirely; secrets should be supplied via a protected environment/secret manager if a gateway integration is added. |
| Shell command built from filename | Security / Medium | 56–60 | `os.system()` runs a shell command containing a filename, creating command-injection risk. | Removed shell execution and report the receipt path directly. |
| Weak MD5 hash | Security / Medium | 48–49 | MD5 is unsuitable for security-sensitive hashing. | Switched to SHA-256; item hashes are identifiers, not authentication tokens. |
| Predictable PIN generator | Security / Medium | 52–53 | `random.randint()` is not designed for security-sensitive codes. | Switched to `secrets.randbelow()` and return a four-digit string. |
| Mutable default argument | Bug / Medium | 15 | `audit_log=[]` shares one list between calls. | Changed default to `None` and creates a list per call. |
| Bare `except` | Reliability / Medium | 25–29 | A bare exception suppresses every error, not just a missing item. | Used `dict.pop(item_id, None)` and return a success/failure boolean. |
| Unsafe/missing-item lookup | Bug / Medium | 42–44 | An unknown item raises an unhelpful `KeyError`; expression-based discounting compounds the risk. | Validate item existence and raise a clear `KeyError`. |
| Receipt file handling | Quality / Low | 56–59 | File is not managed with a context manager or explicit encoding. | Used `Path.open()` in a context manager with UTF-8 encoding and a filename-only path. |
| Unused import and local | Quality / Low | 4, 33 | `math` and `handling_fee` are unused. | Removed unused code. |
| Naming and formatting | Style / Low | throughout | CamelCase function names, inconsistent indentation and spacing reduce readability. | Renamed functions to snake_case and applied consistent PEP 8 formatting. |
| Sales total after removal | Logic / Medium | 25–29 | Removing an item did not subtract its value from `total_sales`. | Subtracts removed item value and quantity from the running total. |

## Verification note

The execution environment used to prepare this submission did not have Pylint, Bandit, or Flake8 installed, and network access prevented installation. The files in `reports/` therefore transparently identify the analyzers as **not executed** and provide source-inspection notes; they are not fabricated analyzer output. Run the commands in `README.md` locally to generate authentic before/after reports and verify the Pylint score target.
