cask "kitrove" do
  version "0.1.0-rc.5.17"
  sha256 "b94d48341e2bfbc8b991fe1871d19c61853ebec496fb6349999b04472acf5a4e"

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
