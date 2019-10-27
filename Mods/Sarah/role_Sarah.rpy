# ****Sarah profile****
# Personality type: Outgoing, extrovert.
# Background: Childhood friend. Moved away when you were kids but recently moved back to pursue a job that didn't work out. Now selling solar panels door to door, knocks on your door randomly.
#   Has a great HR resume.
#   After first chance meeting, unlocks the HR Supervisor organization policy that unlocks the role and increases maximum company size by 1.
#   After unlocking the policy, the player calls Sarah and hires her.
#   First level corruption:
#   Second level corruption: You catch her stealing breast enhancing serums. Option to forbid her, allow her, or encourage her.
#
#
# Required labels:
# INTRO
# Hire
# Story arc part one: She catches you in the office on Saturday, invites you to bar where she is meeting a friend. Close the bar down with her
# Story arc part two: She comes looking for you at the office on Saturday. Invites you out to drinks with jut her. She winds up at your place.
# Story arc part three: Catch her swiping breast enhancement serums on friday  NOTE: Part three has separate requirements from one and two and could happen before or after either part.
# Following monday, observe the results
# Story part four: Help her seduce another employee
#
# Intro: mandatory event, in the AM knocks on MC home selling solar panels.
# Hiring: mandatory event. Call up Sarah and hire her for the HR position.

init 2 python:

    #Sarah ACTIONS




    def Sarah_mod_initialization(): #Add actionmod as argument#

        Sarah_wardrobe = wardrobe_from_xml("Sarah_Wardrobe")

        Sarah_home = Room("Sarah's home", "Sarah's home", [], apartment_background, [],[],[],False,[0.5,0.5], visible = False, hide_in_known_house_map = False, lighting_conditions = standard_indoor_lighting)
        Sarah_home.add_object(make_wall())
        Sarah_home.add_object(make_floor())
        Sarah_home.add_object(make_bed())
        Sarah_home.add_object(make_window())

        #Sarah_home.link_locations_two_way(downtown)
        list_of_places.append(Sarah_home)

        # init Sarah role
        Sarah_role = Role(role_name ="Childhood Friend", actions =[])

        #global Sarah_role
        global sarah
        sarah = create_random_person(name = "Sarah", last_name ="Cooper", age = 21, body_type = "thin_body", face_style = "Face_3", tits = "A", height = 0.90, hair_colour = "brown", hair_style = short_hair, skin="white",\
            eyes = "dark blue", personality = Sarah_personality, name_color = "#9400D3", dial_color = "#9400D3", starting_wardrobe = None, \
            stat_array = [4,3,3], skill_array = [5,3,2,1,1], sex_array = [1,2,3,1], start_sluttiness = 3, start_obedience = 0, start_happiness = 102, start_love = 3, \
            title = "Sarah", possessive_title = "Your childhood friend",mc_title = mc.name, relationship = "Single", kids = 0)

        sarah.set_schedule([0,4], Sarah_home)
        sarah.set_schedule([1,2,3], mall)

        sarah.home = Sarah_home

        sarah.home.add_person(sarah)
        sarah.event_triggers_dict["epic_tits_progress"] = 0    # 0 = not started, 1 = mandatory event triggered, 2 = tits epic
        sarah.event_triggers_dict["drinks_out_progress"] = 0   # 0 = not started, 1 = third wheel event complete, 2 = grab drinks complete


        Sarah_intro = Action("Sarah_intro",Sarah_intro_requirement,"Sarah_intro_label") #Set the trigger day for the next monday. Monday is day%7 == 0
        mc.business.mandatory_crises_list.append(Sarah_intro) #Add the event here so that it pops when the requirements are met.
        return


init -1 python:
    def Sarah_intro_requirement():
        if day > 2: #Early for testing
            if mc_at_home():
                if time_of_day < 4:
                    return True
        return False

    def Sarah_hire_requirement():
        if HR_director_creation_policy.is_owned():
            return True
        return False

    def Sarah_catch_stealing_requirement():
        if time_of_day == 3:
            if day%7 == 4:  #friday
                if mc.is_at_work():
                    return True
        return False

    def Sarah_new_tits_requirement():
        if time_of_day == 1:
            if day%7 == 0:  #Monday
                return True
        return False

    def Sarah_epic_tits_requirement():
        if time_of_day == 1:
            if day%7 == 0:  #Monday
                return True
        return False

    def Sarah_third_wheel_requirement():
        if sarah.event_triggers_dict.get("epic_tits_progress", 0) == 1: #Don't run this if epic tits is in progress
            return False
        if time_of_day > 1:
            if sarah.sluttiness > 15:
                if day%7 == 5:  #Saturday
                    if mc.is_at_work():
                        return True
        return False

    def Sarah_get_drinks_requirement():
        return False            #This event is currently disabled until i finish writing it.
        if sarah.event_triggers_dict.get("epic_tits_progress", 0) == 1: #Don't run this if epic tits is in progress
            return False
        if time_of_day > 1:
            if sarah.sluttiness > 30:
                if day%7 == 5:  #Saturday
                    if mc.is_at_work():
                        return True
        return False

    def Sarah_remove_bra_from_wardrobe(wardrobe):  #Test this function
        for outfit in wardrobe.outfits:
            if outfit.wearing_bra():
                outfit.remove_clothing(outfit.get_bra())
        for outfit in wardrobe.underwear_sets:
            if outfit.wearing_bra():
                outfit.remove_clothing(outfit.get_bra())

    def test_bra_function(the_person):
        Sarah_remove_bra_from_wardrobe(the_person.wardrobe)


