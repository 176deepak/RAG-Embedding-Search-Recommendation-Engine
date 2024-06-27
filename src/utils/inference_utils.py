

def extract_ids(records:list[dict]) -> list[str]:
    ids = []
    for record in records:
        id = record['id']
        ids.append(id)

    return ids