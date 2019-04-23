# Business Basement Rooms is a proof of concept on best practises for adding rooms to the game via the Room Manager.
# Requires the Room Manager.rpy to be present for it to work as intended.
# Adds a basement section accessable via the business lobby.

# name,formalName,connections,background_image,objects,people,actions,public,map_pos, tutorial_label = None, visible = True)
init -1 python:
    business_basement = [] # List of rooms that are supposed to be in the basement.


init 2 python:
    m_division_basement = Room("security", "Security Room", [], office_background, [],[],[], False, [], None, False)
    p_division_basement = Room("machinery", "Machinery Room", [], office_background, [], [], [], False, [], None, False)
    rd_division_basement = Room("secret lab", "Biotechnology Lab", [], lab_background, [], [], [], False, [], None, False)
    office_basement = Room("dungeon", "Dungeon", [], bar_background, [],[],[], False,[], None, False)

#    room = Room("", "", [], background_image, [], [], [], False, [], None, False)

    business_basement.append(m_division_basement) # I collect the rooms into a list to make appending easier later.
    business_basement.append(p_division_basement)
    business_basement.append(rd_division_basement)
    business_basement.append(office_basement)


    for room in business_basement: # Add the rooms to the list that enables the elevator. This depends on having the Room Manager present.

        if room not in mod_rooms_append:
            mod_rooms_append.append(room)

    for room in business_basement: # I want all of the rooms in the basement to be accessable from the business lobby.
                                   # Modifications and further pathways can be altered later, if I for example want to install a direct elevator into the main office and into the dungeon.
        if room not in mod_rooms_lobby:
            mod_rooms_lobby.append(room)

#    for room in business_basement: # Consider this if you want the rooms to be in the list_of_places list that contain all default locations.

#        if room not in list_of_places:
#            list_of_places.append(room)

#    for room in business_basement: # This will enable the "Go somewhere button..." allowing you to enter the main map screen from within the room.
                                    # Meaning you do not need the "Do something..." action to escape the room.
#        if room not in room.connections:
#            room.link_locations_two_way(room)