label Sarah_intro_label():
    $ the_person = sarah
    "*DING DONG*"
    "You hear the doorbell ring. You don't remember expecting anyone? You go and answer it."
    $ the_person.draw_person()
    "Standing at your door is a cute brunette, fairly short, and strikingly familiar..."
    "She appears to be holding some kind of clipboard. A door to door saleswoman? Do those still exist?"
    the_person.char "Hello sir, I am [the_person.title], with Metropolis Power and Light, I was just wondering if you had ever thought about installing solar panels..."
    "She begins talking about the benefits and tax credits associated with solar panels, but you have a hard time listening."
    "This girl... she look so familiar! Where do you know her from!?!"
    the_person.char "...with even 50%% coverage of the roof you can expect a considerable reduction in your electric bill..."
    "What did she say her name was again? [the_person.title]? Suddenly you get a flash of a memory from a long time again. You quickly interrupt her."
    mc.name "I'm sorry, you said your name was [the_person.title]? Is your name [the_person.title] [the_person.last_name]?"
    "She immediately stops her sales pitch."
    the_person.char "That's right... do... do I know your from somewhere?"
    "Faint memories come flooding back to you. When you were growing up, your dad and his best friend got married around the same time and had kids!"
    "You used to spend a lot of time with your dad and his friend, and his friend's daughter, who was just a few years younger than you!"
    "You aren't sure what happened, but one day the other family moved away, to another city, and you never saw them again."
    mc.name "Your dad, he was friends with my dad! I remember when our dad's used to hang out, we spent a lot of time together!"
    "She looks shocked, but you can see she is also starting to remember..."
    the_person.char "Wait, I think I remember... Mr. [mc.last_name]? So you must be... is it really [mc.name]???"
    "You quickly nod!"
    $ the_person.draw_person(emotion = "happy")
    the_person.char "Oh my god! I don't believe it! You and your dad used to come over every week! And even though I was a few years younger than you, you would be so nice to me!"
    "You don't really remember going out of your way to be nice, but it was also a long time ago."
    $ the_person.draw_person(position = "kissing")
    "Without warning, [the_person.name] throw herself at you and gives you a big hug."
    the_person.char "I never would have thought in a million years I would run into you again!"
    $ the_person.draw_person(position = "stand2", emotion = "happy")
    mc.name "Dad told me your family had to move away from work. What brings you back to town?"
    $ the_person.draw_person(position = "stand2", emotion = "sad")
    the_person.char "Ahh... well, I had just finished my degree and landed an internship at a company in town here. It was a great company, or so I thought..."
    "She clears her throat and continues."
    the_person.char "The director there told me if the internship went well it could become a full time position. I worked my ASS off at that place, for 6 months! And I was bartending in the evenings to make ends meet..."
    the_person.char "... well, when my six months was up, he said, sorry, that wasn't good enough. We are terminating you."
    $ the_person.draw_person(position = "stand2", emotion = "angry")
    the_person.char "I found out later, they hired some dumb bimbo for my position. I made some friends at the company, they are pretty sure the director is banging her in the office every day!"
    $ the_person.draw_person(position = "stand2", emotion = "sad")
    "[the_person.possessive_title] looks down at the ground. It looks like she is about to cry."
    mc.name "That really sucks. I'm sorry to hear that. What were you interning for, anyway?"
    $ the_person.draw_person(position = "stand3")
    "The change of topic helps her keep her composure."
    the_person.char "Well, I just finished up my degree in Sociology, and I was interning for a Human Resources position..."
    "Human Resources? That might actually be fairly useful."
    the_person.char "... I was really hoping to eventually move up to HR director there. I love working with other people, and the small business atmosphere was great!"
    "HR director? You've never heard of such a position."
    mc.name "So, what kind of work would you do as an HR director that is different from a regular HR position?"
    the_person.char "Well, I would be in charge of the direction of the company in general, as far as work values, help with company morale..."
    "She goes on to list multiple duties, aspects of running a small business that you had honestly never considered before."
    "When she finishes, you consider things for a moment. It would be REALLY handy to have someone around like this. She already has some work experience, and is young and ready to prove herself."
    "But, before you hire her, you would need to set up the HR director position at the company. Alternatively, you could still setup the new position, but hire someone else to fill the position."
    menu:
        "Offer to hire her":
            mc.name "So, as it turns out, I just recently started a new business making small run pharmaceuticals. You seem pretty knowledgeable, would you consider running the HR department?"
            "[the_person.title] is caught completely off guard by your offer."
            the_person.char "Wait, so, you run a small business? I mean, I would love to, but I can't afford to do another unpaid internship right now."
            mc.name "I didn't say it was unpaid, this would definitely be a paid position."
            $ the_person.draw_person(position = "stand3", emotion = "happy")
            $ the_person.change_happiness(5)
            $ the_person.change_love(5)
            the_person.char "That would be... incredible! I don't know what to say! I can't wait to get started!"
            mc.name "I'll have to get your phone number. I'll need to set up the position before I can officially hire you, and that might take a few days."
            the_person.char "Oh! Of course, here..."
            "You quickly exchange phone numbers with [the_person.title]."
            mc.name "I'll be in touch with you soon I think."
            the_person.char "This is great, [the_person.mc_title], you won't regret this, I promise!"
            "You say goodbye to her, and she goes to keep selling solar panels until you get back to her after creating the HR director position."
            "In order to hire [the_person.title], you will need to create a new HR Director position via the policy menu."
            $ Sarah_hire = Action("Sarah hire",Sarah_hire_requirement,"Sarah_hire_label")
            $ mc.business.mandatory_crises_list.append(Sarah_hire) #Add the event here so that it pops when the requirements are met.
        "Don't offer to hire her":
            "You decide maybe down the line you could make a new HR director position, but you decide the [the_person.title] is probably not the best fit for it."
            mc.name "I'm sorry it didn't work out, I hope you are able to find something in your field."
            the_person.char "Thanks... well, it was good seeing you. I'd better keep at it."
            "You say goodbye to [the_person.title]. If you want to hire an HR director, you will need to create the position via the policy menu."
            #TODO figure out a way to delete sarah and remove her from the game.


    if HR_director_creation_policy not in organisation_policies_list:       #Hopefully by testint to see if it is already there we can avoid any issues in the future with mod compatability.... *shrug*
        $ organisation_policies_list.append(HR_director_creation_policy)

    return

