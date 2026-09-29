import urllib.request
from pathlib import Path

SOURCE = (
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/"
    "refs/heads/main/BLACK_VLESS_RUS_mobile.txt"
)

OUTPUT = Path("vpn.txt")


def main():
    print("Downloading source list...")

    request = urllib.request.Request(
        SOURCE,
        headers={"User-Agent": "karing-vpn-updater/1.0"}
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        data = response.read()

    OUTPUT.write_bytes(data)

    print(f"Saved {len(data)} bytes to {OUTPUT}")


if __name__ == "__main__":
    main()
