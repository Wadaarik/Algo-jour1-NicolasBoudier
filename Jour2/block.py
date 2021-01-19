from hashlib import sha256
from datetime import datetime


class Block:
    prevHash = None

    def __init__(self, data):
        self.data = data
        self.timestamp = datetime.now()
        self.nonce = 0
        self.hashActu = Block.calculateHash(self)
        self.previousHash = Block.prevHash
        Block.prevHash = self.hashActu

    def getDatetime(self):
        print(self.timestamp)

    def getData(self):
        print(self.data)

    def getHashActu(self):
        # print(self.hashActu)
        return self.hashActu

    def calculateHash(self):
        bloc = str(Block.prevHash) + str(self.timestamp) + str(self.data) + str(self.nonce)
        hashe = sha256(bloc.encode('utf-8')).hexdigest()

        while hashe[:3] != '000':
            self.nonce += 1
            bloc = str(Block.prevHash) + str(self.timestamp) + str(self.data) + str(self.nonce)
            hashe = sha256(bloc.encode('utf-8')).hexdigest()

        return sha256(bloc.encode('utf-8')).hexdigest()


class Blockchain():
    def __init__(self, zero):
        self.block = []
        self.zero = '0'*zero
        self.validity = False

    def addBlock(self, aBlock):
        self.block.append(aBlock)

    def validityBlock(self):
        for index, ablock in enumerate(self.block):
            if ablock.prevHash[:3] == self.zero and index != 0 \
                    and ablock.hashActu[:3] == self.zero \
                    and ablock.previousHash == self.block[index - 1].getHashActu():
                self.validity = True

        return self.validity

    def getBlockchain(self):
        for index, ablock in enumerate(self.block):
            print('Block #' + str(index) + ' [')
            print('    Précédent hash : ' + str(ablock.previousHash))
            print('    Timestamp : ' + str(ablock.timestamp))
            print('    Data : ' + ablock.data)
            print('    Hash : ' + str(ablock.hashActu))
            print('] \n')


block1 = Blockchain(3)

b0 = Block("loituma")
b1 = Block("gerard")
b2 = Block("testos")

block1.addBlock(b0)
block1.addBlock(b1)
block1.addBlock(b2)

print('Blockchain validity: ' + str(block1.validityBlock()))
block1.getBlockchain()