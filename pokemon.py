import random
class Pokemon: #classe de pokemons

    def __init__(self, especie, level=None, nome=None):
        self.especie = especie
        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)
        if nome:
            self.nome = nome
        else:
            self.nome = especie

        self.vida = self.level * 8
        self.ataque = self.level

    def __str__(self):
        return '{} (lv: {})'.format(self.nome, self.level)

    def atacar(self, pokemon): 
        ataque_efetivo = int(self.ataque * random.random() * 1.3)
        pokemon.vida -= ataque_efetivo
        print('{} perdou {} pontos de vida'.format(pokemon, ataque_efetivo))

        if pokemon.vida <= 0:
            print('{} foi derrotado'.format(pokemon))
            return True
        else:
            return False

class PokemonFogo(Pokemon):
    tipo = 'fogo'
    def atacar(self, pokemon):
        print("{} cuspiu uma labareda de fogo em {}!".format(self, pokemon))
        super().atacar(pokemon)

class PokemonAgua(Pokemon):
    tipo = 'agua'
    def atacar(self, pokemon):
        print("{} lançou um jato molhado em {}".format(self, pokemon))
        super().atacar(pokemon)

class PokemonEletrico(Pokemon):
    tipo = 'eletrico'
    def atacar(self, pokemon):
        print("{} lançou um choque do travão em {}!".format(self, pokemon))
        super().atacar(pokemon)
