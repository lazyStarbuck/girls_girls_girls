init 5 python:
    opinions_list.insert(7, "boots")
    opinions_list.insert(10, "high heels")
    opinions_list.insert(13, "dresses")
    opinions_list.insert(15, "the colour green")
    opinions_list.insert(15, "the colour purple")
    opinions_list.insert(15, "the colour white")

    # generate a more useable default color palette
    if len(persistent.colour_palette) == 10:
        persistent.colour_palette = [
            [.20, .29, .70, .95],  [0, .45, .73, .95], [.26, .49, .76, .95], [.89, .65, .34, .95], [.96, .77, .19, .95], [.98, .92, .36, .95],
            [.33, .10, .06, .95], [.80, .26, .04, .95], [.99, .42, .52, .95], [.87, .44, .63, .95], [1, .41, .71, .95], [1, .73, .85, .95],
            [.29, .32, .12, .95], [.18, .54, .34, .95], [.0, .8, .6, .95], [.41, .16, .38, .95], [.45, .31, .59, .95], [.71, .4, .85, .95],
            [.95, .95, .95, .95], [.15, .15, .15, .95],
            [1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]    # allow for 6 unused userdefinable colors
        ]

    class WardrobeBuilder():
        preferences = {}
        preferences["skimpy outfits"] = {}
        preferences["skimpy outfits"]["upper_body"] = [two_part_dress, thin_dress, leotard, tshirt, lace_sweater, sweater, belted_top, lace_crop_top, tanktop, tube_top, business_vest]
        preferences["skimpy outfits"]["lower_body"] = [leggings, booty_shorts, jean_hotpants, belted_skirt, lace_skirt, mini_skirt]
        preferences['skimpy outfits']["feet"] = [thigh_highs, fishnets, garter_with_fishnets, pumps, heels, high_heels, thigh_high_boots]
        preferences["skimpy outfits"]["accessories"] = [lace_choker, wide_choker, spiked_choker]
        preferences["conservative outfits"] = {}
        preferences["conservative outfits"]["upper_body"] = [long_sweater, sleeveless_top, long_tshirt, camisole, long_sleeve_blouse, short_sleeve_blouse, tie_sweater, dress_shirt, summer_dress]
        preferences["conservative outfits"]["lower_body"] = [pencil_skirt, skirt, long_skirt]
        preferences["conservative outfits"]["feet"] = [sandles, shoes, slips, sneakers, tall_boots, short_socks, medium_socks]
        preferences["conservative outfits"]["accessories"] = [wool_scarf]
        preferences["dresses"] = {}
        preferences["dresses"]["lower_body"] = [x for x in dress_list if x not in [lacy_one_piece_underwear, lingerie_one_piece]]
        preferences["skirts"] = {}
        preferences["skirts"]["lower_body"] = skirts_list
        preferences["pants"] = {}
        preferences["pants"]["lower_body"] = pants_list
        preferences["showing her tits"] = {}
        preferences["showing her tits"]["upper_body"] = [strapless_bra, lace_bra, leotard, thin_dress, two_part_dress, lacy_one_piece_underwear, lingerie_one_piece, lace_sweater, sweater, belted_top, tube_top, business_vest, suit_jacket, vest]
        preferences["showing her ass"] = {}
        preferences["showing her ass"]["upper_body"] = [two_part_dress, thin_dress, summer_dress, leotard, lacy_one_piece_underwear, lingerie_one_piece]
        preferences["showing her ass"]["lower_body"] = [cute_panties, lace_panties, cute_lace_panties, tiny_lace_panties, thong, tiny_g_string, leggings, booty_shorts, jean_hotpants]
        preferences["high heels"] = {}
        preferences["high heels"]["feet"] = [sandle_heels, pumps, heels, high_heels, boot_heels, thigh_high_boots]
        preferences["boots"] = {}
        preferences["boots"]["feet"] = [boot_heels, tall_boots, thigh_high_boots]
        preferences["makeup"] = {}
        preferences["makeup"]["accessories"] = [light_eye_shadow, heavy_eye_shadow, blush, lipstick]
        preferences['lingerie'] = {}
        preferences['lingerie']["upper_body"] = [lacy_one_piece_underwear, lingerie_one_piece, strapless_bra, lace_bra, thin_bra, corset]
        preferences['lingerie']["lower_body"] = [cute_panties, lace_panties, cute_lace_panties, tiny_lace_panties, thin_panties, thong, tiny_g_string]
        preferences['lingerie']["feet"] = [thigh_highs, fishnets, garter_with_fishnets]
        preferences['lingerie']['accessories'] = [lace_choker, wide_choker]

        color_prefs = {}
        color_prefs["the colour blue"] = {}
        color_prefs["the colour blue"]["violet blue"] = [.20, .29, .70, .95]
        color_prefs["the colour blue"]["french blue"] = [0, .45, .73, .95]
        color_prefs["the colour blue"]["tufts blue"] = [.26, .49, .76, .95]
        color_prefs["the colour yellow"] = {}
        color_prefs["the colour yellow"]["indian yellow"] = [.89, .65, .34, .95]
        color_prefs["the colour yellow"]["saffron"] = [.96, .77, .19, .95]
        color_prefs["the colour yellow"]["corn"] = [.98, .92, .36, .95]
        color_prefs["the colour red"] = {}
        color_prefs["the colour red"]["bordeaux red"] = [.33, .10, .06, .95]
        color_prefs["the colour red"]["sinopia"] = [.80, .26, .04, .95]
        color_prefs["the colour red"]["wild strawberry"] = [.99, .42, .52, .95]
        color_prefs["the colour pink"] = {}
        color_prefs["the colour pink"]["thulian pink"] = [.87, .44, .63, .95]
        color_prefs["the colour pink"]["hot pink"] = [1, .41, .71, .95]
        color_prefs["the colour pink"]["cotton candy"] = [1, .73, .85, .95]
        color_prefs["the colour black"] = {}
        color_prefs["the colour black"]["midnight black"] = [.15, .15, .15, .95]
        color_prefs["the colour black"]["warm black"] = [0, .26, .36, .95]
        color_prefs["the colour black"]["charcoal"] = [.21, .27, .34, .95]
        color_prefs["the colour green"] = {}
        color_prefs["the colour green"]["army green"] = [.29, .32, .12, .95]
        color_prefs["the colour green"]["sea green"] = [.18, .54, .34, .95]
        color_prefs["the colour green"]["caribbean green"] = [.0, .8, .6, .95]
        color_prefs["the colour purple"] = {}
        color_prefs["the colour purple"]["palatinate purple"] = [.41, .16, .38, .95]
        color_prefs["the colour purple"]["dark lavender"] = [.45, .31, .59, .95]
        color_prefs["the colour purple"]["rich lilac"] = [.71, .4, .85, .95]
        color_prefs["the colour white"] = {}
        color_prefs["the colour white"]["white smoke"] = [.95, .95, .95, .95]
        color_prefs["the colour white"]["ghost white"] = [.97, .97, 1, .95]
        color_prefs["the colour white"]["bright white"] = [1, 1, 1, .95]
        #color_prefs[""][""] = [, , , ]

        earings_only_list = [chandelier_earings, gold_earings, modern_glasses]

        def __init__(self, person):
            if person and isinstance(person, Person):
                self.person = person
            else:
                self.person = create_random_person("Ema","Hesire", 23, "thin_body", "B", 0.91, create_home_location = False)
                self.person.opinions.clear() # reset opinions so every item has an equal chance
                self.person.sexy_opinions.clear()

            skirts_score = self.person.get_opinion_score("skirts")
            pants_score = self.person.get_opinion_score("pants")
            dress_score = self.person.get_opinion_score("dresses")

            # person hates all main clothing items, make her like skirts.
            if skirts_score + pants_score + dress_score == -6:
                self.person.opinions["skirts"] = [1, True]

        def build_outfit(self, outfit_type, points):
            if (outfit_type == "OverwearSets"):
                return self.build_overwear(points)
            if (outfit_type == "UnderwearSets"):
                return self.build_underwear(points)

            underwear = self.build_underwear(points)
            overwear = self.build_overwear(points)

            for item in underwear.upper_body:
                if overwear.can_add_upper(item):
                    overwear.add_upper(item)
            
            for item in underwear.lower_body:
                if overwear.can_add_lower(item):
                    overwear.add_lower(item)
            
            for item in underwear.feet:
                if overwear.can_add_feet(item):
                    overwear.add_feet(item)

            for item in underwear.accessories:
                if overwear.can_add_accessory(item):
                    overwear.add_accessory(item)

            # prevent any item from having no colour set
            for cloth in overwear.upper_body + overwear.lower_body + overwear.feet + overwear.accessories:
                if len(cloth.colour) < 4:
                    cloth.colour = [1, 1, 1, .5]    # transparant white is easy to spot for debuggin

            return overwear

        def get_hate_list(self):
            item_list = []
            for pref in self.preferences:
                score = self.person.get_opinion_score(pref)
                if score == -2:
                    item_list.append(pref)
            return item_list

        def build_overwear(self, points = 0):
            outfit = Outfit("Overwear")

            color_upper, color_lower, color_feet = self.get_main_color_scheme()

            upper_item_list = [x for x in dress_list + shirts_list if x not in [lacy_one_piece_underwear, lingerie_one_piece]]

            # find upper body item
            filtered_upper_list = list(filter(lambda x: x.slut_value <= points, upper_item_list))
            item = self.get_item_from_list("upper_body", filtered_upper_list)
            if item:
                score = self.person.get_opinion_score("not wearing anything")
                if points < 3 or not renpy.random.randint(0, (score + 2) * 5) > 13:
                    outfit.add_upper(item.get_copy(), color_upper)

            # we added a overlay item, so find a real upper item this time
            if item and item.layer == 3:
                filtered_upper_list = list(filter(lambda x: x.slut_value <= points and x.layer == 2, upper_item_list))
                item = self.get_item_from_list("upper_body", filtered_upper_list)
                if item:
                    outfit.add_upper(item.get_copy(), color_lower)

            # find lowerbody item
            if item is None or not item.has_extension:
                item = self.get_item_from_list("lower_body", self.build_filter_list(pants_list + skirts_list, points))
                if item:
                    score = self.person.get_opinion_score("not wearing anything")
                    if points < 3 or not renpy.random.randint(0, (score + 2) * 5) > 13:
                        outfit.add_lower(item.get_copy(), [color_lower[0] * .9, color_lower[1] * .9, color_lower[2] * .9, color_lower[3]])

            # find feet item
            filtered_feet_list = list(filter(lambda x: x.slut_value <= points, shoes_list))
            item = self.get_item_from_list("feet", filtered_feet_list)
            if item:
                outfit.add_feet(item.get_copy(), [color_feet[0] * .8, color_feet[1] * .8, color_feet[2] * .8, color_feet[3]])

            outfit.name = self.get_name_classification(points) + self.get_cloting_name(outfit.upper_body, 2) + " and " + self.get_cloting_name(outfit.lower_body, 2)

            return outfit

        def build_underwear(self, points = 0):
            outfit = Outfit("Underwear")

            color_upper, color_lower, color_feet = self.get_main_color_scheme()
            
            # find upperbody item
            item = self.get_item_from_list("upper_body", self.build_filter_list(bra_list + [lingerie_one_piece, lacy_one_piece_underwear], points))
            if item:
                score = self.person.get_opinion_score("showing her tits") + self.person.get_opinion_score("not wearing underwear")
                if points < 3 or not renpy.random.randint(0, (score + 4) * 5) > 22:
                    outfit.add_upper(item.get_copy(), color_upper)

            # find lowerbody item
            if not item or not item.has_extension:
                item = self.get_item_from_list("lower_body", self.build_filter_list(panties_list, points))
                if item:
                    score = self.person.get_opinion_score("showing her ass") + self.person.get_opinion_score("not wearing underwear")
                    if points < 3 or not renpy.random.randint(0, (score + 4) * 5) > 22:
                        outfit.add_lower(item.get_copy(), color_lower)
            
            if points > 4 or renpy.random.randint(0, 3) == 0:
                item = self.get_item_from_list("feet", self.build_filter_list(socks_list, points))
                if item:
                    outfit.add_feet(item.get_copy(), color_feet)
            
            make_up_score = self.person.get_opinion_score("makeup")
            if make_up_score > 0 or (make_up_score == 0 and renpy.random.randint(0, 4) == 0):
                make_up_score += renpy.random.randint(1, 2)
                if make_up_score > 0:
                    outfit.add_accessory(lipstick.get_copy(), get_random_from_list([[.5, .18, .18, .95], [.75, .05, .05, .95], [.9, .45, .6, .95]]))
                if make_up_score > 1:
                    outfit.add_accessory(blush.get_copy(), [.9, .45, .6, .95])
                if make_up_score > 2:
                    outfit.add_accessory(light_eye_shadow.get_copy(), get_random_from_list([[.15, .15, .15, .95], [.5, .18, .18, .95]]))
                if make_up_score > 3:
                    outfit.add_accessory(heavy_eye_shadow.get_copy(), get_random_from_list([[.15, .15, .15, .95], [.1, .15, .55, .9]]))

            self.add_accessory_from_list(outfit, self.build_filter_list(self.earings_only_list, points), 3, color_lower)
            self.add_accessory_from_list(outfit, self.build_filter_list(bracelet_list, points), 3, color_upper)
            self.add_accessory_from_list(outfit, self.build_filter_list(rings_list, points), 3, color_lower)
            self.add_accessory_from_list(outfit, self.build_filter_list(neckwear_list, points), 3, color_upper)

            outfit.name = self.get_name_classification(points) + self.get_cloting_name(outfit.upper_body, 1) + " and " + self.get_cloting_name(outfit.lower_body, 1)

            return outfit


        def build_filter_list(self, item_list, points):
            return list(filter(lambda x: x.slut_value <= points, item_list))
        
        def add_accessory_from_list(self, outfit, filtered_list, chance, item_color = [.8, .1, .1, .95]):
            if renpy.random.randint(0, chance) == 0:
                item = get_random_from_list(filtered_list)
                if item:
                    outfit.add_accessory(item.get_copy(), item_color)
            return

        def get_main_color_scheme(self):
            primary_color = self.get_color()
            alternate_color = self.get_color()
            
            col_choice = renpy.random.randint(0, 50)
            if col_choice < 10:
                color_upper = primary_color
                color_lower = alternate_color
                color_feet = primary_color
            elif col_choice >= 10 and col_choice < 40:
                color_upper = primary_color
                color_lower = primary_color
                color_feet = alternate_color
            else:
                color_upper = primary_color
                color_lower = alternate_color
                color_feet = alternate_color

            return (color_upper, color_lower, color_feet)

        def get_item_from_list(self, item_group, filtered_list):
            weighted_list = self.build_weighted_list(item_group, filtered_list)

            for pref in self.preferences:
                if item_group in self.preferences[pref]:
                    if self.person.get_opinion_score(pref) == -2:
                        item_list = [x for x in weighted_list if x[0] not in self.preferences[pref][item_group]]
                        if item_list: # check if we have any items left, if not use original weighted list
                            weighted_list = item_list
            
            renpy.random.shuffle(weighted_list)

            item = get_random_from_weighted_list(weighted_list)

            if hasattr(item, "supported_patterns") and item.supported_patterns and renpy.random.randint(0, 1) == 1:
                key_value = get_random_from_list(list(item.supported_patterns.keys()))
                item.pattern = item.supported_patterns[key_value]
                item.colour_pattern = self.get_color()

            return item

        def build_weighted_list(self, item_group, filtered_list):
            item_list = []
            for item in filtered_list:
                item_list.append([item, 0])
            for pref in self.preferences:
                score = self.person.get_opinion_score(pref)
                for name in self.preferences[pref]:
                    if name == item_group:
                        for item in self.preferences[pref][name]:
                            if item in filtered_list:                      
                                [x for x in item_list if item in x][0][1] += (score + 2) * 5

            return [x for x in item_list if x[1] > 0]

        def get_color(self):
            color_list = []
            for cp in self.color_prefs:
                score = self.person.get_opinion_score(cp)
                if score != -2:
                    for col in self.color_prefs[cp]:
                        color_list.append([self.color_prefs[cp][col], (score + 2) * 5])

            renpy.random.shuffle(color_list)
            return get_random_from_weighted_list([x for x in color_list if x[1] > 0])

        def get_name_classification(self, points):
            if points < 2:
                return "Conservative "
            if points < 4:
                return "Relaxed "
            if points < 6:
                return "Sexy "
            return "Slutty "
        
        def get_cloting_name(self, items, layer):
            item = filter(lambda x: x.layer == layer, items)
            if (item):
                return item[0].name
            return "skin"
