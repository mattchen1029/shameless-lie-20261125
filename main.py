import os

LIE = "I deleted nothing important."

MIN_CHARS = 1
MAX_CHARS = 88
MIN_WORDS = 1
MAX_WORDS = 5
OUTPUT_NAME = "entry.txt"


def validate_lie(lie):
    if not (MIN_CHARS <= len(lie) <= MAX_CHARS):
        raise ValueError("lie must be %d-%d chars, got %d" % (MIN_CHARS, MAX_CHARS, len(lie)))
    words = lie.split()
    if not (MIN_WORDS <= len(words) <= MAX_WORDS):
        raise ValueError("lie must be %d-%d words, got %d" % (MIN_WORDS, MAX_WORDS, len(words)))
    if "\n" in lie or "\r" in lie:
        raise ValueError("lie must be a single line")
    if not lie.strip():
        raise ValueError("lie must not be only whitespace")


def write_entry(lie, out_dir):
    validate_lie(lie)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, OUTPUT_NAME), "w", encoding="utf-8") as f:
        f.write(lie)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(LIE, out_dir)


if __name__ == "__main__":
    main()
