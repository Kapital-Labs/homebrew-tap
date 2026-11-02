"""Freeze the reviewed cask, including independently verified release pins.

This is a review tripwire, not a Ruby sandbox or provenance verifier.
"""

import hashlib
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

PREVIEW_CASK = '''cask "kitrove-rc@5.5" do
  version "0.1.0-rc.5.5"
  sha256 "7e603b3a9fb7dc855dcb693dac9b1729310e29531559708fd647d76e28f25f81"

  url "https://github.com/Kapital-Labs/kitrove/releases/download/v#{version}/kitrove-cli-aarch64-apple-darwin.tar.xz"
  name "Kitrove RC5.5 Preview"
  desc "Portable agent environment management"
  homepage "https://github.com/Kapital-Labs/kitrove"

  livecheck do
    skip "Release candidates require reviewed provenance and native acceptance"
  end

  conflicts_with cask: "kitrove-rc"
  depends_on arch: :arm64
  depends_on :macos

  binary "kitrove-cli-aarch64-apple-darwin/kitrove"

  caveats <<~EOS
    Fresh-install evaluation only; not an RC4.2 upgrade or migration.
    Use a new isolated collection and empty destinations with disposable capabilities.
    Do not open RC4.2 collections or use RC4.2 to open RC5.5 collections.
    Homebrew manages this executable, not your Kitrove state.
    Do not point kitrove-installer at this Homebrew-managed installation.
    Clean-Mac online/offline first launch remains unverified.
  EOS
end
'''


class PackageTests(unittest.TestCase):
    def test_exact_reviewed_cask_bytes(self):
        cask = ROOT / "Casks/kitrove-rc.rb"
        self.assertFalse(cask.is_symlink())
        self.assertEqual(hashlib.sha256(cask.read_bytes()).hexdigest(),
                         "41929c84cf3759374fb2ff6745102101167d1b4fc6924a5fbeb3070d9149a9ba")

    def test_closed_package_inventory(self):
        self.assertEqual(sorted(p.name for p in (ROOT / "Casks").iterdir()),
                         ["kitrove-rc.rb", "kitrove-rc@5.5.rb"])
        self.assertFalse((ROOT / "Formula").exists())

    def test_fresh_preview_is_separate_and_exactly_declarative(self):
        cask = ROOT / "Casks/kitrove-rc@5.5.rb"
        self.assertTrue(cask.is_file(), "separate RC5.5 cask is required")
        self.assertFalse(cask.is_symlink())
        self.assertEqual(cask.read_text(), PREVIEW_CASK)


if __name__ == "__main__":
    unittest.main()