label Sarah_hire_label():
    $ the_person = sarah
    "After creating the new HR Director position, you call up [the_person.title]. She answers and says hello."
    mc.name "Hey, I just wanted to let you know, I have the details finalized for an HR Director position."
    the_person.char "That sounds great! When can I get started?"
    mc.name "Tomorrow morning. I'll text the address after this call. We will go over your role and responsibilities when you get there."
    the_person.char "Yes! I'm so glad to finally be done selling solar panels. I'll see you in the morning!"
    "You hang up the phone. You quickly text [the_person.title] the address of your business."
    #TODO Hire Sarah officially here?
    $ HR_director_initial_hire = Action("Hire HR Director",HR_director_initial_hire_requirement,"HR_director_initial_hire_label", args = the_person) #Set the trigger day for the next monday. Monday is day%7 == 0
    $ mc.business.mandatory_crises_list.append(HR_director_initial_hire) #Add the event here so that it pops when the requirements are met.

    return

label Sarah_third_wheel_label():
    $ the_person = sarah
    #TODO going out outfit
    "By yourself on the weekend at work, you get up for a minute and decide to stretch your legs and walk the hallways for a bit."
    "As you pass by the HR offices, you notice the HR Director's office door is open and the light is on. You decide to investigate."
    $ scene_manager.add_actor(the_person, position = "sitting")
    "You see [the_person.possessive_title] sitting at her desk, rummaging through her drawers looking for something."
    "She notices you step in her door and looks surprised."
    the_person.char "Oh! Hey [the_person.mc_title]. I was just looking for something I left in my desk. What are you doing here? Isn't this place closed down for the weekend?"
    mc.name "Yeah, well, I had a few things I wanted to get done over the weekend. Is it something I can help you find?"
    the_person.char "I actually just found it! One second..."
    "You see her pull a small, silver package out of her desk and shove it in her bag quickly... was that a condom?"
    the_person.char "...sorry I just... you know, like to be prepared. You never know!"
    mc.name "You look nice, you have a date tonight?"
    "[the_person.title] blushes and looks down at her desk."
    the_person.char "Errrmm... not really. I'm meeting a friend at the bar for a few drinks. I thought it was just going to be me and her, but she just texted me she is bringing her boyfriend."
    mc.name "Ah... your friend... is she like, your wing-woman or something? Helping you pick up guys at the bar?"
    the_person.char "Well, not exactly. I don't really want to talk about it right now."
    "She glances up and looks at you for a moment. Suddenly you realize she is checking you out."
    the_person.char "Say, what are you up to tonight, [the_person.mc_title]?"
    mc.name "Well, I was gonna get a few more things done around here. But to be honest, I wouldn't be against grabbing a few drinks with an old friend, if that were to be suggested."
    $ scene_manager.update_actor(the_person, emotion = "happy")
    the_person.char "Aww, you wouldn't mind coming along? I hate being the third wheel. If you get bored you can leave at any time, I promise!"
    mc.name "Nonsense, let me just wrap up what I was doing, lockup and we'll go."
    "You head downtown with [the_person.char]. You decide to walk since it isn't very far, and enjoy talking with her as you go."

    $ mc.change_location(downtown)
    $ mc.location.show_background()

    $ scene_manager.update_actor(the_person, position = "stand2")
    "Getting curious, you decide to ask her why she needed the condom at the office."
    mc.name "So... when I first stepped into your office you were looking for something in your desk... was that a condom?"
    "[the_person.title] doesn't stop walking, but you can see her get a little tense."
    the_person.char "Yeah, it was."
    mc.name "So, why did you need to come back and grab that?"
    the_person.char "Well my friend has been dating this guy for a while and keeps complaining, he wants them to open up their relationship some, maybe bring a lucky guy or girl back to their place sometime..."
    the_person.char "I've been out with them a couple of times now, hoping maybe they would show interest in me, but so far nothing."
    if sarah.event_triggers_dict.get("epic_tits_progress", 0) < 2:
        the_person.char "Her boyfriend... it's like he just looks right through me. I've seen them leave the bar with a girl before, and its always some dumb looking, busty girl."
        mc.name "Don't be silly, you are so sexy. There is more to look for in a woman than chest size."
        "She laughs at you sarcastically."
        the_person.char "Ha! Very funny. No, I'm afraid the guys I meet tend to friend zone me pretty quick. The flat chested third wheel! I suspect that is how things will go tonight."
    else:
        the_person.char "I though that, you know, after taking those serums that her boyfriend might actually notice me now."
        the_person.char "Really though, I'm about ready to move on. They still think of me as that flat chested third wheel I used to be!"
    "[the_person.title] considers things for a bit."
    the_person.char "However tonight goes... its pretty amazing you are willing to come out here with me like this."
    mc.name "Of course, I can't remember the last time I said no to drinks with a single lady as beautiful as you."
    the_person.char "There you go again! You know, it was a long time ago that we grew up together. But I still have so many fond memories of you. You always used to be so nice to me."
    the_person.char "I remember one time, we were playing in the living room at my house, and suddenly a bug landed on my head. I started screaming! I was so scared."
    $ scene_manager.update_actor(the_person, position = "stand4", emotion = "happy")
    "She stops walking for a moment and turns to you, a serious, but happy look on her face."
    the_person.char "Suddenly, you grabbed me. HOLD STILL! you yelled, and you knocked the bug off me and on the floor and stomped on it."
    the_person.char "When my family moved away and the memories got old... I kept telling myself, we were just kids. He was sweet because we were just kids."
    the_person.char "But meeting you again, now that we are adults... and getting to know you all over again. You are still that sweet boy."
    the_person.char "You didn't even think twice about it tonight, when I asked you to go. That means a lot to me, you know?"
    $ scene_manager.update_actor(the_person, position = "stand2")
    "[the_person.possessive_title] turns and continues walking. You walk beside her the rest of the way to the bar in silence."

    #TODO change background to bar.
    $ mc.change_location(downtown_bar)
    $ mc.location.show_background()

    $ sarah_friend = create_random_person() #TODO figure out how to properly delete this character later
    $ sarah_friend.title = sarah_friend.name
    $ sarah_friend.mc_title = mc.name
    "When you get to the bar, [the_person.title] quickly spots her friend and leads you over to the table."
    $ scene_manager.update_actor(the_person, position = "sitting")
    $ scene_manager.add_actor(sarah_friend, position = "sitting", character_placement = character_left_flipped)
    the_person.char "Hey [sarah_friend.title]! Good to see you."
    sarah_friend.char "Hey girl! Is he with you?"
    "She nods towards you."
    the_person.char "Yup! This is my bo... I mean, an old friend of mine. [mc.name] this is [sarah_friend.title]!"
    "You make acquaintance and sit down. [sarah_friend.title] also introduces you to her boyfriend."
    "You chat for a bit, but notice that [sarah_friend.title] keeps checking you out. Normally you would be testing the waters with her, but with [the_person.title] here, you are a little leary."
    mc.name "Hey, how about I get us a couple drinks, [the_person.title]?"
    the_person.char "Oh! That sounds great! Can you get me an appletini?"
    "As you start to get up, [sarah_friend.title]'s boyfriend also excuses himself to the restroom, leaving the girls alone."
    "It takes a few minutes to get the attention of the bartender. You order the drink for [the_person.title] and get yourself a nice bourbon, straight."
    $ scene_manager.update_actor(the_person, position = "sitting", emotion = "sad")
    "When you come back to the table, you notice that [the_person.possessive_title] is looking down at the table and looks upset about something."
    mc.name "Hey! Here's your drink... are you okay?"
    the_person.char "Yeah... yeah I'm fine I just umm, I need to go use the lady's room."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "She gets up in a hurry and walks quickly away. You look at [sarah_friend.title]"
    $ scene_manager.remove_actor(the_person, reset_actor = False)
    mc.name "Umm... any idea what that is about?"
    sarah_friend.char "No idea... we were just talking about, well you actually."
    "Something about the way she says it makes you uncomfortable."
    sarah_friend.char "[the_person.name] says you are a great guy, a good friend of hers."
    mc.name "Yeah, something like that I guess..."
    sarah_friend.char "What do you say we get out of here? Like back to my place?"
    mc.name "That sounds pretty good actually. [the_person.name] will be excited to hear that I think."
    sarah_friend.char "Ha! No no, I mean, just you. [the_person.name] is a good friend but..."
    mc.name "but?"
    if sarah.event_triggers_dict.get("epic_tits_progress", 0) < 2:
        sarah_friend.char "My boyfriend... he just isn't attracted to her. I mean, have you seen her chest? Like, neither have we!"
        "You feel yourself getting angry at her crude remarks."
    elif sarah.event_triggers_dict.get("epic_tits_progress", 0) == 2:
        sarah_friend.char "My boyfriend can't stop staring at her tits. It's pissing me off! I can't believe she got implants, she is such a whore."
        "You feel yourself getting angry at her crude remarks."
    else:
        sarah_friend.char "Like, one day she's got nothing, next thing I know, her tits are fucking huge!?! She's such a bimbo."
        "You feel yourself getting angry at her crude remarks."
    "You are able to restrain yourself, but only just barely."
    mc.name "[the_person.name] has an amazing body, and a great personality to go with it. If you and your boyfriend don't see that, I don't think anything with me can work out."
    sarah_friend.char "Pfft, whatever. There's a dozen other dicks at the bar. Why don't you go find your date, she's probably sulking in the bathroom again!"
    "You decide not to stoop to her level and to end your conversation there. You grab you and [the_person.title]'s drink and get up, not bothering to say goodbye."
    $ scene_manager.remove_actor(sarah_friend, reset_actor = False)
    "You walk over to where the restrooms are and wait for [the_person.title]. You stand there for several minutes but start to get worried about her."
    "You don't seen anyone come in or out of the women's restroom so you decide to risk it. You walk to the door and slowly open it."
    $ scene_manager.add_actor(the_person, position = "stand2", emotion = "sad")
    "Inside you see [the_person.title] looking at herself in the mirror. She is forlorn and from the look of her makeup has obviously been crying."
    mc.name "Hey, are you okay? I don't mean to invade your privacy, but I was starting to get worried about you."
    "She quickly looks up and is surprised to see you. She briefly pulls herself together."
    the_person.char "Is that [the_person.mc_title]? You're still here? I thought you would be gone by now..."
    mc.name "What are you talking about?"
    the_person.char "Well, [sarah_friend.title] said... she was asking me about you, asked if we were involved, and when I said no said she was going to make a pass at you tonight..."
    the_person.char "I just assumed, when I left the table that, I mean, why didn't you go with her?"
    "She assumed when her friend made a pass at you that you would bail on her! You quickly reassure her."
    mc.name "[the_person.title]. I came here to support you, and to spend time with my long lost friend having fun and having a few drinks."
    mc.name "If you think I'm going to miss out on that for a silly one night stand, you are mistaken."
    $ scene_manager.update_actor(the_person, position = "stand2", emotion = "happy")
    the_person.char "I'm sorry! I didn't mean that I think you're shallow or anything I just... Look, give me one more minute and I'll be right out, okay?"
    mc.name "Sounds good!"
    "You step out of he lady's room and shortly after [the_person.title] steps out and joins you. You hand her the appletini."
    the_person.char "Thanks for waiting! I'm so sorry, I honestly thought you were going to go with them."
    the_person.char "Thank you for... I mean, everything you've done for me. You gave me a job, you let me drag you out to a bar with strangers, and then stuck with me even when you probably shouldn't have..."
    mc.name "You're crazy. It's not everday a long last childhood friend literally knocks on your front door."
    the_person.char "You've always been amazing to me. I should have known better."
    $ the_person.change_happiness(20)
    $ the_person.change_obedience(10)
    $ the_person.change_love(10)
    "She takes a long sip of her drink. You begin to chat and catch up a bit."
    $ scene_manager.update_actor(the_person, position = "sitting")
    "You spend several hours with [the_person.title] sitting in a secluded booth catching up. After multiple appletinis and whiskeys, you are both feeling pretty good."
    the_person.char "Well, I suppose it is getting pretty late. You have no idea how great this was. I don't want to say goodbye yet..."
    "[the_person.title] thinks for a moment."
    the_person.char "Hey... do you want to walk me home?"
    mc.name "That sounds like a perfect way to end the evening. Let's go."

    $ mc.change_location(downtown)
    $ mc.location.show_background()

    $ scene_manager.update_actor(the_person, position = "stand3")
    "You walk together with [the_person.title] through the streets as she slowly leads the way. You converse a bit, but things are mostly quiet as you walk."
    "Soon you are standing in front of the door to her apartment building."
    the_person.char "Thanks for today! It really means a lot to me that you spend the whole evening with me."
    mc.name "Consider it making up for lost time."
    "[the_person.possessive_title] blushes and looks down."
    mc.name "Goodnight."
    "You step close and put your arms around her."
    $ scene_manager.update_actor(the_person, position = "kissing")
    "She quickly wraps her arms around you and embraces you. You move your head to kiss her on the cheek, but at the last second she moves her head and you find your lips pressing into hers."
    the_person.char "Ohhh! Mmmmm..."
    "At first she opens her eyes in surprise, but quickly closes them and begins to kiss you back."
    "Her lips part and your tongue quickly takes advantage and begins to explore her soft lips. They taste sweet, with just a hint of appletini."
    "You stand there in front of [the_person.title]'s building, holding each other and making out for several seconds until the kiss stops and you step back. Her eyes are still closed."
    mc.name "I'll see you on Monday?"
    $ scene_manager.update_actor(the_person, position = "stand4")
    "She suddenly snaps back to reality. Her cheeks are flushed."
    the_person.char "Right! Yes of course. Goodnight!"
    $ time_of_day = 3
    "She turns and heads into her building. You check your watch and realize how late it is."
    $ scene_manager.remove_actor(the_person, reset_actor = False)
    $ del sarah_friend #Cleanup?




    return

