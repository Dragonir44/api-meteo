from Data.authors import authors

def get_author_by_id(id):
    for author in authors:
        if author["id"] == int(id):
            return author
    return None

def get_author_by_name(name):
    for author in authors:
        if author["name"] == name:
            return author
    return None