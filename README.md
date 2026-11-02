# Kitrove Homebrew tap

Official experimental packages for [Kitrove](https://github.com/Kapital-Labs/kitrove).
The release-candidate casks support **Apple Silicon macOS only**.

## Install

With Homebrew already installed:

```sh
brew install --cask kapital-labs/tap/kitrove
kitrove --version
kitrove --help
```

The `kitrove` cask installs the latest reviewed preview, currently the signed CLI
from `v0.1.0-rc.5.5`. The package name is shorter; this is **not a stable release**.
It does not run a separate Kitrove installer, initialize Kitrove, or change harness
configuration. This is a **fresh-install evaluation preview**. Use a
new isolated collection and empty destinations with synthetic or disposable
capabilities. RC4.2 cannot read RC5.5 authored-pack collections; binary rollback
does not roll collection data backward. No rollback-compatible predecessor is
declared, and installer refusals must not be bypassed.

New preview versions are selected by reviewed package updates, not automatic
latest-release discovery. Future updates still require compatibility and recovery
review. Do not point `kitrove-installer` at a Brew-managed installation.

## Start the walkthrough

```sh
kitrove init
```

Choose first-computer setup, connect a second computer, combine local skills
with an existing collection, or import selected items. Every change has a preview
and confirmation. Revisit your setup with `kitrove configure`. Credentials and
trust decisions stay local; applying skills is a separate confirmed step.
See the [versioned Getting Started guide](https://github.com/Kapital-Labs/kitrove/blob/v0.1.0-rc.5.5/docs/GETTING-STARTED.md)
and [RC5.5 release notes](https://github.com/Kapital-Labs/kitrove/releases/tag/v0.1.0-rc.5.5).

## Existing installations

The older `kitrove-rc` cask remains pinned to RC4.2, and `kitrove-rc@5.5` remains
pinned to RC5.5. They are retained for existing users; neither is automatically
renamed or replaced by `kitrove`. All three casks share the same executable name.
The new cask explicitly conflicts with both older tokens. An occupied executable
also refuses installation without replacing it.

This is not an RC4.2 upgrade or migration. Do not uninstall an existing installation
or remove its state merely to bypass a conflict; review ownership and recovery
needs first. Preserve collections and local state. Do not force an overwrite,
use `--zap`, or open an older collection with a new preview as a migration shortcut.

### Historical RC4.2 channel

The following commands apply only to the older RC4.2 channel, not RC5.5:

```sh
brew update
brew upgrade --cask kapital-labs/tap/kitrove-rc
kitrove --version
kitrove configure
```

Finish pending application transactions before downgrading to RC3, which cannot
recover the newer nested-home application layout. Do not delete your collection
or local state to restart the walkthrough.

## Uninstall

Remove an executable installed by the current cask with:

```sh
brew uninstall --cask kapital-labs/tap/kitrove
```

If you installed the versioned RC5.5 cask instead, use its original token:

```sh
brew uninstall --cask kapital-labs/tap/kitrove-rc@5.5
```

Uninstall does not remove Kitrove data or harness configuration. No `zap` rule is
provided. Package installation is not permission to execute imported capabilities.

## Trust and limits

You trust Homebrew and this tap to select the package. Homebrew checks its pinned
SHA-256. Maintainers verify exact release provenance and native signatures before
reviewing package changes. This is different from running Kitrove's offline
attestation verifier on every consumer installation. Quarantine and Gatekeeper
remain enabled; do not disable them to work around a launch failure.

RC4.1 installation followed by RC4.2 upgrade, removal, fresh RC4.2 installation and
removal passed on an existing Apple Silicon Mac in an isolated Homebrew prefix.
Each launch followed independent provenance, exact executable digest, native
signature, notarization and quarantine checks. Synthetic collection and harness
canaries remained unchanged. Earlier RC3 conflict-refusal evidence remains scoped
to RC3. These checks do not prove clean-Mac online/offline first launch, Intel Mac,
Linux, Windows, or preservation of every populated real-user state layout.
First launch may require network access. This remains a prerelease, not stable
support. Homebrew replacement does not provide the custom installer's state locks,
retained rollback kits or recovery protocol. Binary downgrade is not data rollback.

## RC5.5 release review

- Release: [v0.1.0-rc.5.5](https://github.com/Kapital-Labs/kitrove/releases/tag/v0.1.0-rc.5.5)
- Source: `64771911eecdb5f167c07c88e1606dc5bf83c9a3`
- Release run: [41241628037](https://github.com/Kapital-Labs/kitrove/actions/runs/41241628037)
- Archive SHA-256: `7e603b3a9fb7dc855dcb693dac9b1729310e29531559708fd647d76e28f25f81`

The current cask and retained older tokens preserve the distribution policy: no
incompatible automatic replacement without a reviewed recovery design. A plain
package name does not authorize an incompatible future package update. It does
not add state locks, migration, automatic trust or rollback to Homebrew. Native
RC5.5 acceptance passed on an existing Apple Silicon Mac in a disposable Homebrew
prefix: an occupied binary path and an installed RC4.2 cask were refused without
replacement; authenticated RC5.5 fresh installation, strict signature/notarization
checks, retained quarantine, explicit version/help and removal passed. Synthetic
collection/harness canaries stayed unchanged. No RC4.2 collection, setup or state
migration was exercised. This is warm-host/non-default-prefix evidence, not
clean-Mac online/offline first launch or standard-prefix migration acceptance.
See [the scoped source and package review](REVIEW-RC55.md).
The current-name cask and its additional conflict checks are reviewed separately
in [the naming and onboarding review](REVIEW-CURRENT.md).

- Executable SHA-256: `c80caa70969f14f953f615c76cb63ce0d9129edc1ca0a06cb5681e8040ae0e79`
- Reviewed cask SHA-256: `816c4c8e37215e61df182b66f865997ec689d84da648eac7379f7d64f3c165d1`

### Historical RC4.2 release review

- Release: [v0.1.0-rc.4.2](https://github.com/Kapital-Labs/kitrove/releases/tag/v0.1.0-rc.4.2)
- Source: `f9f4e43ccc258e85ad2fff91df4bde90e1e09b4f`
- Release run: [38603835793](https://github.com/Kapital-Labs/kitrove/actions/runs/38603835793)
- Archive SHA-256: `cfac95704204b675b577d668ee9de8a0d6495a28684a368d443c5acc40264d39`
- Executable SHA-256: `fdd15d76756c81baf4ee085a598124302fcebca7c6471a4f607100c4e7c64aa8`
- Package preparation and acceptance: [Kitrove PR #53](https://github.com/Kapital-Labs/kitrove/pull/53)

The maintainer approved this experimental distribution channel and public tap on
2026-10-10. The ADR in PR #53 records the proposal before that approval; publication
does not close its remaining clean-machine or upgrade acceptance gates.

Changes require a protected pull request and passing package/secret checks,
including for administrators. No automatic release discovery, version bumps,
signing credentials or publication workflow is configured. Before an update,
reverify its immutable tag/commit, production provenance, native signature,
archive inventory and exact executable bytes using the existing Kitrove verifier.
Review state compatibility and native install/upgrade/removal evidence separately.
Do not derive trust from a filename, release-page checksum or old verification log.

Run `python3 -m unittest discover -s tests` before pushing. The frozen cask hash is
a review tripwire, not a Ruby sandbox or artifact authenticator. Changing it requires
reviewing the complete cask diff and release evidence. Homebrew parsing/audit and
native package acceptance are separate checks recorded by the maintainer.
