from classes.game import person, bcolors
from classes.magic import spell
from classes.inventory import item

fire = spell("fire", 10, 100, "rage")  # attacking spells
thunder = spell("thunder", 30, 120, "rage")
shocker = spell("shocker", 50, 150, "rage")
meteor = spell("meteor", 70, 170, "rage")
quake = spell("quake", 100, 200, "rage")

potion = item('potion', 'potion', 'heals 50 hp', 50)  # items
hipotion = item('hipotion', 'potion', 'heals 100 hp', 100)
megapotion = item('megapotion', 'potion', 'heals 500 hp', 500)
elixir = item('elixir', 'potion', 'fully heals', 9999)

grenade = item('grenade', 'bomb', 'deals 500 damage', 500)  # attacking item

cure = spell("cure", 12, 120, "heal")  # healing spells
aid = spell("aid", 14, 150, "heal")

# instantiate
player1 = person('pekka', 465, 60, 30, 34, [fire, thunder, shocker, meteor, quake, cure, aid],
                 [potion, hipotion, megapotion, elixir, grenade])
player2 = person('goblin', 800, 100, 30, 34, [fire, thunder, shocker, meteor, quake, cure, aid],
                 [potion, hipotion, megapotion, elixir, grenade])
player3 = person('giant', 950, 150, 30, 34, [fire, thunder, shocker, meteor, quake, cure, aid],
                 [potion, hipotion, megapotion, elixir, grenade])
enemy = person('witch', 1000, 600, 200, 45, [], [])

players = [player1, player2, player3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + 'ENEMY ATTACKS!' + bcolors.ENDC)

while running:
    print('***************************')
    print('\n')
    # printing stats
    player1.stats()
    print('\n')
    for player in players:  # calling action for different players
        player.choose_action()  # calling action function
        # player.choose_spell_magic()  # calling spell function
        choice = input('choose your action:')
        index = int(choice) - 1  # to satisfy array list indexing
        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print('you attacked for', dmg, 'points of damage. enemy hp:', enemy.get_hp())
        # print('you selected', player.get_spell_name(int(choice) - 1))
        # running = False

        elif index == 1:
            player.choose_spell_magic()
            magic_choice = int(input('choose your spell:')) - 1
            if magic_choice == -1:
                continue

            # magic_dmg = player.generate_spell_damage(magic_choice)
            # spell = player.get_spell_name(magic_choice)
            # cost = player.get_spell_mp_cost(magic_choice)

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()
            if spell.cost > current_mp:
                print(bcolors.FAIL + '\nyou are out of mp!' + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == 'heal':
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + "heals for" + str(magic_dmg + "hp" + bcolors.ENDC))
            elif spell.type == 'rage':
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + '\n' + spell.name + 'deals', str(magic_dmg), 'pojnts of damage' + bcolors.ENDC)

        elif index == 2:
            player.choose_item()
            item_choice = int(input('choose your item:')) - 1
            if item_choice == -1:
                continue
            item = player.items[item_choice]

            if item.type == 'potion':
                player.heal(item.prop)
                print(bcolors.OKGREEN + '\n' + item.name + ' heals for', str(item.prop), 'hp' + bcolors.ENDC)
            elif item.type == 'bomb':
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + '\n' + item.name + ' damages for', str(item.prop), 'hp' + bcolors.ENDC)

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player1.take_damage(enemy_dmg)
    print('enemy attacks for', enemy_dmg)
    print('--------------------------------------')
    print('enemy hp:', bcolors.FAIL + str(enemy.get_hp()) + '/' + str(enemy.get_max_hp()) + bcolors.ENDC + '\n')
    print('your hp:', bcolors.OKGREEN + str(player.get_hp()) + '/' + str(player.get_max_hp()) + bcolors.ENDC + '\n')
    print('your mp:', bcolors.OKBLUE + str(player.get_mp()) + '/' + str(player.get_max_mp()) + bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + 'you WIN!' + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + 'you are LOST!' + bcolors.ENDC)
        running = False
