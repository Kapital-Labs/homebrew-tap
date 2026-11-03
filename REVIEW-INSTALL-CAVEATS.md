# Homebrew install-message review

The maintainer requested less output during installation. The current `kitrove`
cask now prints two lines: a fresh-install preview label with `kitrove init`,
and the setup/compatibility documentation link. Compatibility, ownership and
acceptance limitations remain in README and the linked setup guide, rather than
being repeated in every installation message.

The previous RC5.6 package review remains a historical record. Its reviewed cask
SHA-256 was `128738bb6dbd07ad6705d9cd0c06766bca5a5a7fc262afc489b11ef4ff7c5286`.
The new copy-only cask SHA-256 is
`24a1b3434f7bcb0870d8e007ade85894bc62dd41083ac453cf419b7399be6fd0`.

Complete cask diff review confirms only the caveat string changed. Version,
archive URL/SHA-256, binary path, both older-token conflicts, ARM/macOS constraints
and livecheck refusal remain unchanged. Both historical casks stay byte-identical.
No hooks, automatic setup, custom installer, state migration, force overwrite,
quarantine exceptions, signing or new application release are introduced.

The nine package tests cover the exact declarative cask, frozen historical
packages, two-line output and retained detailed documentation. The two output
assertions failed against the old caveats before the copy change and passed
afterward. Native Homebrew JSON parsing/rendering returned exactly the two intended
lines with unchanged version, archive digest and conflict/architecture fields.
Homebrew style (one file, no offenses) and strict audit passed in an isolated
Homebrew worktree without installing or executing Kitrove. The linked live guide
contains RC5.6 setup and existing-installation guidance. This manual source review
is not an exhaustive or independent
agent review, and does not claim clean-Mac/offline first-launch acceptance.
