"""Core High-Throughput PII Token Masker."""
import re
from typing import Dict, Tuple

class MaskResult:
    def __init__(self, masked_text: str, mask_map: Dict[str, str]):
        self.masked_text = masked_text
        self.mask_map = mask_map

class PIITokenMasker:
    PATTERNS = [
        (r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "[EMAIL_{id}]"),
        (r"\b\d{3}-\d{2}-\d{4}\b", "[SSN_{id}]"),
        (r"\b(?:\d[ -]*?){13,16}\b", "[CARD_{id}]")
    ]

    def __init__(self):
        self.forward_map: Dict[str, str] = {}
        self.reverse_map: Dict[str, str] = {}
        self._next_id = 1

    def mask(self, text: str) -> MaskResult:
        masked = text
        for pat, mask_tmpl in self.PATTERNS:
            matches = re.findall(pat, masked)
            for m in matches:
                if m not in self.forward_map:
                    mask_token = mask_tmpl.format(id=self._next_id)
                    self._next_id += 1
                    self.forward_map[m] = mask_token
                    self.reverse_map[mask_token] = m
                masked = masked.replace(m, self.forward_map[m])
        return MaskResult(masked, self.reverse_map)

    def unmask(self, text: str) -> str:
        res = text
        for mask_token, original in self.reverse_map.items():
            res = res.replace(mask_token, original)
        return res
