init -1 python:
    biotech_room_actions = []
    biotech_gene_modifications = []
    biotech_body_modifications = []

init 3 python:

    def biotech_lab_requirement():
        return True

    biotech_lab_action = Action("Do things in the lab", biotech_lab_requirement, "biotechs",
        menu_tooltip = "Do stuff")

    def gene_modification_requirement():
        return True

    gene_modification = Action("Do genetic modifications", gene_modification_requirement, "biotech_gene_modifications",
        menu_tooltip = "Do stuff with genes or cosmetic alterations")
    biotech_room_actions.append(gene_modification)

    def clone_person_requirement():
        if not time_of_day == 4:
            return True
        else:
            return "Too late."

    clone_person = Action("Clone a person {image=gui/heart/Time_Advance.png}", clone_person_requirement, "clone_person",
        menu_tooltip = "Create a near identical clone of the targeted person")
    biotech_gene_modifications.append(clone_person)

    def modify_person_requirement():
        return True

    modify_person = Action("Modify a person", modify_person_requirement, "modify_person",
        menu_tooltip = "Modify the appearance of a person through magic, not science")
    biotech_gene_modifications.append(modify_person)

    def change_body_requirement():
        hypothyroidism = find_in_list(lambda x: x.name == hypothyroidism_serum_trait.name, list_of_traits)
        anorexia = find_in_list(lambda x: x.name == anorexia_serum_trait.name, list_of_traits)

        if not hypothyroidism is None and not anorexia is None and hypothyroidism.researched and anorexia.researched:
            return True
        else:
            return "Requires: [hypothyroidism_serum_trait.name] and [anorexia_serum_trait.name] researched"

    change_body = Action("Change body: [person.body_type]", change_body_requirement, "change_body",
        menu_tooltip = "Modify [person.title]'s body type.")
    biotech_body_modifications.append(change_body)

    def change_skin_requirement():
        pigment = find_in_list(lambda x: x.name == pigment_serum_trait.name, list_of_traits)
        if not pigment is None and pigment.researched:
            return True
        else:
            return "Requires: [pigment_serum_trait.name] researched"

    change_skin = Action("Change skin: [person.skin]", change_skin_requirement, "change_skin",
        menu_tooltip = "Modify [person.title]'s skin tone.")
    biotech_body_modifications.append(change_skin)

    def change_face_requirement():
        return True

    change_face = Action("Change face: [person.face_style]", change_face_requirement, "change_face",
        menu_tooltip = "Modify [person.title]'s face style.")
    biotech_body_modifications.append(change_face)

    def change_breasts_requirement():
        if breast_enhancement.researched and breast_reduction.researched:
            return True
        else:
            return "Requires: [breast_enhancement.name] and [breast_reduction.name]"

    change_breasts = Action("Change breasts: [person.tits]", change_breasts_requirement, "change_breasts",
        menu_tooltip = "Modify [person.title]'s cup size.")
    biotech_body_modifications.append(change_breasts)



label biotechs():
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
                biotech_options = []
                for act in biotech_room_actions:
                    biotech_options.append(act)
                biotech_options.append("Back")
                act_choice = call_formated_action_choice(biotech_options)

        if act_choice == "Back":
            return
        else:
            $ act_choice.call_action()

label biotech_gene_modifications():
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
                gene_modification_options = []
                for act in biotech_gene_modifications:
                    gene_modification_options.append(act)
                gene_modification_options.append("Back")
                act_choice = call_formated_action_choice(gene_modification_options)

        if act_choice == "Back":
            return
        else:
            $ act_choice.call_action()


label clone_person():
    $ clone_name = None
    $ clone_last_name = None
    $ clone_age = None

    while True:
        $ people_list = ["Clone Person"]
        $ people_list.extend(known_people_in_the_game([mc]) + ["Back"])
        call screen main_choice_display([people_list])
        $ person_choice = _return
        $ del people_list

        if person_choice == "Back":
            return # Where to go if you hit "Back".
        else:
            call cloning_process(person_choice) from _call_cloning_process

    return

