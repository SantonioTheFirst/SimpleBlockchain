import time
from Crypto.Hash import SHA256
import json


class Block:
    def __init__(self, creation_time=None, data=None) -> None:
        self.id = None
        self.creation_time = creation_time if creation_time != None else time.time()
        self.data = data if data != None else []
        self.previous_hash = None
        self.nonce = 0
        self.hash = self.get_hash()


    def __repr__(self) -> str:
        return json.dumps({
            'id': self.id,
            'creation_time': self.creation_time,
            'data': self.data,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce,
            'hash': self.hash
            }, indent=4)


    def get_hash(self) -> str:
        hash = SHA256.new()
        hash.update(str(self.id).encode('utf-8'))
        hash.update(str(self.creation_time).encode('utf-8'))
        hash.update(str(self.data).encode('utf-8'))
        hash.update(str(self.previous_hash).encode('utf-8'))
        hash.update(str(self.nonce).encode('utf-8'))
        return hash.hexdigest()


    def mine(self, difficulty: int) -> None:
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.get_hash()


if __name__ == '__main__':
    block = Block()
    print(block)
    difficulty = 5

    start = time.time()
    block.mine(difficulty)
    print(block)
    print(time.time() - start)