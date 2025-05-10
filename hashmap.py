import numpy as np
from dataclasses import dataclass
import random
import string
from typing import Optional
import hashlib

@dataclass
class Entry:
    key: any
    value: any
    next: Optional['Entry'] = None

class Hashmap:
    def __init__(self, size: int, load_factor: float = 0.75):
        self.size = size
        self.count = 0
        self.base_array = np.empty(size, dtype=object)
        self.load_factor = load_factor
    
    def __str__(self):
        return self.base_array.__str__()
    
    def show_hashmap(self):
        for i in range(self.size):
            current = self.base_array[i]

            if current is None:
                print(f"bucket {i}: null")
                continue

            entries = []
            while current != None:
                key_repr = repr(current.key)
                value_repr = repr(current.value)
                entries.append(f"({key_repr}, {value_repr})")
                current = current.next
            
            print(f"bucket {i}: " + " -> ".join(entries))
        print()
        print(f"count: {self.count}")
        print(f"size: {self.size}")
        print(f"load_factor threshold: {self.load_factor}")
        print(f"actual load_factor: {self.count / self.size}")
            
    def _hash(self, key):
        key_bytes = str(key).encode('utf-8')
        hash_digest = hashlib.sha256(key_bytes).hexdigest()
        return int(hash_digest, 16) % self.size

    def _rehashing(self):
        old_array = self.base_array
        self.size *= 2
        self.base_array = np.empty(self.size, dtype=object)
        self.count = 0

        for entry in old_array:
            current = entry
            while current:
                self.set(current.key, current.value)
                current = current.next

    def set(self, key: any, value: any):
        index = self._hash(key)
        current = self.base_array[index]

        if current is None:
            self.base_array[index] = Entry(key, value)
            self.count += 1
        else:
            while True:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = Entry(key, value)
            self.count += 1
        
        if self.count / self.size >= self.load_factor:
            self._rehashing()
    
    def remove(self, key: any):
        index = self._hash(key)
        current = self.base_array[index]
        prev = None

        while current != None:
            if current.key == key:
                if prev is None:
                    self.base_array[index] = current.next
                else:
                    prev.next = current.next

                self.count -= 1
                return True
            
            prev = current
            current = current.next
        
        return False

    def get(self, key: any):
        index = self._hash(key)
        current = self.base_array[index]
        
        while current:
            if current.key == key:
                return current.value
            
            current = current.next
        
        return None
