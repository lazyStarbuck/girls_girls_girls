
init 2 python:
    def ashley_mod_initialization(): #Add actionmod as argument#

        ashley_wardrobe = wardrobe_from_xml("Sarah_Wardrobe")
        ashley_base_outfit = Outfit("ashley's base accessories")
        the_glasses = big_glasses.get_copy()
        the_glasses.colour = [.15, .15, .15, 1.0]
        the_eyeshadow = light_eye_shadow.get_copy()   #Change this
        the_eyeshadow.colour = [.45,.31,.59,1.0]
        ashley_base_outfit.add_accessory(the_glasses)
        ashley_base_outfit.add_accessory(the_eyeshadow)

        #TODO make ashley live with Stephanie

        # ashley_home = Room("ashley's home", "ashley's home", [], apartment_background, [],[],[],False,[0,0], visible = False, hide_in_known_house_map = False, lighting_conditions = standard_indoor_lighting)
        # ashley_home.add_object(make_wall())
        # ashley_home.add_object(make_floor())
        # ashley_home.add_object(make_bed())
        # ashley_home.add_object(make_window())

        #ashley_home.link_locations_two_way(downtown)
        #list_of_places.append(ashley_home)

        # init ashley role
        ashley_role = Role(role_name ="Ashley", actions =[], hidden = True)

        #global ashley_role
        #TODO make most variables identical to Stephanie
        global ashley
        ashley = create_random_person(name = "Ashley", last_name =stephanie.last_name, age = 22, body_type = "standard_body", face_style = "Face_3",  tits="B", height = 0.92, hair_colour="brown", hair_style = ponytail, skin="white" , \
            eyes = "brown", personality = relaxed_personality, name_color = "#228b22", dial_color = "228b22" , starting_wardrobe = ashley_wardrobe, \
            stat_array = [1,4,4], skill_array = [1,1,3,5,1], sex_array = [4,2,2,2], start_sluttiness = 7, start_obedience = -18, start_happiness = 119, start_love = 0, \
            title = "Ashley", possessive_title = "Your intern", mc_title = mc.name, relationship = "Single", kids = 0)

        ashley.set_schedule([0,4], stephanie.home)
        ashley.set_schedule([1,2,3], stephanie.home)

        ashley.home = stephanie.home

        ashley.home.add_person(ashley)
        ashley.event_triggers_dict["epic_tits_progress"] = 0    # 0 = not started, 1 = mandatory event triggered, 2 = tits epic
        ashley.event_triggers_dict["drinks_out_progress"] = 0   # 0 = not started, 1 = third wheel event complete, 2 = grab drinks complete
        ashley.event_triggers_dict["dating_path"] = False       # False = not started, or doing FWB during story, True = dating her.
        ashley.event_triggers_dict["stripclub_progress"] = 0    # 0 = not complete, 1 = strip club even complete
        ashley.event_triggers_dict["initial_threesome_target"] = None    #this will hold who ashley decides she wants to have a threesome with.
        ashley.event_triggers_dict["threesome_unlock"] = False   #Set this to true after first threesome with ashley

        # add appoint
        #office.add_action(HR_director_appointment_action)

        ashley_intro = Action("ashley_intro",ashley_intro_requirement,"ashley_intro_label") #Set the trigger day for the next monday. Monday is day%7 == 0
        mc.business.mandatory_crises_list.append(ashley_intro) #Add the event here so that it pops when the requirements are met.

        ashley.opinions["production work"] = [2, True]  # she loves prod work
        ashley.opinions["work uniforms"] = [-1, False]  # uniforms stifle creativity
        ashley.opinions["flirting"] = [1, False]  # she likes attention, even if she is awkward
        ashley.opinions["working"] = [1, False]  # Her first real job
        ashley.opinions["the colour green"] = [2, False] #She loves green!
        ashley.opinions["pants"] = [1, False]  #And pants
        ashley.opinions["the colour blue"] = [-2, False] #She hates blue
        ashley.opinions["classical"] = [1, False]  #like calm, relaxing music.


        ashley.sexy_opinions["taking control"] = [2, False]  # she likes taking control, closet dom
        ashley.sexy_opinions["getting head"] = [2, False] # Loves to be serviced
        ashley.sexy_opinions["giving blowjobs"] = [-2, False]  # ultimate act of submission

        #TODO make her know Nora from before graduation. She is familiar with serums and their effects

        return

