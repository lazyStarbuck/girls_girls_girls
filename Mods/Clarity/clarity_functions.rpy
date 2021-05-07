init 3 python:
    def get_clarity_multiplier():
        multiplier = 1.0
        if perk_system.has_ability_perk("Intelligent Clarity"):
            multiplier += (mc.int * .05) #5% increase per intelligence point
        if perk_system.has_ability_perk("Charismatic Clarity"):
            multiplier += (mc.charisma * .05) #5% increase per charisma point
        if perk_system.has_ability_perk("Focused Clarity"):
            multiplier += (mc.focus * .05) #5% increase per charisma point

        return multiplier

    def add_intelligence_clarity_perk():
        if perk_system.has_ability_perk("Intelligent Clarity"):
            return
        perk_system.add_ability_perk(Ability_Perk(description = "You gain increase clarity based on your intelligence.", toggle = False, usable = False), "Intelligent Clarity")
        return

    def add_charismatic_clarity_perk():
        if perk_system.has_ability_perk("Charismatic Clarity"):
            return
        perk_system.add_ability_perk(Ability_Perk(description = "You gain increase clarity based on your charisma.", toggle = False, usable = False), "Charismatic Clarity")
        return

    def add_focus_clarity_perk():
        if perk_system.has_ability_perk("Focused Clarity"):
            return
        perk_system.add_ability_perk(Ability_Perk(description = "You gain increase clarity based on your focus.", toggle = False, usable = False), "Focused Clarity")
        return

    persuade_action = ActionMod("Use Persuasion", requirement = persuade_person_requirement, effect = "persuade_person",
        menu_tooltip = "Leverage your clarity to persuade her to do something.", category = "Generic People Actions")

    def build_specific_action_list_extended(org_func):
        def build_specific_action_list_wrapper(person):
            # run original function
            result = org_func(person)
            # run extension code (append new action to base game menu)
            if persuade_action.enabled:
                persuade_action.args = [person]
                persuade_action.requirement_args = [person]
                result.append(persuade_action)
            return result

        return build_specific_action_list_wrapper

    # wrap up the build_specific_action_list function
    build_specific_action_list = build_specific_action_list_extended(build_specific_action_list)
