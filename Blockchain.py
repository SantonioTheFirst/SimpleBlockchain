import time
from Block import Block
import json


class Blockchain:
    def __init__(self, difficulty: int, block_time: int) -> None:
        genesis_block = Block(data=['Genesis block'])
        genesis_block.id = 0
        self.blockchain = [genesis_block]
        self.difficulty = difficulty
        self.block_time = block_time
    

    def __repr__(self) -> str:
        return json.dumps(
            [
                {
                    'id': block.id,
                    'creation_time': block.creation_time,
                    'data': block.data, 'previous_hash': block.previous_hash,
                    'nonce': block.nonce, 'hash': block.hash

                } for block in self.blockchain
            ], indent=4
        )


    def get_last_block(self) -> Block:
        return self.blockchain[-1]


    def add_block(self, block: Block) -> None:
        block.id = self.get_last_block().id + 1
        block.previous_hash = self.get_last_block().hash
        block.hash = block.get_hash()
        block.mine(self.difficulty)
        self.blockchain.append(block)
        self.difficulty += 1 if time.time() - self.get_last_block().creation_time < self.block_time else -1


    def check(self) -> bool:
        for i in range(1, len(self.blockchain)):
            if self.blockchain[i].hash != self.blockchain[i].get_hash():
                return False
            elif self.blockchain[i].previous_hash != self.blockchain[i - 1].hash:
                return False
            elif self.blockchain[i].creation_time <= self.blockchain[i - 1].creation_time:
                return False
            elif self.blockchain[i].id != self.blockchain[i - 1].id + 1:
                return False
            else:
                return True


if __name__ == '__main__':
    bch = Blockchain(1, 10)

    for i in range(10):
        start = time.time()
        t = Block(data=[f'{i} block with data'])
        bch.add_block(t)
        print(time.time() - start, bch.check())
        print(bch.blockchain[-1])

    print(bch)

