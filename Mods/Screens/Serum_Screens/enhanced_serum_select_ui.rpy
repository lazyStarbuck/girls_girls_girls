init -1 python:
        def get_trait_side_effect_text(trait):
            trait_side_effects = trait.get_effective_side_effect_chance()

            if trait_side_effects >= 60: # Red (Color code the side effect risk for quicker identification)
                return "{color=#cd5c5c}" + str(trait_side_effects) + "{/color}"
            elif trait_side_effects >= 20: # Yellow
                return "{color=#eee000}" + str(trait_side_effects) + "{/color}"
            else: # Green
                return "{color=#98fb98}" + str(trait_side_effects) + "{/color}"

        def get_trait_mastery_text(trait):
            if trait.mastery_level <= 10: # Red
                return "{color=#cd5c5c}" + str(trait.mastery_level) + "{/color}"
            elif trait.mastery_level <= 50: # Yellow
                return "{color=#eee000}" + str(trait.mastery_level) + "{/color}"
            else: # Green
                return "{color=#98fb98}" + str(trait.mastery_level) + "{/color}"

init 2:
    screen serum_select_ui: #How you select serum and trait research
        add "Science_Menu_Background.png"
        vbox:
            xalign 0.08
            yalign 0.4
            frame:
                background "#888888"
                xsize 1200
                frame:
                    background "#000080"
                    xsize 1190
                    if not mc.business.active_research_design == None:
                        $ trait_side_effects_text = get_trait_side_effect_text(mc.business.active_research_design)
                        $ trait_mastery_text = get_trait_mastery_text(mc.business.active_research_design)
                        text "Current Research: [mc.business.active_research_design.name] ([mc.business.active_research_design.current_research]/[mc.business.active_research_design.research_needed])" + "{size=14} Mastery Level: [trait_mastery_text] | Side Effect Chance: [trait_side_effects_text] %" style "serum_text_style"
                    else:
                        text "Current Research: None!" style "serum_text_style"

            null height 20

            frame:
                background "#888888"
                xsize 1200
                ysize 900
                hbox:
                    spacing 5
                    vbox:
                        frame:
                            background "#000080"
                            xsize 380
                            text "Research New Traits" style "serum_text_style"

                        viewport:
                            xsize 380
                            ysize 780
                            scrollbars "vertical"
                            mousewheel True
                            vbox:
                                xsize 370
                                for trait in sorted(sorted(list_of_traits, key = lambda trait: trait.exclude_tags, reverse = True), key=lambda trait: trait.tier, reverse = True): # Sort traits by exclude tags (So all production traits are grouped, for example), then by tier (so the highest tier production tag ends up at the top
                                    if not trait.researched and trait.has_required() and "Production" in trait.exclude_tags:
                                        $ trait_tags = ""
                                        if trait.exclude_tags:
                                            $ trait_tags = "\nExcludes Other: "
                                            for a_tag in trait.exclude_tags:
                                                $ trait_tags += "[" + a_tag + "]"
                                        $ trait_title = trait.name + " " + "(" +str(trait.current_research)+"/"+ str(trait.research_needed) + ")" + trait_tags

                                        textbutton "[trait_title]":
                                            style "textbutton_style"
                                            text_style "serum_text_style_traits"
                                            action [Hide("trait_tooltip"),Return(trait)]

                                            hovered Show("trait_tooltip",None,trait)
                                            unhovered Hide("trait_tooltip")
                                            xsize 365

                                for trait in sorted(sorted(list_of_traits, key = lambda trait: trait.exclude_tags, reverse = True), key=lambda trait: trait.tier, reverse = True): # Sort traits by exclude tags (So all production traits are grouped, for example), then by tier (so the highest tier production tag ends up at the top
                                    if not trait.researched and trait.has_required() and "Suggest" in trait.exclude_tags:
                                        $ trait_tags = ""
                                        if trait.exclude_tags:
                                            $ trait_tags = "\nExcludes Other: "
                                            for a_tag in trait.exclude_tags:
                                                $ trait_tags += "[" + a_tag + "]"
                                        $ trait_title = trait.name + " " + "(" +str(trait.current_research)+"/"+ str(trait.research_needed) + ")" + trait_tags

                                        textbutton "[trait_title]":
                                            style "textbutton_style"
                                            text_style "serum_text_style_traits"
                                            action [Hide("trait_tooltip"),Return(trait)]

                                            hovered Show("trait_tooltip",None,trait)
                                            unhovered Hide("trait_tooltip")
                                            xsize 365

                                for trait in sorted(sorted(list_of_traits, key = lambda trait: trait.exclude_tags, reverse = True), key=lambda trait: trait.name, reverse = False): # Sort traits by exclude tags (So all production traits are grouped, for example), then by name since tier does not matter.
                                    if not trait.researched and trait.has_required() and "Production" not in trait.exclude_tags and "Suggest" not in trait.exclude_tags:
                                        $ trait_tags = ""
                                        if trait.exclude_tags:
                                            $ trait_tags = "\nExcludes Other: "
                                            for a_tag in trait.exclude_tags:
                                                $ trait_tags += "[" + a_tag + "]"
                                        $ trait_title = trait.name + " " + "(" +str(trait.current_research)+"/"+ str(trait.research_needed) + ")" + trait_tags

                                        textbutton "[trait_title]":
                                            style "textbutton_style"
                                            text_style "serum_text_style_traits"
                                            action [Hide("trait_tooltip"),Return(trait)]

                                            hovered Show("trait_tooltip",None,trait)
                                            unhovered Hide("trait_tooltip")
                                            xsize 365
                    vbox:
                        frame:
                            background "#000080"
                            xsize 410
                            text "Master Existing Traits:" style "serum_text_style"

                        viewport:
                            xsize 410
                            ysize 780
                            scrollbars "vertical"
                            mousewheel True
                            vbox:
                                xsize 400
                                for trait in sorted(sorted(list_of_traits, key = lambda trait: trait.exclude_tags, reverse = True), key=lambda trait: trait.tier, reverse = True): # Sort traits by exclude tags (So all production traits are grouped, for example), then by tier (so the highest tier production tag ends up at the top
                                    if trait.researched and "Production" in trait.exclude_tags:
                                        $ trait_tags = ""
                                        if trait.exclude_tags:
                                            $ trait_tags = "\nExcludes Other: "
                                            for a_tag in trait.exclude_tags:
                                                $ trait_tags += "[" + a_tag + "]"

                                        $ trait_title = trait.name + " " + "(" +str(trait.current_research)+"/"+ str(trait.research_needed) + ")" + trait_tags

                                        $ trait_side_effects_text = get_trait_side_effect_text(trait)
                                        $ trait_mastery_text = get_trait_mastery_text(trait)

                                        textbutton "[trait_title]\nMastery Level: [trait_mastery_text] | Side Effect Chance: [trait_side_effects_text] %":
                                            text_xalign 0.5
                                            text_text_align 0.5

                                            action [Hide("trait_tooltip"),Return(trait)] style "textbutton_style"
                                            text_style "serum_text_style_traits"
                                            hovered Show("trait_tooltip",None,trait)
                                            unhovered Hide("trait_tooltip")
                                            xsize 395

                                for trait in sorted(sorted(list_of_traits, key = lambda trait: trait.exclude_tags, reverse = True), key=lambda trait: trait.tier, reverse = True): # Sort traits by exclude tags (So all production traits are grouped, for example), then by tier (so the highest tier production tag ends up at the top
                                    if trait.researched and "Suggest" in trait.exclude_tags:
                                        $ trait_tags = ""
                                        if trait.exclude_tags:
                                            $ trait_tags = "\nExcludes Other: "
                                            for a_tag in trait.exclude_tags:
                                                $ trait_tags += "[" + a_tag + "]"

                                        $ trait_title = trait.name + " " + "(" +str(trait.current_research)+"/"+ str(trait.research_needed) + ")" + trait_tags

                                        $ trait_side_effects_text = get_trait_side_effect_text(trait)
                                        $ trait_mastery_text = get_trait_mastery_text(trait)

                                        textbutton "[trait_title]\nMastery Level: [trait_mastery_text] | Side Effect Chance: [trait_side_effects_text] %":
                                            text_xalign 0.5
                                            text_text_align 0.5

                                            action [Hide("trait_tooltip"),Return(trait)] style "textbutton_style"
                                            text_style "serum_text_style_traits"
                                            hovered Show("trait_tooltip",None,trait)
                                            unhovered Hide("trait_tooltip")
                                            xsize 395

                                for trait in sorted(sorted(list_of_traits, key = lambda trait: trait.exclude_tags, reverse = True), key=lambda trait: trait.name, reverse = False): # Sort traits by exclude tags (So all production traits are grouped, for example), then by name since tier does not matter.
                                    if trait.researched and "Production" not in trait.exclude_tags and "Suggest" not in trait.exclude_tags:
                                        $ trait_tags = ""
                                        if trait.exclude_tags:
                                            $ trait_tags = "\nExcludes Other: "
                                            for a_tag in trait.exclude_tags:
                                                $ trait_tags += "[" + a_tag + "]"

                                        $ trait_title = trait.name + " " + "(" +str(trait.current_research)+"/"+ str(trait.research_needed) + ")" + trait_tags

                                        $ trait_side_effects_text = get_trait_side_effect_text(trait)
                                        $ trait_mastery_text = get_trait_mastery_text(trait)

                                        textbutton "[trait_title]\nMastery Level: [trait_mastery_text] | Side Effect Chance: [trait_side_effects_text] %":
                                            text_xalign 0.5
                                            text_text_align 0.5

                                            action [Hide("trait_tooltip"),Return(trait)] style "textbutton_style"
                                            text_style "serum_text_style_traits"
                                            hovered Show("trait_tooltip",None,trait)
                                            unhovered Hide("trait_tooltip")
                                            xsize 395

                    vbox:
                        frame:
                            background "#000080"
                            xsize 380
                            text "Research New Designs:" style "serum_text_style"

                        viewport:
                            xsize 380
                            ysize 780
                            scrollbars "vertical"
                            mousewheel True
                            vbox:
                                xsize 370

                                for serum in mc.business.serum_designs:
                                    if not serum.researched:
                                        textbutton "[serum.name] ([serum.current_research]/[serum.research_needed])":
                                            text_xalign 0.5
                                            text_text_align 0.5

                                            action [Hide("serum_tooltip"),Return(serum)] style "textbutton_style"
                                            text_style "serum_text_style_traits"
                                            hovered Show("serum_tooltip",None,serum)
                                            unhovered Hide("serum_tooltip")
                                            xsize 365

                textbutton "Do not change research." action [Return("None"), Hide("trait_tooltip")] style "textbutton_style" text_style "serum_text_style" yalign 0.995 xanchor 0.5 xalign 0.5

        imagebutton:
            auto "/tutorial_images/restart_tutorial_%s.png"
            xsize 54
            ysize 54
            yanchor 1.0
            xalign 0.0
            yalign 1.0
            action Function(mc.business.reset_tutorial,"research_tutorial")

        $ research_tutorial_length = 5 #The number of  tutorial screens we have.
        if mc.business.event_triggers_dict["research_tutorial"] > 0 and mc.business.event_triggers_dict["research_tutorial"] <= research_tutorial_length: #We use negative numbers to symbolize the tutorial not being enabled
            imagebutton:
                auto
                sensitive True
                xsize 1920
                ysize 1080
                idle "/tutorial_images/research_tutorial_"+__builtin__.str(mc.business.event_triggers_dict["research_tutorial"])+".png"
                hover "/tutorial_images/research_tutorial_"+__builtin__.str(mc.business.event_triggers_dict["research_tutorial"])+".png"
                action Function(mc.business.advance_tutorial,"research_tutorial")