label Sarah_get_drinks_label():
    $ the_person = sarah
    #TODO going out outfit
    "Lost in thought as you get your work done in the silence of the weekend, a sudden voice startles you."
    the_person.char "[the_person.mc_title]! I figured I'd find you around here on a Saturday again!"
    "You look up to see the now familiar face of [the_person.title] standing in the doorway."
    $ scene_manager.add_actor(the_person, emotion = "happy")
    "It is crazy to think that just a short time ago, she was out of your life completely, but after you chance encounter, you feel like you have been friends forever."
    mc.name "Hey [the_person.title]. You look great! Are you going out tonight?"
    the_person.char "Actually, I'm not sure yet. I hope so! But I'm not sure if the guy I want to go out with is going to be able to go yet or not..."
    mc.name "Is that so? I hope he can make it and that he treats you well!"
    the_person.char "Hahaha, yeah me too. And don't worry, he's always treated me right."
    "[the_person.possessive_title] looks down at the floor for a minute and mumbles something. Its obvious she is trying to work up the courage to ask you out, but it is cute watching her fumble a bit."
    the_person.char "So... you uhh, have any big plans for the evening, [the_person.mc_title]?"
    mc.name "Oh, well, certainly nothing as big as what you have planned! I'm just trying to get a little a head of work for next week."
    the_person.char "Ah! That's good. It is pretty amazing how much work you put into this place. It's something I admire a lot..."
    the_person.char "Anyway, I've seen how hard you work and I was thinking that, maybe we could go out and get a few drinks?"
    "You decide to tease her a bit."
    mc.name "Ahh, I see. You meeting another friend tonight? I'm not sure I want..."
    "She quickly interrupts you."
    the_person.char "No! God no, that was awful. I thought we could just go out, you know? Me and you?"
    mc.name "You mean like a date?"
    "She stutters a moment before she replies."
    the_person.char "Well, ermm, I mean, uhh..."
    the_person.char "Yeah. Pretty much that is exactly what I'm trying to ask..."
    "You admire her courage. She must be really interested in you to have the guts to ask you out like this! If you accept, she might assume you are interested in a relationship..."
    menu:
        "Sounds great!": #Begin the dating path with Sarah
            pass
        "Just as friends.\n (Coming Later) (disabled)":
            pass
            #TODO when Vren release boyfriend girlfriend relations, evaluate this option to eventually shift to a FWB scenario over dating.
    mc.name "I'm actually at a great stopping point. Let's go!"
    the_person.char "Great! Do you want to walk again tonight? It was kind of nice when we walked together last time."
    mc.name "Sounds good to me, it's good to get out and stretch the legs once in a while."
    "You lock up on your way out and head toward downtown."

    $ mc.change_location(downtown)
    $ mc.location.show_background()

    "You enjoy pleasant conversation with [the_person.possessive_title] as you walk downtown."
    #TODO the convo




    $ mc.change_location(downtown_bar)
    $ mc.location.show_background()

    "You walk into the bar. [the_person.title] spots an empty booth."
    the_person.char "Hey, there's an empty table over there!"
    mc.name "Go grab it. Appletini?"
    the_person.char "Sounds great!"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "She walks off to the booth while you head up to the bar."
    "You order your drinks with the bartender. If you wanted to, now would be a good time to slip a serum into her drink..."
    menu:
        "Slip in a serum":
            "After you get the drinks, you carefully add a serum to it."
            call give_serum(the_person) from _call_give_sarah_serum_001
        "Leave alone":
            "You decide to leave her drink alone."
    "You grab your drinks and then head to the table. You sit down across from [the_person.title]."
    $ scene_manager.update_actor(the_person, position = "sitting")
    the_person.char "Thanks! I love these things..."
    "She takes a long sip from her glass."

    return


