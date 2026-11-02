# RC5.5 versioned Homebrew cask review

The maintainer authorized RC5.5 Homebrew preparation/publication with fresh-install
checks. RC5.5 has no supported in-place migration or rollback-compatible
predecessor. The existing RC4.2 cask therefore remains byte-identical (SHA256
41929c84cf3759374fb2ff6745102101167d1b4fc6924a5fbeb3070d9149a9ba).
`kitrove-rc@5.5` is a separate opt-in token with an explicit `kitrove-rc` conflict,
the same occupied binary-name refusal and no custom installation hooks. Ordinary
upgrades of the old token do not cross the incompatible collection boundary.

The new cask pins the immutable CLI archive only, never the separate installer or
a generated convenience script. Existing production tag/source/run are retained;
no rebuild, signing, tag/release mutation, permission change, credentials, automatic
latest discovery, migration, runtime or APT/RPM/WinGet channel work is included.
No shell/profile changes, executable probes, setup/scan, package hooks, zap rules,
collection/state selection or data deletion are performed by the cask.

NS-07/NS-08/NS-09 remain intact: this is the existing explicit Homebrew/tap distribution
authority, not downloaded self-authentication or general package-management creep
in Kitrove. Capability discovery/adoption, portable/native preservation, fidelity,
provenance/receipts, synchronization/conflicts, trust and local-only data boundaries
do not change. The versioned cask preserves ADR0046's incompatible-update refusal;
it does not claim a new supported migration or platform guarantee.

Require fresh exact tag/source/workflow provenance, source-built archive metadata
verification, notice bytes and native signature/notarization before product
execution. Require Homebrew parsing/style/audit and isolated ordinary-user prefix
tests: old installed-cask conflict, occupied link unchanged, fresh install exact
bytes with quarantine retained, explicit version/help, normal removal and canary
preservation. No operator-prefix installation, real collection or harness mutation.
Warm-host synthetic tests do not establish clean-Mac/offline first launch.

Static tests freeze the complete declarative candidate, old cask digest and exact
two-cask inventory. They are a review tripwire, not a Ruby sandbox or artifact
authenticator. Manual full diff and evidence review is required before commit;
exact protected package/secret checks and freshly green current tap main precede
guarded merge, then verify exact merged main and published cask availability.

## Observed before commit

Fresh download matched pinned archive `7e603b3a...`; immutable tag dereference
`64771911...` and the release API's 21-file inventory were checked. Fresh GitHub attestation verification
pinned exact production workflow/tag/source/signer and denied self-hosted runners.
The preserved independently reviewed-source-built RC5.5 installer (SHA256
3a14e0d6b56727208bceb437a23f5ef9c936d27e670d7c462f980f2841fd55e9)
freshly selected/authenticated the application bundle. All three notice companions
were byte-equal to exact source, including the two files under release/.

Homebrew 7.0.9 parsed the exact pin, single binary, arm64/macOS requirements and
installed-cask conflict. Style and strict audit passed without exceptions. Native
acceptance used a disposable prefix from the same Homebrew Git revision
cdc1ca503231b9a96da64526774915d913c3ec9f, private caches/logs and no HOME override.
Runtime/dev-tool dependencies were confined to that prefix and its evidence caches.
No operator-prefix package or collection was installed/selected.

Normal install refused the exact occupied binary canary, preserving its bytes.
An authenticated RC4.2 fixture was installed but never launched; RC5.5's declared
conflict refused replacement, retaining its exact link and digest. After normal
removal of that owned fixture, RC5.5 installed normally. Installed executable
c80caa70969f14f953f615c76cb63ce0d9129edc1ca0a06cb5681e8040ae0e79
matched the authenticated archive. Strict Developer ID/team requirement and native
notarization checks passed before version/help execution. Quarantine remained
unchanged before/after launch. Version was exactly `kitrove 0.1.0-rc.5.5`;
help succeeded. Normal removal deleted its owned link
and cask directory while preserving collection/harness/occupied-name fixtures.
Failures and their exact expected categories were retained, not bypassed with
force/adopt/no-quarantine. The non-default prefix is Homebrew Tier3; it is not
clean-host or operator-prefix migration evidence.

All three repository package tests passed following two expected red failures
before the new cask existed. Existing RC4.2 cask/workflow/permission bytes remain
unchanged. This tap contains no Rust workspace: its full package suite, Ruby style,
strict audit and native acceptance are the relevant validation; no new product
Rust/MSRV execution is claimed. The unchanged published product source's complete
stable/MSRV and exact release CI remain independently recorded.

Manual full candidate/evidence review, not an independent-agent or exhaustive
repository assurance. Protected PR, exact checks, guarded merge, green merged
main and public-command verification remain the publication gates.
