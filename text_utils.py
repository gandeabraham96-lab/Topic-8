def truncate(text, max_length):
    if len(text) <= max_length:
        return text
    else:
        return text[:max_length] + "..."