label Sarah_catch_stealing_label():
    $ the_person = sarah
    $ sarah.event_triggers_dict["epic_tits_progress"] = 1
    "As you walk to halls of your company, getting ready to pack things up for the weekend, you notice [the_person.title] sneaking out of the research division."
    $ the_person.draw_person()
    mc.name "Hello [the_person.title]... what brings you to research on a late Friday evening?"
    "She looks down at the ground and mutters for a second, trying to think of something. It is clear she is hiding something."
    the_person.char "Hey [the_person.mc_title]! I was just, well, [stephanie.name] had something for me that umm, I asked her for help with and so I was just grabbing it before I left for the weekend!"
    "With one hand behind her back, it doesn't appear she wants you to know what is it that she has."
    mc.name "Is that so? That's awfully nice of her. What is she helping with? Can I see it?"
    if the_person.obedience > 120:
        "Realizing that you need to know what she was doing in there, she lowers her head and brings her hand forward. In it are several glass vials with some prototype serum labeled 'T+'"
        the_person.char "I'm sorry... I know I shouldn't... distract the research staff but, when you told me on Monday that we had come up with a breast enhancement serum, I immediately knew I had to get some I just..."
    else:
        the_person.char "Oh, don't worry about it, it is just between me and her!"
        "You furrow your brow. Hopefully you can convince her to come clean with whatever it is that she is doing."
        mc.name "I'm sure it is fine, but you ARE coming out of a research on a Friday, after everyone has left for the weekend. Let me see what you have."
        "Realing that you aren't going to back down, she slowly brings her hand forward. In it are several glass vials with some prototype serum labeled 'T+'"
        the_person.char "Don't be mad! When you told me on Monday that we had come up with a breast enhancement serum, I knew I had to get my hands on one of the prototypes..."
    mc.name "It okay. I didn't realize that was something you would be interested in. If you had asked me, I would have seen it arranged without having to sneak around!"
    $ the_person.change_happiness(5)
    $ the_person.change_love(3)
    $ the_person.draw_person(emotion = "happy")
    "She is very relieved to hear that."
    the_person.char "Oh! Thank you [the_person.mc_title]! I'm sorry, I won't be sneaky like that again. I just... you know I've always had such a small chest and been really self concious about it."
    the_person.char "I've thought about getting implants before but... surgery seems so extreme for a cosmetic issue."
    mc.name "So, how many are you planning to take?"
    the_person.char "Oh, well, research says we don't know for sure how effective they are... I figure I'll just take one each day until I go up a few cup sizes."
    the_person.char "I've already ordered new bras and everything. I'm going to keep a careful record of how many I take and when, and then take measurements over the weekend."
    "[stephanie.name] is going to stop by this weekend to help document everything, she said it would be good for research..."
    "You think about it for a moment. You picture [the_person.title] for a moment with some nice 'C' cup tits... but then you can't help but imagine if she went crazy with it and took more."
    menu:
        "Sounds like a good plan":
            mc.name "You should definitely take it slow. I mean, worst case scenario, you can just take more later if you need to."
        "You should take them all":
            "[the_person.title] looks up at you, a bit surprised."
            the_person.char "Wh... what? I mean, I've always dreamed of having huge tits but... I mean I can always take more later, right?"
            mc.name "Fortune favors the bold, [the_person.title]. I don't think you will regret it if you do it."
            the_person.char "But... I've already bought all new bras and lingerie... I don't have the money right now to do that all over again!"
            menu:
                "Buy her new bras ($300)":
                    $ mc.business.funds += -300
                    mc.name "I'll consider it an investment, from the business. It is the least we can do if you are willing to test the new serum prototypes."
                    the_person.char "Oh... that's very generous! I mean, I suppose if you're willing to do that. I can probably return a bunch of the other ones too."
                    "She stands there for a few moments, considering her options."
                    the_person.char "Ok! I'll do it! Oh god I'm so excited. I'm going to go straight home and take a few before bedtime."
                    mc.name "Sounds good. I'll look forward to seeing... all of you... on Monday."
                    "She blushes and nods."
                    the_person.char "Alright, see you Monday!"
                    $ Sarah_epic_tits = Action("Sarah epic tits",Sarah_epic_tits_requirement,"Sarah_epic_tits_label")
                    $ mc.business.mandatory_crises_list.append(Sarah_epic_tits) #Add the event here so that it pops when the requirements are met.
                    return
                "Stop wearing bras":
                    #TODO make new function to iterate through her wardrobe and remove the bra from every outfit.
                    if the_person.sluttiness > 40:
                        $ the_person.draw_person(position = "stand4", emotion = "happy")
                        the_person.char "Oh! Well that's an idea. Funny, why hadn't I thought of that?"
                        #TODO if based on if she has a uniform
                        # the_person.char "If I do that... Are you going to relax the dress code a bit? That's fine as long as I don't have to wear bras to work anymore..."
                        # mc.name "I will definitely look into it, if it helps you make up your mind."
                        "She stands there for a few moments, considering her options."
                        the_person.char "Ok! I'll do it! Oh god I'm so excited. I'm going to go straight home and take a few before bedtime."
                        mc.name "Sounds good. I'll look forward to seeing... all of you... on Monday."
                        "She blushes and nods."
                        the_person.char "Alright, see you Monday!"
                        $ Sarah_remove_bra_from_wardrobe(the_person.wardrobe)
                        $ Sarah_epic_tits = Action("Sarah epic tits",Sarah_epic_tits_requirement,"Sarah_epic_tits_label")
                        $ mc.business.mandatory_crises_list.append(Sarah_epic_tits) #Add the event here so that it pops when the requirements are met.
                        return
                    else:
                        the_person.char "I just... I don't think I can do that right now. I'm sorry [the_person.mc_title]!"
                        mc.name "It's fine, I just want you to be happy with your body."
                        the_person.char "Right. I mean, I can always take more later if I need to."

                "You're right":
                    mc.name "I just want you to be happy with your body."
                    "[the_person.title] looks a bit relieved."
                    the_person.char "Thanks [the_person.mc_title]."
    mc.name "Alright, you be careful this weekend. I'll look forward to seeing... all of you... on Monday."
    "She blushes and nods."
    the_person.char "Alright, see you Monday!"
    $ Sarah_new_tits = Action("Sarah new tits",Sarah_new_tits_requirement,"Sarah_new_tits_label")
    $ mc.business.mandatory_crises_list.append(Sarah_new_tits) #Add the event here so that it pops when the requirements are met.

    return

