#Blank for now#


init 2 python:
    #def casual_sex_mod_initialization(action_mod):
    workout_wardrobe = wardrobe_from_xml("Workout_Wardrobe")

    def casual_sex_test():

        people_to_process = [] #Create a list of everyone
        for place in list_of_places:
            for people in place.people:
                people_to_process.append([people,place])

        for (people,place) in people_to_process: #Figure out if person already has an important role
            disqualifying_role = 0
            for role in people.special_role:
                if role == generic_people_role:
                    pass
                else:
                    disqualifying_role = 1
            if disqualifying_role == 0:         #Assign new casual sex roles#
                if people.age < 30:
                    assign_casual_athlete_role(people)
                    people.wardrobe = copy.copy(workout_wardrobe)

                elif people.age < 40:
                    assign_casual_hotwife_role(people)

                #else:
                    #assign_casual_FA_role(people)
        num_FAs = renpy.random.randint(6,10)
        FA_counter = 0
        while FA_counter < num_FAs:
            new_FA = Casual_Flight_Attendant()
            local_FA_personality = Personality("FA", default_prefix = new_FA.personality.personality_type_prefix,
            common_likes = ["traveling"],
            common_sexy_likes = ["casual sex"],
            common_dislikes = ["relationships"],
            common_sexy_dislikes = [],
            titles_function = FA_titles, possessive_titles_function = FA_possessive_titles, player_titles_function = FA_player_titles)
            new_FA.special_role.append(casual_FA_role)
            local_FA_personality.response_dict["hookup_rejection"] = "FA_hookup_rejection"
            new_FA.personality = local_FA_personality
            new_FA.event_triggers_dict["reject_position"] = "blowjob"
            purgatory.add_person(new_FA)
            FA_counter += 1

        return

    # def casual_sex_init():
    #     people_to_process = [] #Create a list of everyone
    #     athlete_count = 0
    #     hotwife_count = 0
    #     FA_count = 0
    #     for place in list_of_places:
    #         for people in place.people:
    #             people_to_process.append([people,place])

    #     for (people,place) in people_to_process: #Figure out if person already has an important role
    #         disqualifying_role = 0
    #         for role in people.special_role:
    #             if role == generic_people_role:
    #                 pass
    #             else:
    #                 disqualifying_role = 1
    #         if disqualifying_role == 0:         #Assign new casual sex roles#
    #             if people.age < 25:
    #                 if people.body_type == "thin_body":
    #                     assign_casual_athlete_role(people)
    #                     people.wardrobe = copy.copy(workout_wardrobe)
    #                     athlete_count += 1
    #             elif people.age < 40 and people.age > 30:
    #                 if people.relationship == "Married":
    #                     assign_casual_hotwife_role(people)
    #                     hotwife_count += 1

    #             #else:
    #                 #assign_casual_FA_role(people)
    #     # num_FAs = renpy.random.randint(6,10)
    #     # FA_counter = 0
    #     # while FA_counter < num_FAs:
    #     #     new_FA = Casual_Flight_Attendant()
    #     #     local_FA_personality = Personality("FA", default_prefix = new_FA.personality.personality_type_prefix,
    #     #     common_likes = ["traveling"],
    #     #     common_sexy_likes = ["casual sex"],
    #     #     common_dislikes = ["relationships"],
    #     #     common_sexy_dislikes = [],
    #     #     titles_function = FA_titles, possessive_titles_function = FA_possessive_titles, player_titles_function = FA_player_titles)
    #     #     new_FA.special_role.append(casual_FA_role)
    #     #     local_FA_personality.response_dict["hookup_rejection"] = "FA_hookup_rejection"
    #     #     new_FA.personality = local_FA_personality
    #     #     new_FA.event_triggers_dict["reject_position"] = "blowjob"
    #     #     purgatory.add_person(new_FA)
    #     #     FA_counter += 1

    #     if athlete_count == 0:
    #         casual_sex_create_athlete()
    #         pass
    #         #create athlete
    #     if hotwife_count == 0:
    #         casual_sex_create_hotwife()
    #         pass
    #         #create hotwife

    #     return

    def casual_sex_create_athlete():
        new_athlete = create_random_person( body_type = "thin_body", age = renpy.random.randint(19,25))
        new_athlete.original_personality = athlete_personality
        assign_casual_athlete_role(new_athlete)
        gym.add_person(new_athlete)
        return True

    def casual_sex_create_hotwife():
        new_hotwife = create_random_person(age = renpy.random.randint(30,40))
        new_hotwife.original_personality = hotwife_personality
        assign_casual_hotwife_role(new_hotwife)
        downtown_bar.add_person(new_hotwife)
        return True

    def college_athlete_personality_requirement():
        return True

    def hot_wife_personality_requirement():
        return True

    def init_college_athlete_personality(self):
        # create 2 athletes
        for x in range(0, 2):
            casual_sex_create_athlete()
        return

    def init_hot_wife_personality(self):
        # create 2 hot wifes
        for x in range(0, 2):
            casual_sex_create_hotwife()
        return

    def change_college_athlete_personality_enabled(enabled):
        for person in all_people_in_the_game([mc] + unique_character_list):
            if person.original_personality == athlete_personality:
                if enabled:
                    assign_casual_athlete_role(person)
                else:
                    remove_casual_athlete_role(person)
        return

    def change_hot_wife_personality_enabled(enabled):
        for person in all_people_in_the_game([mc] + unique_character_list):
            if person.original_personality == hotwife_personality:
                if enabled:
                    assign_casual_hotwife_role(person)
                else:
                    remove_casual_hotwife_role(person)
        return

