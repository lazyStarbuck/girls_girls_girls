# Anorexia Serum

init -1 python:
    anorexia_serum_mod_init = False

    def anorexia_serum_on_turn(person, add_to_log):
        return person.change_weight(amount = -.2, chance = 20)
        

init 2 python:
    def anorexia_serum_mod_init_requirement():
        if anorexia_serum_mod_init == False:
            return True
        return False

    anorexia_serum_mod_init_event = Action("Anorexia Serum Mod Initialization Event",anorexia_serum_mod_init_requirement,"anorexia_serum_mod_init_label")
    mod_list.append(anorexia_serum_mod_init_event)

label anorexia_serum_mod_init_label():
    # "Initiating Anorexia Serum Mod Initialization"
    python:
        anorexia_serum_trait = SerumTrait(name = "Anorexia Serum",
            desc = "Decrease target subject body mass, using peptide YY3-36 as a serum component that acts on the hypothalamic feeding centers to inhibit hunger and calorie intake.",
            positive_slug = "-$15 Value, 20% Chance/Turn to reduce body mass by 200 grams",
            negative_slug = "+125 Serum Research",
            value_added = -15,
            research_added = 125,
            base_side_effect_chance = 20,
            on_turn = anorexia_serum_on_turn,
            requires = basic_med_app,
            research_needed = 500)

        if anorexia_serum_trait not in list_of_traits:
            list_of_traits.append(anorexia_serum_trait)

        anorexia_serum_mod_init = True
    return
