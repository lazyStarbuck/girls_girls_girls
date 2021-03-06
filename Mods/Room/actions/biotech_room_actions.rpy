init -1 python:
    biotech_body_modifications = []

init 3 python:
    def biotech_clone_person_requirement():
        if time_of_day == 4:
            return "Too late"
        elif not mc.has_dungeon():
            return "Dungeon required"
        return True

    biotech_clone_person = Action("{image=dna_sequence} Clone a person {image=gui/heart/Time_Advance.png}", biotech_clone_person_requirement, "biotech_clone_person",
        menu_tooltip = "Create a near identical clone of the targeted person")

    def biotech_modify_person_requirement():
        return True

    biotech_modify_person = Action("Modify a person", biotech_modify_person_requirement, "biotech_modify_person",
        menu_tooltip = "Modify the appearance of a person through magic, not science")

    def biotech_change_body_requirement():
        if mc.business.is_trait_researched("Hypothyroidism") and mc.business.is_trait_researched("Methabolizer"):
            return True
        else:
            return "Requires: Hypothyroidism Trait and Methabolizer Trait researched"

    biotech_change_body = Action("Change body: [person.body_type]", biotech_change_body_requirement, "biotech_change_body",
        menu_tooltip = "Modify [person.title]'s body type.")
    biotech_body_modifications.append(biotech_change_body)

    def biotech_change_skin_requirement():
        if mc.business.is_trait_researched("Pigment"):
            return True
        else:
            return "Requires: Pigment Trait researched"

    biotech_change_skin = Action("Change skin: [person.skin]", biotech_change_skin_requirement, "biotech_change_skin",
        menu_tooltip = "Modify [person.title]'s skin tone.")
    biotech_body_modifications.append(biotech_change_skin)

    def biotech_change_face_requirement():
        return True

    biotech_change_face = Action("Change face: [person.face_style]", biotech_change_face_requirement, "biotech_change_face",
        menu_tooltip = "Modify [person.title]'s face style.")
    biotech_body_modifications.append(biotech_change_face)

    def biotech_change_breasts_requirement():
        if mc.business.is_trait_researched(breast_enhancement):
            return True
        else:
            return "Requires: [breast_enhancement.name] and [breast_reduction.name]"

    def create_clone(person, clone_name, clone_last_name, clone_age):
        if clone_name is None:
            clone_name = get_random_name()
        if clone_last_name is None:
            clone_last_name = get_random_last_name()
        if clone_age is None:
            clone_age = person.age

        clone = make_person(name = clone_name, last_name = clone_last_name, age = clone_age, body_type = person.body_type, face_style = person.face_style, tits = person.tits, height = person.height, hair_colour = person.hair_colour, hair_style = person.hair_style, skin = person.skin, eyes = person.eyes, job = None,
            personality = person.personality, custom_font = None, name_color = None, dial_color = None, starting_wardrobe = person.wardrobe, stat_array = [person.charisma, person.int, person.focus], skill_array = [person.hr_skill, person.market_skill, person.research_skill, person.production_skill, person.supply_skill], sex_array = [person.sex_skills["Foreplay"], person.sex_skills["Oral"], person.sex_skills["Vaginal"], person.sex_skills["Anal"]],
            start_sluttiness = person.sluttiness, start_obedience = person.obedience - 100, start_happiness = person.happiness, start_love = person.love, start_home = dungeon, title = "Clone", possessive_title = "Your creation", mc_title = "Creator", relationship = "Single", kids = 0, forced_sexy_opinions = [["being submissive", 2 , True]] , force_random = True)

        clone.set_schedule(dungeon, times = [0,1,2,3,4])
        clone.add_role(clone_role)

        dungeon.add_person(clone) #Create rooms for the clones to inhabit until a schedule is given (through being hired or player input)
        return

    biotech_change_breasts = Action("Change breasts: [person.tits]", biotech_change_breasts_requirement, "biotech_change_breasts",
        menu_tooltip = "Modify [person.title]'s cup size.")
    biotech_body_modifications.append(biotech_change_breasts)

    def build_body_type_choice_menu():
        body_types = []
        for n in list_of_body_types:
            body_types.append(n)
        body_types.append("Back")
        return renpy.display_menu(simple_list_format(body_types, n, string = "Body Type: ", ignore = "Back"), True, "Choice")

    def build_skin_style_choice_menu():
        skin_styles = [x[0] for x in list_of_skins]
        skin_styles.append("Back")
        return renpy.display_menu(simple_list_format(skin_styles, x[0], string = "Skin Type: ", ignore = "Back"), True, "Choice")

    def build_face_style_choice_menu():
        face_styles = []
        for face in list_of_faces:
            face_styles.append(face)
        face_styles.append("Back")
        return renpy.display_menu(simple_list_format(face_styles, face, string = "Face Type: ", ignore = "Back"), True, "Choice")

    def build_cup_size_choice_menu():
        cup_sizes = [x[0] for x in list_of_tits]
        cup_sizes.append("Back")
        return renpy.display_menu(simple_list_format(cup_sizes, x[0], string = "Cup Size: ", ignore = "Back"), True, "Choice")

