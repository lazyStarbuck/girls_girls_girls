#This file contains the generic clothes shoping label as well as Candace specific version.
#Clothes shopping is unlocked after Candace takes you.
#Label starts out at a regular store, girl tries on three outfits. If players approves of less than 2, she prompts player to pick something out.
#After, based on sluttiness,  she picks out a set of new underwear. If not slutty, its regular underwear. If moderately slutty, its lingerie. If very slutty, pulls MC into room with her for sex scene.
#Anytime girl tries on outfit that she REALLY likes, if she works for MC, asks MC to wear to work. If yes, add outfit to her department uniform options.
#TODO, should we give option to add outfit to player's outfit selection?


label candace_goes_clothes_shopping_label(the_person):
    $ the_person.draw_person(position = "sitting")
    "You step up to [the_person.possessive_title]'s desk. She's been working for you for a week now, so you decide to check up on her."
    mc.name "Hey there, [the_person.title]. How are you settling in?"
    the_person.char "Oh hey [the_person.mc_title]! Its going pretty good!"
    mc.name "Everything been working out okay?"
    the_person.char "Yes! It sure has! I have really been enjoying the work here, and the freedom I have now is great!"
    the_person.char "Guess what I did last night?"
    mc.name "What's that?"
    "[the_person.title] lowers her voice so as not to disturb others around her."
    the_person.char "I fucked my landlord!"
    mc.name "Oh! That's... great?!?"
    the_person.char "I know! And this time I did it just for fun! I didn't even need the rent discount! I just got my first paycheck. I've been trying to figure out what to do with it."
    mc.name "That's good to hear. And don't worry. It's not a race! You don't have to spend it as it comes in, you can always save some back."
    the_person.char "Yeah, I suppose. But it feels like, its my first one, right? I should use it for something fun?"
    mc.name "That's true. Any ideas?"
    the_person.char "Well, I was thinking about going over to the mall. My boyf... I mean, my ex... he purged a lot of my favorite outfits. I was thinking about buying a couple new skirts or something!"
    mc.name "That's actually a really good idea."
    the_person.char "Yeah. I guess I'll just wait until this weekend. By the time I get off work here, I'm so tired."
    "You think about it for a moment."
    mc.name "You know... if you want to, you could always take a chunk of the day off and go. Honestly, I understand your situation, and I think it would be good for you to build your wardrobe back up."
    the_person.char "Oh! Are you sure? I mean, I only just started... playing hooky from work already?"
    "She thinks about it for a bit."
    the_person.char "That's really tempting... but, you know, back with my... ex... he used to help me pick out stuff to wear. I'm not sure I know what even looks good on me anymore!"
    mc.name "Umm, honestly, with a body like yours, just about anything looks good."
    $ the_person.change_happiness(2)
    $ the_person.change_love(2)
    the_person.char "Aww, you charmer! I don't know, I just wish I had someone to go with me. A second set of eyes on everything, you know?"
    "Hmm... you COULD volunteer... you've never been clothes shopping with a woman before. All the tropes make it sound so boring. But, with a girl like [the_person.title], how boring could it be?"
    "You ponder it silently for a bit."
    the_person.char "Wait a minute... you're a guy!"
    mc.name "Yes... that is true?"
    the_person.char "Oh my god! Will you take me? PLEASE PLEASE PLEASE PLEEEEEAAASSSSEEEEE!"
    mc.name "You want me to go with you?"
    the_person.char "Of course! I mean, who else would be better to judge how sexy the outfits are? You, umm... you're into girls right?"
    if the_person.has_taboo("vaginal_sex"):
        mc.name "Ha! Yes, I'm definitely into girls."
    else:
        mc.name "Umm... we've had sex."
        the_person.char "Oh! Right... of course."
    the_person.char "Good, come on, just do it! I promise you won't regret it!"
    "A promise like that from [the_person.possessive_title] should not be taken lightly."
    mc.name "Ok. Let's go."
    $ the_person.draw_person()
    the_person.char "Yay! I can't wait!"

    $ mc.change_location(clothing_store)
    $ mc.location.show_background()

    "You leave the business and soon find yourself at the mall. You let [the_person.possessive_title] lead the way into the first store."
    "She browses through the racks of clothes but eventually finds a couple things she likes."
    the_person.char "Okay, you wait right here, I'll be right back to show you what I picked out!"
    $ renpy.scene("Active")
    call trying_on_clothes_label(the_person) from _clothes_shopping_candace_intro_01
    "You walk with [the_person.title] up to the checkout line."
    the_person.char "God, that was fun! We should do that again sometime!"
    "You are surprised to admit it, but you actually had a lot of fun too."
    mc.name "Yeah I'd be up for doing that again sometime!"
    "After checking out, you part ways with [the_person.possessive_title]."
    mc.name "I'm not going back to work right away. Feel free to take the rest of the day off if you want."
    the_person.char "You're sweet. Thanks for the shopping trip!"
    $ the_person.draw_person(position = "walking_away")
    "This was really a fun way to watch [the_person.title] try on stuff in an intimate setting... maybe you should invite some other girls to go shopping sometime?"
    "You have now unlocked clothes shopping! Return to the clothing store anytime to invite a girl to go shopping with you."
    #TODO actually add this action
    $ candace.event_triggers_dict["clothes_shopping"] = 1

    return

