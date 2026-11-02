# Current-name Homebrew package review

User requested `kitrove` as the primary latest-preview cask without `-rc` in its
name. The fixed version is still RC5.5, not stable. Manual complete diff/caller
review; no independent-agent review claim. No product, workflow, permissions,
old cask, release/tag or state compatibility change.

The new declarative cask differs from the reviewed versioned RC5.5 cask ONLY in
token, display name and explicit conflicts with BOTH retained old tokens. There
are no hooks/zap rules, dynamic latest discovery, automatic migration or custom
installer execution. Future package updates still need compatibility review
(ADR0046, NS07/08/09); a shorter name does not grant that authority. Product
discovery/adoption, portable/native/fidelity/provenance/receipt/sync/conflict
behavior and all local-only data boundaries are unchanged.

Baseline three tests passed. Three intended failures preceded implementation;
all five final static tests pass, freezing the casks, inventory and current-first
instructions. Both old casks are byte-identical. Fresh exact RC5.5 production
attestation/tag/source/signer checks and archive SHA passed. Native parsing,
style (one file, no offenses) and strict audit passed without exemptions.

Warm Apple Silicon macOS private-prefix acceptance passed: occupied-name refusal,
both installed legacy-token conflicts and reverse occupied-name refusals preserve
bytes; normal fresh current-cask installation; exact archive/executable bytes;
strict full Developer ID and notarization; retained quarantine; explicit version
and help; normal removal; synthetic state/collection canaries unchanged. Older
fixture products were never executed. No operator-prefix changes, real state,
setup, scan, trust settings, account credentials or Kitrove installer invocation.

Initial native fixture stopped before the intended occupied-name assertion:
lint dependencies in the same private Homebrew prefix caused JSON Ruby/extension
mismatch during sandbox extraction. Failure retained; clean consumer worktree
separated from lint worktree, normal sandbox enabled, then entire native suite
passed. No cask/product fix, sandbox bypass or assertion weakening.

This is warm-host/non-default-prefix evidence, not clean-Mac/offline first launch,
standard-prefix migration or compatibility acceptance. No Rust workspace exists
in this tap: full package/native tests apply, not a new Rust/MSRV validation claim.
Exact public PR/main gates and postmerge actual-public-command check remain
required before channel completion.

Evidence: homebrew-current-name-20261102-rGYfOM in the external release evidence
directory; includes all failures, static/native logs and provenance. Paused
readiness/WinGet/APT/signing monitors stay paused. Separate user-approved
metadata-only renewal for website deployment is not part of this tap change.
