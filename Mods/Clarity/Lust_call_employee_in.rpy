init 1 python:
    def lust_blowjob_intro_requirement():
        if mc.business.is_open_for_business(): #Only trigger if people are in the office.
            if mc.is_at_work(): #Check to see if the main character is at work
                if len(get_willing_lust_blowjob_girl_list()) > 2 and get_lust_tier() > 2:
                    return True
        return False

    def lust_blowjob_office_requirement():
        if mc.business.is_open_for_business(): #Only trigger if people are in the office.
            if mc.is_at_work(): #Check to see if the main character is at work
                if get_lust_tier() > 2:
                    return True
                else:
                    return "Not enough Lust"
        else:
            return "Business isn't open"


init 2 python:

    def get_willing_lust_blowjob_girl_list():
        willing_blowjob_list = []
        the_taboo = blowjob.associated_taboo

        for person in mc.business.get_employee_list():
            final_slut_requirement, final_slut_cap = blowjob.calculate_position_requirements(person, False)

            if person.effective_sluttiness(the_taboo) > final_slut_requirement and person.energy > 80 and person.get_opinion_score("giving blowjobs") > -2: #Only include willing participants for the intro portion
                willing_blowjob_list.append(person)
        return willing_blowjob_list

    def lust_blowjob_build_employee_list():
        return mc.business.get_employee_list()

init 3 python:
    lust_blowjob_office = ActionMod("Office Blowjob {image=gui/heart/Time_Advance.png}", lust_blowjob_office_requirement, "lust_blowjob_office_label",
        menu_tooltip = "Order an employee to give you a blowjob", category="Business")
    lust_blowjob_intro = Action("Lust triggered meeting", lust_blowjob_intro_requirement, "lust_blowjob_intro_label")


label lust_blowjob_intro_label():
    $ the_person = None
    "In between shifts, you make your way around the office. You stop one in a while to admire some of the women you have employed."
    "Someone stops and asks you about something... it takes several seconds of starting at their tits before you realize they are talking to you."
    "Your sexual tension is starting to distract you from your work. You decide to hide in your office. You lock the door behind you."
    $ ceo_office.show_background()
    "You sit down at your computer and lookup some porn. You browse for a bit, looking for something good to watch."
    "As you are looking around though, you start to rethink this decision."
    "You own this business. You employee all these women. With the progress you've made with the serums, surely you could convince someone to help you out?"
    "You pull up your employee list on your computer... who should you call down?"
    $ emp_list = get_willing_lust_blowjob_girl_list()
    call screen enhanced_main_choice_display(build_menu_items([["Call in"] + emp_list], draw_hearts_for_people = False))
    $ the_person = _return
    if the_person == None:
        return
    "You walk over to your door and unlock it as you call [the_person.possessive_title]. You tell her to come to your office ASAP."
    "You walk back to your desk and sit down. Soon, there's a knock on your door."
    mc.name "Come in."
    $ the_person.draw_person()
    the_person "You wanted to see me?"
    mc.name "I did. Step inside and close the door... and lock it."
    the_person "Oh... okay..."
    "She does as you instruct before walking over to your desk and sitting down across from you."
    $ the_person.draw_person(position = "sitting")
    mc.name "Okay, I'm going to get straight to the point. I can't focus on work becuase of all the distractions around here. I need you to get me off so I can get back to work."
    the_person "Oh! Wow I didn't realize... god you scared me calling me in here like this!"
    if the_person.has_taboo("sucking_cock"):
        "[the_person.title] gets a shy smile on her face."
        the_person "So... you want like... a blowjob?"
        mc.name "It doesn't have to be your mouth, if you don't feel comfortable you could just use your hand."
        the_person "That's okay. To be honest I kinda want to find out how you taste."
    else:
        "[the_person.title] smiles at you."
        the_person "How about a blowjob? Would that help you get back to work?"
        if the_person.sluttiness > 70:
            the_person "Or do you need a different hole?"
        mc.name "A blowjob sounds perfect."
    "[the_person.possessive_title] walks around your desk, then gets on her knees next your chair. You turn to her."
    $ the_person.draw_person(position = "blowjob")
    "She fumbles with your zipper for a second, but soon has your cock out. She looks up at you while she gives it a couple strokes."
    the_person "Mmm, you're right, it's so hard! I bet you've got a big load saved up for me..."
    "[the_person.title] runs her tongue along the tip, tasting your pre-cum. She moans quietly before opening her mouth and slowly sliding the tip in her mouth."
    $ the_person.break_taboo("sucking_cock")
    call fuck_person(the_person, private = True, start_position = blowjob, skip_intro = True, position_locked = True) from _lust_blowjob_at_work_01
    $ the_report = _return

    if the_report.get("guy orgasms", 0) == 0:
        $ the_person.draw_person(position = "blowjob")
        "Frustrated with her service, you take control of the situation and finish yourself off by hand."
        $ the_person.cum_on_face()
        $ the_person.draw_person(position = "blowjob")
        "As you finish, you point your cock at [the_person.possessive_title]'s face, covering it in your seed."
        $ ClimaxController.manual_clarity_release()
    else:
        "Fully spent, you let yourself relax in your chair."
    $ the_person.draw_person(position = "stand3")
    "[the_person.title] stands up."
    the_person "Wow, I hope that helps you focus again [the_person.mc_title]. If you need this again, just let me know..."
    mc.name "Don't worry, I will."
    $ the_person.change_stats(obedience = 5, happiness = 5, slut_temp = 3)
    $ the_person.review_outfit()
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] turns and walks out of your office. That went great!"
    "You can now order an employee to give you a blowjob from the privacy of your office."
    "Realizing you have employees willing to suck your cock anytime you ask, you think about the mental gymnastics you've always put yourself through."
    "Lust has always been a taboo thing, to be shoved down and repressed, until you have the rare opportunity to utilize it."
    "But now... why bother repressing it? You make a mental note to stop repressing it. Now whenever you would normally gain lust, you gain extra."
    $ add_lust_gain_perk()
    "You have gained a new perk! Everytime you normally gain lust, you gain 5 extra."
    $ office.add_action(lust_blowjob_office)
    #TODO link up the room event here.
    return

