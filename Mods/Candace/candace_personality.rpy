### PERSONALITY CHARACTERISTICS ###
init 1300:
    python:
        def candace_titles(the_person):
            return the_person.name
        def candace_possessive_titles(the_person):
            return candace_titles(the_person)
        def candace_player_titles(the_person):
            valid_mc_titles = []
            valid_mc_titles.append(mc.name)
            valid_mc_titles.append("cutie")
            return valid_mc_titles
        candace_personality = Personality("Candace", default_prefix = "bimbo",
        common_likes = ["skirts", "small talk", "the colour pink", "makeup", "pop"],
        common_sexy_likes = ["giving blowjobs", "missionary style sex", "being submissive", "skimpy outfits", "showing her tits", "showing her ass", "not wearing anything", "not wearing underwear", "lingerie", "cum facials"],
        common_dislikes = ["working", "research work", "work uniforms", "conservative outfits", "Mondays", "Pants"],
        common_sexy_dislikes = ["taking control", "masturbating"],
        titles_function = candace_titles, possessive_titles_function = candace_possessive_titles, player_titles_function = candace_player_titles)

### DIALOGUE ###
label candace_introduction(the_person):
    mc.name "Excuse me, could I bother you for a moment?"
    "She turns around at you. She doesn't hide the way she looks your body up and down."
    $ the_person.set_title("???")
    the_person.char "Oh you're cute! Okay, cutie, what do you need?"
    mc.name "I just wanted to get your name. I saw you walking past and..."
    $ title_choice = get_random_title(the_person)
    $ formatted_title = the_person.create_formatted_title(title_choice)
    if the_person.has_large_tits():
        the_person.char "And you liked my tits? Yeah, I get that a lot. I'm [formatted_title], it's nice to meet you!"
    else:
        the_person.char "And you liked my ass? Yeah, I get that a lot. I'm [formatted_title], it's nice to meet you!"
    #the_person.char "Well then, I suppose I shouldn't disappoint you. You can call me [formatted_title]."
    $ the_person.set_title(title_choice)
    $ the_person.set_possessive_title(get_random_possessive_title(the_person))
    the_person.char "So what's your name?"
    return

label candace_greetings(the_person):
    if the_person.love < 0:
        the_person.char "Oh, my, god... What do you want? Do I look like I want to be talking to you?"
    elif the_person.happiness < 90:
        the_person.char "Hi [the_person.mc_title]..."
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 130:
                the_person.char "Hey there [the_person.mc_title]. I mean sir! Hey there, sir!"
            else:
                the_person.char "Hey [the_person.mc_title], what are you doing here? Can I help with anything? Anything at all?"
        else:
            if the_person.obedience > 130:
                the_person.char "Hi there [the_person.mc_title], what can I do for you?"
            else:
                the_person.char "Hi there [the_person.mc_title]!"
    return

