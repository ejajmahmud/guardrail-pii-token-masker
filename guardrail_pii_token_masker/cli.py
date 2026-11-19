"""CLI for PII Masker."""
import argparse
from .core import PIITokenMasker

def main():
    parser = argparse.ArgumentParser(description="Guardrail PII Token Masker CLI")
    parser.add_argument("--demo", action="store_true", help="Run PII masker demo")
    args = parser.parse_args()

    masker = PIITokenMasker()
    raw = "Contact Alice at alice@example.com with SSN 123-45-6789"
    res = masker.mask(raw)
    print(f"Masked: {res.masked_text}")
    unmasked = masker.unmask(res.masked_text)
    print(f"Restored: {unmasked}")

if __name__ == "__main__":
    main()
