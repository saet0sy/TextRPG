from actors.enemy import Enemy
from actors.player import Player
from events.fight import Fight
from items.storage import Storage
from locations.location import Location

# player = Player(first_name="Player", inventory=Storage([]),
#                 hp=100, attack_point=10)
# enemies = [
#     Enemy(first_name="Enemy", inventory=Storage([]), hp=40, attack_point=10),
#     Enemy(first_name="Enemy", inventory=Storage([]), hp=40, attack_point=40),
#     Enemy(first_name="Enemy", inventory=Storage([]), hp=40, attack_point=10)
# ]

# while player.is_alive():
#     for enemy in enemies:
#         Fight.fight_without_steps(player, enemy)
#         if not player.is_alive():
#             break

# if player.is_alive():
#     print("You won!")
# else:
#     print("Wasted!")

