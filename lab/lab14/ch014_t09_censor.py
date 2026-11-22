def censor(text: str, word: str) -> str:
    result = []
    for s in text.split():
        if s == word:
            result.append("*" * len())
        else:
            result.append(s)
