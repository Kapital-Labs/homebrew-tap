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
                         "41929c84cf3759374fb2ff6745102101167d1b4fc6924a5fbeb3070d9149a9ba")

    def test_closed_package_inventory(self):
        self.assertEqual(sorted(p.name for p in (ROOT / "Casks").iterdir()),
                         ["kitrove-rc.rb"])
        self.assertFalse((ROOT / "Formula").exists())


if __name__ == "__main__":
    unittest.main()