#Requirement Labels
init -1 python:
    def ashley_intro_requirement():   #After discovering an obedience serum trait and there is a position available. must be at work
        if day > 1: #Not the first week #TODO change this number later for balance, for now 1 for testing
            if sedatives_trait.researched or obedience_enhancer.researched or large_obedience_enhancer.researched: #Leave this to vanilla traits for now
                if mc.business.max_employee_count == mc.business.get_employee_count():
                    return False
                else:
                    if mc.is_at_work():
                        if mc.business.is_open_for_business():
                            return True
        return False                    #TODO Consider making this true only if recruiting increased via HR director? Would be much delayed intro

    def ashley_hire_directed_requirement(the_person):
        if the_person == stephanie:
            if ashley.event_triggers_dict.get("employed_since", 0) > 0:
                return False
            else:
                if mc.is_at_work():
                    if mc.business.max_employee_count == mc.business.get_employee_count():
                        return "You have too many employees"
                    else:
                        return True
                else:
                    return "Talk to her at work"
        return False


#Story labels
label ashley_intro_label():
    $ the_person = stephanie
    "You are deep in your work when a voice startles you from your concentration."
    the_person.char "Hey [the_person.mc_title]. Sorry to bug you, do you have a minute?"
    $ scene_manager = Scene()  #Clean Scene
    $ scene_manager.add_actor(the_person)
    mc.name "Of course. What can I do for you?"
    the_person.char "Well, I kind of need a favor."
    mc.name "Well, you've taken an awfully large risk coming to work for me here, so I supposed I owe you one."
    the_person.char "You see, it's my sister. She just graduated from college, but is having trouble finding work in her degree. She's had to move in with me because she can't find work!"
    the_person.char "She's is really smart, but very introverted, it's been hard for her to get through interviews."
    mc.name "What is her degree in?"
    the_person.char "Errrmm... well, it's in Art History. Look, I know this isn't going to be her final career, but even just putting something down as an internship would really help her get a career started."
    the_person.char "I brought her resume, will you atleast take a look at it? I think she would be great over in production."
    menu:
        "Take a look":
            pass
        "Not right now":
            mc.name "I'm sorry, I'm not hiring anyone like that right now. But if I change my mind I'll come find you, okay?"
            the_person.char "Of course, that's all I can ask, is that you will keep her in mind. Thanks!"
            call ashley_hire_later() from ashley_hire_later_1
            return
        "Blow me and I'll look" if the_person.sluttiness > 50:
            mc.name "I tell you what, why don't you come suck me off while I look over her documents."
            the_person.char "Oh! A favor for a favor then? Okay!"
            $ scene_manager.update_actor(the_person, position = "blowjob", emotion = "happy")
            "[the_person.possessive_title] gets on her knees and starts to undo your pants."
            the_person.char "You know I would do this anyway, right?"
            mc.name "Of course, but being reminded of your blowjob skills will probably help me make up my mind if I want to hire someone you are related too."
            call fuck_person(the_person, start_position = blowjob, skip_intro = False, position_locked = True) from _call_sex_description_ashley_intro_bonus_BJ_1
            $ the_report = _return
            $scene_manager.update_actor(the_person, position = "stand4")
            if the_report.get("guy orgasms", 0) > 0:
                mc.name "God your mouth is amazing. If your sister sucks anything like you this'll be a no brainer..."
                the_person.char "Hah! Well, to be honest, I don't think she really cares for giving blowjobs, but I guess you never know."
    "You pick up her documents and look over them."
    "From her skill set, it is obvious the best choice of department for here would be in production. The only question is, should you hire her or not?"
    call hire_select_process([ashley, 1]) from _call_hire_ashley_1
    if _return == ashley:
        mc.name "I agree. She would be perfect for the production department. Would you pass along that she can start tomorrow? Or anytime in the next week."
        $ the_person.change_happiness(5)
        $ the_person.change_obedience(5)
        the_person.char "Oh! I didn't think you would say yes. This is great news! I'm sure she'll probably want to get started right away!"
        $ ashley.event_triggers_dict["employed_since"] = day
        $ mc.business.listener_system.fire_event("new_hire", the_person = ashley)
        $ ashley.special_role.append(employee_role)
        python:
            for other_employee in mc.business.get_employee_list():
                if other_employee == stephanie:
                    town_relationships.update_relationship(ashley,the_person, "Sister")
                else:
                    town_relationships.begin_relationship(ashley, other_employee) #They are introduced to everyone at work, with a starting value of "Acquaintance"
            town_relationships.update_relationship(nora, ashley, "Friend")
            town_relationships.update_relationship(lily, ashley, "Rival")
            del other_employee
        "You complete the nessesary paperwork and hire [ashley.name], assigning her to the production department."
        $ mc.business.add_employee_production(ashley)
        $ ashley.set_work([1,2,3], mc.business.p_div)
        $ mc.business.p_div.add_person(ashley)
        #TODO make sure her home is set to Stephanie's house somehow.
        "As you finish up, you notice [the_person.possessive_title] is already calling her sister with the news."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        the_person.char "Hey Ash! Guess what? I got you a starting position at that place I've been..."
        "Her voice trails off as she leaves the room. You hope you made the right decision!"
    else:
        mc.name "I'm sorry, I don't think she is a good fit at this time. But I will keep her in mind for the future, okay?"
        the_person.char "Ahhh, okay. I understand, but please let me know ASAP if you change your mind!"
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "[the_person.possessive_title] gets up and leaves the room. Did you make the right decision? Oh well, if you change your mind, you can always talk to her again."
        call ashley_hire_later() from ashley_hire_later_2

    return