init 3 python:
    college_athlete_personality_action = ActionMod("College Athlete Personality", college_athlete_personality_requirement, "college_athlete_personality_dummy_label",
        menu_tooltip = "Enable or disable the college athlete personality.", category="Personality", initialization = init_college_athlete_personality, on_enabled_changed = change_college_athlete_personality_enabled)

    hot_wife_personality_action = ActionMod("Hot Wife Personality", hot_wife_personality_requirement, "hot_wife_personality_dummy_label",
        menu_tooltip = "Enable or disable the Hot Wife personality.", category="Personality", initialization = init_hot_wife_personality, on_enabled_changed = change_hot_wife_personality_enabled)

init 1302 python:
    def assign_casual_athlete_role(the_person):
        the_person.special_role.append(casual_athlete_role)

        athlete_personality.response_dict["hookup_rejection"] = "athlete_hookup_rejection"
        athlete_personality.response_dict["hookup_accept"] = "athlete_hookup_accept"
        the_person.personality = athlete_personality
        the_person.event_triggers_dict["reject_position"] = "standing_doggy"
        the_person.schedule[1] = gym
        the_person.schedule[2] = university
        the_person.schedule[3] = gym
        the_person.relationship = "Single"
        the_person.SO_name = None
        the_person.kids = 0

        return

    def remove_casual_athlete_role(the_person):
        the_person.special_role.remove(casual_athlete_role)
        #"relaxed", "reserved", "wild", "introvert", "cougar"
        if the_person.personality.default_prefix == "relaxed":
            the_person.personality = relaxed_personality
        elif the_person.personality.default_prefix == "reserved":
            the_person.personality = reserved_personality
        elif the_person.personality.default_prefix == "wild":
            the_person.personality = wild_personality
        elif the_person.personality.default_prefix == "introvert":
            the_person.personality = introvert_personality
        elif the_person.personality.default_prefix == "cougar":
            the_person.personality = cougar_personality
        else:
            the_person.personality = relaxed_personality  #Catch all for personalities#

        the_person.schedule[1] = None    #Reset their schedule
        the_person.schedule[2] = None
        the_person.schedule[3] = None
        return

    def assign_casual_hotwife_role(the_person):
        the_person.special_role.append(casual_hotwife_role)

        hotwife_personality.response_dict["hookup_rejection"] = "hotwife_hookup_rejection"
        hotwife_personality.response_dict["hookup_accept"] = "hotwife_hookup_accept"
        the_person.personality = hotwife_personality
        the_person.event_triggers_dict["reject_position"] = "blowjob"
        the_person.schedule[2] = downtown_bar
        the_person.schedule[3] = downtown_bar
        the_person.relationship = "Married"
        the_person.SO_name = get_random_male_name()
        the_person.kids = 0

        return

    def remove_casual_hotwife_role(the_person):
        the_person.special_role.remove(casual_hotwife_role)
        #"relaxed", "reserved", "wild", "introvert", "cougar"
        if the_person.personality.default_prefix == "relaxed":
            the_person.personality = relaxed_personality
        elif the_person.personality.default_prefix == "reserved":
            the_person.personality = reserved_personality
        elif the_person.personality.default_prefix == "wild":
            the_person.personality = wild_personality
        elif the_person.personality.default_prefix == "introvert":
            the_person.personality = introvert_personality
        elif the_person.personality.default_prefix == "cougar":
            the_person.personality = cougar_personality
        else:
            the_person.personality = relaxed_personality  #Catch all for personalities#

        the_person.schedule[2] = None    #Reset their schedule
        the_person.schedule[3] = None

        return


    def assign_casual_FA_role(the_person):
        the_person.special_role.append(casual_FA_role)
        local_FA_personality = Personality("FA", default_prefix = the_person.personality.personality_type_prefix,
        common_likes = ["traveling"],
        common_sexy_likes = ["casual sex"],
        common_dislikes = ["relationships"],
        common_sexy_dislikes = [],
        titles_function = FA_titles, possessive_titles_function = FA_possessive_titles, player_titles_function = FA_player_titles)
        local_FA_personality.response_dict["hookup_rejection"] = "FA_hookup_rejection"
        local_FA_personality.response_dict["hookup_accept"] = "FA_hookup_accept"
        the_person.personality = local_FA_personality
        the_person.event_triggers_dict["reject_position"] = "blowjob"
        the_person.schedule[3] = downtown_bar

        return

    def remove_casual_FA_role(the_person):
        the_person.special_role.remove(casual_FA_role)
        #"relaxed", "reserved", "wild", "introvert", "cougar"
        if the_person.personality.default_prefix == "relaxed":
            the_person.personality = relaxed_personality
        elif the_person.personality.default_prefix == "reserved":
            the_person.personality = reserved_personality
        elif the_person.personality.default_prefix == "wild":
            the_person.personality = wild_personality
        elif the_person.personality.default_prefix == "introvert":
            the_person.personality = introvert_personality
        elif the_person.personality.default_prefix == "cougar":
            the_person.personality = cougar_personality
        else:
            the_person.personality = relaxed_personality  #Catch all for personalities#

        the_person.schedule[2] = None    #Reset their schedule
        the_person.schedule[3] = None

        return
