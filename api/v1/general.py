"""General API endpoints."""

def test(name:str):
    """A test endpoint just to see if i understand what connexion/openAPI is doing."""
    return jsonify({'response': f"Hello, world! And hello to {name}!"})

def search(q:str) -> dict:
    """Stub for search function"""
    return {'results': []}

def license(q:str) -> dict:
    """Stub for license function"""
    return {'results': []}