label trying_on_clothes_label(the_person): #This label starts with trying on clothes, to finishing up with picking them out. The particulars of the setup and the transaction are for the calling label
    "You wait patiently while [the_person.title] changes." #lol make MC wait while we generate all the outfits.
    python:
        outfit_slut_points = max(int(the_person.sluttiness / 8), 12)
        outfit_counter = 0

        outfit_1 = WardrobeBuilder(the_person).build_outfit(None, outfit_slut_points)
        outfit_2 = WardrobeBuilder(the_person).build_outfit(None, outfit_slut_points)
        outfit_3 = WardrobeBuilder(the_person).build_outfit(None, outfit_slut_points)
        underwear_1 = WardrobeBuilder(the_person).build_outfit("UnderwearSets", outfit_slut_points)
        preferences = WardrobePreference(the_person) #For determining if she loves the outfit or not
        the_person.apply_outfit(outfit_1)
    "It isn't long until [the_person.title] emerges from the dressing room."
    $ the_person.draw_person()
    the_person.char "Hey! What do you think?"
    "She gives you a little turn so you can see all sides."
    $ the_person.draw_person(position = "back_peek")
    if preferences.evaluate_outfit(outfit_1, the_person.sluttiness + 10, sluttiness_min = the_person.sluttiness - 10):
         the_person.char "I actually really like this one!"
    else:
         the_person.char "I'm not certain about this one to be honest!"
    $ the_person.draw_person(position = "stand4")
    the_person.char "Be honest!"
    menu:
        "Keep that outfit":
            #TODO change responses based on sluttiness of outfit
            mc.name "It looks really good on you."
            the_person.char "Aww, thank you! Okay!"
            $ outfit_counter += 1
            $ the_person.wardrobe.add_outfit(outfit_1)
            call clothes_shopping_ask_to_add_to_uniform(the_person, outfit_1, preferences) from _clothes_shopping_uniform_addition_1
        "Try something else":
            mc.name "I'm not sure that is the best look for you. Maybe try something else?"
            the_person.char "Hmm, yeah, I think you might be right."
    the_person.char "Okay, stay right there, I'll be right back with the next one."
    $ renpy.scene("Active")
    "You hang out for a bit. Your mind wanders a bit, thinking about [the_person.title] getting naked in the dressing room..."
    $ the_person.apply_outfit(outfit_2)
    $ the_person.draw_person()
    the_person.char "Hey... you aren't dozing off on me are you?"
    "You look up and check out [the_person.title]'s next outfit."
    mc.name "Hmm... interesting. Let me see the back."
    $ the_person.draw_person(position = "back_peek")
    the_person.char "Does it look good?"
    $ the_person.draw_person(position = "stand3")
    menu:
        "Keep that outfit":
            #TODO change responses based on sluttiness of outfit
            mc.name "That one is definitely a keeper."
            the_person.char "Great!"
            $ outfit_counter += 1
            $ the_person.wardrobe.add_outfit(outfit_2)
            call clothes_shopping_ask_to_add_to_uniform(the_person, outfit_2, preferences) from _clothes_shopping_uniform_addition_2
        "Try something else":
            mc.name "I'm not sure that outfit works. What else do you have?"
    the_person.char "Okay, I have one more, I'll be right back with the last one."
    $ renpy.scene("Active")
    "Hmm... [the_person.title] is back there right now, stripping down, slipping into something else... maybe you should try and sneak a peak..."
    $ the_person.apply_outfit(outfit_3)
    $ the_person.draw_person()
    "You are just starting to consider trying to sneak back there when she pops out of the dressing room."
    the_person.char "Alright! Third time is a charm. How about this?"
    $ the_person.draw_person(position = "back_peek")
    the_person.char "Make sure to check all the angles!"
    $ the_person.draw_person(position = "stand4")
    menu:
        "Keep that outfit":
            #TODO change responses based on sluttiness of outfit
            mc.name "Yep! That outfit was MADE for you."
            the_person.char "Aww. Okay!"
            $ outfit_counter += 1
            $ the_person.wardrobe.add_outfit(outfit_3)
            call clothes_shopping_ask_to_add_to_uniform(the_person, outfit_3, preferences) from _clothes_shopping_uniform_addition_3
        "Try something else":
            mc.name "Honestly I think you would be better off with something else. It just isn't flattering."
    if outfit_counter == 0:
        the_person.char "Seriously? Not a single outfit? You are impossible!"
        the_person.char "Tell you what. I'm gonna go change out of this. While I'm in there, pick out something for me to try on that YOU think is good and I'll try it on, okay?"
        mc.name "Okay."
        $ renpy.scene("Active")
        "[the_person.possessive_title] disappears to the back room to change. You look around at the different clothing racks, looking for something for her to try on."
        call screen outfit_creator(Outfit("New Outfit"))
        if _return:
            $ created_outfit = _return
            "You put together an outfit and take them to the back."
            if preferences.evaluate_outfit(created_outfit, the_person.sluttiness + 10, sluttiness_min = the_person.sluttiness - 10):
                the_person.char "Oh! This looks really nice! Ok give me just a minute and I'll be out, but I think I like it!"
            else:
                the_person.char "Hmm, normally I probably wouldn't pick out something like this, but I'll try it on for you..."
            $ the_person.apply_outfit(created_outfit)
            $ the_person.draw_person()
            "The dressing room door opens and you see [the_person.title] standing there."
            if created_outfit.get_full_outfit_slut_score() > the_person.sluttiness + 20:
                the_person.char "I umm... I don't think I can come out of here in this."
                mc.name "What are you talking about? It looks fantastic!"
                the_person.char "No. Get your looks in, [the_person.mc_title], but I understand now why you want me to come clothes shopping with you!"
                $ renpy.scene("Active")
                "She closes the door. Damn, you must have gone a little overboard with that outfit..."
                the_person.char "I'm going to change back into, you know, DECENT clothes."
                $ the_person.change_happiness(-5)
                $ the_person.change_slut_temp(5)
            else:
                the_person.char "Alright, what do you think?"
                $ the_person.draw_person(position = "back_peek")
                the_person.char "I'm trying it on just for you!"
                $ the_person.draw_person(position = "stand4")
                menu:
                    "Keep that outfit":
                        #TODO change responses based on sluttiness of outfit
                        mc.name "What can I say, I have good taste!"
                        the_person.char "Alright!"
                        $ outfit_counter += 1
                        $ the_person.wardrobe.add_outfit(created_outfit)
                    "Try something else":
                        mc.name "I'm sorry, I think maybe I'm not the one who should be doing this."
                        the_person.char "Geeze, you're awful! Whatever, I liked the last outfit, I'm gonna get it even if you didn't like it!"
                        $ the_person.wardrobe.add_outfit(outfit_3)
                the_person.char "Alright, I'm gonna change back into my other clothes now..."
                $ renpy.scene("Active")
        $ the_person.apply_outfit(the_person.planned_outfit)
        #TODO consider something sexy here
        "You give her a minute to change back into her regular outfit."
        $ the_person.draw_person()
    else:
        the_person.char "Alright! I feel like this was actually a productive trip! I'm gonna go get changed back into my normal clothes."
        $ renpy.scene("Active")
        $ the_person.apply_outfit(the_person.planned_outfit)
        "You give her a minute to change back into her regular outfit."
        $ the_person.draw_person()
        the_person.char "Alright, I'm gonna go check out now."
        mc.name "I'll follow you."
        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title] begins walking toward the front of the department store."
        "As you are walking, you walk by the section of women's undergarments."
        the_person.char "Oh! That's a really a good sale!"
        "Suddenly, [the_person.title] takes a detour into the underwear section."
        the_person.char "This is great!"
        if the_person.sluttiness < 25:
            "You see [the_person.title] looking at normal women's undergarments. You see her pick out a pair."
            the_person.char "I'm gonna go try these on real quick..."
            mc.name "Go ahead, I'll wait outside the door."
            the_person.char "Okay!"
            $ renpy.scene("Active")
            $ the_person.apply_outfit(underwear_1)
            "Behind the closed door, you hear [the_person.title] shuffling around a bit."
            the_person.char "Okay... I can't decide if I like this set or not. I know this is kinda crazy but, would you tell me what you think?"
            mc.name "Absolutely."
            $ the_person.draw_person()
            the_person.char "What do you think?"
            menu:
                "Looks great!":
                    mc.name "The color and cut looks great on you!"
                    the_person.char "Aww, thank you! Okay that's enough peaking..."
                    $ the_person.change_slut_temp(2)
                    $ the_person.change_happiness(2)
                    $ the_person.wardrobe.add_outfit(underwear_1)
                "Not your style":
                    mc.name "Your body looks great, but this particular cut isn't flattering."
                    the_person.char "Yeah I was afraid of that. Thank you for your honesty! Okay that's enough peaking..."
                    $ the_person.change_slut_temp(2)
                    $ the_person.change_obedience(2)
            $ renpy.scene("Active")
            $ the_person.apply_outfit(the_person.planned_outfit)
            "In another few moments, [the_person.title] emerges from the dressing room."
            $ the_person.draw_person()
            the_person.char "Alright, let's go before I try on something else!"

        else:
            "You watch as [the_person.title] goes through the lingerie. There is some really sexy stuff here..."
            "You see as she grabs a couple of things."
            the_person.char "I'm gonna go try these on really quick."
            "She lowers her voice to a hush."
            the_person.char "I'll be looking for your expert opinion, so stay by the door, okay [the_person.mc_title]?"
            mc.name "Hell yeah I'll be right there."
            "She giggles and heads off to the dressing room."
            $ renpy.scene("Active")
            $ the_person.apply_outfit(underwear_1)
            "Behind the closed door, you hear [the_person.title] shuffling around a bit."
            the_person.char "Okay, are you ready out there?"
            mc.name "Absolutely."
            $ the_person.draw_person()
            the_person.char "What do you think?"
            "She gives you a quick turn, then bends over the the bench in the dressing room."
            $ the_person.draw_person(position = "standing_doggy")
            "She wiggles her hips a couple of times."
            the_person.char "Do you think I'll be able to get a man's attention with this?"
            menu:
                "Looks sexy!":
                    mc.name "It certainly has my attention. Is there room for two in that dressing room?"
                    the_person.char "Mmm, not today [the_person.mc_title]."
                    $ the_person.change_slut_temp(2)
                    $ the_person.change_happiness(2)
                    $ the_person.wardrobe.add_outfit(underwear_1)
                "Not your style":
                    mc.name "Your body looks great, but this particular cut isn't flattering."
                    the_person.char "Yeah I was afraid of that. Thank you for your honesty!"
                    $ the_person.change_slut_temp(2)
                    $ the_person.change_obedience(2)
            "You gawk for another moment, but eventually the door closes and [the_person.title] begins changing back into her normal outfit."
            $ renpy.scene("Active")
            $ the_person.apply_outfit(the_person.planned_outfit)
            "In another few moments, [the_person.title] emerges from the dressing room."
            $ the_person.draw_person()
            the_person.char "Alright, let's go before I try on something else!"
    python:
        del outfit_slut_points
        del outfit_counter
        del outfit_1
        del outfit_2
        del outfit_3
        del underwear_1
        del preferences

    return


