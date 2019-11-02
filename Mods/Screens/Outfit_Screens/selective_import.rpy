# Allows you to preview and select singular items from an XML file before importing.

init 2 python:
    def add_outfit(wardrobe, the_outfit, outfit_type = "full"):
            if outfit_type == "under":
                wardrobe.add_underwear_set(the_outfit)
            elif outfit_type == "over":
                wardrobe.add_overwear_set(the_outfit)
            else: #outfit_type = full
                wardrobe.add_outfit(the_outfit)

    def selected_xml_wardrobe(target_wardrobe, xml_filename): # TODO: Use this instead -> Show("import_outfit_manager", None, target_wardrobe, n)
        renpy.show_screen("import_outfit_manager", target_wardrobe, xml_filename)
    def selected_xml_clothing(outfit):
        renpy.show_screen("outfit_creator", outfit.get_copy())

init 2:
    screen import_outfit_manager(target_wardrobe, xml_filename, show_export = True): ##Brings up a list of the players current saved outfits, returns the selected outfit or None.
        $ wardrobe = wardrobe_from_xml(xml_filename)


        default outfit_categories = {"Full": ["FullSets", "full", "get_outfit_list"], "Overwear": ["OverwearSets", "over", "get_overwear_sets_list"], "Underwear": ["UnderwearSets", "under", "get_underwear_sets_list"]}
        add "Paper_Background.png"
        modal True
        zorder 100
        default preview_outfit = None
        grid len(outfit_categories) 1:
            xsize 900
            for category in outfit_categories: # NOTE: Dictionary is not sorted. Don't know the best way to make it so.
                vbox:
                    xsize 500
                    frame:
                        text category style "serum_text_style" xalign 0.5
                        xfill True
                    viewport:
                        if len(getattr(wardrobe, outfit_categories[category][2])()) > 6:
                            scrollbars "vertical"
                        mousewheel True
                        vbox:
                            if len(getattr(wardrobe, outfit_categories[category][2])()) > 0:
                                frame:
                                    vbox:
                                        for outfit in sorted(getattr(wardrobe, outfit_categories[category][2])(), key = lambda outfit: outfit.slut_requirement):  # Not sure if there's any good reason to sort XML lists since the default way it works is to place the newest outfit at the bottom which is predictable.
                                            frame:
                                                vbox:
                                                    xfill True
                                                    textbutton outfit.name  + "\n" + get_heart_image_list_cloth(outfit.slut_requirement, 1) +"":
                                                        xfill True
                                                        style "textbutton_no_padding_highlight"
                                                        text_style "serum_text_style"
                                                        action [
                                                            Show("outfit_creator", None, outfit.get_copy(), target_wardrobe, outfit_type = category[1]),
                                                            Hide(renpy.current_screen().screen_name)
                                                            ]

                                                        hovered Show("mannequin", None, outfit)

                                                    if show_export:
                                                        default exported = []

                                                        textbutton "Export to .xml File":
                                                            style "textbutton_no_padding_highlight"
                                                            text_style "serum_text_style"
                                                            xfill True

                                                            action [
                                                                Function(exported.append,outfit), Function(log_outfit, outfit, outfit_class = "FullSets", wardrobe_name = "Exported_Wardrobe"),
                                                                Function(renpy.notify, "Outfit exported to Exported_Wardrobe.xml")
                                                                ]

                                                            sensitive outfit not in exported

                                                        textbutton "Import to wardrobe: [target_wardrobe.name]":
                                                            style "textbutton_no_padding_highlight"
                                                            text_style "serum_text_style"
                                                            xfill True

                                                            action [
                                                                Function(add_outfit, target_wardrobe, outfit, outfit_type = "full"),
                                                                Function(renpy.notify, "Outfit imported to " + target_wardrobe.name)
                                                                ]
                                                            sensitive not target_wardrobe.has_outfit_with_name(outfit.name)


        frame:
            background None
            anchor [0.5,0.5]
            align [0.5,0.88]
            xysize [500,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                action Hide("import_outfit_manager")
            textbutton "Return" align [0.5,0.5] text_style "return_button_style"