label ashley_hire_later():  #This label adds an action to staphnie's role that allows you to talk to her about hiring her sister.
    $ ashley_hire_directed = Action("Reconsider hiring her sister.", ashley_hire_directed_requirement, "ashley_hire_directed_label",
    menu_tooltip = "Talk to Stephanie about hiring her sister. She might be disappointed if you decide not to again...")
    $ head_researcher.add_action(ashley_hire_directed)

    return

label ashley_hire_directed_label(the_person):
    if the_person != stephanie:
        "Not steph? How did we get here?"
        return
    mc.name "I wanted to talk to you again about your sister."
    the_person.char "Oh? Have you decided to reconsider?"
    mc.name "I have. Do you still have her documents that I could look over them again?"
    the_person.char "Of course! Let me get them."
    "[the_person.possessive_title] runs over to her desk and comes back with a folder."
    the_person.char "Here you go!"
    "You pick up her documents and look over them."
    "From her skill set, it is obvious the best choice of department for here would be in production. The only question is, should you hire her or not?"
    call hire_select_process([ashley, 1]) from _call_hire_ashley_2
    if _return == ashley:
        mc.name "I agree. She would be perfect for the production department. Would you pass along that she can start tomorrow? Or anytime in the next week."
        $ the_person.change_happiness(5)
        $ the_person.change_obedience(5)
        the_person.char "Oh! This is great news! I'm sure she'll probably want to get started right away!"
        $ ashley.event_triggers_dict["employed_since"] = day
        $ mc.business.listener_system.fire_event("new_hire", the_person = ashley)
        $ ashley.special_role.append(employee_role)
        python:
            for other_employee in mc.business.get_employee_list():
                if other_employee == stephanie:
                    town_relationships.update_relationship(ashley,the_person, "Sister")
                else:
                    town_relationships.begin_relationship(new_person, other_employee) #They are introduced to everyone at work, with a starting value of "Acquaintance"
            town_relationships.update_relationship(nora, ashley, "Friend")
            town_relationships.update_relationship(lily, ashley, "Rival")
            del other_employee
        "You complete the nessesary paperwork and hire [ashley.name], assigning her to the production department."
        $ mc.business.add_employee_production(ashley)
        $ ashley.set_work([1,2,3], mc.business.p_div)
        $ mc.business.p_div.add_person(ashley)
        #TODO make sure her home is set to Stephanie's house somehow.
        "As you finish up and start to leave, you notice [the_person.possessive_title] is already calling her sister with the news."
        the_person.char "Hey Ash! Guess what? I got you a starting position at that place I've been..."
        "Her voice trails off as you leave the room. You hope you made the right decision!"
    else:
        mc.name "I'm sorry, I don't think she is a good fit at this time. But I will keep her in mind for the future, okay?"
        the_person.char "Wow, really? Why did you even talk to me about this?"
        $ the_person.change_happiness(-10)
        $ the_person.change_obedience(-10)
        $ the_person.change_love(-10)
        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title] gets up and leaves the room. You should probably avoid getting her hopes up again like this."

    return