label clothes_shopping_ask_to_add_to_uniform(the_person, the_outfit, preferences):
    if not the_person.is_employee():#Only run if person is employee
        return
    if preferences.evaluate_outfit(the_outfit, the_person.sluttiness + 10, sluttiness_min = the_person.sluttiness - 25): #Only run if she loves the outfit
        the_person.char "I really like this outfit. Do you think maybe, you could add it to the work uniform list?"
        the_person.char "I'd love to be able to wear it to work!"
        $ slut_limit, underwear_limit, limited_to_top = mc.business.get_uniform_limits()
        if limited_to_top: #For now, we don't have clothes shopping for overwear only, so if its limited to overwear then we certainly don't have the required policy
            "You take a look at the outfit, but quickly realize that it does not match the current uniform guidelines."
            mc.name "I'm sorry, but the current employee contract wouldn't allow for me to add that to the uniform guidelines."
            "She gives you a little pout, but seems to understand."
            return
        menu:
            "Add it to the uniforms"if the_outfit.get_full_outfit_slut_score() <= slut_limit:
                mc.name "I think I'll do that when we get back to the office."
                the_person.char "Yay! Thank you [the_person.mc_title]!"
                $ clothes_shopping_get_work_wardrobe(the_person).add_outfit(the_outfit)
                #TODO figure out a way to make this count toward uniform goal count
            "Add it to the uniforms\n{color=#ff0000}{size=18}Too slutty!{/size}{/color} (disabled)" if the_outfit.get_full_outfit_slut_score() > slut_limit:
                pass
            "Don't add to the uniforms":
                mc.name "I looks great, but I don't think the other girls would wear it as well as you."
                "She gives you a little pout, but seems to understand."
    return

init python:
    def clothes_shopping_get_work_wardrobe(the_person):
        if the_person in mc.business.research_team:
            return mc.business.r_uniform
        if the_person in mc.business.market_team:
            return mc.business.m_uniform
        if the_person in mc.business.supply_team:
            return mc.business.s_uniform
        if the_person in mc.business.production_team:
            return mc.business.p_uniform
        if the_person in mc.business.hr_team:
            return mc.business.h_uniform