label biotech_gene_modifications():
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
            gene_modification_options = []
            for act in biotech_gene_modifications:
                gene_modification_options.append(act)
            gene_modification_options.append("Back")
            act_choice = call_formated_action_choice(gene_modification_options)
            del gene_modification_options

        if act_choice == "Back":
            return
        else:
            $ act_choice.call_action()


label biotech_clone_person():
    # only known people who are not unique character or clone herself (genetic degradation too high)
    call screen enhanced_main_choice_display(build_menu_items([get_sorted_people_list([x for x in known_people_in_the_game(unique_character_list) if x.can_clone()], "Clone Person", ["Back"])]))
    if _return != "Back":
        call cloning_process(_return) from _call_cloning_process
    return

label cloning_process(person = the_person): # default to the_person when not passed as parameter
    $ person.draw_person(emotion = "default")
    $ clone_name = None
    $ clone_last_name = None
    $ clone_age = None

    while True:
        menu:

            "Give the clone a name":
                $ clone_name = str(renpy.input("Name: ", person.name))
                $ clone_last_name = str(renpy.input("Last name: ", person.last_name))
            "Age":
                $ clone_age = __builtin__.int(renpy.input("Age: ", person.age))
                if clone_age < 18:
                    $ clone_age = 18
            "Begin production: {image=gui/heart/Time_Advance.png}\n{color=#ff0000}{size=18}Name: [clone_name] [clone_last_name], Age: [clone_age]{/size}{/color}":
                $ create_clone(person, clone_name, clone_last_name, clone_age)
                "The clone has been created and is now awaiting you in the [dungeon.formal_name]."
                call advance_time from _call_advance_time_cloning_process
                return
            "Back":
                return

label biotech_modify_person():
    call screen enhanced_main_choice_display(build_menu_items([get_sorted_people_list(known_people_in_the_game(), "Modify Person", ["Back"])]))
    if _return != "Back":
        call modification_process(_return) from _call_modification_process
    return

label modification_process(person = the_person): # when called without specific person use the_person variable
    $ person.draw_person(emotion = "default")
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
            body_modification_options = []
            for act in biotech_body_modifications:
                body_modification_options.append(act)
            body_modification_options.append("Back")
            act_choice = call_formated_action_choice(body_modification_options)
            del body_modification_options

        if act_choice == "Back":
            $ clear_scene()
            return
        else:
            $ act_choice.call_action()
            $ del act_choice

label biotech_change_body():
    while True:
        #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
        $ body_choice = build_body_type_choice_menu()

        if body_choice == "Back":
            return
        else:
            $ person.body_type = body_choice
            $ person.draw_person()
            $ del body_choice

label biotech_change_skin():
    while True:
        #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
        $ skin_choice = build_skin_style_choice_menu()

        if skin_choice == "Back":
            return

        else:
            $ person.skin = skin_choice
            $ person.match_skin(skin_choice)
            $ person.draw_person()
            $ del skin_choice

label biotech_change_face():
    while True:
        #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
        $ face_choice = build_face_style_choice_menu()

        if face_choice == "Back":
            return
        else:
            $ person.face_style = face_choice
            $ person.match_skin(person.skin)
            $ person.draw_person()
            $ del face_choice

label biotech_change_breasts():
    while True:
        #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
        $ cup_choice = build_cup_size_choice_menu()

        if cup_choice == "Back":
            return
        else:
            $ person.tits = cup_choice
            $ person.draw_person()
            $ del cup_choice
