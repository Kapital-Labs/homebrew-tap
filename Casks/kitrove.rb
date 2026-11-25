cask "kitrove" do
  version "0.1.0-rc.5.23"
  sha256 "eeeedcc583daf23846e3771670148a1c29f716c3347d5cc5548ee9e50c05cb70"

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
    Fresh-install preview. Start with: kitrove
    Setup and compatibility: https://kitrove.dev/docs/
  EOS
end
