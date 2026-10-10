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

This installs the signed CLI from `v0.1.0-rc.3`. It does not run a separate Kitrove
installer, initialize Kitrove, or change harness configuration. If a `kitrove`
binary already occupies the destination, resolve ownership explicitly; do not
force an overwrite. Do not point `kitrove-installer` at this Brew-managed path.

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

RC3 installation, conflict refusal, version/help and removal passed on an existing
Apple Silicon Mac in an isolated, non-default Homebrew prefix. This does not prove
clean-Mac online/offline first launch, Intel Mac, Linux, Windows or Brew upgrades.
First launch may require network access. This remains a prerelease, not stable
support. Homebrew replacement does not provide the custom installer's state locks,
retained rollback kits or recovery protocol. Binary downgrade is not data rollback.

## Release review

- Release: [v0.1.0-rc.3](https://github.com/Kapital-Labs/kitrove/releases/tag/v0.1.0-rc.3)
- Source: `4212327d45097c1826e64a0a8f6e556c40bffc7f`
- Release run: [37640833426](https://github.com/Kapital-Labs/kitrove/actions/runs/37640833426)
- Archive SHA-256: `49229e4d6c0eee3f7f711c42b50274a24a29dfa90768b1cedbed21e16b44b28e`
- Executable SHA-256: `0dad5b176d6502c207ce317f636cfe38afd494f50e9707696a86803981bcc034`
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
