init 5 python:
    add_label_hijack("normal_start", "updated_room_background")
    add_label_hijack("after_load", "updated_room_background")

    # scaled images
    taboo_break_image = im.Scale(Image(get_file_handle("taboo_lock_alt.png")), 16, 16)
    renpy.image("taboo_break", taboo_break_image)
    thumbs_up_image = im.Scale(Image(get_file_handle("thumbs_up_small.png")), 18, 18)
    renpy.image("thumbs_up", thumbs_up_image)
    thumbs_down_image = im.Scale(Image(get_file_handle("thumbs_down_small.png")), 18, 18)
    renpy.image("thumbs_down", thumbs_down_image)

    energy_token_small_image = im.Scale(Image(get_file_handle("energy_token.png")), 18, 18)
    renpy.image("energy_token_small", energy_token_small_image)

    arousal_token_small_image = im.Scale(Image(get_file_handle("arousal_token.png")), 18, 18)
    renpy.image("arousal_token_small", arousal_token_small_image)

    question_mark_small_image = im.Scale(Image(get_file_handle("question.png")), 18, 18)
    renpy.image("question_mark_small", question_mark_small_image)

    vial_image = Image(get_file_handle("vial.png"))
    question_image = Image(get_file_handle("question.png"))


init -1 python:
    # override default render backgrounds
    enhanced_office_backgrounds = room_background_image("Main_Office_Background.jpg")
    enhanced_marketing_backgrounds = room_background_image("Marketing_Background.jpg")
    enhanced_production_backgrounds = room_background_image("Production_Background.jpg")
    enhanced_research_backgrounds = room_background_image("RandD_Background.jpg")
    enhanced_lobby_backgrounds = room_background_image("Lobby_Background.jpg")
    # updated (no existing backgrounds)
    standard_sex_store_backgrounds = room_background_image("Sex_Shop_Background.jpg")
    standard_gym_backgrounds = room_background_image("Gym_Background.jpg")
    # extra backgrounds
    standard_biotech_backgrounds = room_background_image("Biotech_Background.jpg")
    standard_dungeon_backgrounds = room_background_image("Dungeon_Background.jpg")
    standard_hotel_backgrounds = room_background_image("Hotel_Room_Background.jpg")
    standard_fancy_restaurant_backgrounds = room_background_image("Fancy_Restaurant_Background.jpg")
    standard_gym_shower_backgrounds = room_background_image("Gym_Shower_Background.jpg")
    standard_salon_backgrounds = room_background_image("Salon_Background.jpg")
    standard_home_shower_backgrounds = room_background_image("Home_Shower_Background.jpg")

label updated_room_background(stack):
    python:
        # as long as the base game has no nice images, we use these to make navigating a little more fun
        office.background_image = enhanced_office_backgrounds[:]
        m_division.background_image = enhanced_marketing_backgrounds[:]
        p_division.background_image = enhanced_production_backgrounds[:]
        rd_division.background_image = enhanced_research_backgrounds[:]
        lobby.background_image = enhanced_lobby_backgrounds[:]

        #As long a there is a mall background for these, replace it with our custom background
        sex_store.background_image = standard_sex_store_backgrounds[:]
        gym.background_image = standard_gym_backgrounds[:]

        # continue on the hijack stack if needed
        execute_hijack_call(stack)

    # Load extra GUI images
    image serum_vial = "[vial_image.filename]"
    image question_mark = "[question_image.filename]"

    return
