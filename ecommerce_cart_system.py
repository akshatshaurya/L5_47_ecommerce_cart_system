"""Shopping cart utilities for a small e-commerce example."""

import hashlib
import secrets
from pathlib import Path
from typing import Any

cart_items: dict[str, dict[str, Any]] = {
    "ITEM1": {"name": "Wireless Mouse", "price": 25.0, "qty": 2},
    "ITEM2": {"name": "Mechanical Keyboard", "price": 80.0, "qty": 1},
    "ITEM3": {"name": "USB-C Hub", "price": 45.0, "qty": 3},
}

total_sales = sum(
    item["price"] * item["qty"] for item in cart_items.values()
)


def add_item_to_cart(
    item_id: str,
    name: str,
    price: float,
    qty: int = 1,
    audit_log: list[str] | None = None,
) -> bool:
    """Add a new item and record the operation; return whether it was added."""
    global total_sales

    if item_id in cart_items or not item_id or not name:
        return False
    if price < 0 or qty <= 0:
        raise ValueError("Price must be non-negative and quantity must be positive.")

    if audit_log is None:
        audit_log = []

    cart_items[item_id] = {"name": name, "price": float(price), "qty": qty}
    total_sales += float(price) * qty
    audit_log.append(f"Added {item_id} with price {price:.2f}")
    return True


def remove_item_from_cart(item_id: str) -> bool:
    """Remove an item if it exists and keep the sales total consistent."""
    global total_sales

    item = cart_items.pop(item_id, None)
    if item is None:
        return False

    total_sales -= item["price"] * item["qty"]
    return True


def check_cart_status(item_id: str) -> bool:
    """Return True when the requested item exists and has positive quantity."""
    item = cart_items.get(item_id)
    return item is not None and item["qty"] > 0


def calculate_discounted_total(item_id: str, discount_rate: float = 0.10) -> float:
    """Calculate an item's discounted price using a rate between 0 and 1."""
    if not 0 <= discount_rate <= 1:
        raise ValueError("Discount rate must be between 0 and 1.")

    item = cart_items.get(item_id)
    if item is None:
        raise KeyError(f"Unknown cart item: {item_id}")

    return round(item["price"] * (1 - discount_rate), 2)


def generate_item_hash(item_id: str) -> str:
    """Return a SHA-256 digest for a non-secret item identifier."""
    return hashlib.sha256(item_id.encode("utf-8")).hexdigest()


def generate_checkout_pin() -> str:
    """Generate a four-digit PIN using a cryptographically secure generator."""
    return f"{secrets.randbelow(9000) + 1000:04d}"


def export_cart_receipt(filename: str = "receipt.txt") -> Path:
    """Write a receipt to a file in the current directory."""
    safe_name = Path(filename).name
    if not safe_name or safe_name in {".", ".."}:
        raise ValueError("Please provide a valid receipt filename.")

    receipt_path = Path.cwd() / safe_name
    with receipt_path.open("w", encoding="utf-8") as receipt_file:
        receipt_file.write("E-commerce cart receipt\n")
        receipt_file.write("========================\n")
        for item_id, details in cart_items.items():
            line_total = details["price"] * details["qty"]
            receipt_file.write(
                f"{item_id}: {details['name']} | "
                f"qty={details['qty']} | unit={details['price']:.2f} | "
                f"line total={line_total:.2f}\n"
            )
        receipt_file.write(f"Total: {total_sales:.2f}\n")

    return receipt_path


def get_cart_summary(items: dict[str, dict[str, Any]]) -> int:
    """Return the total number of units across all positive-quantity items."""
    return sum(details["qty"] for details in items.values() if details["qty"] > 0)


def main() -> None:
    """Demonstrate the cart operations."""
    audit_log: list[str] = []
    add_item_to_cart("ITEM4", "Monitor Stand", 35.0, 1, audit_log)
    remove_item_from_cart("ITEM2")

    print("Is ITEM1 in cart:", check_cart_status("ITEM1"))
    print("Discounted Price:", calculate_discounted_total("ITEM1"))
    print("Item Hash:", generate_item_hash("ITEM1"))
    print("Checkout PIN:", generate_checkout_pin())
    print("Receipt saved to:", export_cart_receipt())
    print("Total items:", get_cart_summary(cart_items))
    print("Audit log:", audit_log)


if __name__ == "__main__":
    main()
