# Current Homebrew RC5.6 package review

Maintainer requested continuation through release and the plain kitrove package
as latest reviewed preview. New application release v0.1.0-rc.5.6 at
d306adb76af9380a3ac5ebd82add524fa293a0ed, annotated tagbf072cb31fa790d306f6db387483bad6e3b3690f,
run41566118041 attempt1, passed every protected release job. Independent verifier
checked all21assets/14exact-source attestations/six notice payloads/native ARM image
and exact reviewed release notes. No downloaded product was executed by that verifier.

Archiveabc42e83f27d585fb14734cc6f3cf6e29e50944c497fe8183ab64922bfdb4d40;
CLIaa96751956190a422405cfa31c9572d17feebbadaa52f9ad31288a2a53d85fb7;
cask128738bb6dbd07ad6705d9cd0c06766bca5a5a7fc262afc489b11ef4ff7c5286.
Current cask differs in ONLY version, archive digest and caveat version. Both
old casks are byte-identical; inventory remains3casks, no formula/hooks/zap/custom
installer/dynamic latest discovery. Existing conflicts/architecture/native checks
and ordinary Homebrew trust authority remain unchanged (ADR0046, NS07/08/09).

RC5.5-to-RC5.6 Rust source diff is ONLY setup.rs, setup/collection.rs and its tests.
No core/model/adapters/storage/state-lifecycle format, dependency graph or local
credential/trust/receipt behavior change. No schema migration or new data rollback
guarantee. Empty installer predecessor policy remains; Homebrew does not acquire
the standalone installer's locks or retained recovery kits. Binary replacement
is not data migration, and RC4.2 collections remain outside this preview scope.

Five baseline tests passed; new pin/onboarding assertions failed before changes.
All7 final tests passed, freezing current and historical casks and documented
selection/approval boundaries. Ruby parse/style/strict audit passed. Native warm
Apple Silicon private-prefix acceptance passed normal same-token55-to56 upgrade,
fresh6 install/removal, full DeveloperID/native notarization/quarantine/exact bytes/
version/help, both legacy-token conflicts, occupied and reverse refusals. Synthetic
canaries stayed byte-identical; older conflict fixture products were not executed.
The55 fixture separately authenticated before version/help. No real collection,
init/configure/scan, operator-prefix binary/state, permissions or trust change.

This is manual full-diff/source/evidence review, not independent-agent/exhaustive
assurance, clean-Mac/offline first launch, standard-prefix or real-state migration
acceptance. No Rust workspace exists in this tap; package/native checks apply,
not a new Rust/MSRV claim. Required public PR/main checks, green prior main and
postmerge actual public-command acceptance remain mandatory before completion.
No product re-signing, tag/release mutation, APT/RPM/WinGet/channel scope expansion,
new workflow permissions or resumption of paused readiness monitors.
