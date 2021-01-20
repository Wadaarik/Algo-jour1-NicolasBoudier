from hashlib import sha256
from datetime import datetime
import json


class Block:
    prevHash = None

    def __init__(self, data):
        self.data = data
        self.timestamp = str(datetime.now())
        self.nonce = 0
        self.hashActu = Block.calculateHash(self)
        self.previousHash = Block.prevHash
        Block.prevHash = self.hashActu

    def getData(self):
        return self.data

    def getDatetime(self):
        return self.timestamp

    def getNonce(self):
        return self.nonce

    def getHashActu(self):
        return self.hashActu

    def getPreviousHash(self):
        return self.previousHash

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
        self.nbZero = zero
        self.zero = '0' * zero
        self.validity = False

    def addBlock(self, aBlock):
        self.block.append(aBlock)

    # Check que le hash precedent a le bon nbe de 0
    # Check si le hash actuel a le bon nbe de 0
    # Check si le hash precedent est bien equivaut au hash du block precedent
    def validityBlock(self):
        for index, ablock in enumerate(self.block):
            if index != 0:
                if ablock.prevHash[:self.nbZero] == self.zero \
                        and ablock.hashActu[:self.nbZero] == self.zero \
                        and ablock.previousHash == self.block[index - 1].getHashActu() \
                        and ablock.data \
                        and ablock.timestamp:
                    self.validity = True
            else:
                if ablock.prevHash[:self.nbZero] == self.zero \
                        and ablock.hashActu[:self.nbZero] == self.zero \
                        and ablock.data \
                        and ablock.timestamp:
                    self.validity = True

        return self.validity

    def getBlockchain(self):
        for index, ablock in enumerate(self.block):
            print('Block #' + str(index) + ' [')
            print('    Précédent hash : ' + str(ablock.previousHash))
            print('    Timestamp : ' + str(ablock.timestamp))
            print('    Data : ' + ablock.data)
            print('    Hash : ' + str(ablock.hashActu))
            print('    Nonce : ' + str(ablock.nonce))
            print('] \n')

    def deleteLastBlock(self):
        self.block.pop()
        Block.prevHash = self.block[-1].hashActu

    def saveBlockchain(self):
        dateUse = str(datetime.now().strftime("%y%m%d-%H_%M_%S"))
        print('Le fichier est : ' + dateUse + '.json')
        json_file = open("saveBlockchain-" + dateUse + '.json', "w")
        json_file.write(json.dumps(self.block, default=lambda x: x.__dict__))
        json_file.close()


blockchain = Blockchain(3)

nbBlock = int(input('Combien de block voulez-vous créer ? '))

for x in range(nbBlock):
    data = input('Veuillez rentrer une donnée pour le block n°' + str(x + 1) + ' : ')
    b = Block(data)
    blockchain.addBlock(b)

    if x != 0:
        toDeleteLastBlock = input('Voulez-vous supprimer le dernier block ? (y/n) ')
        if toDeleteLastBlock == 'y' or toDeleteLastBlock == 'yes':
            blockchain.deleteLastBlock()

toSave = input('\nVoulez-vous sauvegarder la blockchain dans un ficher ? (y/n) ')
if toSave == 'y' or toSave == 'yes':
    blockchain.saveBlockchain()

print('\nBlockchain validity: ' + str(blockchain.validityBlock()))
blockchain.getBlockchain()