label candace_sex_responses_foreplay(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, you know just how to touch me [the_person.mc_title]!"
        else:
            "[the_person.title] giggles softly while you touch her."

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Do you like touching me [the_person.mc_title]? I know I like it when you do!"
        else:
            the_person.char "Do you like touching me [the_person.mc_title]? You seem to know exactly what to do."

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Yes! That feels really nice!"
            "She giggles happily, clearly having a good time."
        else:
            the_person.char " Mmm, you're driving me crazy [the_person.mc_title]!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "I can, like, feel it happening! You're going to make me cum my fucking brains out [the_person.mc_title]! Please, make me cum!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Oh fuck! My [so_title] would be so pissed if he knew how much better you feel when you touch me!"
                the_person.char "Make me cum! Make me cum my brains out!"

        else:
            the_person.char "Oh my god, I might cum if you keep touching me like that!"
    return

label candace_sex_responses_oral(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Aww, you always know what I like [the_person.mc_title]!"
        else:
            "[the_person.title] giggles softly."

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Does my pussy taste good [the_person.mc_title]? I'll repay the favour suck your cock later!"
        else:
            the_person.char "That, like, feels so good [the_person.mc_title]!"

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Ah! Hehe, that's feels so good!"
            "She giggles happily, clearly having a good time."
        else:
            the_person.char "Oh wow! Mmmm, you're tongue is, like, driving me crazy [the_person.mc_title]!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "I can, like, feel it happening! You're going to make me cum with your mouth! Make me cum, please!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Oh fuck! My [so_title] would be so pissed if he knew how much better you make me feel!"
                the_person.char "He never licks my pussy though, so make me cum! Make me cum my brains out!"

        else:
            the_person.char "Oh my god, you're... You might make me cum if you keep licking my pussy like that!"
    return

label candace_sex_responses_vaginal(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, you know what I like [the_person.mc_title]!"
        else:
            "[the_person.title] giggles softly."

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Is your cock always this big, or are you just happy to see me? Hehe!"
        else:
            the_person.char "Am I your dirty girl [the_person.mc_title]? Because I'm having so much fun right now!"

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Yes! Keep fucking me!"
            "She giggles happily, clearly having a good time."
        else:
            the_person.char "Oh wow! Mmmm, you're cock is driving me crazy [the_person.mc_title]!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "I can, like, feel it happening! You're going to make me cum my fucking brains out [the_person.mc_title]! Please, make me cum!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Oh fuck! My [so_title] would be so pissed if he knew how much better your cock feels!"
                the_person.char "Oh well, I just want to cum! Make me cum! Make me cum my brains out!"

        else:
            the_person.char "Oh my god, you're... You might make me cum if you keep going!"
    return

label candace_sex_responses_anal(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "I can, like, feel every single inch of you in me! You're so big!"
        else:
            the_person.char "You're, like, {i}huge{/i} inside of me! I don't know if I can do this for very long!"

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Fuck my ass [the_person.mc_title], fuck me it's raw and you're done with me!"
        else:
            the_person.char "Oh, it feels like you're stirring up my insides with your dick! Ah!"

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "I'm so stretched out, I think I'm starting to get the hang of this!"
            "She giggles happily, clearly proud of her accomplishment."
        else:
            the_person.char "My mind is going blank, all I can think about is your cock inside of me!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "I can, like, feel it happening! Fuck my ass and make me cum [the_person.mc_title]! Do it!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Oh fuck! My [so_title] would be so pissed if he knew I was letting you anal me."
                the_person.char "He's been begging for it for {i}months{/i}, but I just know he wouldn't feel nearly as good inside me as you do!"

        else:
            the_person.char "Oh my god, you're... You might make me cum if you keep fucking my ass! Please make me cum!"
    return

label candace_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person.char "Oh god, I'm going to cum! All I want to do is cum [the_person.mc_title], ah!"
        "She squeals with pleasure and excitement."
    else:
        the_person.char "Oh my god, this feeling. I'm... I'm... cumming!"

    return

label candace_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Oh god, make me cum [the_person.mc_title]! My mind is going blank, I just need to cum!"
    else:
        the_person.char "That feels, like, {i}so good{/i}!"
        "She closes her eyes and squeals with pleasure."
    return

label candace_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Oh god I'm going to cum! Ahh, make me cum [the_person.mc_title], it's all I want right now!"
        "She closes her eyes and squeals with pleasure."
    else:
        the_person.char "Yes, yes, yes! Make me cum! Make me cum hard!"
    return

label candace_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Oh my god! I'm going to cum with your cock up my ass!"
        "She squeals loudly."
    else:
        the_person.char "Oh my god! I'm such a slut, I'm about to cum! Oh fuck!"

    return

label candace_clothing_accept(the_person):
    if the_person.obedience > 130:
        the_person.char "Oh that's cute! You have such a good sense of style [the_person.mc_title], this is just what I like to wear!"
    else:
        the_person.char "It's so cute! I love getting new clothes - you should see my closet at home, there's no such thing as too many shoes, right?"
    return

label candace_clothing_reject(the_person):
    if the_person.obedience > 130:
        the_person.char "Uh... I don't think I'm allowed to wear that. I really wish I could though, just for you!"
    else:
        if the_person.sluttiness > 60:
            the_person.char "That's not really an outfit, is it? I like something a little cuter - some heels, add a dash of pink, and a top to show off my tits!"
            "[the_person.title] looks the outfit over again for a momnt and shakes her head."
            the_person.char "Yeah, this just isn't going to do it. Thanks for the thought though!"
        else:
            the_person.char "Aww, I don't think I could ever wear something like that! I wish I could though, could you imagine the looks I would get? It would be. So. Hot."
    return

label candace_clothing_review(the_person):
    if the_person.obedience > 130:
        the_person.char "Hehe, you really made a mess of me. I should go get tidied up, I'm suppose to be a proper lady here!"
    else:
        if the_person.sluttiness > 40:
            "[the_person.title] looks down at herself and giggles."
            the_person.char "Hehe, I'm all messed up after that! I need to go sort this out, this outfit just doesn't work right now!"
        else:
            the_person.char "Oh darn, my outfit's all confuzzled! I'm going to go fix this up, I'll be back before you know it!"
    return

label candace_strip_reject(the_person):
    if the_person.obedience > 130:
        the_person.char "Don't you think I look cuter with it on? Leave it alone for now, okay?"
    elif the_person.obedience < 70:
        the_person.char "Oh no-no-no, I'm going to decide when that comes off. I want to see you work for it!"
    else:
        "[the_person.title] giggles and bats your hand away playfully."
        the_person.char "Not yet, there's so much fun stuff we have to do first!"
    return

label candace_sex_accept(the_person):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            the_person.char "Oh yeah, that's one of my favourite things to do! Come on, let's do it!"
        else:
            the_person.char "Yeah, let's do it! You're so cute when you're horny, did you know that?"
    else:
        the_person.char "Oh? Oh! Yeah, lets do that!"
    return

label candace_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Wow that's a... does that even work? I thought... well I guess I should try it before I knock it!"
    else:
        if the_person.obedience > 130:
            the_person.char "If that's what you want, boss man, that's what you'll get!"
        else:
            the_person.char "You bring out the worst in me, you know that [the_person.mc_title]? I was a nice, respectable girl before you showed up!"
    return

label candace_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person.char "No, no, no, not yet. I want you to make me wait for it a little bit, get me really begging for it."
    else:
        the_person.char "Uh, I don't think that sounds fun. Let's do something else. Come on, you pick!"
    return

label candace_sex_angry_reject(the_person):
    if not the_person.relationship == "Single":
        $ so_title = SO_relationship_to_title(the_person.relationship)
        the_person.char "What? I have a [so_title], and he treats me so much better than you could EVER hope to. Understood?"
        "She rolls her eyes dramatically and walks away."
        the_person.char "Perv."
    elif the_person.sluttiness < 20:
        the_person.char "Uh, what the ACTUAL FUCK?! What do you think you're doing? Just saying that must be... illegal, or something!"
        "[the_person.title] glares at you you and walks away."
    else:
        the_person.char "Eew! No, no, no! I will NEVER do that with ANYONE! Eew!"
        "[the_person.title] shakes her head and walks away."
    return

label candace_seduction_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "Oh yay, I know how to deal with this! You just relax and I'll make you feel very, very good!"
        else:
            the_person.char "All I can think about is that cute little dress I saw this morning. Oh, that's not you meant, was it..."
            "[the_person.title] giggles."
            the_person.char "Never mind, lead the way!"
    else:
        if the_person.sluttiness > 50:
            the_person.char "Yay! I was getting so horny that I was ready to jump you in the hall!"
        elif the_person.sluttiness > 10:
            the_person.char "Hehe, I thought you had the that look in your eye. I have a sixth sense, but it's for horny guys instead of ghosts!"
        else:
            the_person.char "Oh, I don't really know what to say [the_person.mc_title]..."
    return

label candace_flirt_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "Just make it an official order and it's all yours, boss man."
        else:
            the_person.char "Hehe, thank you, you're way too nice to me!"

    elif not the_person.relationship == "Single":
        $so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (the_person.get_opinion_score("cheating on men")*5) > 50:
            the_person.char "That's like, super hot to hear you say. We just can't let my [so_title] or he would flip out."
        else:
            the_person.char "Oh my god, you're so cute! My [so_title] never says things like that to me."
            "She pouts for a moment before returning to her bubbly self."

    else:
        if the_person.sluttiness > 50:
            the_person.char "You should try your luck sometimes. Maybe take me out for a drink, I get wild after I've had a few. Wild-er, I guess."
        else:
            the_person.char "Oh you, stop it! You're going to make me blush!"
    return

label candace_flirt_response_low(the_person):
    if the_person.outfit == the_person.planned_uniform:
        if the_person.judge_outfit(the_person.outfit):
            #She's in uniform and likes how it looks.
            the_person.char "Hehe, thanks! I love these outfits you make us wear, they're, like, so cute!"
            the_person.char "Maybe you should pick out other things for me to wear. I bet you have some good ideas!"
            mc.name "For you I certainly do. Maybe I'll talk to you later about it."
            "She smiles happily."
            the_person.char "Alright!"

        else:
            #She's in uniform, but she thinks it's a little too slutty.
            if the_person.outfit.vagina_visible():
                # Her pussy is on display.
                the_person.char "Thanks! I keep worrying I'm going to get in trouble, but then I remember I'm allowed to be dressed like this!"
                mc.name "Not just allowed: required."
                the_person.char "Yeah! This is such a crazy place to work!"
                "[the_person.possessive_title] bounces happily, unintentionally jiggling her tits."

            elif the_person.outfit.tits_visible():
                #Her tits are out
                if the_person.has_large_tits():
                    the_person.char "Hehe, thanks! I really like how it shows off my big tits!"
                    "[the_person.possessive_title] bounces happily, jiggling her breasts."
                    the_person.char "People are always telling me I need to hide them, but at work I don't have to worry about that!"
                else:
                    the_person.char "Hehe, thanks! I really like how I it shows off my boobs!"
                    "[the_person.possessive_title] looks down at her own chests and pouts."
                    the_person.char "I wish they were bigger though. Oh well!"

            elif the_person.outfit.underwear_visible():
                # Her underwear is visible.
                the_person.char "Hehe, thank you! I know it's a little slutty, but I like how little these outfits you make us wear cover!"
                mc.name "I certainly do too."
                "She laughs and sticks her tongue out."
                the_person.char "You're silly, you know that? But like, in a fun way."
            else:
                # It's just generally slutty.
                the_person.char "Hehe, thank you! I don't think I'm brave enough to wear something like this outside, but at work it's okay! Right?"
                mc.name "More than okay, it's required."
                the_person.char "Oh yeah, right! I'm sorry, there are so many rules here, I'm always forgetting them!"
                mc.name "Well don't worry, you're doing a great job so far."
                "[the_person.possessive_title] smiles and bounces happily."
                the_person.char "Yay!"

    else:
        #She's in her own outfit.
        the_person.char "Aw, thanks! It took me sooooo long to decide what to wear today. I picked this because it made my ass look good. What do you think?"
        $ the_person.draw_person(position = "back_peek")
        "[the_person.possessive_title] spins around and leans forward a little, wiggling her butt at you."
        mc.name "Oh yeah, I think it looks really good."
        $ the_person.draw_person()
        the_person.char "Yay!"
    return

label candace_flirt_response_mid(the_person):
    if the_person.outfit == the_person.planned_uniform:
        if the_person.judge_outfit(the_person.outfit):
            if the_person.outfit.tits_visible():
                the_person.char "Hehe, thanks! Do you like my boobs?"
                "She puts her hands behind her back and thrusts her chest out at you, waiting for your response."
                mc.name "They look fantastic."
                "[the_person.possessive_title] smiles and giggles."
                the_person.char "Yay! I like having my boobs out at work. It feels naughty, but I'm, like, allowed to do it!"
            else:
                the_person.char "Hehe, thanks! I think you're, like, pretty hot too!"
                the_person.char "Oh my god! We should go partying together! That would be, like, so much fun!"
                mc.name "That does sound like fun. Maybe we will."
                "She nods and smiles happily."
        else:
            "[the_person.possessive_title] smiles and giggles."
            the_person.char "Hehe, thanks! I think you're pretty hot too!"
            the_person.char "Oh, we should totally go partying together! That would be, like, so much fun!"
            mc.name "That does sound like fun. Maybe we will."
            "She nods and smiles happily."
            the_person.char "I can even wear something nice for you, instead of this silly uniform you make..."
            "She stops suddenly and covers her mouth with her hand."
            the_person.char "Oops. I'm sorry, I didn't mean that. I just kind of talk without thinking sometimes." #TODO: On with the spanking! And then, the oral sex!
            mc.name "It's fine. You don't have to like your uniform as long as you're wearing it."
            "[the_person.title] puts on a stern face and nods severely."
            the_person.char "Of course, [the_person.mc_title]!"

    else:
        if the_person.effective_sluttiness() < 20 and mc.location.get_person_count() > 1:
            the_person.char "Hehe, thanks! I uh..."
            "[the_person.possessive_title] bites her lip and leans closer to you to whisper in your ear."
            the_person.char "I think you're, like, pretty hot too."
            "She pulls back and smiles playfully."

        else:
            the_person.char "Hehe, thank you! I think you're looking, like, pretty hot too."
            the_person.char "Oh, we should totally go partying some time! I can wear something even cuter for you..."
            $ the_person.draw_person(position = "back_peek")
            the_person.char "Maybe something that shows off my butt a little more... Doesn't that sound fun?"
            "[the_person.possessive_title] wiggles her hips, shaking her butt for your enjoyment."
            mc.name "That does sound like fun. Maybe we should go out one day."
            $ the_person.draw_person()
            "She turns back to you and smiles."
            the_person.char "Yay!"
    return

label candace_flirt_response_high(the_person):
    if mc.location.get_person_count() > 1 and the_person.effective_sluttiness() < (25 - (5*the_person.get_opinion_score("public_sex"))):
        "[the_person.possessive_title] giggles and looks around nervously."
        the_person.char "Oh my god, [the_person.mc_title]! That's so naughty!"
        menu:
            "Find someplace quiet":
                mc.name "Come with me and we can do some more naughty things."
                "[the_person.title] giggles again and nods eagerly. You take her hand and lead her away."
                "When you're finally alone you put your arm around her waist and pull her close."

                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                else:
                    pass
                "You kiss her, and she responds by leaning her body against you eagerly."
                call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_55123

            "Just flirt":
                mc.name "Wait until I get you alone and you'll see how naughty I can get."
                the_person.char "Hehe, I'm excited to find out!"

    else: # She wants to kiss you, leading to other things.
        if mc.location.get_person_count() == 1:
            the_person.char "Oh my god, [the_person.mc_title]! you're so naughty!"
            "She giggles playfully and looks you up and down."
            the_person.char "But maybe... We could fool around, if you really want to. I think you're pretty cute."

        else:  #She's into turning you on.
            if the_person.has_large_tits(): #Bounces her tits for you
                "She giggles and grabs her own tits, jiggling them for you."
                $ the_person.draw_person(the_animation = blowjob_bob)

            else:
                "She giggles and wiggles her hips for you."
            the_person.char "Do you want to have some fun?"

        menu:
            "Kiss her":
                mc.name "Yeah, I do. Come here."
                $ the_person.draw_person()
                if the_person.has_taboo("kissing"):
                    "You put your arm around [the_person.title]'s waist and pull her close. She giggles as she falls against your body."
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "You kiss her, and she rubs her body against you eagerly."
                else:
                    "You put your arm around [the_person.title]'s waist and pull her close. She leans her body against you eagerly as you kiss her."
                call fuck_person(the_person, start_position = kissing, skip_intro = True) from _call_fuck_person_56123

            "Just flirt":
                mc.name "I do, but it'll have to be some other time."
                $ the_person.draw_person(emotion = "sad")
                "She pouts and crosses her arms dramatically."
                the_person.char "Aww, why? Can't you, like, just do something with me right now?"
                mc.name "I'll make it up to you, I promise."
                "[the_person.title] sighs and nods."
                the_person.char "Okay..."
    return

label candace_cum_face(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "Do I look cute covered in your cum, [the_person.mc_title]?"
            "[the_person.title] licks her lips, cleaning up a few drops of your semen that had run down her face."
        else:
            the_person.char "I hope this means I did a good job."
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    else:
        if the_person.sluttiness > 80:
            the_person.char "Ah... I love a nice, hot load on my face. Don't you think I look cute like this?"
        else:
            the_person.char "Fuck me, you really pumped it out, didn't you?"
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    return

label candace_cum_mouth(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "That was very nice [the_person.mc_title], thank you."
        else:
            "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
            the_person.char "Thank you [the_person.mc_title], I hope you had a good time."
    else:
        if the_person.sluttiness > 80:
            the_person.char "Your cum tastes great [the_person.mc_title], thanks for giving me so much of it."
            "[the_person.title] licks her lips and sighs happily."
        else:
            the_person.char "Bleh, I don't know if I'll ever get use to that."
    return

label candace_cum_vagina(the_person):
    if mc.condom:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            the_person.char "That condom is so stretchy! I can feel how much cum you put into it and it's, like, a lot!"
        else:
            the_person.char "Mmm, your cum is so nice and hot!"

    else:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Mmm, I love having all your cum inside me. That might make me pregnant, right?"
                "She thinks about this for a second, then shrugs."
                the_person.char "Oh well, my [so_title] will just take care of it, so that doesn't matter!"
            else:
                the_person.char "Mmm, I love having all your cum inside me. That might make me pregnant, right?"
                "She thinks about this for a second, then shrugs."
                the_person.char "Oh well, it's worth it to feel like this!"
        else:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Oh, that's so hot... But wait, if I get pregnant what do I tell my [so_title]?"
                "She bites her lip and looks worried."
                the_person.char "We shouldn't do this too often. Next time you can cum somewhere else, okay?"
            else:
                the_person.char "Oh, that's so hot... But what do I do if I get pregnant?"
                "She bites her lip and looks worried."
                the_person.char "We shouldn't do this too often, okay? Next time you can cum, like, somewhere else, right?"
    return

label candace_cum_anal(the_person):
    if the_person.sluttiness > 75 or the_person.get_opinion_score("anal creampies") > 0:
        the_person.char "Give me your cum! I want you to cum in my ass! Ah!"
    else:
        the_person.char "Oh! Fuck, I hope there's room for all your cum!"
    return

label candace_suprised_exclaim(the_person):
    $rando = renpy.random.choice(["Fuck!","Shit!","Oh fuck!","Fuck me!","Ah! Oh fuck!", "Ah!", "Fucking tits!", "Holy shit!", "Fucking shit!"])
    the_person.char "[rando]"
    return

label candace_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person.char "Hi, I'm like, really sorry but I have way more stuff than you can imagine that I have to get done right now. Could we catch up later?"
    else:
        the_person.char "Hey, I'm sorry but I'm just suuuper busy right now! Hit me up later though, I'd love to chat once I get all this stupid work done!"
    return

label candace_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal < 50:
            the_person.char "Oh wait, I know what you want to see more of..."
        else:
            the_person.char "Ugh, all this clothing is getting in the way!"

    elif the_person.sluttiness < 60:
        if the_person.arousal < 50:
            the_person.char "I spent so much time this morning picking out this outfit, but I think you'd enjoy it more if I took it off, right?"
        else:
            the_person.char "Ah... I need to get all of this silly stuff off of me!"

    else:
        if the_person.arousal < 50:
            the_person.char "Teehee, just wait a moment and I'll strip this off for you..."
        else:
            the_person.char "Oh my god, let me strip for you [the_person.mc_title], let me be your slutty stripper!"

    return

label candace_sex_watch(the_person, the_sex_person, the_position):
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry")
        the_person.char "Is that, like, allowed? I thought that was illegal or something. Ugh."
        $ the_person.change_obedience(-2)
        $ the_person.change_happiness(-1)
        "[the_person.title] looks away while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person()
        the_person.char "Could you two get a room or something? There are some of us here who are trying to focus and you're being very distracting."
        $ the_person.change_happiness(-1)
        "[the_person.title] tries to avert her gaze while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person()
        the_person.char "Wow [the_sex_person.name] you're so adventurous, I don't think I could ever do that. But it looks, like, super fun!"
        $ change_report = the_person.change_slut_temp(1)
        "[the_person.title] averts her gaze, but keeps glancing over while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person()
        the_person.char "Oh. My. God. That is so fucking hot... Keep it up girl, you're doing great!"
        $ change_report = the_person.change_slut_temp(2)
        "[the_person.title] watches you and [the_sex_person.name] [the_position.verb]."

    else:
        $ the_person.draw_person(emotion = "happy")
        the_person.char "Mmm, come on [the_person.mc_title], you should do something more to her. I bet she wants it real bad. I know I do..."
        "[the_person.title] watches eagerly while you and [the_sex_person.name] [the_position.verb]."
    return

label candace_being_watched(the_person, the_watcher, the_position):
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person.char "I can handle it [the_person.mc_title], you can be rough with me."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person.char "Don't listen to [the_watcher.title], I'm having a great time. Look, she can't stop peeking over."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        the_person.char "Oh god, having you watch us like this..."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person.char "[the_person.mc_title], maybe we shouldn't be doing this here..."
        $ the_person.change_arousal(-1)
        $ the_person.change_slut_temp(-1)
        "[the_person.title] seems uncomfortable with [the_watcher.title] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        the_person.char "Oh my god, having you watch us do this feels so dirty. I think I like it!"
        $ the_person.change_arousal(1)
        $ the_person.change_slut_temp(1)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [the_watcher.title] around."

    return

label candace_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        "[the_person.title] looks at you, pouts, then looks back at her work."

    elif the_person.happiness > 120:
        if the_person.sluttiness > 40:
            "[the_person.title] looks at you when you enter the room and smiles."
            the_person.char "[the_person.mc_title]! I'm so glad you're stopping by, I've been so bored without you."
            "She pouts at you, eyes running up and down your body shamelessly."
            the_person.char "I hope you're here for something fun!"
        else:
            "[the_person.title] looks up from her work when you come into the room and smiles."
            the_person.char "[the_person.mc_title]! It's so good to see you! I've been having, like, the best day!"

    else:
        if the_person.obedience < 100:
            the_person.char "Hi [the_person.mc_title]! Do you need anything, any way I can help you?"
        else:
            the_person.char "Hi [the_person.mc_title]! Duh, I mean sir! Hi sir!"
            "[the_person.title] sticks out her tongue, then smiles and turns back to her work."

    return

label candace_date_seduction(the_person):
    if the_person.sluttiness > the_person.love:
        if the_person.sluttiness > 40:
            the_person.char "So [the_person.mc_title], don't you think it's time you came back home with me and we had some real fun?"
            "[the_person.title] bites her lip and puffs out her chest just a little bit."

        else:
            the_person.char "[the_person.mc_title], I swear you're driving me crazy. Do you, like, want to come home with me and just get wild?"

    else:
        if the_person.love > 40:
            the_person.char "[the_person.mc_title], I don't know how you do it but I swear you've been driving me, like, totally crazy all night."
            "[the_person.title] runs her hand along your arm and giggles."
            the_person.char "I want you to come back to my place so I can have you all to my self."
        else:
            the_person.char "Oh my god [the_person.mc_title], tonight has been so much fun. Do you want to, like, come back home with me and drink some more?"
    return

label candace_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal > 60:
                the_person.char "Aww sweety, I was just getting close to cumming and you're done?!"
            else:
                the_person.char "That's all? Aww, I hope you had a good time with me..."
        else:
            if the_person.arousal > 60:
                "Wait, you're stopping? Aren't crazy horny right now too?"
            else:
                the_person.char "Don't you want to play with me any more? Oh well, your loss."

    else:
        if the_person.love > 40:
            if the_person.arousal > 60:
                the_person.char "You're actually done? But weren't you, like, having fun? I'm so fucking horny now..."
            else:
                the_person.char "Is that all you wanted to do? I thought guys had to, like, cum or it hurt."
        else:
            if the_person.arousal > 60:
                the_person.char "Aww, I was just getting getting warmed up!"

            else:
                the_person.char "That's it? Well, I guess that was a fun time well it lasted."
    return

## Role Specific Section ##
label candace_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time in the lab there's something I wanted to talk to you about."
    the_person.char "Okay, how can I help?"
    mc.name "All of our research and development up until this point has been based on the limited notes I have from my university days. I'm sure there's more we could learn, and I want you to look into it for me."
    "[the_person.title] nods happily."
    "There's a long pause."
    mc.name "Do you know what to do?"
    the_person.char "Uh, duh! Look into the serum-stuff we make and make it better-er!"
    mc.name "Right, and do you have any idea how to actually do that?"
    "[the_person.title]'s eyebrows knit together as she tries to think."
    the_person.char "Uhm... not yet but... what if..."
    "You imagine you can see the little hamster in her head running as fast as it can."
    the_person.char "I've got it! What if you test it on me!"
    mc.name "Do you think that's a good idea!"
    the_person.char "Duh, that's why I thought of it! Come on, how bad could it be? Just let me try it! Record it or something and I'll tell you what it feels like!"
    return

## Taboo break dialogue ##
# label candace_kissing_taboo_break(the_person):
#
#     return
#
# label candace_touching_body_taboo_break(the_person):
#
#     return
#
# label candace_touching_penis_taboo_break(the_person):
#
#     return
#
# label candace_touching_vagina_taboo_break(the_person):
#
#     return
#
# label candace_sucking_cock_taboo_break(the_person):
#
#     return
#
# label candace_licking_pussy_taboo_break(the_person):
#
#     return
#
# label candace_vaginal_sex_taboo_break(the_person):
#
#     return
#
# label candace_anal_sex_taboo_break(the_person):
#
#     return
#
# label candace_condomless_sex_taboo_break(the_person):
#
#     return
#
# label candace_underwear_nudity_taboo_break(the_person, the_clothing):
#
#     return
#
# label candace_bare_tits_taboo_break(the_person, the_clothing):
#
#     return
#
# label candace_bare_pussy_taboo_break(the_person, the_clothing):
#
#     return
#
# label candace_facial_cum_taboo_break(the_person):
#
#     return
#
# label candace_mouth_cum_taboo_break(the_person):
#
#     return
#
# label candace_body_cum_taboo_break(the_person):
#
#     return
#
# label candace_creampie_taboo_break(the_person):
#
#     return
#
# label candace_anal_creampie_taboo_break(the_person):
#
#     return