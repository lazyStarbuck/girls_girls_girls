## Booty Call Crisis. Girl you are FWB with calls you for some casual sex.
init -1 python:
    booty_call_mod_weight = 5     # Set High for testing. TODO set lower after play testing

init 3 python:
    #sports_bar = Room("bar", "Bar", [], room_background_image("bar_background.png"), [make_floor(), make_wall(), make_chair(), make_window()], [], [], True, [6,5], None, True)
    def casual_sex_booty_call_requirement():
        if time_of_day > 0 : #Not early morning
            if time_of_day < 4: #Not night
                return not get_casual_sex_booty_call_person() is None
        return False

    def get_casual_sex_booty_call_person():
        possible_people = []
        for person in known_people_in_the_game():
            # check if person has a casual sex role and we have her phone number
            if person.has_role([casual_hotwife_role, casual_FA_role]) and person.event_triggers_dict.get("booty_call", False) and day > person.event_triggers_dict.get("last_booty_call", 0) + 10:
                possible_people.append(person)

        return get_random_from_list(possible_people)

    casual_sex_booty_call = ActionMod("Booty Call", casual_sex_booty_call_requirement,"casual_sex_booty_call_label",
        menu_tooltip = "A friend sends you a phone message", is_crisis = True, crisis_weight = booty_call_mod_weight)

label casual_sex_booty_call_label:
    $ the_person = get_casual_sex_booty_call_person()
    # No one qualified so end here
    if the_person is None:
        return

    "While you're going about your day you get a text from [the_person.possessive_title!l]."
    $ mc.having_text_conversation = the_person
    the_person "Hey stud! Up for some fun?"
    menu:
        "Definitely":
            the_person "Great!"
            $ the_person.event_triggers_dict["last_booty_call"] = day
            $ the_person.strip_outfit(delay = 0)
            $ the_person.call_dialogue("hookup_accept")
            if the_person.arousal > 100 and the_person.core_sluttiness < 100:
                $ the_person.change_slut_core(2)

        "Not Now":
            $ mc.having_text_conversation = None
            "After a few minutes, you get a response."
            $ mc.having_text_conversation = the_person
            $ the_person.call_dialogue("hookup_rejection")
            $ the_person.strip_outfit(delay = 0)
            $ the_person.draw_person(position = the_person.event_triggers_dict.get("reject_position", "missionary"))
            $ mc.having_text_conversation = None
            "She sends you a pic of herself masturbating."
    $ mc.having_text_conversation = None
    $ the_person.reset_arousal()
    $ the_person.apply_planned_outfit()
    $ clear_scene()
    return
