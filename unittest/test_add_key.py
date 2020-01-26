from unittest.mock import MagicMock

def add_key(data):
    # data.update({"k1": "v1"})
    data_copy = data.copy()
    data_copy.update({"k1": "v1"})
    return data_copy

def call_add_key(data, message, func):
    data_copy = func(data)
    data_copy["message"] = message
    return data_copy

def test_add_key_called_with_data():
    data = {"foo": "bar"}
    data_copy = data.copy()
    message = "hello"
    add_key = MagicMock()
    call_add_key(data, message, add_key)
    add_key.assert_called_with(data)
    # add_key.assert_called_with(data)

# class TestExample(unittest.TestCase):

#     def test_something(self):
#         data = {"foo": "bar"}
#         data_copy = data.copy()
#         message = "hello"
#         add_key = MagicMock()
#         r = call_add_key(data, message, add_key)
#         self.assertEqual(r, data_copy)
