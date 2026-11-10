# RC5.11 cask review

The `kitrove` cask selects the signed Apple Silicon CLI from
[Kitrove 0.1.0-rc.5.11](https://github.com/Kapital-Labs/kitrove/releases/tag/v0.1.0-rc.5.11).
This preview is for fresh-install evaluation with an isolated collection.

- Source commit `694d097e89e417745f649a3e528d6f240c86a543`
- Annotated tag object `221bd164f083118762b42cbee6406eb87190692f`
- Protected release [42874731000](https://github.com/Kapital-Labs/kitrove/actions/runs/42874731000), attempt 1
- CLI archive SHA-256 `0faa29e3e888759d82e3f25b2a2dc7090ac5d32853e50a37326721bf9f149542`
- Executable SHA-256 `9248cc507daeea6fbaf40312185e99d9ff2c7e724705c9bbc6e657ddb1c981bc`
- Cask SHA-256 `90884cbc7478f6aeaa5a7fc4ccca2f11467df21c7f833b6964a1e2af4a4a0d06`

All eight protected release jobs passed. Independent verification matched all
21 published files, 14 provenance attestations, six archive notice inventories
and the native Apple Silicon installer image and payload. Temporary signing
activation was removed and its absence verified.

The current cask changes only its version and archive digest. Both legacy
casks and the workflows stay byte-identical. The tap README documents read-only
scan navigation and keeps the explicit Homebrew upgrade steps.

All 12 package tests passed, along with qualified Homebrew style, strict cask
audit and metadata inspection. RC5.10-to-RC5.11 executable replacement, fresh
install, strict Developer ID and notarization, retained quarantine, version,
help and removal passed in an isolated prefix. The signed packaged CLI also
passed a real-terminal inventory test with disposable inputs and unchanged
fixture bytes. Occupied paths and legacy conflicts refused replacement.

These tests cover the executable on an existing Apple Silicon Mac. Clean-Mac
first launch, collection migration and interrupted sync recovery remain
unverified. Verify the public cask after merging before advertising it.
