

import random
from pokemon import *


#listas para escolha aleatoria
NOMES = [
    'joao', 'mariano', 'fernandinando', 'gary', 'mary',
    'joseph', 'guilherme', 'maria' 
    ]

POKEMONS = [
    PokemonAgua(especie='squirdle'),
    PokemonAgua('magicarp'),
    PokemonAgua('vaporeon'),
    PokemonEletrico('pikachu'),
    PokemonEletrico('electrabuzz'),
    PokemonEletrico('Raichu'),
    PokemonFogo('charmander'),
    PokemonFogo('charmelion'),
    PokemonFogo('charizard')
    ]




class Personagens:
   
    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)
        self.pokemons = pokemons
        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome



    def mostrar_pokemons(self):
        if self.pokemons: 
            print('pokemons de {}:'.format(self))
            for index, pokemon in enumerate(self.pokemons):
                print('{} - {}'.format(index, pokemon))
        
        else: 
                print('{} não tem nunhum pokemon!'.format(self))

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print("{} escolheu {}".format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("{} não tem pokemons para serem escolhidos".format(self))


        #dinheiro
    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print('Você recebeu $ {}'.format(quantidade))
        self.mostrar_dinheiro()

    def mostrar_dinheiro(self):
        print("Você possui $ {} em sua conta".format(self.dinheiro))


        #combate
    def batalhar(self, adversario):
        print('{} iniciou uma batalha com {}'.format(self, Personagens))
       
        adversario.mostrar_pokemons()
        pokemon_inimigo = adversario.escolher_pokemon()
        pokemon = self.escolher_pokemon()
        

        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print('{} ganhou a batalha'.format(self))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break
                
                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print('{} ganhou a batalha!'.format(adversario))
                    break
        else:
            print('essa batalha não pode ocorrer')




class jogador(Personagens):
    tipo = 'jogador'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print('{} capturou {}'.format(self, pokemon))
        
    def escolher_pokemon(self):
        self.mostrar_pokemons()
        if self.pokemons:
            while True:
                escolha = input('Escolha seu pokemon:')
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print('{} eu escolho você!!!'.format(pokemon_escolhido))
                    return pokemon_escolhido
                    break
                except:
                    print('Escolha invalida!')
                
        else:
            print('{} não tem pokemons!'.format(self))



    def explorar(self):
        if random.random() <= 0.3:
            pokemon = random.choice(POKEMONS)
            print('um pokemon selvagem apareceu: {}'.format(pokemon))
            escolha = input("Deseja capturar pokemon? (s/n): ")
            if escolha == "s":
                if random.random() >= 0.5:
                    self.capturar(pokemon)
                else:
                    print("{} fugiu, que pena!!!".format(pokemon))
            else:
                print('O pokemon fugiu!')
        else:
            print('Exploração sem resultado!')



class adversario(Personagens):
    tipo = 'adversario'

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            pokemons_aleatorios = []
            for i in range(random.randint(1, 6)):
                pokemons_aleatorios.append(random.choice(POKEMONS))
            super().__init__(nome=nome, pokemons=pokemons_aleatorios)
            
        else:
            super().__init__(nome=nome, pokemons=pokemons)