label ashley_first_talk_label(the_person):
    mc.name "Hello there. You must be [the_person.name]. I'm [mc.name], the one who owns this place."
    "She looks at you, and see a hint of surprise on her face."
    the_person.char "Oh!... hello sir. It's nice to meet you. I'm sorry, my sister said this place was all women..."
    mc.name "That's right. Except me, the owner."
    the_person.char "Ah... I see... Well thank you for the opportuniy. I appreciate the work."
    mc.name "Of course, [stephanie.title] is a good friend. Do you go by [the_person.name]? Or something else?"
    the_person.char "[the_person.title] is fine..."
    mc.name "[the_person.title] it is then."
    "You chit chat with [the_person.title] for a minute, but she speaks in short, one or two word replies. She seems very reserved."
    "Maybe she is just shy? You decide to let her get back to work."
    return

label ashley_room_excitement_overhear_label(the_person):
    "As you step into the production room, you can overhear [the_person.title] talking excitedly to another coworker."
    the_person.char "I know! I can't wait to go. All of my friend's say that is so much fun..."
    "But as you enter the room, she notices, and immediately stops talking."
    the_person.char "..."
    "Clearly she has no issue talking to her coworkers... why is she so quiet with you? Maybe you should ask her sister about it."
    return

label ashley_ask_sister_about_attitude_label(the_person):
    "You approach [the_person.title], intent to ask her about her sister."
    mc.name "Hello [the_person.title]. Do you have a moment?"
    the_person.char "Of course sir. What can I do for you?"
    "You lower your voice. You don't necessarily need anyone overhearing you."
    mc.name "Well... I'm not sure how to say this but, I'm a little concerned about [ashley.title]."
    "A grimace forms on her face, but she waits for you to continue."
    mc.name "Earlier, I walked into production, and I could hear her carrying on with her coworkers. But as soon as I entered the room, she went completely silent."
    "[the_person.title] nods her head as you keep going."
    mc.name "She barely says a word anytime I talk to her. I feel like I've gotten off to a bad start with her. Do you have any advice?"
    "[the_person.title] clears her throat."
    the_person.char "Well... [ashley.title] is a bit complicated. She has trouble talking to, and being around men in general..."
    mc.name "Oh? Oh! I see, I mean I guess that makes sense, not everyone is heterosexual..."
    the_person.char "Noooo, no. It isn't that. She's had boyfriends in the past. But something happened between her and her last boyfriend in college."
    the_person.char "I'm not sure what happened, but they broke up all of a sudden, and she's never been the same way around men since then."
    mc.name "Hmm, that sounds like something bad might have happened."
    the_person.char "That's what I think as well, but so far atleast, she hasn't opened up to anyone about it."
    "[the_person.title] shakes her head, lost in thought."
    the_person.char "If you find out something, I guess let me know. I've suggested therapy, but so far she hasn't seemed interested."
    mc.name "Thank you for the insight. I appreciate it."
    the_person.char "Of course."

    return

