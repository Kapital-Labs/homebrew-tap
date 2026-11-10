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

The install message shows only the fresh-install preview label, `kitrove init`
and the [setup and compatibility guide](https://kitrove.dev/docs/). The detailed
preview boundaries below remain unchanged.

The `kitrove` cask installs the latest reviewed preview, currently the signed CLI
from `v0.1.0-rc.5.12`. This is **not a stable release**.
It does not run a separate Kitrove installer, initialize Kitrove, or change harness
configuration. This is a **fresh-install evaluation preview**. Use a
new isolated collection and empty destinations with synthetic or disposable
capabilities. RC4.2 cannot read RC5.12 authored-pack collections; binary rollback
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
with an existing collection, or import selected items. In skill collection,
Enter previews recommendations without writing them. Choose `1,4,7` for only
those entries, or `all,-3,-8` (also `-3,-8`) for everything except entries 3 and 8.
After a nonempty preview, Enter or `y` approves only the reviewed ready set.
Use `r` to walk through individual plans: Enter/y accepts
the shown plan, n skips, and r renames before a new preview.

If overlapping names leave nothing ready to collect, choose a numbered source
tool to preview its copies. Your exclusions still apply. You can also type
`from codex`, `from claude`, `from pi` or `from opencode` at the selection prompt.
For example, `from codex,-13,-20` uses the original inventory numbers. Existing
collection names and duplicates within one tool still need an explicit choice
or individual review.

The preview shows skipped-item counts by reason. Press `d` for all details.
Ready plans retain full source, fidelity and loss details. An empty preview
offers no adoption approval. Enter or `s` chooses again using the same scan.
After a nonempty preview, `s` also lets you choose again.

Bulk adoption is sequential, not atomic: stale inputs, pending recovery or a
failed commit stop later items, while completed items remain and are reported.
Revisit setup with `kitrove configure`. Original source files stay in place.
After setup, select **Choose skills to add to your AI tools** for local application,
or **Share this collection with another computer** for bidirectional sync. `init`
offers to continue a valid existing setup after confirmation; it does not recreate
the collection or local state. Questions/input use optional cyan; output and
previews have separate labels. Set `NO_COLOR` for plain text with the same approvals.
Closed menus accept a single displayed key without Enter. Selection expressions,
paths, names and URLs remain text prompts: type the value and press Enter.
An Enter left over from an earlier prompt cannot approve a later preview.
Apply and sync keep separate confirmations; Enter skips those writes.
Credentials and trust decisions stay local.
Use `kitrove scan` to browse the inventory without changes. Press a displayed
number to open a group, `d` for diagnostics, or Enter to finish.

See the [current quick collection guide](https://github.com/Kapital-Labs/kitrove/blob/main/docs/SETUP-QUICK-ADOPTION.md)
and [RC5.12 release notes](https://github.com/Kapital-Labs/kitrove/releases/tag/v0.1.0-rc.5.12).

When sharing, choose a shared folder or **Git repository**. Paste an existing
clone URL or type `c` for instructions to create an empty private repository on
your Git host. Then paste its clone URL. `https://...` selects HTTPS and may ask
for a username and hidden access token. `ssh://...` selects SSH and requires an
absolute known-hosts path. A URL without its scheme asks which connection to use.
Review and approve the synchronization plan separately.

## Existing installations

### Upgrade the current cask

If you already installed `kapital-labs/tap/kitrove`, refresh the tap before
asking Homebrew to upgrade it:

```sh
brew update
brew upgrade --cask kapital-labs/tap/kitrove
kitrove --version
```

Homebrew can report that the latest version is installed when its local copy
of the tap is stale. The upgrade replaces the Homebrew-managed executable.

### Older cask names

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

The following commands apply only to the older RC4.2 channel.

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

## RC5.12 release review

The [RC5.12 review](REVIEW-RC512.md) records the release source, checksums,
signed provenance and isolated Homebrew checks.

## Historical RC5.11 release review

The [RC5.11 review](REVIEW-RC511.md) records the release source, checksums,
signed provenance and isolated Homebrew tests.

## Historical RC5.10 release review

The [RC5.10 review](REVIEW-RC510.md) records the release source, checksums,
signed provenance and isolated Homebrew tests.

## Historical RC5.9 release review

- Release: [v0.1.0-rc.5.9](https://github.com/Kapital-Labs/kitrove/releases/tag/v0.1.0-rc.5.9)
- Source: `229ebd6b7aaddd4249d997b734d7d59c4fe8b20d`
- Release run: [42410283120](https://github.com/Kapital-Labs/kitrove/actions/runs/42410283120)
- Archive SHA-256: `512da247586e0a1a050e5b59a2d029ddfa959d195aabb4d7b3d1d77f944d884b`
- Executable SHA-256: `adb004ec1c6959411cbf3ee60a9899697bb896ed43dc483a7842c1b40bad751c`
- Current cask SHA-256: `6b5db1bfed82b87fe8c4beaf389ba4127a335f773975bd9902af60f998b2d3a1`

All 21 published files, 14 exact-source attestations, six archives' notice bytes
and the native Mac image passed independent verification before selecting this
package. Only the plain current cask's version and digest change; both older
casks, conflicts and short install message stay unchanged.

RC5.9 adds immediate closed-menu choices and visible nonempty-preview Enter
adoption, simplifies explicit Git URL selection, and corrects aggregate retained
sync-base inventory handling. Ordinary per-skill limits, exact approvals,
no-follow/identity checks and separate Apply/sync authority remain. No format
migration or automatic recovery of a real interrupted operation is claimed.

Disposable normal RC5.8-to-RC5.9 executable replacement, fresh install/removal,
native signature/notarization/quarantine, occupied/legacy refusals and unchanged
synthetic canaries passed. No real collection was opened, no setup was run, and
no interrupted sync was retried. Warm-host/non-default-prefix tests are not
clean-Mac/offline launch, state migration or custom-installer rollback evidence.
Exact package PR/main checks and a fresh public-qualified consumer check are
required before advertising the updated cask. See [the RC5.9 review](REVIEW-RC59.md).

## Historical RC5.8 release review

- Release: [v0.1.0-rc.5.8](https://github.com/Kapital-Labs/kitrove/releases/tag/v0.1.0-rc.5.8)
- Source: `d6e1cf5d74f568261658943f0c798be344ceb9da`
- Release run: [42088135078](https://github.com/Kapital-Labs/kitrove/actions/runs/42088135078)
- Archive SHA-256: `269d096bf0e6c4dfee496efa4328a6b505e33fac7bd4b9acc1b13e471a849bf2`
- Executable SHA-256: `5b788e082a773cec2e2eaff197842e80da9f9be2e60c046e66bda42ec729a740`
- Current cask SHA-256: `d9a2066b85195e4cf6abd85d63bffef0a1e5b33921b38ef0ce0da978bb0cfe11`

All 21 published files, 14 exact-source attestations, six archives' notice bytes
and native Mac image passed independent verification before selecting this cask.
Only the plain current cask's version and archive digest change; both older casks
and the short install message stay unchanged. Runtime changes from RC5.7 are
guided setup selection/preview improvements, not core/model/state-format,
dependency-graph, signing-policy or migration changes.

Normal RC5.7-to-RC5.8 executable replacement, fresh install/removal, native identity,
notarization and retained quarantine passed in an isolated Homebrew prefix.
Occupied names and both legacy-token conflicts refused without replacing bytes;
synthetic collection/state canaries stayed unchanged. No real collection was
opened or setup run. This is warm-host/non-default-prefix evidence, not clean-Mac/
offline launch, data migration or the custom installer's rollback protocol.
Exact public package checks and a public-qualified consumer check remain separate
publication gates. See [the RC5.8 review](REVIEW-RC58.md).

## Historical RC5.7 release review

- Release: [v0.1.0-rc.5.7](https://github.com/Kapital-Labs/kitrove/releases/tag/v0.1.0-rc.5.7)
- Source: `bebda46f4061e39fd50f1c87ef3282befa0b1bcd`
- Release run: [41904636002](https://github.com/Kapital-Labs/kitrove/actions/runs/41904636002)
- Archive SHA-256: `7c1ebc5af5b30bc127e35ff91fd692ea32e2a3f4b427d22656057b251f60c1f6`
- Executable SHA-256: `daafbb368ebd40d2de220ca362a610929cff467965f9d3558f744185d5be8c8c`
- Current cask SHA-256: `2e47e4ce6a96cf619947919fccf642f4f772679100a6199807d66d226483ad97`

The release's 21-file inventory, 14 exact-source attestations, six archives' notice
bytes and native Mac image passed independent verification before selecting this
package. Only the plain current cask's version and archive digest change; its short
install message and both older casks stay unchanged. Product-code changes from
RC5.6 are confined to guided CLI setup. Core/model/state-lifecycle code, dependency
graph and publication policy are unchanged. No data migration is introduced.

Normal RC5.6-to-RC5.7 executable replacement, fresh install/removal, native
signature/notarization and retained quarantine passed in a disposable Homebrew
prefix. Occupied names and both legacy-token conflicts refused without replacing
existing bytes; synthetic collection/state canaries stayed unchanged. No real
collection was opened or setup run. This is warm-host/non-default-prefix evidence,
not clean-Mac/offline launch, data migration or custom-installer rollback support.
See [the RC5.7 review](REVIEW-RC57.md).

## Historical RC5.6 release review

- Release: [v0.1.0-rc.5.6](https://github.com/Kapital-Labs/kitrove/releases/tag/v0.1.0-rc.5.6)
- Source: `d306adb76af9380a3ac5ebd82add524fa293a0ed`
- Release run: [41566118041](https://github.com/Kapital-Labs/kitrove/actions/runs/41566118041)
- Archive SHA-256: `abc42e83f27d585fb14734cc6f3cf6e29e50944c497fe8183ab64922bfdb4d40`
- Executable SHA-256: `aa96751956190a422405cfa31c9572d17feebbadaa52f9ad31288a2a53d85fb7`
- Current cask SHA-256: `24a1b3434f7bcb0870d8e007ade85894bc62dd41083ac453cf419b7399be6fd0`

The release's complete inventory, exact-source attestations, notice contents and
native Mac image passed independent verification before selecting this package.
Only the plain current cask changes; both older casks stay byte-identical. The
product-code delta from RC5.5 is confined to guided CLI setup, with no change to
collection/state formats or dependency graph. No data migration is introduced.

Normal RC5.5-to-RC5.6 binary replacement, fresh install/removal, native signatures,
notarization and retained quarantine passed in a disposable Homebrew prefix.
Both older-token conflicts and occupied-name refusals preserved installed bytes;
synthetic collection/state canaries stayed unchanged. These checks did not open
a real collection, grant trust or run setup. Finish pending Kitrove operations
before a package replacement and preserve collections and local state. This is
warm-host/non-default-prefix evidence, not clean-Mac/offline first launch, real
data migration, or the standalone installer's rollback/recovery protocol.
See [the RC5.6 source and package review](REVIEW-RC56.md).
The subsequent install-message change is recorded in
[the caveat copy review](REVIEW-INSTALL-CAVEATS.md); release and executable bytes
are unchanged.

## Historical RC5.5 release review

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
