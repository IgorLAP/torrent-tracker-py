def query_formatter(query: str, provider: str):
    first_pattern = {
        " ": "%20",
        "'": "",
        "/": "",
    }

    second_pattern = {
        " ": "-",
        "'": "%20",
        "/": "-",
    }

    third_pattern = {
        " ": "+",
        "'": "%27",
        "/": "%2F",
    }

    keys: list[str]
    values: list[str]

    if provider == "seven" or provider == "torrentCsv":
        keys = list(first_pattern.keys())
        values = list(first_pattern.values())
    elif provider == "torrentGalaxy" or provider == "solidTorrents":
        keys = list(third_pattern.keys())
        values = list(third_pattern.values())
    else:
        keys = list(second_pattern.keys())
        values = list(second_pattern.values())

    it_needs_formatter = False
    for key in keys:
        if query.strip().__contains__(key):
            it_needs_formatter = True
            break

    if not it_needs_formatter:
        return query.strip()

    replaces: list[str] = []
    for index in range(len(keys)):
        if len(replaces) > 0 and replaces[index - 1]:
            replaces.append(replaces[index - 1].strip().replace(keys[index], values[index]))

        if len(replaces) == 0 and query.strip().__contains__(keys[index]):
            replaces.append(query.strip().replace(keys[index], values[index]))

    return replaces[len(replaces) - 1]