label ashley_room_warming_up_label(the_person):
    "As you step into the production room, you can overhear [the_person.title] talking excitedly to another coworker."
    the_person.char "I know, the city symphony is performing a collection of Johannes Brahm's symphonies. I want to go so bad but I can't find anyone to go with..."
    "As you enter the room, she looks and stops talking."
    the_person.char "Ahh... hello sir. Having a good day?"
    "Whoa. She actually said hi to you? Maybe she is warming up to you a little bit?"
    mc.name "It's been great so far. And you?"
    the_person.char "Oh... its been good I guess..."
    mc.name "Glad to hear it."
    "Hmm... she is looking for someone to go with her to a classical music concert. Maybe that person could be you?"

    return

label ashley_ask_date_classic_concert_label(the_person):
    mc.name "So... I couldn't help hearing earlier, you are looking to go to the Brahm Symphony recital, but you don't have anyone to go with?"
    the_person.char "Ummm yeah, something like that..."
    "She is looking down, avoiding eye contact with you."
    mc.name "That sounds like a great cultural event. I was wondering if you would be willing to let me take you?"
    "She is caught off gaurd. She wasn't expecting you to ask something like this!"
    the_person.char "Oh! I uhh, I'm not sure..."
    if stephanie.love > 30 or stephanie.obedience > 130:
        the_person.char "I suppose... I mean... Steph keeps telling me you are a nice guy..."
    else:
        the_person.char "I don't know, I mean you seem like a nice guy but..."
        mc.name "I'll tell you what. We could let [stephanie.title] know when it is. She could drop you off and pick you up afterwards."
        "[the_person.title] mumbles something for a second, then relents."
        the_person.char "I suppose... I mean... Steph keeps telling me I need to go out more."
    mc.name "Ah, great! Do you know when the concert is?"
    the_person.char "It's on Thursday night."
    mc.name "Ok. I'll plan to meet you there on Thursday night then?"
    the_person.char "Sure! I'll plan on it."
    "You feel good about this as you finish up your conversation. Maybe you can finally get her to come out of her shell a little..."
    return

label ashley_classical_concert_date_label():
    #TODO move downtown.
    $ the_person = ashley
    "It's thursday. "
    return

label ashley_porn_video_discover_label():
    $ the_person = ashley
    $ scene_manager = Scene()
    "It's been a long day. You consider heade for bed, but you've got a lot of energy, you aren't sure you would be able to fall asleep."
    "You decide to hop on your PC and watch some porn and jack off before you go to bed. That always helps you fall asleep."
    "You load up your porn accounts and start browsing thorugh some videos."
    "'Desparate Slut Begs for Creampie'? Nah! 'Guy Fucks Step Sister Stuck In Bear Trap'? hmm... maybe later."
    "As you browse, you notice a clip thumbnail with a girl on her knees. She looks kinda familiar? Reminds you of someone from work maybe?"
    "'College Co-Ed Forced Deepthroat On Camera'? EH, it's worth a shot anyway. You click on it and wait for the generic porn intro to finish."
    "You mouth falls open when the seen starts."
    $ scene_manager.add_actor (the_person, position = "blowjob", emotion = "sad")
    "On her knees, with her hands cuffed behind her back, is [the_person.title]. She doesn't look like she wants to be there, either..."
    "The guy enters the frame, with his back to the camera. You watch, horrified as [the_person.title] looks up at him."
    the_person.char "Look... you don't have to do this. I'll blow you, I promise! Just please turn off the camera!..."
    "?????" "It's too late for that. You promised me a memorable evening, but it looks like its up to me to make it memorable."
    "He grabs her by the hair and brings her face to his cock. She submissively opens her mouth, but the guy grabs her hair with both hands and starts to fuck her face."
    "Normally, you would assume a video like this was just acted out, but knowing [the_person.title] form work, you are absolutely certain this is a real act of rape."
    "You are totally disgusted, but you continue watching. Not because it's arousing you, but you want to understand exactly what [the_person.title] went through."
    "As the video is nearing the end, the guy grabs her head with both hands cums straight down her throat. She is gagging and coughing."
    "As the guy steps away from her and picks up the camera, you can hear the sound of crying in the background."
    $ scene_manager.clear_scene()
    "MOTHER FUCKER. You can't believe this guy took advantage of [the_person.title] like that. It makes your blood boil."
    "You turn off your PC, and spend the rest of the night contemplating how you smash this guy's face in if you ever met him."
    "You aren't sure what to do though. Should you try and talk to [the_person.title] about it? That seems like a bad idea. You decide to think about it for a few days."

    return

