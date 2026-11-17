# Kitrove RC5.15 Homebrew review

- [Signed preview](https://github.com/Kapital-Labs/kitrove/releases/tag/v0.1.0-rc.5.15)
- Source commit `dfe5303dbf8fcb5a2eadcfdec8d7e6d1b5c3ac02`
- [Protected release run](https://github.com/Kapital-Labs/kitrove/actions/runs/44190793971)
- Apple Silicon CLI archive SHA-256 `832e42b4050bbb3218e058a55d40f511882bc2c7cc9a4e1fbad7d10ba94853c7`
- Apple Silicon CLI executable SHA-256 `e09516de1ad53f1c834c1c94577abf1642598df8c75b3083b7e199556e3dcc91`

Independent verification covered all 21 public files, 14 exact-source attestations,
notice bytes across six archives and the authenticated signed/notarized native ARM
installer image. The current `kitrove` cask selects that verified CLI archive.

RC5.15 adds collection directly from scan, grouped source/content status and a
tool-first guided flow across Claude, Codex, Pi and OpenCode. Existing ownership,
trust, exact approvals and sync boundaries remain. No dependency graph, state
format or signing policy change is introduced. Intel support and the other
package channels remain unchanged.

This remains fresh-install evaluation. Disposable executable replacement/removal,
native signature/notarization/quarantine and terminal checks precede commit;
exact public PR/main and published-tap installation checks precede promotion
claims. These checks do not establish collection migration, rollback support or
clean-Mac/offline launch. Personal installation, state and sync are excluded.
