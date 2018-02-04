def fit(text, size):
    """
    Fit the text to the given size
    """
    size = int(size)
    if size <= 1 or len(text) <= size:
        return text.ljust(size)
    return text[:size - 1] + "\u2026"


def fit_wrapped(text, size):
    """
    Break text into a list of lines to fit a section
    so the text is all displayed without ellipsis
    """
    size = int(size)
    if size <= 1 or len(text) <= size:
        return [text.ljust(size)]
    lines = []
    while len(text) > size:
        line = text[:size]
        new_line = line.find("\n")
        if new_line != -1:
            lines.append(text[:new_line])
            text = text[new_line + 1:]
            continue
        space = line.rfind("\s")
        if space == -1:
            space = size

        lines.append(text[:space])
        text = text[space + 1:]
    if len(text) > 0:
        lines.append(text)
    return lines
