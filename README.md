# Kitrove Homebrew tap

Official experimental packages for [Kitrove](https://github.com/Kapital-Labs/kitrove).
The initial release candidate supports **Apple Silicon macOS only**.

## Install

With Homebrew already installed:

```sh
brew install --cask kapital-labs/tap/kitrove-rc
kitrove --version
kitrove --help
```

This installs the signed CLI from `v0.1.0-rc.4.2`. It does not run a separate Kitrove
installer, initialize Kitrove, or change harness configuration. If a `kitrove`
binary already occupies the destination, resolve ownership explicitly; do not
force an overwrite. Do not point `kitrove-installer` at this Brew-managed path.

## Start the walkthrough

```sh
kitrove init
```

Choose first-computer setup, connect a second computer, combine local skills
with an existing collection, or import selected items. Every change has a preview
and confirmation. Revisit your setup with `kitrove configure`. Credentials and
trust decisions stay local; applying skills is a separate confirmed step.
See the [Getting Started guide](https://github.com/Kapital-Labs/kitrove/blob/v0.1.0-rc.4.2/docs/GETTING-STARTED.md).

For an existing Homebrew installation:

```sh
brew update
brew upgrade --cask kapital-labs/tap/kitrove-rc
kitrove --version
kitrove configure
```

Finish pending application transactions before downgrading to RC3, which cannot
recover the newer nested-home application layout. Do not delete your collection
or local state to restart the walkthrough.

Remove the executable with:

```sh
brew uninstall --cask kapital-labs/tap/kitrove-rc
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

## Release review

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