label Sarah_epic_tits_label():
    $ the_person = sarah
    $ sarah.tits = "F"
    $ sarah.event_triggers_dict["epic_tits_progress"] = 3
    $ the_person.change_slut_core(10)
    $ the_person.change_slut_temp(10)
    call Sarah_tits_reveal_label() from Sarah_epic_tits_call_1
    return

label Sarah_new_tits_label():
    $ the_person = sarah
    $ sarah.tits = "D"
    $ sarah.event_triggers_dict["epic_tits_progress"] = 2
    $ the_person.change_slut_core(5)
    $ the_person.change_slut_temp(5)
    call Sarah_tits_reveal_label() from Sarah_new_tits_call_1
    return

label Sarah_tits_reveal_label():
    $ the_person = sarah
    $ the_person.draw_person()
    "[the_person.title] steps confidently into your office."
    the_person.char "Good morning [the_person.mc_title]! Ready for our Monday meeting?"
    "Your jaw drops when you look up."
    mc.name "Wow, [the_person.title], you are awfully perky this morning!"
    "She laughs at you and smiles."
    $ the_person.draw_person(position = "stand4", emotion = "happy")
    the_person.char "Thank you [the_person.mc_title]. I'm sorry again about being sneaky about the whole thing. I really appreciate you letting me do this!"
    "You notice she turns and closes your office door... and then locks it."
    if the_person.outfit.tits_available():
        "[the_person.title] takes a breast in her hand, enjoying the weight of it."
        the_person.char "It is incredible. So much better than a implant, and they've gotten more sensitive too."
        "Her hand begins to idly pinch one of her nipples."
        $ the_person.change_arousal(15)
        the_person.char "Mmm. Go ahead and touch them. I want to feel your hands one me!"

    else:
        the_person.char "Do you want to give them a closer look? I mean, you are the man who made this all possible..."
        "You quickly agree."
        while not the_person.outfit.tits_available():    #If covered up, have her take her top off
            $ the_clothing = the_person.outfit.get_upper_ordered()[-1]
            "[the_person.possessive_title] takes off her [the_clothing.name]"
            $ the_person.draw_animated_removal(the_clothing)
        "Her chest now bare before you, [the_person.title] takes a breast in her hand, enjoying the weight."
        the_person.char "Go ahead and touch them. These are so much better than implants, I can't believe how good they feel. And they are so sensitive too..."
    "With both hands your reach and cup her considerable chest. The skin is soft and pliable in your hands."
    $ the_person.change_arousal(15)
    the_person.char "Mmmmmm. Don't be shy! Play with them a bit. It feels so goooood..."
    "You begin to knead her chest a bit rougher now. She gasps as you struggle to get all of her pleasant titflesh in your hands."
    $ the_person.change_arousal(15)
    the_person.char "Oh god, you are getting me so hot..."
    "Her knees buckle for a second when you start to play with her nipples. You pinch and roll them in your fingers."
    $ the_person.change_arousal(15)
    the_person.char "Ah! Stop! God that feels amazing. But theres something else I want to try..."
    mc.name "Oh? What is that?"
    the_person.char "Well, I've tried this a couple times before but to be honest my chest was so small I don't think it was very good for the guy but... I want your cock between my tits!"
    mc.name "That sounds hot. Lets do it!"
    "You turn your chair to the side and [the_person.title] gets on her knees in front of you."
    $ the_person.draw_person(position = "blowjob")
    "[the_person.possessive_title] eagerly begins opening your pants. She pulls out your cock and gives it a few gentle strokes."
    the_person.char "I can't believe I'm finally doing this. This all feels like a dream!"
    "She looks up at you from her knees. She looks you right in the eyes as she leans forward and slides your cock between her pillowy tits."
    "With both hands holding her breasts together, she slowly starts to move her pillowy flesh up and down your erection."
    call sex_description(the_person, SB_Titfuck_Kneeling, make_floor(), round = 1, private = True, girl_in_charge = True) from _call_sex_description_sarah_tits_reveal_1
    if the_person.arousal > 100: #She finished!
        the_person.char "Oh my god, I came so hard... I can't believe it. That felt so good! I need to do that again soon!"
        if the_person.get_opinion_score("showing her tits") < 2:
            $ the_person.sexy_opinions["showing her tits"] = [2, True]
            "[the_person.title] now loves showing her tits!"
    else:
        the_person.char "Mmm that was so hot. I can't wait to try that again..."
        if the_person.get_opinion_score("showing her tits") < 1:
            $ the_person.sexy_opinions["showing her tits"] = [1, True]
            "[the_person.title] now likes showing her tits!"
    the_person.char "Okay... let me go get cleaned up... then I'll come back and we can start our regular Monday meeting!"
    $ the_person.draw_person(position = "walking_away")
    "She gets up and leaves the room. You smile to yourself, thinking about how good her new tits felt around your cock."
    $ the_person.reset_arousal()
    $ the_person.review_outfit(show_review_message = False)

    return