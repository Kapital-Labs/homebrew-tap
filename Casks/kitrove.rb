cask "kitrove" do
  version "0.1.0-rc.5.5"
  sha256 "7e603b3a9fb7dc855dcb693dac9b1729310e29531559708fd647d76e28f25f81"

  url "https://github.com/Kapital-Labs/kitrove/releases/download/v#{version}/kitrove-cli-aarch64-apple-darwin.tar.xz"
  name "Kitrove"
  desc "Portable agent environment management"
  homepage "https://github.com/Kapital-Labs/kitrove"

  livecheck do
    skip "Release candidates require reviewed provenance and native acceptance"
  end

  conflicts_with cask: ["kitrove-rc", "kitrove-rc@5.5"]
  depends_on arch: :arm64
  depends_on :macos

  binary "kitrove-cli-aarch64-apple-darwin/kitrove"

  caveats <<~EOS
    Fresh-install evaluation only; not an RC4.2 upgrade or migration.
    Use a new isolated collection and empty destinations with disposable capabilities.
    Do not open RC4.2 collections or use RC4.2 to open RC5.5 collections.
    Homebrew manages this executable, not your Kitrove state.
    Do not point kitrove-installer at this Homebrew-managed installation.
    Clean-Mac online/offline first launch remains unverified.
  EOS
end
