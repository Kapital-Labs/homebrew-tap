# Kitrove RC5.14 Homebrew review

- [Signed preview](https://github.com/Kapital-Labs/kitrove/releases/tag/v0.1.0-rc.5.14)
- Source commit `dcd5fe5414d525111b49145375fc152579257306`
- [Protected release run](https://github.com/Kapital-Labs/kitrove/actions/runs/43918492833)
- Apple Silicon CLI archive SHA-256 `59bf73c3f490f367d0ffff2bb32a7820836986eb3aa25b027c43d6c561f8ac14`
- Apple Silicon CLI executable SHA-256 `3c0f53ab8867ec795db0507fa86c8834273607e97d79214526e5c01eeac2fa01`

Independent verification covered the complete public inventory of 21 files,
14 exact-source attestations, source notice bytes across six archives and
native verification of the signed, notarized Apple Silicon installer image.
Homebrew selects that verified CLI archive using the existing `kitrove` cask.

The preview includes closed-pipe and Windows path-root fixes, reviewed SSH and
filesystem dependency patches, and safe hosted Apple authentication diagnostics.
Intel support, Linux package versions, WinGet and historical casks are unchanged.

This is fresh-install evaluation. Isolated Homebrew executable replacement and
removal tests use disposable canaries and do not establish collection migration,
rollback support or clean-Mac/offline first launch. Personal installations and
synchronization are excluded from verification.

Package tests, style, strict audit, native signature/notarization/quarantine,
version/help and executable upgrade/removal checks must pass before commit;
exact public PR and merged-main checks precede publication claims.
