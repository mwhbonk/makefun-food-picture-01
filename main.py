#!/usr/bin/env python3
"""food-picture-01 entry: write one food picture to /output/entry.png.

The picture is a steaming bowl of tonkotsu ramen in a black ceramic
bowl on a dark walnut table: glossy noodles lifted high by wooden
chopsticks, glistening chashu pork, a halved soft egg with a jammy
orange yolk, scallions, chilli-oil swirls and nori, with steam rising
in warm golden light. It is stored in this repository as base64 text
in food.jpg.b64 (a single line, so the repository holds no binary
files). The program decodes it and writes the JPEG bytes to
/output/entry.png.

No network, no randomness, no timestamps: two runs write the same bytes.
"""

import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "food.jpg.b64")
DST = "/output/entry.png"

# Hard limit from the competition brief (checked after decoding).
MAX_BYTES = 1_048_576  # 1 MiB


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(SRC, "r", encoding="ascii") as f:
        data = base64.b64decode(f.read())
    if data[:3] != b"\xff\xd8\xff":
        raise ValueError("decoded picture is not a JPEG file")
    if len(data) > MAX_BYTES:
        raise ValueError(
            "picture is %d bytes, over the 1 MiB limit" % len(data)
        )
    with open(DST, "wb") as out:
        out.write(data)
    print("wrote %s (%d bytes)" % (DST, len(data)))


if __name__ == "__main__":
    main()
