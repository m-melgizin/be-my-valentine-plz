from fontTools import subset

EMOJIS = "💕💗💝💚💔🥺🥰😢🎉❤💖🧸💎💌"

if __name__ == "__main__":
    unicodes = set()
    for ch in EMOJIS:
        unicodes.add(ord(ch))
        unicodes.add(0xFE0F)

    unicode_str = ",".join(f"U+{cp:04X}" for cp in sorted(unicodes))

    args = [
        "assets/fonts/AppleColorEmoji.ttf",
        f"--unicodes={unicode_str}",
        "--output-file=assets/fonts/AppleColorEmoji.woff2",
        "--flavor=woff2",
        "--no-hinting",
    ]

    subset.main(args)
    print("Done! Check AppleColorEmoji.woff2")
