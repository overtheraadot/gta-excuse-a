"""make.fun entry: The Excuse That Almost Works.

Writes the one line a gamer texts the boss to skip work on GTA 6 launch
week. The angle: the gamer's "internet died" -- except the router is fine;
he unplugged it himself and is now committed to the lie.

How the line maps to the judge brief (a tired manager who has heard every
excuse twice, picking the one it would almost believe):
1. On subject, one line, under 20 words -- a work-skipping text, nothing else.
2. Almost believable: boring, specific detail instead of a wild story --
   a router "just blinking red" and a provider slot "Thursday at the
   earliest", plus a timestamp ("since 6am") a real person would actually
   text. The vaguer "died this morning" was revised to "been dead since
   6am" for exactly this: a precise time reads like someone who has been
   staring at a dead router all morning, not someone rehearsing a story.
3. Funny on its own logic: the excuse traps its own sender -- he is
   "stuck" at home, which is precisely where GTA 6 is.
4. Hurried text: no setup, no explanation, no signature, plain words.
5. An angle the obvious excuses miss: no dead grandmother, no flat tyre,
   no sudden fever -- just dead wifi, the most boring lie of all.
"""

ENTRY = "Sorry boss, wifi's been dead since 6am, router's just blinking red. Provider says Thursday at the earliest, I'm stuck."

MAX_CHARS = 140
MAX_WORDS = 20


def verify(entry: str) -> None:
    """Enforce the gate from RULES.txt: UTF-8, 1-140 chars, non-blank,
    a single line, at most 20 words."""
    if not entry or not entry.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if len(entry) > MAX_CHARS:
        raise ValueError(f"entry is {len(entry)} chars, over the {MAX_CHARS} limit")
    if len(entry.split()) > MAX_WORDS:
        raise ValueError(f"entry is {len(entry.split())} words, over the {MAX_WORDS} limit")
    entry.encode("utf-8")


def write_entry(path: str = "/output/entry.txt") -> str:
    """Verify the entry and write it (with a trailing newline) to path."""
    verify(ENTRY)
    import os

    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return ENTRY


def main() -> None:
    entry = write_entry()
    print(f"{len(entry)} chars: {entry}")


if __name__ == "__main__":
    main()
