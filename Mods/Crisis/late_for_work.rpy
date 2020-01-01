## Late for Work Crisis Mod by Tristimdorion
init -1 python:
    late_for_work_weight = 10   # Increase weight because it only occurs in one timeslot.

init 2 python:
    def late_for_work_requirement():
        if mc.business.get_employee_count() > 0:
            if time_of_day == 1: #is morning when employees arrive.
                if mc.business.is_open_for_business() and mc.is_at_work():
                    return True
        return False

    late_for_work_action = ActionMod("Late for Work", late_for_work_requirement, "late_for_work_action_label",
        menu_tooltip = "An employee is late for work.", category = "Business", is_crisis = True, crisis_weight = late_for_work_weight)

label late_for_work_action_label:
    #Lets get the girl of interest.
    $ the_person = get_random_from_list(mc.business.get_employee_list())

    "As you are walking through the main corridor you spot [the_person.possessive_title] rushing through the entrance doors."

    if the_person.sluttiness < 40:
        $ the_person.draw_person(position="stand3", emotion="default")
        menu:
            "Lecture Her On Being Late":
                $ the_person.draw_person(emotion = 'sad')
                mc.name "Do you know what time we start here [the_person.title]?"
                the_person.char "Sorry [the_person.mc_title], I missed my bus."
                mc.name "I don't care what you have to do, but I need you to be here on time. Now get going..."
                $ the_person.change_obedience(3)
                $ the_person.change_happiness(-2)

            "Let it slide":
                $ the_person.draw_person(emotion = 'happy')
                mc.name "Well, ok, now quickly run along [the_person.title]."
                $ the_person.change_obedience(-2)
                $ the_person.change_happiness(2)

        $ the_person.draw_person(position = 'walking_away')
        "[the_person.possessive_title] quietly rushes to her desk."
    elif the_person.relationship != "Single":
        $ the_person.cum_on_tits()
        $ the_person.draw_person(position="stand3", emotion="default")
        the_person.char "I'm sorry [the_person.mc_title], [the_person.SO_name] needed some personal attention when he dropped me off at the office."
        $ upper_clothing = the_person.outfit.get_upper_ordered()[-1]
        menu:
            "Lecture Her On Being Late":
                $ the_person.draw_person(emotion = 'sad')
                mc.name "Do you know what time we start here [the_person.title]?"
                the_person.char "I am really sorry [the_person.mc_title]."
                if (upper_clothing):
                    mc.name "I don't care, next time be on time and cleanup your [upper_clothing.name]"
                else:
                    mc.name "I don't care, next time be on time and make your tits presentable."
                $ the_person.change_obedience(3)
                $ the_person.change_happiness(-2)

            "Let it slide":
                $ the_person.draw_person(emotion = 'happy')
                if (upper_clothing):
                    mc.name "Well at least cleanup your [upper_clothing.name], before you start."
                else:
                    mc.name "At least get that cum of your tits, before you go to work."
                the_person.char "Thank you, [the_person.mc_title]!"
                $ the_person.change_obedience(-2)
                $ the_person.change_happiness(2)

            "What a coincidence..." if affair_role in the_person.special_role:   #Hope this is okay I added this... - Starbuck
                mc.name "I'm feeling the need for a little personal attention myself."
                the_person.char "Oh, is that so?"
                if (upper_clothing):
                    mc.name "That's right. Get on your knees, I want your practiced mouth on my cock now."
                else:
                    mc.name "That's right. Get on your knees, I won't be content with just your tits."
                if the_person.get_opinion_score("being submissive") > 0:
                    $ the_person.change_obedience(5)
                    $ the_person.change_happiness(5)
                    $ the_person.change_slut_temp(5)
                    the_person.char "Oh god, I love it when you take charge like this..."
                else:
                    the_person.char "Mmm, sounds fun..."
                $ the_person.draw_person(position = "blowjob")
                "She quickly gets down on her knees. She pulls your cock out of you pants and gives it a couple strokes."
                the_person.char "Mmm, can't believe I get to suck my two favorite cocks in the same morning..."
                "Her mouth opens and envelopes your cock. She begins to suck you off eagerly."
                call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True, private = True) from _call_late_for_work_BJ_1
                $ the_report = _return
                if the_report.get("girl orgasms",0) > 0:
                    "It takes [the_person.title] a minute before she finally stands up, recovering from her orgasm."
                $ the_person.draw_person(position="stand3", emotion="default")
                if the_report.get("guy orgasms",0) > 0:
                    "Satisfied with her work, you enjoy the afterglow of your orgasm."
                else:
                    "You decide not to cum for her at this time."
                mc.name "That's enough for now. Try to be on time from now on, or atleast be ready to service me again if you ARE going to be late."
                the_person.char "Yes sir!"
                $ the_person.change_obedience(2)
                $ the_person.change_slut_temp(2)

        $ the_person.draw_person(position = 'walking_away')
        "[the_person.possessive_title] rushes to the ladies room to cleanup."
    elif the_person.sluttiness < 80:
        $ the_person.draw_person(position="stand3", emotion="default")
        the_person.char "[the_person.mc_title]! I know this looks bad. I have a great excuse for being late, I swear!"
        "You feel yourself roll you eyes for a moment involuntarily."
        the_person.char "I just had to... ummm... my car had a... a thing wrong with it!"
        mc.name "Oh? What was it doing?"
        the_person.char "It was... Look I'm sorry I'm late, it won't happen again. Please don't write me up!"
        $ the_person.draw_person(position="stand4", emotion="happy")
        "She gives you a big fake smile and strikes a pose."
        the_person.char "I could do something... you know... to make it up to you!"
        "She puts her hand on your crotch. She looks you in the eye and licks her lips."
        menu:
            "Lecture Her On Being Late":
                $ the_person.draw_person(emotion = 'sad')
                mc.name "Do you know what time we start here [the_person.title]?"
                the_person.char "I am really sorry [the_person.mc_title]."
                mc.name "I don't care, next time be on time and make your tits presentable."
                $ the_person.change_obedience(3)
                $ the_person.change_happiness(-2)

            "Let it slide":
                $ the_person.draw_person(emotion = 'happy')
                mc.name "Well, ok, now quickly run along [the_person.title]."
                $ the_person.change_obedience(-2)
                $ the_person.change_happiness(2)

            "Make it up to me":
                mc.name "If you want to make it up to me, get on your knees."
                if the_person.get_opinion_score("being submissive") > 0:
                    $ the_person.change_obedience(5)
                    $ the_person.change_happiness(5)
                    $ the_person.change_slut_temp(5)
                    the_person.char "Oh god, I love it when you take charge like this..."
                else:
                    the_person.char "Yes sir!"
                $ the_person.draw_person(position = "blowjob")
                "She quickly gets down on her knees. She pulls your cock out of you pants and gives it a couple strokes."
                if the_person.get_opinion_score("giving blowjobs") < 0:
                    the_person.char "Mmm, can't believe I get to suck your cock. This is how to start the day off right..."
                "Her mouth opens and envelopes your cock. She begins to suck you off eagerly."
                call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True, private = True) from _call_late_for_work_BJ_2
                $ the_report = _return
                if the_report.get("girl orgasms",0) > 0:
                    "It takes [the_person.title] a minute before she finally stands up, recovering from her orgasm."
                $ the_person.draw_person(position="stand3", emotion="default")
                if the_report.get("guy orgasms",0) > 0:
                    "Satisfied with her work, you enjoy the afterglow of your orgasm."
                else:
                    "You decide not to cum for her at this time."
                mc.name "That's enough for now. Try to be on time from now on, or atleast be ready to service me again if you ARE going to be late."
                the_person.char "Yes sir!"
                $ the_person.change_obedience(2)
                $ the_person.change_slut_temp(2)

    else:
        $ the_person.cum_on_face()
        $ the_person.cum_on_tits()
        $ the_person.draw_person(position="stand3", emotion="default")
        the_person.char "Sorry [the_person.mc_title], a client caught me in the parking lot and wanted to have a business meeting in his car. You can let marketing know I made the sale."
        mc.name "Well, it sure does look like it was a productive meeting. Go clean yourself up before you get back to work. I don't want you dripping that all over the building."
        if the_person.get_opinion_score("cum facials") > 0:
            the_person.char "Aww. But I like the way it feels."
        elif the_person.get_opinion_score("cum facials") < 0:
            the_person.char "Definitely, I hate feeling all sticky."
        else:
            the_person.char "Of Course [the_person.mc_title]."

        $ the_person.draw_person(position = 'walking_away')
        "The client wires the money to your company account, but must have forgot to actually placed an order."
        $ mc.business.pay(250)

    $ renpy.scene("Active")
    $ the_person.review_outfit(show_review_message = False)
    return
