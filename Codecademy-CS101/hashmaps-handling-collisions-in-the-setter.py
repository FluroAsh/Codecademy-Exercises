class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]
    
    # If no key is found at the arrays index
    if current_array_value is None:
      self.array[array_index] = [key, value]
      return
    
    # If both keys are the same, overwrite!
    elif current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return
    # If array holds a different key value
    return

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    return self.array[array_index]