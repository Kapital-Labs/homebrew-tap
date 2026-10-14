"""Freeze the reviewed cask, including independently verified release pins.

This is a review tripwire, not a Ruby sandbox or provenance verifier.
"""

import hashlib
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_exact_reviewed_cask_bytes(self):
        cask = ROOT / "Casks/kitrove-rc.rb"
        self.assertFalse(cask.is_symlink())
        self.assertEqual(hashlib.sha256(cask.read_bytes()).hexdigest(),
                         "d9b132214eb476579adbef974daabae3f31c04acf4bf70d21aaa6163d652ca0b")

    def test_closed_package_inventory(self):
        self.assertEqual(sorted(p.name for p in (ROOT / "Casks").iterdir()),
                         ["kitrove-rc.rb"])
        self.assertFalse((ROOT / "Formula").exists())


if __name__ == "__main__":
    unittest.main()
