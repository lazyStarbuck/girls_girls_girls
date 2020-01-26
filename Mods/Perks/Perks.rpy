init -1 python:
    class Perks(renpy.store.object):
        def __init__(self):
            self.stat_perks = {}
            self.item_perks = {}
            self.ability_perks = {}

        def update(self):  #By adding an update, we can add temporary perks that may expire.
            def expired_perks(perk_dict):
                perk_names = []
                for key, item in perk_dict.items():
                    if item.bonus_is_temp and day >= item.duration + item.start_day:
                        perk_names.append(key)
                return perk_names

            def remove_perk(perk_dict, perk_name):
                perk_dict[perk_name].remove()
                perk_dict.pop(perk_name)

            for perk_name in expired_perks(self.stat_perks):
                remove_perk(self.stat_perks, perk_name)

            for perk_name in expired_perks(self.item_perks):
                remove_perk(self.item_perks, perk_name)

            for perk_name in expired_perks(self.ability_perks):
                remove_perk(self.ability_perks, perk_name)
            return

        def add_stat_perk(self, perk, perk_name):
            if self.has_stat_perk(perk_name):
                #We already have this perk, check if we need to update temporary bonus.
                if not perk.bonus_is_temp:
                    return

                # Update duration for existing temporary perk.
                comp_perk = self.get_stat_perk(perk_name)  
                if comp_perk.duration < perk.duration:
                    comp_perk.duration = perk.duration
                if comp_perk.start_day < perk.start_day:
                    comp_perk.start_day = perk.start_day
            else:
                perk.apply()
                self.stat_perks[perk_name] = perk
            return

        def has_stat_perk(self, perk_name):
            if perk_name in self.stat_perks:
                return True
            return False

        def get_stat_perk(self, perk_name):
            if self.has_stat_perk(perk_name):
                return self.stat_perks[perk_name]
            return None

        def add_item_perk(self, perk, perk_name):
            if not self.has_item_perk(perk_name):
                self.item_perks[perk_name] = perk

        def has_item_perk(self, perk_name):
            if perk_name in self.item_perks:
                return True
            return False

        def get_item_perk(self, perk_name):
            if self.has_item_perk(perk_name):
                return self.item_perks[perk_name]
            return None

    class Stat_Perk(renpy.store.object):
        # owner can be MC or any other Person object (default is MC)
        # when owner is Person object we can add temporary stats without using a serum
        def __init__(self, description, owner = mc, cha_bonus = 0, int_bonus = 0, foc_bonus = 0,
            hr_bonus = 0, market_bonus = 0, research_bonus = 0, production_bonus = 0, supply_bonus = 0,
            foreplay_bonus = 0, oral_bonus = 0, vaginal_bonus = 0, anal_bonus = 0, energy_bonus = 0,
            stat_cap = 0, skill_cap = 0, sex_cap = 0, energy_cap = 0,
            bonus_is_temp = False, duration = 0):

            self.owner = owner
            self.description = description
            self.cha_bonus = cha_bonus
            self.int_bonus = int_bonus
            self.foc_bonus = foc_bonus
            self.hr_bonus = hr_bonus
            self.market_bonus = market_bonus
            self.research_bonus = research_bonus
            self.production_bonus = production_bonus
            self.supply_bonus = supply_bonus
            self.foreplay_bonus = foreplay_bonus
            self.oral_bonus = oral_bonus
            self.vaginal_bonus = vaginal_bonus
            self.anal_bonus = anal_bonus
            self.energy_bonus = energy_bonus
            self.stat_cap = stat_cap
            self.skill_cap = skill_cap
            self.sex_cap = sex_cap
            self.energy_cap = energy_cap
            self.bonus_is_temp = bonus_is_temp
            self.duration = duration
            self.start_day = day

            if description == None:
                self.description = ""

        def apply(self):
            self.owner.charisma += self.cha_bonus
            self.owner.int += self.int_bonus
            self.owner.focus += self.foc_bonus
            self.owner.hr_skill += self.hr_bonus
            self.owner.market_skill += self.market_bonus
            self.owner.research_skill += self.research_bonus
            self.owner.production_skill += self.production_bonus
            self.owner.supply_skill += self.supply_bonus
            self.owner.sex_skills["Foreplay"] += self.foreplay_bonus
            self.owner.sex_skills["Oral"] += self.oral_bonus
            self.owner.sex_skills["Vaginal"] += self.vaginal_bonus
            self.owner.sex_skills["Anal"] += self.anal_bonus
            self.owner.max_energy += self.energy_bonus
            if isinstance(self.owner, MainCharacter):
                self.owner.max_stats += self.stat_cap
                self.owner.max_work_skills += self.skill_cap
                self.owner.max_sex_skills += self.sex_cap
                self.owner.max_energy_cap += self.energy_cap
            return

        def remove(self):
            self.owner.charisma -= self.cha_bonus
            self.owner.int -= self.int_bonus
            self.owner.focus -= self.foc_bonus
            self.owner.hr_skill -= self.hr_bonus
            self.owner.market_skill -= self.market_bonus
            self.owner.research_skill -= self.research_bonus
            self.owner.production_skill -= self.production_bonus
            self.owner.supply_skill -= self.supply_bonus
            self.owner.sex_skills["Foreplay"] -= self.foreplay_bonus
            self.owner.sex_skills["Oral"] -= self.oral_bonus
            self.owner.sex_skills["Vaginal"] -= self.vaginal_bonus
            self.owner.sex_skills["Anal"] -= self.anal_bonus
            self.owner.max_energy -= self.energy_bonus
            if isinstance(self.owner, MainCharacter):
                self.owner.max_stats -= self.stat_cap
                self.owner.max_work_skills -= self.skill_cap
                self.owner.max_sex_skills -= self.sex_cap
                self.owner.max_energy_cap -= self.energy_cap
            return

    class Item_Perk(renpy.store.object):
        # owner can be MC or any other Person object (default is MC)
        def __init__(self, description, owner = mc, usable = False, bonus_is_temp = False, duration = 0):
            self.owner = owner
            self.description = description
            self.usable = usable
            self.bonus_is_temp = bonus_is_temp
            self.duration = duration
            self.start_day = day
