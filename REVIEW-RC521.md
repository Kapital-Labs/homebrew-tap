# Kitrove RC5.21 Homebrew review

- [Published preview](https://github.com/Kapital-Labs/kitrove/releases/tag/v0.1.0-rc.5.21)
- Source commit `4529533a6f00aa690f257cb110948c42426165dc`
- [Protected release workflow](https://github.com/Kapital-Labs/kitrove/actions/runs/45489441648)
- Apple Silicon CLI archive SHA-256 `5e2245d0598d75bee87e5eb31f2a7ea5f0ff5bd46575a408bf9a78239662dece`
- Apple Silicon CLI executable SHA-256 `6a61eead98043fd772709b68d45fe62030dcab4ed1bf12c38b5e0778b6ffc7a1`

Independent verification checked 21 public files, 14 exact-source attestations,
notice bytes in six archives and the native Apple Silicon installer image.

The preview adds a ready-only option after a blocked bulk selection, puts the
full list of selection commands under `help`, and identifies Unix device or
file identity mismatches in doctor. Placement still requires approval.

Homebrew checks cover an isolated upgrade from RC5.20, native signature,
notarization, quarantine and executable removal. The tap workflow checks
package metadata and the older, separately pinned casks.
