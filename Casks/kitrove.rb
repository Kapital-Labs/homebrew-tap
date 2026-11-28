cask "kitrove" do
  version "0.1.0"
  sha256 "9e2cafbc025a4ae72e9715b6e3ad3f50fad37b3c5deef3905ee6927e0865da16"

  url "https://github.com/Kapital-Labs/kitrove/releases/download/v#{version}/kitrove-cli-aarch64-apple-darwin.tar.xz"
  name "Kitrove"
  desc "Portable agent environment management"
  homepage "https://github.com/Kapital-Labs/kitrove"

  livecheck do
    skip "Updates require reviewed provenance and native acceptance"
  end

  conflicts_with cask: ["kitrove-rc", "kitrove-rc@5.5"]
  depends_on arch: :arm64
  depends_on :macos

  binary "kitrove-cli-aarch64-apple-darwin/kitrove"

  caveats <<~EOS
    Start with: kitrove
    Setup and compatibility: https://kitrove.dev/docs/
  EOS
end
