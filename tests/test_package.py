"""Freeze the cask copied from the reviewed Kitrove PR #53.

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
                         "95dea68698a66cde70baf2c42fcb3ba9d84d34dd0fe13baf7f9445513da98119")

    def test_closed_package_inventory(self):
        self.assertEqual(sorted(p.name for p in (ROOT / "Casks").iterdir()),
                         ["kitrove-rc.rb"])
        self.assertFalse((ROOT / "Formula").exists())


if __name__ == "__main__":
    unittest.main()
