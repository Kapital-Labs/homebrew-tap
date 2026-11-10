# RC5.10 cask review

The `kitrove` cask selects the signed Apple Silicon CLI from
[Kitrove 0.1.0-rc.5.10](https://github.com/Kapital-Labs/kitrove/releases/tag/v0.1.0-rc.5.10).
This preview is for fresh-install evaluation with an isolated collection.

- Source commit `0a1df04cd1c9b53ae082fbe73756b6f6bcea4f78`
- Annotated tag object `00320c48a183f5e9ad3e96758b231b38b60f3da7`
- Protected release [42725905091](https://github.com/Kapital-Labs/kitrove/actions/runs/42725905091), attempt 1
- CLI archive SHA-256 `4c0bc02e074801ad1949592f881de8a18f456a4e5e0940908b9a3261be505350`
- Executable SHA-256 `3c7837c7378b42d5da0aa2a616995c5279ec1a560b7d353e34dca6c708e43a6e`
- Cask SHA-256 `708b7bf779beef8998d317d42231446cfbffcd43f955110c1ea0ebc675b3262f`

All eight release jobs passed. Independent verification matched all 21 release
files, checked 14 attestations against the release source and signing workflow,
matched notice bytes to source in all six archives, and verified the native
Apple Silicon installer image and its exact payload with a read-only mount.
Both temporary signing markers were absent after publication.

Only the current cask's version and digest change. The tests pin its complete
contents and the legacy casks. The current setup guidance covers the numbered
source choice, preserved exclusions and summary counts for skipped skills.
Selecting a source opens a new preview with its own confirmation.

All 12 package tests passed, along with Homebrew style, strict cask audit and
JSON inspection of the version and digest. In an isolated Homebrew prefix on
Apple Silicon, normal RC5.9-to-RC5.10 executable replacement, fresh installation
and removal passed. The installed executable matched the verified digest and
passed strict Developer ID, notarization, version and help checks with quarantine
retained. Existing legacy casks and occupied executable paths refused
replacement, and synthetic collection and local-state files stayed byte-identical.

These tests cover the executable on an existing Apple Silicon Mac. Clean-Mac
first launch, collection migration and interrupted sync recovery remain
unverified. Verify the public cask again after merging before advertising it.
