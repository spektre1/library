

def test(name:str):
    """A test endpoint just to see if i understand what connexion/openAPI is doing."""
    return jsonify({'response': f"Hello, world! And hello to {name}!"})
