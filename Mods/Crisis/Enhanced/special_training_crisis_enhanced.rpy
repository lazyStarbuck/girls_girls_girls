# Originally written by Pilotus13
init 10 python:

    config.label_overrides["special_training_crisis_label"] = "enhanced_special_training_crisis_label"

init 2 python:
    def build_seminar_improvement_menu(the_person):
        work_seminar = [] # NOTE: We can allow seminars for both main and sex skills, e.g through introducing a company hosted seminar type.
        dict_work_skills = get_work_skills()
        for skill in dict_work_skills:
            work_seminar.append([dict_work_skills[skill][0] + "\nCurrent: " + str(getattr(the_person, dict_work_skills[skill][1])), dict_work_skills[skill][1]])
        work_seminar.insert(0, "Work Skills")
        return [work_seminar]



label enhanced_special_training_crisis_label():
    if not mc.business.get_employee_count() > 0:
        return #We must have had someone quit or be fired, so we no longer can get a random person.

    $ the_person = get_random_from_list(mc.business.get_employee_list())
    show screen person_info_ui(the_person)
    "You get a text  from [the_person.title]."
    the_person.char "[the_person.mc_title], I've just gotten word about a training seminar going on right now a few blocks away. I would love to take a trip over and see if there is anything I could learn."
    the_person.char "There's a sign up fee of $500. If you can cover that, I'll head over right away."
    if the_person.sluttiness >= 20:
        the_person.char "I'll personally repay you for it later..."
    menu:
        "Send [the_person.title] to the Seminar. -$500" if mc.business.funds >= 500:
            "You type up a response."
            the_person.mc_title "That sounds like a great idea. I'll call and sort out the fee, you start heading over."
            the_person.char "Understood, thank you sir! What would you like me to focus on?"

            call screen enhanced_main_choice_display(build_menu_items(build_seminar_improvement_menu(the_person)))
            if _return != "None":
                $ mc.business.change_funds(-500)
                $ setattr(the_person, _return, getattr(the_person, _return) + 2) #TODO: Make this line be generic.
                $ mc.log_event("[the_person.title]: " + "+2 " + get_work_skills()[_return][0], "float_text_grey")
                "[the_person.title] leaves work for a few hours to attend the training seminar. When she returns she has learned several useful techniques." # NOTE: Make this less generic

            if mc.is_at_work():#NOTE: So far the branches expect you to be in the office.

                if the_person.sluttiness >= 20:
                    $ the_person.draw_person(position="stand4")
                    "[the_person.title] returns from the seminar and enters your office where you are in your chair, idly tending to your duties."
                    the_person.char "There you are, [the_person.mc_title]! I'm back from the seminar and ready to show you the gratidude I promised."
                    $ seminar_clothing = the_person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)
                    if seminar_clothing is not None:
                        $ the_person.draw_animated_removal (seminar_clothing)
                        "Before you have time to reply, [the_person.title] begins stripping off her [seminar_clothing.name] right in front of you."
                        the_person.char "I thought it wouldn't hurt to show you a bit of skin, hope you don't mind?"
                        the_person.mc_title "Not at all, I always appreciate a pleasant sight, [the_person.title]."
                    if the_person.sluttiness >= 50:
                        $ seminar_clothing = the_person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
                        if seminar_clothing is not None:
                            "[the_person.possessive_title] isn't impressed by your reaction to her display.\nWanting to sweeten the deal for you, she continues on."
                            the_person.char "You deserve a bit more I guess... How about I take off my [seminar_clothing.name] for you?"
                            $ the_person.draw_animated_removal (seminar_clothing)
                            the_person.char "Do you like the view of [the_person.possessive_title] undressing?"
                        if the_person.age > 30:
                            "Your dick twitches at the sight of [the_person.title]'s mature body."
                        else:
                            "Your dick twitches at the sight of [the_person.title]'s nubile body."
                        if the_person.sluttiness >= 80:
                            $ seminar_clothing = the_person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
                            if seminar_clothing is not None:
                                the_person.char "You know... the seminar really did help me out..."
                                #$ seminar_clothing = the_person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
                                $ the_person.draw_animated_removal(seminar_clothing)
                            the_person.char "You like when I'm a bit naked, huh?"
                            "You feel like you could explode just from the view of [the_person.title]'s naked body as she stands there, teasing you."

                if the_person.sluttiness >= 90 or (the_person.sluttiness >= 60 and the_person.get_opinion_score("being covered in cum")) > 0 or (the_person.sluttiness >= 60 and the_person.get_opinion_score("giving blowjobs") > 0) or (the_person.sluttiness >= 60 and the_person.get_opinion_score("big dicks") > 0):
                    $ the_person.draw_person(emotion="sad")
                    "She stops to think for a second, putting on a frown before turning it into a bright, mischevious smile."
                    $ the_person.draw_person(emotion="happy")
                    the_person.char "Being naked in front of you made so... horny! You deserve some real gratitude! How about a quick BJ?"
                    "\"There's always time for a quick blowjob\" you think to yourself before swiftly unzipping your pants as [the_person.possessive_title] gets onto her knees."
                    $ the_person.draw_person(position="kneeling1")
                    the_person.char "[the_person.mc_title], you have such a nice cock, it'll be perfect inside of my mouth..."
                    $ the_person.draw_person(position="blowjob", special_modifier="blowjob")
                    "[the_person.title] opens her mouth and begins to vigorously suck on your dick with the full intent of giving you at least $500's worth of suction." #Nice. SUUUCTIIIIOOON
                    the_person.mc_title "I truly appreciate having such gracious employees; keep on going [the_person.title]."
                    $ the_person.draw_person(position="blowjob")
                    "[the_person.title] lets your cock drop out of her mouth as she grabs a hold of it, ministrating an enthusiastic handjob as she looks at your eyes with a smile plastered onto her face."
                    the_person.char "\", and I truly appreciate working for such a wonderful man!\" she replies while tugging at your length, cherishing your compliment."
                    the_person.char "You know... [the_person.mc_title], I owe you and your company a lot. I hope you know that I'll go to any lenghts to make the company succeed."
                    "She speeds up stroking your dick while cupping and massaging your balls with her other hand."
                    the_person.char "I hope the company will come to benefit from the techniques the seminar taught me... It will, right, [the_person.mc_title]?" # I would do anything to win the promotion.
                    $ the_person.draw_person(position="blowjob", special_modifier="blowjob")
                    "Before you can answer her, [the_person.title] swallows all of your cock into her mouth and begins moaning into it."
                    the_person.char "Mrmrmm... Mrmmmmm..."
                    "[the_person.title] continues to speed up and you begin to feel that it won't be long before you explode."
                    if the_person.get_opinion_score("giving blowjobs") > 0:
                        the_person.mc_title "It feels great, [the_person.title]! Get ready for a big one."
                    else:
                        pass
                    if the_person.get_opinion_score("being covered in cum") > 0 or the_person.get_opinion_score("giving blowjobs") > 0:
                        $ the_person.draw_person(position="kneeling1")
                        "Right before you hit your climax she pulls your cock out of her mouth and looks up into your eyes."
                        the_person.char "Yes, [the_person.mc_title]! I want to be covered by your sperm! Unleash it onto me, please!"
                        the_person.mc_title "OK, [the_person.title], keep still. Here it goes!"
                        $ the_person.cum_on_face()
                        "You start to unleash your load onto [the_person.possessive_title]'s face."
                        $ the_person.draw_person(position="blowjob", special_modifier="blowjob")
                        "She opens her mouth and attempts to catch some of the load that is being sprayed onto her face, cherishing each drop that falls inside."
                        $ the_person.cum_in_mouth()
                        $ the_person.draw_person(position="blowjob", special_modifier="blowjob")
                        "Soon [the_person.title]'s mouth is filled to the brim with your sperm from the torrent you're unleashing upon her, but you just cannot stop."
                        $ the_person.cum_on_tits()
                        $ the_person.draw_person(position="kneeling1")
                        "She closes her mouth shut to secure the load in her stomach while the excess cum drips down onto her tits, painting them white."
                        the_person.mc_title "There you go, [the_person.title]! That's how a decent [mc.business.name] employee should look like!"
                        #"The image of [the_person.title] sitting contently in front of with her body sealed in your sperm really fires you up."
                        $ the_person.draw_person(position = "stand2", emotion = "happy")
                        "[the_person.title] pushes herself up off the floor then takes in the spectacle of her body. Her eyes trail down her chest as drops of your sperm fall onto the carpet below."
                        the_person.char "Really, [the_person.mc_title]? Maybe you would like to have a better look?"
                        $ the_person.draw_person(position = "back_peek")
                        "[the_person.title] starts to turn around with the intention of striking various poses, allowing you to enjoy the sight of her cum drenched body."
                        $ the_person.draw_person(position = "missionary", emotion = "happy")
                        "She lies herself back onto the floor before spreading her legs, giving you a perfect view of her now dripping vagina. Her juices flow onto the carpet, mixing itself with yours."
                        the_person.char "Do you prefer this view? My pussy is yours to use however you want for the sake of [mc.business.name]." # Should probably include some less NTR- suggestive dialogue depending on preferences etc.
                        "She basks in the pleasurable sensation that announcing her devotion to you and [mc.business.name] is giving her.\nShe then continues her routine of displaying herself from multiple angles."
                        the_person.char "If my pussy is off limits... then how about this."
                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                        "[the_person.title] rolls herself onto her stomach, then gets up on her knees as she opens her mouth, whipping her tongue while reaching down to rub at her clit."
                        the_person.char "I can be on my knees handing out blowjobs to whoever you want..."
                        the_person.char "I'll gladly suck any dick you instruct me to if it helps [mc.business.name] prosper."
                        $ the_person.draw_person(position = "standing_doggy", emotion = "happy")
                        "[the_person.title] then rotates her back towards you, reaching up to support herself by resting her arms on the desk as she arches her back forward, pushing her ass in your direction, wiggling it left and right."
                        #the_person.char "You should also check up this ass. It is also usable if you would like so."
                        the_person.char "I wouldn't mind if you share this ass of mine with your investors or friends either. I'd actually love that, [the_person.mc_title]!"
                        $ the_person.draw_person(position = "back_peek", emotion = "happy")
                        "[the_person.title] straightens her back then walks towards the door to that leads out of your office. In the doorway she stops and turns to you."
                        the_person.char "Remember [the_person.mc_title], anything for the company."
                    else:
                        $ seminar_cum = renpy.random.randint(1,4)
                        if seminar_cum > 3:
                            $ the_person.cum_on_face()
                            "She pulls your cock out of her mouth then looks intently at your eyes."
                            the_person.char "Yes, [the_person.mc_title]. Shoot it right onto me! Give me one... big... facial."
                        else:
                            if seminar_cum > 2:
                                $ the_person.cum_on_stomach()
                                "She pulls your cock out of her mouth then looks up into your eyes as she leans away from you."
                                the_person.char "Oh, [the_person.mc_title]. I just applied new makeup. Please, don't ruin it."
                            else:
                                if seminar_cum > 1:
                                    $ the_person.cum_in_mouth()
                                    "She withdraws her mouth from your cock, resting it by the tip as she looks into your eyes with her mouth wide open."
                                    the_person.char "Yes, [the_person.mc_title]! Shoot your load right into my mouth. I love the taste of you."
                                else:
                                    $ the_person.cum_on_tits()
                                    "She pulls your cock out of her mouth then looks up into your eyes as she presents her chest to you."
                                    the_person.char "Like my tits, [the_person.mc_title]? They'll look much better covered in your cum..."
                        $ the_person.draw_person(position="blowjob")
                        "[the_person.title] keeps sitting on her knees while receiving you load."
                        the_person.char "Aaaah, it feels great!"
                        $ the_person.draw_person(position = "stand3", emotion = "happy")
                        "[the_person.title] kisses the tip of your cock before standing up, smiling."
                        the_person.char "Thanks, [the_person.mc_title]. That's just what I needed! I hope you found my repayment adequate."
                        the_person.char "Now back to work."
                else:
                    if the_person.sluttiness >= 60:
                        "She leans in and strokes your cock a little, then leaves the room."
                    else:
                        "She gives you a kiss on the cheek before leaving the room."

        "Tell her to stay at work.":
            "You type up a response."
            the_person.mc_title "I'm sorry [the_person.title], but there aren't any extra funds in the budget right now."
            the_person.char "Noted, maybe some other time then."

    return