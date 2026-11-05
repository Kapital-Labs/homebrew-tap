cask "kitrove" do
  version "0.1.0-rc.5.8"
  sha256 "269d096bf0e6c4dfee496efa4328a6b505e33fac7bd4b9acc1b13e471a849bf2"

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
    Fresh-install preview. Start with: kitrove init
    Setup and compatibility: https://kitrove.dev/docs/
  EOS
end
