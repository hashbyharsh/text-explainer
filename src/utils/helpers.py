import hashlib
import re
from typing import Optional

def get_text_hash(selected_text: str, context: Optional[str], locale: str, simplify: bool) -> str:
    """Generate a hash of selected_text, context, locale, and simplify flag."""
    context = context or ""
    return hashlib.sha256((selected_text + context + locale + str(simplify)).encode()).hexdigest()

# def get_text_hash(selected_text: str, context: str | None, locale: str, simplify: bool) -> str:
#     """Generate a hash of selected_text, context, locale, and simplify flag."""
#     context = context or ""
#     return hashlib.sha256((selected_text + context + locale + str(simplify)).encode()).hexdigest()

def store_search_text(redis_client, selected_text: str, cache_key: str, ttl: int):
    """Store the search text in Redis with the same TTL as the cache."""
    redis_client.setex(f"search:{cache_key}", ttl, selected_text)

def is_gibberish(text: str) -> bool:
    """Check if the text appears to be gibberish using enhanced heuristics."""
    text = text.lower().strip()
    if not text or len(text) < 2 or len(text) > 20:  # Too short or unreasonably long
        return True
    # Whitelist for common valid short terms
    whitelist = {"ai", "io", "url", "id"}
    if text in whitelist:
        return False
    # Check for repeated characters (e.g., "aaa", "vvvv")
    if all(c == text[0] for c in text):
        return True
    # Check for numeric-only sequences (e.g., "123", "45678")
    if text.isdigit():
        return True
    # Check for special characters only (e.g., "@#$%", "!!!")
    if all(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in text):
        return True
    # Check for keyboard-like sequences (e.g., "qwrt", "asdf")
    keyboard_patterns = [r"qwertyuiop", r"asdfghjkl", r"zxcvbnm"]
    if any(re.search(pattern, text) for pattern in keyboard_patterns):
        return True
    # Check for lack of vowels and random consonant sequences
    vowels = set("aeiou")
    if not any(c in vowels for c in text) and len(text) > 3:
        return True
    # Check for mixed random strings (e.g., "a1b2c3", "x@y#z")
    if re.search(r"^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{}|;:,.<>?]{4,}$", text) and not any(c.isalpha() for c in text[1:]):
        return True
    return False