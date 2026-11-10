# Kitrove RC5.12 Homebrew review

- [Signed preview](https://github.com/Kapital-Labs/kitrove/releases/tag/v0.1.0-rc.5.12)
- Source commit `de2cf846ada24b8fcf1c7b55036ff257ff534a7b`
- [Protected release run](https://github.com/Kapital-Labs/kitrove/actions/runs/42907249482)
- Apple Silicon CLI archive SHA-256 `63abd08dfda722750c5e457bebbff65be9a8ef734e3cd112418ce49b7092c9fb`
- Apple Silicon CLI executable SHA-256 `452d0d882a5001a003edbc153e9f28fc2d928c0ed7bd10865fbce91f9c2c1c3e`

Independent verification covered the exact public inventory of 21 files,
14 source-pinned attestations, notices across six application archives and
the signed, notarized Apple Silicon installer image. Homebrew installs the
verified Apple Silicon CLI archive under the existing `kitrove` cask.

RC5.12 fixes the guided HTTPS credential prompt and adds guidance for
creating an empty private repository before sharing. It is a fresh-install
evaluation preview. Homebrew verification uses an isolated prefix and
disposable canaries; an executable replacement does not establish migration
or rollback support for collection data.
