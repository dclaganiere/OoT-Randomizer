import collections
from BaseClasses import Region, Location, Entrance, RegionType


def create_regions(world):

    world.regions = [
        create_ow_region('Kokiri Forest', ['Kokiri Sword Chest', 'GS1', 'GS2', 'GS3'], ['Links House', 'Mido House', 'Saria House', 'House of Twins', 'Know It All House', 'Kokiri Shop', 'Deku Tree', 'Lost Woods', 'Lost Woods Bridge']),
        create_interior_region('Links House', None, ['Links House Exit', 'Child Forest Warp Pad', 'Adult Forest Warp Pad', 'Temple Warp Pad', 'Crater Warp Pad', 'Lake Warp Pad', 'Graveyard Warp Pad']),
        create_interior_region('Mido House', ['Mido Chest Top Left', 'Mido Chest Top Right', 'Mido Chest Bottom Left', 'Mido Chest Bottom Right'], ['Mido House Exit']),
        create_interior_region('Saria House', None, ['Saria House Exit']),
        create_interior_region('House of Twins', None, ['House of Twins Exit']),
        create_interior_region('Know It All House', None, ['Know It All House Exit']),
        create_interior_region('Kokiri Shop', None, ['Kokiri Shop Exit']),
        create_dungeon_region('Deku Tree Lobby', ['Deku Tree Lobby Chest', 'Deku Tree Compass Chest', 'Deku Tree Compass Room Side Chest', 'Deku Tree Basement Chest', 'GS8', 'GS9', 'GS10'], ['Deku Tree Exit', 'Deku Tree Slingshot Passage', 'Deku Tree Basement Path']),
        create_dungeon_region('Deku Tree Slingshot Room', ['Deku Tree Slingshot Chest', 'Deku Tree Slingshot Room Side Chest'], ['Deku Tree Slingshot Exit']),
        create_dungeon_region('Deku Tree Boss Room', ['GS11', 'Queen Gohma'], ['Deku Tree Basement Vines']),        
        create_ow_region('Lost Woods', ['Skull Kid', 'Ocarina Memory Game', 'Target in Woods', 'Deku Salesman Woods', 'GS4', 'GS5'], ['Lost Woods Front', 'Meadow Entrance', 'Woods to Goron City', 'Lost Woods Dive Warp', 'Adult Meadow Access', 'Forest Generic Grotto', 'Deku Theater', 'Forest Sales Grotto']),
		create_ow_region('Sacred Forest Meadow Entryway', None, ['Meadow Exit', 'Meadow Gate', 'Front of Meadow Grotto']),
		create_ow_region('Sacred Forest Meadow', ['Song from Saria'], ['Meadow Gate Exit', 'Meadow Fairy Grotto']),
		create_ow_region('Lost Woods Bridge', ['Gift from Saria'], ['Kokiri Forest Entrance', 'Forest Exit']),
        create_ow_region('Hyrule Field', ['Ocarina of Time', 'Song from Ocarina of Time'], ['Field to Forest', 'Field to Lake', 'Field to Valley', 'Field to Castle Town', 'Field to Kakariko', 'Field to Zora River', 'Lon Lon Rance Entrance',
                                                     'Remote Southern Grotto', 'Field Near Lake Outside Fence Grotto', 'Field Near Lake Inside Fence Grotto', 'Field Valley Grotto', 'Field West Castle Town Grotto',
                                                     'Field Far West Castle Town Grotto', 'Field Kakariko Grotto', 'Field North Lon Lon Grotto']),
        create_ow_region('Lake Hylia', ['Underwater Bottle', 'GS55', 'GS56', 'GS57', 'GS58'], ['Lake Exit', 'Lake Hylia Dive Warp', 'Lake Hylia Lab', 'Fishing Hole', 'Water Temple Entrance', 'Lake Hylia Grotto']),
        create_interior_region('Lake Hylia Lab', ['Diving in the Lab', 'GS59']),
        create_interior_region('Fishing Hole', ['Child Fishing', 'Adult Fishing']),
        create_dungeon_region('Water Temple Lobby', ['Water Temple Map Chest', 'Water Temple Compass Chest', 'Water Temple Torches Chest', 'Water Temple Dragon Chest', 'Water Temple Central Bow Target Chest', 'Water Temple Boss Key Chest', 'Morpha', 'GS73', 'GS77'], ['Water Temple Exit', 'Water Temple Central Pillar', 'Water Temple Upper Locked Door']),
        create_dungeon_region('Water Temple Middle Water Level', ['Water Temple Central Pillar Chest', 'Water Temple Cracked Wall Chest', 'GS75']),
        create_dungeon_region('Water Temple Dark Link Region', ['Water Temple Dark Link Chest', 'Water Temple River Chest', 'GS74', 'GS76']),
        create_ow_region('Gerudo Valley', None, ['Valley Exit', 'Valley River']),
        create_ow_region('Castle Town', None, ['Castle Town Exit', 'Temple of Time', 'Hyrule Castle Grounds', 'Castle Town Rupee Room', 'Castle Town Bazaar', 'Castle Town Mask Shop', 'Castle Town Shooting Gallery', 'Ganons Castle Grounds',
                                               'Castle Town Bombchu Bowling', 'Castle Town Potion Shop', 'Castle Town Treasure Chest Game', 'Castle Town Bombchu Shop', 'Castle Town Dog Lady', 'Castle Town Man in Green House']),
        create_interior_region('Temple of Time', None, ['Temple of Time Exit', 'Door of Time']),
        create_interior_region('Beyond Door of Time', ['Master Sword Pedestal', 'Sheik at Temple', 'Ganon'], ['Emerge as Adult']),
        create_ow_region('Hyrule Castle Grounds', ['GS15'], ['Hyrule Castle Grounds Exit', 'Hyrule Castle Garden', 'Hyrule Castle Fairy', 'Castle Storms Grotto']),
        create_ow_region('Hyrule Castle Garden', ['Zeldas Letter', 'Impa at Castle'], ['Hyrule Castle Garden Exit']),
        create_interior_region('Hyrule Castle Fairy', ['Hyrule Castle Fairy Reward']),
        create_ow_region('Ganons Castle Grounds', ['GS17'], ['Ganons Castle Grounds Exit']),
        create_interior_region('Castle Town Rupee Room', ['10 Big Poes', 'GS14']),
        create_interior_region('Castle Town Bazaar'),
        create_interior_region('Castle Town Mask Shop'),
        create_interior_region('Castle Town Shooting Gallery', ['Child Shooting Gallery']),
        create_interior_region('Castle Town Bombchu Bowling', ['Bombchu Bowling Bomb Bag', 'Bombchu Bowling Piece of Heart']),
        create_interior_region('Castle Town Potion Shop'),
        create_interior_region('Castle Town Treasure Chest Game'),
        create_interior_region('Castle Town Bombchu Shop'),
        create_interior_region('Castle Town Dog Lady', ['Dog Lady']),
        create_interior_region('Castle Town Man in Green House'),
        create_ow_region('Kakariko Village', ['Man on Roof', 'Anjus Chickens', 'Sheik in Kakariko', 'GS22', 'GS23', 'GS24', 'GS25', 'GS26', 'GS27'], ['Kakariko Exit', 'Carpenter Boss House', 'House of Skulltulla', 'Impas House', 'Impas House Back', 'Windmill', 'Kakariko Bazaar', 'Kakariko Shooting Gallery', 'Bottom of the Well',
                                                                                                'Kakariko Potion Shop Front', 'Kakariko Potion Shop Back', 'Odd Medicine Building', 'Kakariko Bombable Grotto', 'Kakariko Back Grotto', 'Graveyard Entrance', 'Death Mountain Entrance']),
        create_interior_region('Carpenter Boss House'),
        create_interior_region('House of Skulltulla', ['10 Gold Skulltulla Reward', '20 Gold Skulltulla Reward', '30 Gold Skulltulla Reward', '40 Gold Skulltulla Reward', '50 Gold Skulltulla Reward']),
        create_interior_region('Impas House'),
        create_interior_region('Impas House Back'),
        create_interior_region('Windmill', ['Song at Windmill']),
        create_interior_region('Kakariko Bazaar'),
        create_interior_region('Kakariko Shooting Gallery', ['Adult Shooting Gallery']),
        create_interior_region('Kakariko Potion Shop Front'),
        create_interior_region('Kakariko Potion Shop Back'),
        create_interior_region('Odd Medicine Building'),
        create_dungeon_region('Bottom of the Well', ['Bottom of the Well Front Left Hidden Wall', 'Bottom of the Well Front Center Bombable', 'Bottom of the Well Right Bottom Hidden Wall', 'Bottom of the Well Center Large Chest', 'Bottom of the Well Center Small Chest', 'Bottom of the Well Back Left Bombable',
                                                     'Bottom of the Well Defeat Boss', 'Bottom of the Well Invisible Chest', 'Bottom of the Well Underwater Front Chest', 'Bottom of the Well Underwater Left Chest', 'Bottom of the Well Basement Chest', 'Bottom of the Well Locked Pits', 'Bottom of the Well Behind Right Grate', 'GS78', 'GS79', 'GS80'], ['Bottom of the Well Exit']),
        create_ow_region('Graveyard', ['GS28', 'GS29'], ['Shield Grave', 'Composer Grave', 'Heart Piece Grave', 'Dampes Grave', 'Dampes House', 'Graveyard Exit']),
        create_interior_region('Shield Grave', ['Shield Grave Chest']),
        create_interior_region('Heart Piece Grave', ['Heart Piece Grave Chest']),
        create_interior_region('Composer Grave', ['Composer Grave Chest', 'Song from Composer Grave']),
        create_interior_region('Dampes Grave', ['Hookshot Chest']),
        create_interior_region('Dampes House'),
        create_ow_region('Shadow Temple Warp Region', None, ['Drop to Graveyard', 'Shadow Temple Entrance']),
        create_dungeon_region('Shadow Temple Beginning', ['Shadow Temple Map Chest', 'Shadow Temple Hover Boots Chest'], ['Shadow Temple Exit', 'Shadow Temple First Pit']),
        create_dungeon_region('Shadow Temple First Beamos', ['Shadow Temple Compass Chest', 'Shadow Temple Early Silver Rupee Chest'], ['Shadow Temple Bomb Wall']),
        create_dungeon_region('Shadow Temple Huge Pit', ['Shadow Temple Invisible Blades Visible Chest', 'Shadow Temple Invisible Blades Invisible Chest', 'Shadow Temple Falling Spikes Lower Chest', 'Shadow Temple Falling Spikes Upper Chest', 'Shadow Temple Falling Spikes Switch Chest', 'Shadow Temple Invisible Spikes Chest', 'GS81', 'GS82'], ['Shadow Temple Hookshot Target']),
        create_dungeon_region('Shadow Temple Wind Tunnel', ['Shadow Temple Wind Hint Chest', 'Shadow Temple After Wind Enemy Chest', 'Shadow Temple After Wind Hidden Chest', 'GS83', 'GS84'], ['Shadow Temple Boat']),
        create_dungeon_region('Shadow Temple Beyond Boat', ['Shadow Temple Spike Walls Left Chest', 'Shadow Temple Boss Key Chest', 'Shadow Temple Hidden Floormaster Chest', 'Bongo Bongo', 'GS85']),
        create_ow_region('Death Mountain', ['Death Mountain Bombable Chest', 'GS30', 'GS31', 'GS32', 'GS33'], ['Death Mountain Exit', 'Goron City Entrance', 'Mountain Crater Entrance', 'Mountain Summit Fairy', 'Dodongos Cavern Rocks', 'Mountain Bombable Grotto']),
        create_ow_region('Dodongos Cavern Entryway', None, ['Dodongos Cavern', 'Mountain Access from Behind Rock']),
        create_ow_region('Goron City', ['Goron City Leftmost Maze Chest', 'Goron City Left Maze Chest', 'Goron City Right Maze Chest', 'Rolling Goron as Child', 'Link the Goron', 'GS34', 'GS35'], ['Goron City Exit', 'Goron City Bomb Wall', 'Darunias Chamber', 'Crater Access']),
        create_ow_region('Goron City Woods Warp', None, ['Goron City from Woods', 'Goron City to Woods']),
        create_ow_region('Darunias Chamber', ['Darunias Joy'], ['Darunias Chamber Exit']),
        create_ow_region('Death Mountain Crater Upper', ['GS36'], ['Crater Exit', 'Crater Hover Boots', 'Crater Scarecrow', 'Top of Crater Grotto']),
        create_ow_region('Death Mountain Crater Lower', None, ['Crater to City', 'Crater Fairy', 'Crater Bridge', 'Crater Ascent', 'Top of Crater Grotto']),
        create_ow_region('Death Mountain Crater Central', ['Sheik in Crater', 'GS37'], ['Crater Bridge Reverse', 'Fire Temple Entrance']),
        create_interior_region('Crater Fairy'),
        create_interior_region('Mountain Summit Fairy', ['Mountain Summit Fairy Reward']),
        create_dungeon_region('Dodongos Cavern Beginning', None, ['Dodongos Cavern Exit', 'Dodongos Cavern Lobby']),
        create_dungeon_region('Dodongos Cavern Lobby', ['Dodongos Cavern Map Chest', 'GS38', 'GS42'], ['Dodongos Cavern Retreat', 'Dodongos Cavern Left Door']),
        create_dungeon_region('Dodongos Cavern Climb', ['Dodongos Cavern Compass Chest', 'Dodongos Cavern Bomb Flower Platform', 'GS39'], ['Dodongos Cavern Bridge Fall', 'Dodongos Cavern Slingshot Target']),
        create_dungeon_region('Dodongos Cavern Far Bridge', ['Dodongos Cavern Bomb Bag Chest', 'Dodongos Cavern End of Bridge Chest', 'GS41'], ['Dodongos Cavern Bomb Drop', 'Dodongos Cavern Bridge Fall 2']),        
        create_dungeon_region('Dodongos Cavern Boss Area', ['Chest Above King Dodongo', 'King Dodongo', 'GS40'], ['Dodongos Cavern Exit Skull']),
        create_ow_region('Zora River Bottom', ['GS43'], ['Zora River Exit', 'Zora River Rocks', 'Zora River Adult']),
        create_ow_region('Zora River Top', ['Magic Bean Salesman', 'Frog Ocarina Game', 'Frogs in the Rain', 'GS44'], ['Zora River Downstream', 'Zora River Dive Warp', 'Zora River Waterfall', 'Zora River Plateau Open Grotto', 'Zora River Plateau Bombable Grotto']),
        create_ow_region('Zora River Adult', ['GS45', 'GS46'], ['Zoras Domain Adult Access']),
        create_ow_region('Zoras Domain', ['Diving Minigame', 'Zoras Domain Torch Run', 'King Zora Moves'], ['Zoras Domain Exit', 'Zoras Domain Dive Warp', 'Behind King Zora', 'Zora Shop']),
        create_ow_region('Zoras Fountain', ['GS48', 'GS49'], ['Zoras Fountain Exit', 'Jabu Jabus Belly', 'Zoras Fountain Fairy']),
        create_ow_region('Zoras Domain Frozen', ['King Zora Thawed', 'GS47'], ['Zoras Fountain Adult Access']),
        create_ow_region('Outside Ice Cavern', ['GS50'], ['Ice Cavern Entrance']),
        create_dungeon_region('Ice Cavern', ['Ice Cavern Map Chest', 'Ice Cavern Compass Chest', 'Ice Cavern Iron Boots Chest', 'Sheik in Ice Cavern', 'GS70', 'GS71', 'GS72'], ['Ice Cavern Exit']),
        create_interior_region('Zora Shop'),
        create_interior_region('Zoras Fountain Fairy', ['Zoras Fountain Fairy Reward']),
        create_dungeon_region('Jabu Jabus Belly Beginning', None, ['Jabu Jabus Belly Exit', 'Jabu Jabus Belly Ceiling Switch']),
        create_dungeon_region('Jabu Jabus Belly Main', ['Boomerang Chest', 'GS51'], ['Jabu Jabus Belly Retreat', 'Jabu Jabus Belly Tentacles']),
        create_dungeon_region('Jabu Jabus Belly Depths', ['Jabu Jabus Belly Map Chest', 'Jabu Jabus Belly Compass Chest', 'GS52', 'GS53'], ['Jabu Jabus Belly Elevator', 'Jabu Jabus Belly Octopus']),
        create_dungeon_region('Jabu Jabus Belly Boss Area', ['Barinade', 'GS54'], ['Jabu Jabus Belly Final Backtrack']),
        create_ow_region('Lon Lon Ranch', ['Talons Chickens', 'Epona', 'Song from Malon', 'GS18', 'GS19', 'GS20', 'GS21'], ['Lon Lon Exit', 'Talon House', 'Ingo Barn', 'Lon Lon Corner Tower', 'Lon Lon Grotto']),
        create_interior_region('Talon House'),
        create_interior_region('Ingo Barn'),
        create_interior_region('Lon Lon Corner Tower'),
        create_interior_region('Forest Temple Entry Area', ['Sheik Forest Song', 'GS6', 'GS7'], ['Adult Meadow Exit', 'Forest Temple Entrance']),
        create_dungeon_region('Forest Temple Lobby', ['Forest Temple First Chest', 'Forest Temple Chest Behind Lobby', 'GS60', 'GS61'], ['Forest Temple Exit', 'Forest Temple Song of Time Block', 'Forest Temple Lobby Eyeball Switch', 'Forest Temple Lobby Locked Door']),
        create_dungeon_region('Forest Temple NW Outdoors', ['Forest Temple Well Chest', 'Forest Temple Map Chest', 'GS63'], ['Forest Temple Through Map Room']),
        create_dungeon_region('Forest Temple NE Outdoors', ['Forest Temple Outside Hookshot Chest', 'GS62'], ['Forest Temple Well Connection', 'Forest Temple Outside to Lobby', 'Forest Temple Scarecrows Song']),
        create_dungeon_region('Forest Temple Falling Room', ['Forest Temple Falling Room Chest'], ['Forest Temple Falling Room Exit', 'Forest Temple Elevator']),
        create_dungeon_region('Forest Temple Block Push Room', ['Forest Temple Block Push Chest'], ['Forest Temple Outside Backdoor', 'Forest Temple Twisted Hall', 'Forest Temple Straightened Hall']),
        create_dungeon_region('Forest Temple Straightened Hall', ['Forest Temple Boss Key Chest'], ['Forest Temple Boss Key Chest Drop']),
        create_dungeon_region('Forest Temple Outside Upper Ledge', ['Forest Temple Floormaster Chest'], ['Forest Temple Outside Ledge Drop']),
        create_dungeon_region('Forest Temple Bow Region', ['Forest Temple Bow Chest', 'Forest Temple Red Poe Chest', 'Forest Temple Blue Poe Chest'], ['Forest Temple Drop to Falling Room']),
        create_dungeon_region('Forest Temple Boss Region', ['Forest Temple Near Boss Chest', 'Phantom Ganon', 'GS64']),
        create_dungeon_region('Fire Temple Lower', ['Fire Temple Chest Near Boss', 'Fire Temple Fire Dancer Chest', 'Fire Temple Boss Key Chest', 'Fire Temple Big Lava Room Bombable Chest', 'Fire Temple Big Lava Room Open Chest', 'Volvagia', 'GS65', 'GS69'], ['Fire Temple Exit', 'Fire Temple Early Climb']),
        create_dungeon_region('Fire Temple Middle', ['Fire Temple Boulder Maze Lower Chest', 'Fire Temple Boulder Maze Upper Chest', 'Fire Temple Boulder Maze Side Room', 'Fire Temple Boulder Maze Bombable Pit', 'Fire Temple Scarecrow Chest', 'Fire Temple Map Chest', 'Fire Temple Compass Chest', 'GS66', 'GS67', 'GS68'], ['Fire Temple Fire Maze Escape']),
        create_dungeon_region('Fire Temple Upper', ['Fire Temple Highest Goron Chest', 'Fire Temple Megaton Hammer Chest']),
        create_grotto_region('Forest Generic Grotto'),
        create_grotto_region('Deku Theater', ['Deku Theater Skull Mask', 'Deku Theater Mask of Truth']),
        create_grotto_region('Forest Sales Grotto', ['Deku Salesman Lost Woods Grotto']),
        create_grotto_region('Meadow Fairy Grotto'),
        create_grotto_region('Front of Meadow Grotto'),
        create_grotto_region('Lon Lon Grotto'),
        create_grotto_region('Remote Southern Grotto'),
        create_grotto_region('Field Near Lake Outside Fence Grotto'),
        create_grotto_region('Field Near Lake Inside Fence Grotto'),
        create_grotto_region('Field Valley Grotto', ['GS13']),
        create_grotto_region('Field West Castle Town Grotto'),
        create_grotto_region('Field Far West Castle Town Grotto'),
        create_grotto_region('Field Kakariko Grotto', ['GS12']),
        create_grotto_region('Field North Lon Lon Grotto'),
        create_grotto_region('Castle Storms Grotto', ['GS16']),
        create_grotto_region('Kakariko Bombable Grotto'),
        create_grotto_region('Kakariko Back Grotto'),
        create_grotto_region('Mountain Bombable Grotto'),
        create_grotto_region('Top of Crater Grotto'),
        create_grotto_region('Zora River Plateau Open Grotto'),
        create_grotto_region('Zora River Plateau Bombable Grotto'),
        create_grotto_region('Lake Hylia Grotto')
    ]

    world.intialize_regions()

