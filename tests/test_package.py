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

CURRENT_CASK = PREVIEW_CASK.replace('cask "kitrove-rc@5.5" do', 'cask "kitrove" do').replace(
    'name "Kitrove RC5.5 Preview"', 'name "Kitrove"'
).replace(
    'conflicts_with cask: "kitrove-rc"',
    'conflicts_with cask: ["kitrove-rc", "kitrove-rc@5.5"]'
).replace(
    'version "0.1.0-rc.5.5"', 'version "0.1.0-rc.5.7"'
).replace(
    'sha256 "7e603b3a9fb7dc855dcb693dac9b1729310e29531559708fd647d76e28f25f81"',
    'sha256 "7c1ebc5af5b30bc127e35ff91fd692ea32e2a3f4b427d22656057b251f60c1f6"'
).replace(
    'open RC5.5 collections', 'open RC5.7 collections'
).replace(
    '''    Fresh-install evaluation only; not an RC4.2 upgrade or migration.
    Use a new isolated collection and empty destinations with disposable capabilities.
    Do not open RC4.2 collections or use RC4.2 to open RC5.7 collections.
    Homebrew manages this executable, not your Kitrove state.
    Do not point kitrove-installer at this Homebrew-managed installation.
    Clean-Mac online/offline first launch remains unverified.''',
    '''    Fresh-install preview. Start with: kitrove init
    Setup and compatibility: https://kitrove.dev/docs/'''
)


class PackageTests(unittest.TestCase):
    def test_exact_reviewed_cask_bytes(self):
        cask = ROOT / "Casks/kitrove-rc.rb"
        self.assertFalse(cask.is_symlink())
        self.assertEqual(hashlib.sha256(cask.read_bytes()).hexdigest(),
                         "41929c84cf3759374fb2ff6745102101167d1b4fc6924a5fbeb3070d9149a9ba")

    def test_closed_package_inventory(self):
        self.assertEqual(sorted(p.name for p in (ROOT / "Casks").iterdir()),
                         ["kitrove-rc.rb", "kitrove-rc@5.5.rb", "kitrove.rb"])
        self.assertFalse((ROOT / "Formula").exists())

    def test_fresh_preview_is_separate_and_exactly_declarative(self):
        cask = ROOT / "Casks/kitrove-rc@5.5.rb"
        self.assertTrue(cask.is_file(), "separate RC5.5 cask is required")
        self.assertFalse(cask.is_symlink())
        self.assertEqual(cask.read_text(), PREVIEW_CASK)

    def test_current_cask_is_exact_preview_without_automatic_replacement(self):
        cask = ROOT / "Casks/kitrove.rb"
        self.assertTrue(cask.is_file(), "plain kitrove cask is required")
        self.assertFalse(cask.is_symlink())
        self.assertEqual(cask.read_text(), CURRENT_CASK)

    def test_primary_instructions_use_current_name_and_keep_preview_boundary(self):
        readme = (ROOT / "README.md").read_text()
        install = readme.split("## Install\n", 1)[1].split("## Start", 1)[0]
        self.assertIn("brew install --cask kapital-labs/tap/kitrove\n", install)
        self.assertNotIn("brew install --cask kapital-labs/tap/kitrove-rc", install)
        self.assertIn("v0.1.0-rc.5.7", install)
        self.assertIn("not a stable release", install)
        self.assertIn("## Existing installations", readme)

    def test_current_channel_selects_reviewed_rc57_without_changing_old_casks(self):
        current = (ROOT / "Casks/kitrove.rb").read_text()
        self.assertIn('version "0.1.0-rc.5.7"', current)
        self.assertIn('conflicts_with cask: ["kitrove-rc", "kitrove-rc@5.5"]', current)
        self.assertEqual(hashlib.sha256((ROOT / "Casks/kitrove-rc@5.5.rb").read_bytes()).hexdigest(),
                         "816c4c8e37215e61df182b66f865997ec689d84da648eac7379f7d64f3c165d1")

    def test_latest_onboarding_covers_numbered_exclusions_and_keeps_confirmation(self):
        readme = (ROOT / "README.md").read_text()
        install = readme.split("## Install\n", 1)[1].split("## Start", 1)[0]
        self.assertIn("v0.1.0-rc.5.7", install)
        self.assertIn("all,-3,-8", readme)
        self.assertIn("Enter previews", readme)
        self.assertIn("sequential", readme)
        self.assertIn("reviewed ready set", readme)

    def test_install_caveats_are_two_actionable_lines(self):
        current = (ROOT / "Casks/kitrove.rb").read_text()
        caveats = current.split("  caveats <<~EOS\n", 1)[1].split("  EOS\n", 1)[0]
        self.assertEqual([line.strip() for line in caveats.splitlines()], [
            "Fresh-install preview. Start with: kitrove init",
            "Setup and compatibility: https://kitrove.dev/docs/",
        ])

    def test_detailed_install_limits_remain_in_documentation(self):
        readme = (ROOT / "README.md").read_text()
        for guidance in (
            "new isolated collection and empty destinations",
            "RC4.2 cannot read RC5.7 authored-pack collections",
            "Do not point `kitrove-installer` at a Brew-managed installation",
            "Uninstall does not remove Kitrove data or harness configuration",
            "not clean-Mac/offline first launch",
            "do not force an overwrite",
        ):
            with self.subTest(guidance=guidance):
                self.assertIn(guidance.lower(), readme.lower())

    def test_latest_setup_uses_goal_labels_and_optional_prompt_color(self):
        readme = (ROOT / "README.md").read_text()
        for guidance in ("Choose skills to add to your AI tools", "Share this collection with another computer",
                         "valid existing setup", "NO_COLOR", "cyan"):
            self.assertIn(guidance, readme)


if __name__ == "__main__":
    unittest.main()
