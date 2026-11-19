"""Tests for PII Masker."""
import unittest
from guardrail_pii_token_masker.core import PIITokenMasker

class TestPIITokenMasker(unittest.TestCase):
    def test_mask_and_unmask(self):
        m = PIITokenMasker()
        text = "Send mail to user@test.com"
        res = m.mask(text)
        self.assertNotIn("user@test.com", res.masked_text)
        self.assertIn("[EMAIL_1]", res.masked_text)
        restored = m.unmask(res.masked_text)
        self.assertEqual(restored, text)
