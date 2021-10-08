class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key):
    key_bytes = key.encode() # String method to convert it into bytes (list-like object)
    hash_code = sum(key_bytes) # Creates the hash code by adding all the bytes calculated from the method above
    return hash_code
