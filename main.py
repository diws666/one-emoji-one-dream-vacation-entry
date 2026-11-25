import os

# U+1F3D6 U+FE0F — 7 bytes UTF-8, exactly one emoji
EMOJI = "\U0001f3d6\U0000fe0f"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(EMOJI)
