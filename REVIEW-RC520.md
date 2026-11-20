# Kitrove RC5.20 Homebrew review

- [Signed preview](https://github.com/Kapital-Labs/kitrove/releases/tag/v0.1.0-rc.5.20)
- Source commit `9899510ec80d7330d08e6384ac0227e98e9d69b3`
- [Protected release run](https://github.com/Kapital-Labs/kitrove/actions/runs/44801191158)
- Apple Silicon CLI archive SHA-256 `50a89a801eff6297b10474dc9275c56486fabc1e996f503934e07f8145590c94`
- Apple Silicon CLI executable SHA-256 `5768169afd8bd1393ec4a389a14187973baed47a62946869d5a982ebcf0c68df`

Independent verification covered all 21 public files, 14 exact-source attestations,
notice bytes in six archives and the authenticated native ARM installer image.
This cask selects that verified CLI archive; earlier casks/assets stay unchanged.

RC5.20 adds specific first-failure retained-cleanup findings to doctor's normal
report and optional schema-2 redacted details. It preserves mutation refusals,
inspection ordering/budgets, native protection, no-follow checks and privacy.
Doctor does not repair data, test writes or establish a historical failure cause.

Required before commit: isolated RC5.19-to-RC5.20 executable replacement/removal,
strict native signature, notarization/quarantine, version/help, existing terminal,
script/pack and four-tool receipt-refresh checks. Fresh exact PR/main checks and
actual published-tap install/removal remain completion gates. Logs and COMPLETE
record outcomes separately; this note does not assert pending gates passed.

Personal installation/state/trust/sync are excluded. This is file placement on
an existing Mac, not clean-Mac/offline, live-agent/helper execution, migration,
stable support, Intel support or the standalone installer's recovery protocol.
