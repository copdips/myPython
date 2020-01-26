def add_key(data):
    data.update({"k1": "v1"})

def call_add_key(data, message):
    add_key(data)
    data["message"] = message
    return data