label lust_blowjob_office_label():
    "You head into your office and sit down at your computer."
    $ ceo_office.show_background()
    "All the skin and sexy outfits you've been exposed to at work has got you hard as a rock and you need some relief. You decide to call an employee in for a blowjob."
    $ emp_list = lust_blowjob_build_employee_list()
    call screen enhanced_main_choice_display(build_menu_items([["Call in"] + emp_list], draw_hearts_for_people = True))
    if _return == "Leave" or _return == None:
        "After looking at your employee list, you change your mind. Maybe another opportunity will present itself later."
        return
    $ the_person = _return
    "You call [the_person.possessive_title] and tell her to come to your office ASAP."
    "Soon, there's a knock on your door."
    mc.name "Come in."
    $ the_person.draw_person()
    the_person "You wanted to see me?"
    mc.name "I did. Step inside and close the door... and lock it."
    the_person "Oh... okay..."
    "She does as you instruct before walking over to your desk and sitting down across from you."
    $ the_person.draw_person(position = "sitting")
    mc.name "Okay, I'm going to get straight to the point. I can't focus on work becuase of all the distractions around here."
    mc.name "I need you to give me a blowjob."
    $ slut_base = the_person.effective_sluttiness("sucking_cock")
    $ final_slut_requirement, final_slut_cap  = blowjob.calculate_position_requirements(the_person, False)
    if slut_base > (final_slut_requirement * 1.5) and not the_person.has_taboo("sucking_cock"):  #She's very slutty. Gets excited and strips first.
        the_person "Wow! Of all the employees here, you picked me for this? Thank you!"
        $ the_person.draw_person(position = "stand3")
        "[the_person.possessive_title] stands up and walks excitedly around your desk."
        the_person "Here, I bet this will help."
        $ the_person.strip_outfit(position = "stand3")
        "[the_person.title] sheds her clothes, giving you a good look at her naked body before getting down on her knees."
        $ the_person.draw_person(position = "blowjob")
        "She unzips your pants and pulls your cock out, giving it a couple strokes."
        if the_person.has_cum_fetish():
            "With her other hand she cups your balls, feeling their weight."
            the_person "Oh god... I can feel how full you are. You've saved up a big load for me, haven't you?"
            "[the_person.possessive_title] leans forward and licks all around the tip, savoring the taste of your cum."
            $ the_person.change_arousal(20)
            the_person "Oh fuck its so warm... I can't wait to feel it explode!"
            "[the_person.title] opens her mouth and takes you easily inside and down her throat. You run a hand through her hair as she starts to blow you."
            call get_fucked(the_person, private= True, start_position = cum_fetish_blowjob, start_object = make_floor(), skip_intro = True, allow_continue = False) from _call_cum_fetish_lust_blowjob_01
            $ the_report = _return
            if the_report.get("guy orgasms", 0) == 0:
                $ the_person.draw_person(position = "blowjob")
                "You decide to take control of the situation and finish yourself off by hand."
                $ the_person.cum_on_face()
                $ the_person.draw_person(position = "blowjob")
                "As you finish, you point your cock at [the_person.possessive_title]'s face, covering it in your seed."
                $ ClimaxController.manual_clarity_release()
            else:
                "Fully spent, you let yourself relax in your chair."
            $ the_person.draw_person(position = "stand3")
            "[the_person.title] stands up."
            the_person "Wow, I needed that too. Thank you so much for calling me [the_person.mc_title]"
            $ the_person.draw_person(position = "walking_away")
            "[the_person.possessive_title] turns and walks out of your office. She doesn't even bother to clean up."
        else:
            the_person "God you are so hard today. I bet you've got a big load saved up in there for me, don't you?"
            call fuck_person(the_person, private = True, start_position = blowjob, skip_intro = True, position_locked = True) from _lust_blowjob_at_work_02
            $ the_report = _return
            if the_report.get("guy orgasms", 0) == 0:
                $ the_person.draw_person(position = "blowjob")
                "Frustrated with her service, you take control of the situation and finish yourself off by hand."
                $ the_person.cum_on_face()
                $ the_person.draw_person(position = "blowjob")
                "As you finish, you point your cock at [the_person.possessive_title]'s face, covering it in your seed."
                $ ClimaxController.manual_clarity_release()
            else:
                "Fully spent, you let yourself relax in your chair."
            $ the_person.draw_person(position = "stand3")
            "[the_person.title] stands up."
            the_person "Wow, I hope that helps you focus again [the_person.mc_title]. I'm always happy to suck you off when you need it."
            mc.name "Thanks."
            $ the_person.change_stats(obedience = 5, happiness = 5)
            $ the_person.review_outfit()
            $ the_person.draw_person(position = "walking_away")
            "[the_person.possessive_title] turns and walks out of your office."


    elif  slut_base > final_slut_requirement:   #She accepts
        the_person "Oh! Wow I didn't realize... god you scared me calling me in here like this!"
        if the_person.has_taboo("sucking_cock"):
            "[the_person.title] gets a shy smile on her face."
            the_person "So... you want a blowjob?"
            mc.name "Yes. I've always wanted to feel your lips wrapped around me."
            the_person "Mmm... okay. To be honest I kinda want to find out how you taste."
        else:
            "[the_person.title] smiles at you."
            the_person "Mmm, a blowjob. Okay I'll do it."
        "[the_person.possessive_title] walks around your desk, then gets on her knees next your chair. You turn to her."
        $ the_person.draw_person(position = "blowjob")
        "She fumbles with your zipper for a second, but soon has your cock out. She looks up at you while she gives it a couple strokes."
        the_person "Mmm, you're right, it's so hard! I bet you've got a big load saved up for me..."
        "[the_person.title] runs her tongue along the tip, tasting your pre-cum. She moans quietly before opening her mouth and slowly sliding the tip in her mouth."
        $ the_person.break_taboo("sucking_cock")
        call fuck_person(the_person, private = True, start_position = blowjob, skip_intro = True, position_locked = True) from _lust_blowjob_at_work_03
        $ the_report = _return
        if the_report.get("guy orgasms", 0) == 0:
            $ the_person.draw_person(position = "blowjob")
            "Frustrated with her service, you take control of the situation and finish yourself off by hand."
            $ the_person.cum_on_face()
            $ the_person.draw_person(position = "blowjob")
            "As you finish, you point your cock at [the_person.possessive_title]'s face, covering it in your seed."
            $ ClimaxController.manual_clarity_release()
        else:
            "Fully spent, you let yourself relax in your chair."
        $ the_person.draw_person(position = "stand3")
        "[the_person.title] stands up."
        the_person "Wow, I hope that helps you focus again [the_person.mc_title]. If you need this again, just let me know..."
        mc.name "Don't worry, I will."
        $ the_person.change_stats(obedience = 5, happiness = 5, slut_temp = 3)
        $ the_person.review_outfit()
        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title] turns and walks out of your office."
    elif slut_base + (the_person.obedience-100) >= final_slut_requirement:  #You can order her to do it
        "[the_person.possessive_title] gasps."
        the_person "Wh... What??? You want me to..."
        "She lowers her voice to a whisper."
        the_person "Suck on it?"
        "You can see a troubled look in her eyes. You can tell she wants to, but her propriety is holding her back."
        mc.name "That is exactly what I want. Is there a problem?"
        the_person "I... sir are you sure that would be... proper?"
        mc.name "[the_person.title], is it proper for you to do the work that is assigned to you? Tasks that are assigned to you by me?"
        the_person "Of course..."
        mc.name "Then just think of this as an extra task that I am assigning. You can say no, if you choose, but it would really be helping me out if you would do it."
        if the_person.has_taboo("sucking_cock"):
            the_person "I suppose, but we... we just haven't done anyhting like this before!"
            mc.name "I know, but it would really help me out. And it would help the company, if I can finally concentrate on my work."
            "[the_person.title] takes several seconds to consider what you are saying."
            the_person "I suppose... I could try it."
        else:
            "[the_person.title] takes several seconds to consider what you are saying."
            the_person "I suppose... I mean... we've done this before..."
        the_person "What do you want me to do?"
        mc.name "Just come around here, and get on your knees."
        $ the_person.draw_person(position = "blowjob")
        "As [the_person.possessive_title] obediently gets down, you pull your cock out. She gasps when she sees it."
        the_person "Wow... it looks so hard! Its okay... I'll take care of it!"
        $ the_person.add_situational_slut("situation",10, "I'm doing my work duties.")
        "[the_person.title] opens her mouth and begins to suck you off. She starts off tentatively, but soon has a good rhythm going."
        call fuck_person(the_person, private = True, start_position = blowjob, skip_intro = True, position_locked = True) from _lust_blowjob_at_work_04
        $ the_report = _return
        $ the_person.clear_situational_slut("situation")
        if the_report.get("guy orgasms", 0) == 0:
            $ the_person.draw_person(position = "blowjob")
            "Frustrated with her service, you take control of the situation and finish yourself off by hand."
            $ the_person.cum_on_face()
            $ the_person.draw_person(position = "blowjob")
            "As you finish, you point your cock at [the_person.possessive_title]'s face, covering it in your seed."
            $ ClimaxController.manual_clarity_release()
        else:
            "Fully spent, you let yourself relax in your chair."
        $ the_person.draw_person(position = "stand3")
        "[the_person.title] stands up."
        mc.name "See? That was exactly what I needed. Thank you [the_person.title]."
        $ the_person.change_stats(obedience = 5, happiness = -5, slut_temp = 5, slut_core = 3)
        the_person "I suppose that was okay... let's not make a habit of this... okay?"
        mc.name "Don't worry, I won't."
        $ the_person.review_outfit()
        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title] turns and walks out of your office."
    else:   #She refuses
        $ the_person.draw_person(emotion="angry")
        the_person "Wha... what the fuck? You scare me half to death, calling me in here ASAP, thinking I'm in trouble for something..."
        "Her face grows red in anger."
        the_person "You're a sick man. I'm not some floozy for you to get your rocks off with!"
        $ the_person.draw_person(position = "walking_away")
        $ the_person.change_happiness(-5)
        $ the_person.change_obedience(-1)
        $ the_person.change_love(-2)
        $ the_person.change_slut_temp(3)
        "[the_person.possessive_title] quickly stands up and storms out of your office. Maybe you should be more careful who you pick for this?"
    call advance_time from _call_advance_time_lusty_blowjob_01
    return


label lust_blowjob_unit_test():
    $ mc.free_clarity = 0
    $ mc.change_locked_clarity(500)
    if not lust_blowjob_intro_requirement():
        "Intro requirements not met! Aborting unit test"
        return
    call lust_blowjob_intro_label() from _lust_unit_test_1
    $ mc.energy = mc.max_energy
    $ mc.change_locked_clarity(mc.free_clarity * 3)
    if not lust_blowjob_office_requirement():
        "Office blowjob requirements not met! aborting unit test"
        return
    call lust_blowjob_office_label() from _lust_unit_test_2
    "Unit test successful completion."
    return
