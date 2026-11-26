cask "kitrove" do
  version "0.1.0-rc.5.24"
  sha256 "5189f066efe4e09a4fb0995307a858df1e89c1335f423513a04f627c5b31370d"

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