def create_ow_region(name, locations=None, exits=None):
    return _create_region(name, RegionType.Overworld, locations, exits)

def create_interior_region(name, locations=None, exits=None):
    return _create_region(name, RegionType.Interior, locations, exits)

def create_dungeon_region(name, locations=None, exits=None):
    return _create_region(name, RegionType.Dungeon, locations, exits)

def create_grotto_region(name, locations=None, exits=None):
    return _create_region(name, RegionType.Grotto, locations, exits)

def _create_region(name, type, locations=None, exits=None):
    ret = Region(name, type)
    if locations is None:
        locations = []
    if exits is None:
        exits = []

    for exit in exits:
        ret.exits.append(Entrance(exit, ret))
    for location in locations:
        address, default, type = location_table[location]
        ret.locations.append(Location(location, address, default, type, ret))
    return ret

location_table = {'Kokiri Sword Chest': (0x20A6142, 0x04E0, 'Chest'),
                  'Mido Chest Top Left': (0x2F7B08A, 0x59A0, 'Chest'),
                  'Mido Chest Top Right': (0x2F7B09A, 0x59A1, 'Chest'),
                  'Mido Chest Bottom Left': (0x2F7B0AA, 0x5982, 'Chest'),
                  'Mido Chest Bottom Right': (0x2F7B0BA, 0x5903, 'Chest'),
                  'Shield Grave Chest': (0x328B096, 0x5540, 'Chest'),
                  'Heart Piece Grave Chest': (0x2D0A056, 0xA7C0, 'Chest'),
                  'Composer Grave Chest': (0x332D0EA, 0x8020, 'Chest'),
                  'Death Mountain Bombable Chest': (0x223C3CA, 0x5AA1, 'Chest'),
                  'Goron City Leftmost Maze Chest': (0x227C23A, 0x5AC0, 'Chest'),
                  'Goron City Left Maze Chest': (0x227C24A, 0x5AA1, 'Chest'),
                  'Goron City Right Maze Chest': (0x227C25A, 0x5AA2, 'Chest'),
                  'Zoras Domain Torch Run': (0x2103166, 0xB7C0, 'Chest'),
                  'Hookshot Chest': (0x3063092, 0x1100, 'Chest'),
                  'Deku Tree Lobby Chest': (0x24A7146, 0x0823, 'Chest'),
                  'Deku Tree Slingshot Chest': (0x24C20C6, 0x00A1, 'Chest'),
                  'Deku Tree Slingshot Room Side Chest': (0x24C20D6, 0x5905, 'Chest'),
                  'Deku Tree Compass Chest': (0x25040D6, 0x0802, 'Chest'),
                  'Deku Tree Compass Room Side Chest': (0x25040E6, 0x5906, 'Chest'),
                  'Deku Tree Basement Chest': (0x24C8166, 0x5904, 'Chest'),
                  'Dodongos Cavern Map Chest': (0x1F2819E, 0x0828, 'Chest'),
                  'Dodongos Cavern Compass Chest': (0x1FAF0AA, 0x0805, 'Chest'),
                  'Dodongos Cavern Bomb Flower Platform': (0x1F890DE, 0x59C6, 'Chest'),
                  'Dodongos Cavern Bomb Bag Chest': (0x1F890CE, 0x0644, 'Chest'),
                  'Dodongos Cavern End of Bridge Chest': (0x1F281CE, 0x552A, 'Chest'),
                  'Chest Above King Dodongo': (0x2EB00BA, 0x5020, 'Chest'),
                  'Boomerang Chest': (0x278A0BA, 0x10C1, 'Chest'),
                  'Jabu Jabus Belly Map Chest': (0x278E08A, 0x1822, 'Chest'),
                  'Jabu Jabus Belly Compass Chest': (0x279608A, 0xB804, 'Chest'),
                  'Forest Temple First Chest': (0x23E5092, 0x5843, 'Chest'),
                  'Forest Temple Chest Behind Lobby': (0x2415082, 0x7840, 'Chest'),
                  'Forest Temple Well Chest': (0x244A062, 0x5849, 'Chest'),
                  'Forest Temple Map Chest': (0x2455076, 0x1821, 'Chest'),
                  'Forest Temple Outside Hookshot Chest': (0x241F0D6, 0x5905, 'Chest'),
                  'Forest Temple Falling Room Chest': (0x247E09E, 0x5947, 'Chest'),
                  'Forest Temple Block Push Chest': (0x245B096, 0x8964, 'Chest'),
                  'Forest Temple Boss Key Chest': (0xCB0DC2, 0x27EE, 'Chest'),
                  'Forest Temple Floormaster Chest': (0x2490072, 0x7842, 'Chest'),
                  'Forest Temple Bow Chest': (0x2415092, 0xB08C, 'Chest'),
                  'Forest Temple Red Poe Chest': (0x246607E, 0x784D, 'Chest'),
                  'Forest Temple Blue Poe Chest': (0x246F07E, 0x180F, 'Chest'),
                  'Forest Temple Near Boss Chest': (0x2486082, 0x592B, 'Chest'),
                  'Bottom of the Well Front Left Hidden Wall': (0x32D317E, 0x5848, 'Chest'),
                  'Bottom of the Well Front Center Bombable': (0x32D30FE, 0x5062, 'Chest'),
                  'Bottom of the Well Right Bottom Hidden Wall': (0x32D314E, 0x5845, 'Chest'),
                  'Bottom of the Well Center Large Chest': (0x32D30EE, 0x0801, 'Chest'),
                  'Bottom of the Well Center Small Chest': (0x32D31AE, 0x504E, 'Chest'),
                  'Bottom of the Well Back Left Bombable': (0x32D313E, 0x5C84, 'Chest'),
                  'Bottom of the Well Defeat Boss': (0x32FB0AA, 0x1143, 'Chest'),
                  'Bottom of the Well Invisible Chest': (0x32FB0BA, 0x6AD4, 'Chest'),
                  'Bottom of the Well Underwater Front Chest': (0x32D31BE, 0x5CD0, 'Chest'),
                  'Bottom of the Well Underwater Left Chest': (0x32D318E, 0x5909, 'Chest'),
                  'Bottom of the Well Basement Chest': (0x32E9252, 0x0827, 'Chest'),
                  'Bottom of the Well Locked Pits': (0x32F90AA, 0x552A, 'Chest'),
                  'Bottom of the Well Behind Right Grate': (0x32D319E, 0x554C, 'Chest'),
                  'Fire Temple Chest Near Boss': (0x230808A, 0x5841, 'Chest'),
                  'Fire Temple Fire Dancer Chest': (0x2318082, 0x7CC0, 'Chest'),
                  'Fire Temple Boss Key Chest': (0x238A0D6, 0x27EC, 'Chest'),
                  'Fire Temple Big Lava Room Bombable Chest': (0x23AD076, 0x5842, 'Chest'),
                  'Fire Temple Big Lava Room Open Chest': (0x239D0A6, 0x5844, 'Chest'),
                  'Fire Temple Boulder Maze Lower Chest': (0x2323152, 0x5843, 'Chest'),
                  'Fire Temple Boulder Maze Upper Chest': (0x2323182, 0x5846, 'Chest'),
                  'Fire Temple Boulder Maze Side Room': (0x23B40B2, 0x5848, 'Chest'),
                  'Fire Temple Boulder Maze Bombable Pit': (0x231B0D4, 0x584B, 'Chest'),
                  'Fire Temple Scarecrow Chest': (0x2339082, 0x5ACD, 'Chest'),
                  'Fire Temple Map Chest': (0x237E0C2, 0x082A, 'Chest'),
                  'Fire Temple Compass Chest': (0x23C1082, 0x0807, 'Chest'),
                  'Fire Temple Highest Goron Chest': (0x2365066, 0x5849, 'Chest'),
                  'Fire Temple Megaton Hammer Chest': (0x236C102, 0x01A5, 'Chest'),
                  'Ice Cavern Map Chest': (0x2C4016A, 0x0820, 'Chest'),
                  'Ice Cavern Compass Chest': (0x2C4E236, 0x0801, 'Chest'),
                  'Ice Cavern Iron Boots Chest': (0x2C380A2, 0x15C2, 'Chest'),
                  'Water Temple Map Chest': (0x26690A6, 0x1822, 'Chest'),
                  'Water Temple Compass Chest': (0x25FC0D2, 0x0809, 'Chest'),
                  'Water Temple Torches Chest': (0x26640A6, 0x7841, 'Chest'),
                  'Water Temple Dragon Chest': (0x261F0BA, 0x584A, 'Chest'),
                  'Water Temple Central Bow Target Chest': (0x266D072, 0x5848, 'Chest'),
                  'Water Temple Central Pillar Chest': (0x25EF0D6, 0x5846, 'Chest'),
                  'Water Temple Cracked Wall Chest': (0x265B0A6, 0x5840, 'Chest'),
                  'Water Temple Boss Key Chest': (0x2657066, 0x27E5, 'Chest'),
                  'Water Temple Dark Link Chest': (0x261907A, 0x0127, 'Chest'),
                  'Water Temple River Chest': (0x26740DE, 0x5843, 'Chest'),
                  'Shadow Temple Map Chest': (0x27CC0AA, 0x1821, 'Chest'),
                  'Shadow Temple Hover Boots Chest': (0x27DC0CA, 0x15E7, 'Chest'),
                  'Shadow Temple Compass Chest': (0x27EC09E, 0x1803, 'Chest'),
                  'Shadow Temple Early Silver Rupee Chest': (0x27E40F6, 0x5842, 'Chest'),
                  'Shadow Temple Invisible Blades Visible Chest': (0x282212A, 0x588C, 'Chest'),
                  'Shadow Temple Invisible Blades Invisible Chest': (0x282211A, 0x6976, 'Chest'),
                  'Shadow Temple Falling Spikes Lower Chest': (0x2801132, 0x5945, 'Chest'),
                  'Shadow Temple Falling Spikes Upper Chest': (0x2801142, 0x5886, 'Chest'),
                  'Shadow Temple Falling Spikes Switch Chest': (0x2801122, 0x8844, 'Chest'),
                  'Shadow Temple Invisible Spikes Chest': (0x28090EE, 0x7889, 'Chest'),
                  'Shadow Temple Wind Hint Chest': (0x283609A, 0x6955, 'Chest'),
                  'Shadow Temple After Wind Enemy Chest': (0x28390FE, 0x7888, 'Chest'),
                  'Shadow Temple After Wind Hidden Chest': (0x28390EE, 0x6854, 'Chest'),
                  'Shadow Temple Spike Walls Left Chest': (0x28130B6, 0x588A, 'Chest'),
                  'Shadow Temple Boss Key Chest': (0x28130A6, 0x27EB, 'Chest'),
                  'Shadow Temple Hidden Floormaster Chest': (0x282508A, 0x784D, 'Chest'),
                  'Impa at Castle': (0x2E8E961, 0x2E8E979, 'Song'),
                  'Song from Malon': (0xD7EB53, 0xD7EBCF, 'Song'),
                  'Song from Composer Grave': (0x332A8AD, 0x332A8C5, 'Song'),
                  'Song from Saria': (0x20B1DED, 0x20B1E05, 'Song'),
                  'Song from Ocarina of Time': (0x252FCC5, 0x252FCDD, 'Song'),
                  'Song at Windmill': (0xE42C07, 0xE42B8B, 'Song'),
                  'Sheik Forest Song': (0x20B082D, 0x20B0845, 'Song'),
                  'Sheik at Temple': (0x253137D, 0x2531395, 'Song'),
                  'Sheik in Crater': (0x224D815, 0x224D82D, 'Song'),
                  'Sheik in Ice Cavern': (0x2BEC8F5, 0x2BEC90D, 'Song'),
                  'Sheik in Kakariko': (0x2001035, 0x200104D, 'Song'),
                  'Sheik at Colossus': (0x218C5A1, 0x218C5B9, 'Song'),
                  'Gift from Saria': (None, None, 'NPC'),
                  'Zeldas Letter': (None, None, 'NPC'),
                  'Mountain Summit Fairy Reward': (None, None, 'Fairy'),
                  'Hyrule Castle Fairy Reward': (None, None, 'Fairy'),
                  'Zoras Fountain Fairy Reward': (None, None, 'Fairy'),
                  'Darunias Joy': (0xCF1BFF, 0x54, 'NPC'),
                  'Diving Minigame': (0xE01A2B, 0x37, 'NPC'),
                  'Child Fishing': (0xDCBFBF, 0x3E, 'NPC'),
                  'Adult Fishing': (0xDCC087, 0x38, 'NPC'),
                  'Diving in the Lab': (0xE2CB97, 0x3E, 'NPC'),
                  'Link the Goron': (0xED30EB, 0x2C, 'NPC'),
                  'King Zora Thawed': (0xE56AD7, 0x2D, 'NPC'),
                  'Bombchu Bowling Bomb Bag': (0xE2F093, 0x33, 'NPC'),
                  'Bombchu Bowling Piece of Heart': (0xE2F097, 0x3E, 'NPC'),
                  'Dog Lady': (0xE65163, 0x3E, 'NPC'),
                  'Skull Kid': (0xDF0F33, 0x3E, 'NPC'),
                  'Ocarina Memory Game': (0xDF264F, 0x3E, 'NPC'),
                  '10 Gold Skulltulla Reward': (0xEA7173, 0x45, 'NPC'),
                  '20 Gold Skulltulla Reward': (0xEA7175, 0x39, 'NPC'),
                  '30 Gold Skulltulla Reward': (0xEA7177, 0x46, 'NPC'),
                  '40 Gold Skulltulla Reward': (0xEA7179, 0x03, 'NPC'),
                  '50 Gold Skulltulla Reward': (0xEA717B, 0x3E, 'NPC'),
                  'Man on Roof': (0xE587E3, 0x3E, 'NPC'),
                  'Frog Ocarina Game': (0xDB13D3, 0x3E, 'NPC'),
                  'Frogs in the Rain': (0xDB1387, 0x3E, 'NPC'),
                  'Horseback Archery 1000 Points': (0xE12BC3, 0x30, 'NPC'),
                  'Horseback Archery 1500 Points': (0xE12B6F, 0x3E, 'NPC'),
                  'Child Shooting Gallery': (0xD35EF3, 0x60, 'NPC'),
                  'Adult Shooting Gallery': (0xD35F5B, 0x30, 'NPC'),
                  'Target in Woods': (0xE59CDF, 0x60, 'NPC'),
                  'Deku Theater Skull Mask': (0xEC9A87, 0x77, 'NPC'),
                  'Deku Theater Mask of Truth': (0xEC9CE7, 0x79, 'NPC'),
                  'Deku Salesman Woods': (0xDF8073, 0x77, 'NPC'),
                  'Deku Salesman Lost Woods Grotto': (0xDF80E7, 0x79, 'NPC'),
                  'Anjus Chickens': (0xE1E7A7, 0x0F, 'NPC'),
                  'Talons Chickens': (0xCC14EB, 0x14, 'NPC'),
                  '10 Big Poes': (0xEE6AEF, 0x0F, 'NPC'),
                  'Rolling Goron as Child': (0xED296F, 0x34, 'NPC'),
                  'Zelda': (None, None, 'NPC'),
                  'Magic Bean Salesman': (None, None, 'Event'),
                  'Underwater Bottle': (None, None, 'Event'),
                  'King Zora Moves': (None, None, 'Event'),
                  'Ocarina of Time': (None, None, 'Event'),
                  'Master Sword Pedestal': (None, None, 'Event'),
                  'Epona': (None, None, 'Event'),
                  'Queen Gohma': (None, None, 'Boss'),
                  'King Dodongo': (None, None, 'Boss'),
                  'Barinade': (None, None, 'Boss'),
                  'Phantom Ganon': (None, None, 'Boss'),
                  'Volvagia': (None, None, 'Boss'),
                  'Morpha': (None, None, 'Boss'),
                  'Bongo Bongo': (None, None, 'Boss'),
                  'Twinrova': (None, None, 'Boss'),
                  'Ganon': (None, None, 'Boss'),
                  'GS1': (None, None, 'GS Token'),
                  'GS2': (None, None, 'GS Token'),
                  'GS3': (None, None, 'GS Token'),
                  'GS4': (None, None, 'GS Token'),
                  'GS5': (None, None, 'GS Token'),
                  'GS6': (None, None, 'GS Token'),
                  'GS7': (None, None, 'GS Token'),
                  'GS8': (None, None, 'GS Token'),
                  'GS9': (None, None, 'GS Token'),
                  'GS10': (None, None, 'GS Token'),
                  'GS11': (None, None, 'GS Token'),
                  'GS12': (None, None, 'GS Token'),
                  'GS13': (None, None, 'GS Token'),
                  'GS14': (None, None, 'GS Token'),
                  'GS15': (None, None, 'GS Token'),
                  'GS16': (None, None, 'GS Token'),
                  'GS17': (None, None, 'GS Token'),
                  'GS18': (None, None, 'GS Token'),
                  'GS19': (None, None, 'GS Token'),
                  'GS20': (None, None, 'GS Token'),
                  'GS21': (None, None, 'GS Token'),
                  'GS22': (None, None, 'GS Token'),
                  'GS23': (None, None, 'GS Token'),
                  'GS24': (None, None, 'GS Token'),
                  'GS25': (None, None, 'GS Token'),
                  'GS26': (None, None, 'GS Token'),
                  'GS27': (None, None, 'GS Token'),
                  'GS28': (None, None, 'GS Token'),
                  'GS29': (None, None, 'GS Token'),
                  'GS30': (None, None, 'GS Token'),
                  'GS31': (None, None, 'GS Token'),
                  'GS32': (None, None, 'GS Token'),
                  'GS33': (None, None, 'GS Token'),
                  'GS34': (None, None, 'GS Token'),
                  'GS35': (None, None, 'GS Token'),
                  'GS36': (None, None, 'GS Token'),
                  'GS37': (None, None, 'GS Token'),
                  'GS38': (None, None, 'GS Token'),
                  'GS39': (None, None, 'GS Token'),
                  'GS40': (None, None, 'GS Token'),
                  'GS41': (None, None, 'GS Token'),
                  'GS42': (None, None, 'GS Token'),
                  'GS43': (None, None, 'GS Token'),
                  'GS44': (None, None, 'GS Token'),
                  'GS45': (None, None, 'GS Token'),
                  'GS46': (None, None, 'GS Token'),
                  'GS47': (None, None, 'GS Token'),
                  'GS48': (None, None, 'GS Token'),
                  'GS49': (None, None, 'GS Token'),
                  'GS50': (None, None, 'GS Token'),
                  'GS51': (None, None, 'GS Token'),
                  'GS52': (None, None, 'GS Token'),
                  'GS53': (None, None, 'GS Token'),
                  'GS54': (None, None, 'GS Token'),
                  'GS55': (None, None, 'GS Token'),
                  'GS56': (None, None, 'GS Token'),
                  'GS57': (None, None, 'GS Token'),
                  'GS58': (None, None, 'GS Token'),
                  'GS59': (None, None, 'GS Token'),
                  'GS60': (None, None, 'GS Token'),
                  'GS61': (None, None, 'GS Token'),
                  'GS62': (None, None, 'GS Token'),
                  'GS63': (None, None, 'GS Token'),
                  'GS64': (None, None, 'GS Token'),
                  'GS65': (None, None, 'GS Token'),
                  'GS66': (None, None, 'GS Token'),
                  'GS67': (None, None, 'GS Token'),
                  'GS68': (None, None, 'GS Token'),
                  'GS69': (None, None, 'GS Token'),
                  'GS70': (None, None, 'GS Token'),
                  'GS71': (None, None, 'GS Token'),
                  'GS72': (None, None, 'GS Token'),
                  'GS73': (None, None, 'GS Token'),
                  'GS74': (None, None, 'GS Token'),
                  'GS75': (None, None, 'GS Token'),
                  'GS76': (None, None, 'GS Token'),
                  'GS77': (None, None, 'GS Token'),
                  'GS78': (None, None, 'GS Token'),
                  'GS79': (None, None, 'GS Token'),
                  'GS80': (None, None, 'GS Token'),
                  'GS81': (None, None, 'GS Token'),
                  'GS82': (None, None, 'GS Token'),
                  'GS83': (None, None, 'GS Token'),
                  'GS84': (None, None, 'GS Token'),
                  'GS85': (None, None, 'GS Token'),
                  'GS86': (None, None, 'GS Token'),
                  'GS87': (None, None, 'GS Token'),
                  'GS88': (None, None, 'GS Token'),
                  'GS89': (None, None, 'GS Token'),
                  'GS90': (None, None, 'GS Token'),
                  'GS91': (None, None, 'GS Token'),
                  'GS92': (None, None, 'GS Token'),
                  'GS93': (None, None, 'GS Token'),
                  'GS94': (None, None, 'GS Token'),
                  'GS95': (None, None, 'GS Token'),
                  'GS96': (None, None, 'GS Token'),
                  'GS97': (None, None, 'GS Token'),
                  'GS98': (None, None, 'GS Token'),
                  'GS99': (None, None, 'GS Token'),
                  'GS100': (None, None, 'GS Token')}