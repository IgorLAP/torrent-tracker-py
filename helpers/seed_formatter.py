def seed_formatter(seed: str):
    seed.replace('\n', '')
    if seed is None:
        return seed
    if not seed.__contains__('K') or seed.__contains__(','):
        return int(seed.replace(',', ''))
    if seed.__contains__('.'):
        return int(seed.replace('.', '').replace('K', '00'))
    return int(seed.replace('K', '000'))