cask "kitrove-rc" do
  version "0.1.0-rc.4.2"
  sha256 "cfac95704204b675b577d668ee9de8a0d6495a28684a368d443c5acc40264d39"

  url "https://github.com/Kapital-Labs/kitrove/releases/download/v#{version}/kitrove-cli-aarch64-apple-darwin.tar.xz"
  name "Kitrove Release Candidate"
  desc "Portable agent environment management"
  homepage "https://github.com/Kapital-Labs/kitrove"

  livecheck do
    skip "Release candidates require reviewed provenance and native acceptance"
  end

  depends_on arch: :arm64
  depends_on :macos

  binary "kitrove-cli-aarch64-apple-darwin/kitrove"

  caveats <<~EOS
    This is a prerelease. Homebrew manages this executable, not your Kitrove state.
    Do not point kitrove-installer at this Homebrew-managed installation.
    Clean-Mac offline first launch remains unverified.
  EOS
end