label cloning_process(person = the_person): # default to the_person when not passed as parameter
    $ person.draw_person(emotion = "default")
    while True:
        menu:

            "Give the clone a name":
                $ clone_name = str(renpy.input("Name: ", person.name))
                $ clone_last_name = str(renpy.input("Last name: ", person.last_name))
            "Age":
                $ clone_age = int(renpy.input("Age: ", person.age))
                if clone_age < 18:
                    $ clone_age = 18



            "Begin production:{image=gui/heart/Time_Advance.png} \n{size=22}Name: [clone_name] [clone_last_name], Age: [clone_age]{/size}":
                python:
                    if clone_name is None:
                        clone_name = person.name
                    if clone_last_name is None:
                        clone_last_name = person.last_name
                    if clone_age is None:
                        clone_age = person.age

                    clone = create_random_person(name = clone_name, last_name = clone_last_name, age = clone_age, body_type = person.body_type, face_style = person.face_style, tits = person.tits, height = person.height, hair_colour = person.hair_colour, hair_style = person.hair_style, skin = person.skin, eyes = person.eyes, job = None,
                        personality = person.personality, custom_font = None, name_color = None, dial_color = None, starting_wardrobe = person.wardrobe, stat_array = None, skill_array = None, sex_array = None,
                        start_sluttiness = person.sluttiness, start_obedience = person.obedience, start_happiness = person.happiness, start_love = person.love, start_home = None, title = "Clone", possessive_title = "Your creation", mc_title = "Creator")

                    clone.schedule[0] = rd_division_basement
                    clone.schedule[1] = rd_division_basement
                    clone.schedule[2] = rd_division_basement
                    clone.schedule[3] = rd_division_basement
                    clone.schedule[4] = rd_division_basement

                    clone.special_role.append(clone_role)

                    rd_division_basement.add_person(clone) #Create rooms for the clones to inhabit until a schedule is given (through being hired or player input)

                "[clone.name] [clone.last_name] created and is now awaiting you in [rd_division_basement.formalName]"

                $ del clone    # Release variable
                call advance_time from _call_advance_time_cloning_process
                return
            "Back":
                return

label modify_person():
    while True:
        $ people_list = ["Modify Person"]
        $ people_list.extend(known_people_in_the_game([mc]) + ["Back"])
        call screen main_choice_display([people_list])
        $ person_choice = _return
        $ del people_list

        if person_choice == "Back":
            return # Where to go if you hit "Back".
        else:
            call modification_process(person_choice) from _call_modification_process

label modification_process(person = the_person): # when called without specific person use the_person variable
    $ person.draw_person(emotion = "default")
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
                body_modification_options = []
                for act in biotech_body_modifications:
                    body_modification_options.append(act)
                body_modification_options.append("Back")
                act_choice = call_formated_action_choice(body_modification_options)

        if act_choice == "Back":
            $ renpy.scene("Active")
            return
        else:
            $ act_choice.call_action()

label change_body():
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
                body_types = []
                for n in list_of_body_types:
                    body_types.append(n)
                body_types.append("Back")
                body_choice = renpy.display_menu(simple_list_format(body_types, n, string = "Body Type: ", ignore = "Back"),True,"Choice")

        if body_choice == "Back":
            return
        else:
            $ person.body_type = body_choice
            $ person.draw_person()

label change_skin():
    while True:

        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.



            skin_styles = [x[0] for x in list_of_skins]

            skin_styles.append("Back")
            skin_choice = renpy.display_menu(simple_list_format(skin_styles, x[0], string = "Skin Type: ", ignore = "Back"),True,"Choice")

        if skin_choice == "Back":
            return

        else:
            $ person.skin = skin_choice
            $ person.match_skin(skin_choice)
            $ person.draw_person()

label change_face():
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
                face_styles = []
                for face in list_of_faces:
                    face_styles.append(face)
                face_styles.append("Back")
                face_choice = renpy.display_menu(simple_list_format(face_styles, face, string = "Face Type: ", ignore = "Back"),True,"Choice")

        if face_choice == "Back":
            return
        else:
            $ person.face_style = face_choice
            $ person.match_skin(person.skin)
            $ person.draw_person()

label change_breasts():
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
                cup_sizes = [x[0] for x in list_of_tits]
                cup_sizes.append("Back")
                cup_choice = renpy.display_menu(simple_list_format(cup_sizes, x[0], string = "Cup Size: ", ignore = "Back"),True,"Choice")

        if cup_choice == "Back":
            return
        else:
            $ person.tits = cup_choice
            $ person.draw_person()
