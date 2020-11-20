from personagens import *
from pokemon import *
import pickle

def pokemon_inicial(jogador):
    print('{} escolha o pokemon que irá lhe aconpanhar nesta jornada!'.format(jogador))

    pikachu = PokemonEletrico('Pikachu', level=1)
    charmander = PokemonFogo('Charmander', level=1)
    squirdle = PokemonAgua('Squirdle', level=1)

    print('1 -', pikachu)
    print('2 -', charmander)
    print('3 -', squirdle)
    
    while True:
        escolha = input('escolha o sue pokemon: ')
        if escolha == '1':
            jogador.capturar(pikachu)
            break
        elif escolha == '2':
            jogador.capturar(charmander)
            break
        elif escolha == '3':
            jogador.capturar(squirdle)
            break
        else:
            print('Opção invalida!')

def salvar():
    try:
        with open("database.db", 'wb') as arquivo:
            pickle.dump(jogador, arquivo)
            print('Jogo salvo com sucesso!')
            print('-----------------------')
    except Exception as error:
        print('erro ao salvar jogo')
        print(error)
    
def carregar():
    try:
        with open('database.db', 'rb') as arquivo:
            jogador = pickle.load(arquivo)
            print('Jogo carregado com sucesso')
            print('--------------------------')
            return jogador
    except Exception as error:
        print('erro ao carregar o jogo!')
        print(error)


        


if __name__ == "__main__":
    print('---------------------')
    print('Terminal Pokemon Game')
    print('---------------------')
    carregar()
    nome = input('Qual o seu nome? ')
    jogador = jogador(nome)

    print('Ola {} esse é um mundo habtado por pokemons,\na partir de agora sua missão é se tornar um mestre pokemon'.format(jogador))
    print('capture o maximo de pokemons que conseguir e lute com seus inimigos')
    print('--------------------------------')
    jogador.mostrar_dinheiro()
    print('--------------------------------')

    if jogador.pokemons:
        print('Vejo que tem alguns pokemons')
        jogador.mostrar_pokemons
    else:
        print('Voce não tem nenhum pokemon, precisa conversar com o Dr. J.J.Pokemon')
        pokemon_inicial(jogador)
    print('--------------------------------')

    print('Ótimo, seu arquinimigo do jardim de infancia acabou de sair daqui com um pokemon.')
    print('Va lá e enfrente ele!')
    gary = adversario('Gary', pokemons=[Pokemon('Zigzagon', level=1, nome='Julião')])

    jogador.batalhar(gary)

    while True:
        print('------------------')
        print('Oque deseja fazer?')
        print('------------------')
        print('1 - Explorar o mundo Pokemon')
        print('2 - Lutar com um inimigo')
        print('3 - Mostrar Pokedex')
        print('4 - Salvar jogo')
        print('5 - Carregar jogo')
        print('0 - Sair')
        print('-----------------')

        escolha = input('Sua escolha:')
        if escolha == '1':
            jogador.explorar()
            salvar
        elif escolha == '2':
            inimigo_aleatorio = adversario()
            jogador.batalhar(inimigo_aleatorio)
            salvar()
        elif escolha == '3':
            jogador.mostrar_pokemons
            salvar()
        elif escolha == '4':
            salvar()
        elif escolha == '5':
            carregar()
        elif escolha == '0':
            salvar()
            break
        else:
            print('Escolha invalida!')