label ashley_porn_video_update_label():
    "It's been a few days since you found out that [ashley.title] starred, unwillingly, in a porn video."
    "It has been a turmoil of emotions for you, discovering your good friend was used like that. But realistically, what can you do about it?"
    "You've decided. There's no way you can talk to [ashley.title] about it. Not yet anyway."
    "But... you could always talk to her sister, [stephanie.title]. She might have some ideas on what to do, or even how to track down this guy."

    return

label ashley_ask_sister_about_porn_video_label(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    mc.name "Hello [the_perosn.title]. I need to talk to you about something... sensitive. Could you please come with me to my office?"
    the_person.char "Of course."
    #TODO change background to office
    "You enter your office an gesture for her to sit down."
    $ the_person.update_actor(the_person, position = "sitting")
    if the_person.sluttiness > 50:
        "As she sits down, you notice [the_person.possessive_title]'s posture. She is sticking her chest out. She probably thinks you brought her to your office for some... personal time."
    mc.name "I wanted to talk to you again, about your sister, [ashley.title]."
    the_person.char "Oh!... right..."
    if the_person.sluttiness > 50:
        "Her back slumps noticably when you say that."
    mc.name "This is not going to be an easy, or pleasant conversation, but uhh, I found a video of your sister, being forced to engage in sexual acts against her will..."
    the_person.char "What!?!"
    mc.name "I know! But I think this might explain some things."
    $ the_person.update_actor (the_person, emotion = "sad")
    the_person.char "Oh my god... that is awful. I mean... I suspected but I didn't know..."
    the_person.char "Do you... do you have it?"
    mc.name "The video?"
    the_person.char "Yeah."
    mc.name "I do, but I have to warn you, it is very hard to watch."
    the_person.char "I know. But, she's my sister. I want to know what she went through."
    $ the_person.update_actor (the_person, emotion = "angry")
    "You pull up the video. She watches it, the anger clear on her face. Soon the video finishes."
    the_person.char "Oh my god, no wonder. That asshole! I can't believe he did that!"
    mc.name "You wouldn't happen to know who it is, do you?"
    "She considers for a moment."
    the_person.char "No... I don't. I mean, Ash was off at college, we didn't stay as close as we probably should have. I know she dated several guys, but I never really met any of them..."
    mc.name "Ah. Okay."
    $ the_person.update_actor (the_person, emotion = "sad")
    "You both look at each other for a moment, considering the circumstance."
    mc.name "I want to do something, but I don't know what."
    if the_person.love > 30:
        the_person.char "I don't know either... I guess just... keep being you?"
        the_person.char "You are a wonderful guy. Just be there for her, okay? You are like the only guy she interacts with anymore."
    else:
        the_person.char "I mean, you are like, the only guy she interacts with... at all. She has completely cut herself off from men."
        the_person.char "Maybe you could try like, you know, being there for her? Help her learn that not all men are total assholes?"
    mc.name "I suppose. Do you think, while I focus on her, you could do a little investigating? See if you can figure out who this guy is?"
    the_person.char "I don't know... I suppose. I don't even know where to begin though."
    "After a few solemn moments, you decide to move on with your day."
    mc.name "That's enough for now I suppose. Let me know if you find anything."
    the_person.char "Yes sir... and the same for you."

    return