init -2 python:
    config.layers.insert(2,"Active2") ## The "Active" layer is used to display the girls images when you talk to them. The next two lines signal it is to be hidden when you bring up the menu and when you change contexts (like calling a screen)
    config.menu_clear_layers.append("Active2")
    config.context_clear_layers.append("Active2")

    config.layers.insert(3,"Active3") ## The "Active" layer is used to display the girls images when you talk to them. The next two lines signal it is to be hidden when you bring up the menu and when you change contexts (like calling a screen)
    config.menu_clear_layers.append("Active3")
    config.context_clear_layers.append("Active3")


init -1:
    python:

        def change_location(self, new_location): # Overwrites change_location to have a list of followers follow you around. Will go to scheduled room on time advance.
            self.location = new_location
            for location in list_of_places:
                for person in location.people:
                    if person in list_of_followers:
                        location.move_person(person, new_location)
        MainCharacter.change_location = change_location



        def location(self): # Check what location a person is in e.g the_person.location() == downtown. Use to trigger events?
            for location in list_of_places:
                if self in location.people:
                    return location

        Person.location = location

        ## MATCH SKIN COLOR
        # Matches skin, body, face and expression images based on input of skin color
        def match_skin(self, color):
            self.skin = str(color)
            if self.skin == "white":
                self.body_images = white_skin
            elif self.skin == "tan":
                self.body_images = tan_skin
            elif self.skin == "black":
                self.body_images = black_skin
            self.expression_images = Expression("default", self.skin, self.face_style)
            return
        Person.match_skin = match_skin

        ## CHANGE HEIGHT EXTENSION
        # Returns True when the persons height has changed; otherwise False
        # chance is probability percentage that height change for amount will occur (used by serums)
        def change_height(self, amount, chance):
            if amount == 0 or (self.height == .8 and amount < 0) or (self.height == 1 and amount > 0):
                return False

            if renpy.random.randint(0, 100) <= chance:
                self.height += amount
            else:
                return False

            if self.height > 1:
                self.height == 1

            if self.height < .8:
                self.height = .8

            return True

        # attach change height function to the Person class
        Person.change_height = change_height

        ## CHANGE WEIGHT EXTENSION
        # Returns True when the persons body type has changed; otherwise False
        # chance is probability percentage that weight change for amount will occur (used by serums)
        def change_weight(self, amount, chance):
            check_person_weight_attribute(self)
            if (amount == 0):
                return False

            if renpy.random.randint(0, 100) <= chance:
                self.weight += amount

            # maximum and minimum weight are dependant on height
            max_weight = self.height * 100
            min_weight = self.height * 50
            switch_point_low = self.height * 68
            switch_point_high = self.height * 83

            if (amount > 0):
                if self.weight > switch_point_low + 3 and self.body_type == "thin_body":
                    self.body_type = "standard_body"
                    return True
                if self.weight > switch_point_high + 3 and self.body_type == "standard_body":
                    self.body_type = "curvy_body"
                    return True
                if self.weight > max_weight: #Maximum weight
                    self.weight = max_weight
                return False

            if (amount < 0):
                if self.weight < min_weight:  #Minimum weight
                    self.weight = min_weight
                    return False
                if self.weight < switch_point_low - 3 and self.body_type == "standard_body":
                    self.body_type = "thin_body"
                    return True
                if self.weight < switch_point_high - 3 and self.body_type == "curvy_body":
                    self.body_type = "standard_body"
                    return True
                return False

        # attach change weight function to the Person class
        Person.change_weight = change_weight

        def is_employee(self):
            employment_title = mc.business.get_employee_title(self)
            if employment_title != "None":
                return True
            return False

        Person.is_employee = is_employee

        ## LEARN HOME EXTENSION
        def learn_home(self): # Adds the_person.home to mc.known_home_locations allowing it to be visited without having to go through date label
            if not self.home in mc.known_home_locations:
                mc.known_home_locations.append(self.home)
                return True # Returns true if it succeeds
            return False # Returns false otherwise, so it can be used for checks.

        # Adds learn_home function to the_person.
        Person.learn_home = learn_home

        ## STRIP OUTFIT TO MAX SLUTTINES EXTENSION
        # Strips down the person to a clothing their are comfortable with (starting with top, before bottom)
        # narrator_messages: narrator voice after each item of clothing stripped, use '[person.<title>]' for titles and '[strip_choice.name]' for clothing item.
            # Can be an array of messages for variation in message per clothing item or just a single string or None for silent stripping
        def strip_outfit_to_max_sluttiness(self, top_layer_first = True, exclude_upper = False, exclude_lower = False, exclude_feet = True, narrator_messages = None, character_placement = None, temp_sluttiness_increase = 0):
            # internal function to strip top clothing first.           
            def get_strip_choice_upper_first(outfit, top_layer_first = True, exclude_upper = False, exclude_lower = False, exclude_feet = True):
                strip_choice = outfit.remove_random_upper(top_layer_first)
                if strip_choice is None:
                    strip_choice = outfit.remove_random_any(top_layer_first, exclude_upper, exclude_lower, exclude_feet)
                return strip_choice

            def get_messages(narrator_messages):
                messages = []
                if not narrator_messages:
                    pass
                elif not isinstance(narrator_messages, list):
                    messages = [narrator_messages]
                else:
                    messages = narrator_messages
                return messages
            
            messages = get_messages(narrator_messages)
            msg_count = len(messages)

            test_outfit = the_person.outfit.get_copy()
            removed_something = False

            strip_choice = get_strip_choice_upper_first(test_outfit, top_layer_first, exclude_upper, exclude_lower, exclude_feet)
            while strip_choice and self.judge_outfit(test_outfit, temp_sluttiness_increase):
                self.draw_animated_removal(strip_choice, character_placement = character_placement) #Draw the strip choice being removed from our current outfit
                self.outfit = test_outfit.get_copy() #Swap our current outfit out for the test outfit.
                if msg_count > 0:   # do we need to show a random message and replace titles and outfit name
                    msg_idx = renpy.random.randint(1, msg_count)
                    msg = messages[msg_idx - 1]
                    msg = msg.replace("[the_person.possessive_title]", self.possessive_title).replace("[the_person.title]", self.title).replace("[the_person.mc_title]", self.mc_title).replace("[strip_choice.name]", strip_choice.name)
                    renpy.say(None, msg)
                else:
                    renpy.pause(1) # if no message to show, wait a short while before automatically continue stripping

                strip_choice = get_strip_choice_upper_first(test_outfit, top_layer_first, exclude_upper, exclude_lower, exclude_feet)

            return removed_something

        # Monkey wrench Person class to have automatic strip function
        Person.strip_outfit_to_max_sluttiness = strip_outfit_to_max_sluttiness

        ## ADD OPINION EXTENSION
        ## Adds add_opinion function to Person class
        def add_opinion(self, opinion, degree, discovered = None, sexy_opinion = False, add_to_log = True): # Gives a message stating the opinion has been changed.
            opinion = opinion
            degree = degree
            discovered = discovered
            sexy_opinion = sexy_opinion # False for normal, True for Sexy

            if discovered is None and opinion in self.opinions[0]:  # we passed None for discovered so use existing discovered info
                discovered = self.opinions[opinion][1]

            if discovered is None and opinion in self.sexy_opinions[0]: # we passed None for discovered so use existing discovered info
                discovered = self.sexy_opinions[opinion][1]

            if discovered is None: # we didn't find any discovery information for opinion, so it's new and we passed None, so default set to false
                discovered = False

            if sexy_opinion == False:
                self.opinions[opinion] = [degree, discovered]

                if opinion not in opinions_list: # Appends to the opinion pool #TODO: should we add this to the game pool here? Prevents person specific opinions...
                    opinions_list.append(opinion)

            elif sexy_opinion == True:
                self.sexy_opinions[opinion] = [degree, discovered]

                if opinion not in sexy_opinions_list: # Appends to the opinion pool #TODO: should we add this to the game pool here? Prevents person specific opinions...
                    sexy_opinions_list.append(opinion)

            if add_to_log:
                mc.log_event((self.title or self.name) + " " + opinion_score_to_string(degree) + " " + str(opinion), "float_text_green")
            return

        # Adds a function that edits and adds opinions. It also appends to the vanilla opinion pool.
        Person.add_opinion = add_opinion

        ## CHANGE WILLPOWER EXTENSION
        # changes the willpower of a person by set amount
        def change_willpower(self, amount): #Logs change in willpower and shows new total.
            self.willpower += amount
            if self.willpower < 0:
                self.willpower = 0
            return person.willpower

        # attach to person object
        Person.change_willpower = change_willpower

        ## change person placement on the screen
        def change_placement(self, character_placement = None):
            clear_old_position = True
            if character_placement is None:
                character_placement = character_right
                clear_old_position = False

            if clear_old_position and not self.last_placement is None and self.last_placement != character_placement: # we change location so clear current location.
                old_scene_layer = current_scene_layer(self.last_placement)
                renpy.scene(old_scene_layer)

            active_scene_layer = current_scene_layer(character_placement)
            renpy.scene(active_scene_layer) # Clear current screen position for placement

            self.last_placement = character_placement
            return active_scene_layer
        # add extra function for charater placement
        Person.change_placement = change_placement

        # removes person from scene
        def clear_scene(self):
            active_scene = current_scene_layer(self.last_placement)
            self.last_placement = None
            renpy.scene(active_scene)

        Person.clear_scene = clear_scene

        def review_outfit_enhanced(self, show_review_message = True):
            if self.should_wear_uniform():
                self.wear_uniform()#Reset uniform
#                self.call_uniform_review() #TODO: actually impliment this call, but only when her outfit significantly differs from the real uniform.

            elif self.outfit.slut_requirement > self.sluttiness:
                self.outfit = self.planned_outfit.get_copy()
                if show_review_message:
                    self.call_dialogue("clothing_review")

        Person.review_outfit = review_outfit_enhanced

        def draw_person_enhanced(self,position = None, emotion = None, special_modifier = None, character_placement = None): #Draw the person, standing as default if they aren't standing in any other position.
            if position is None:
                position = self.idle_pose

            # Hack for updating the hair colour based on the name of the hair colour when the colour is black but the name is not.
            if (self.hair_colour != "black" and self.hair_style.colour == [0.1,0.09,0.08,1]):
                update_hair_colour(self)

            displayable_list = [] # We will be building up a list of displayables passed to us by the various objects on the person (their body, clothing, etc.)

            if emotion is None:
                emotion = self.get_emotion()

            if character_placement is None: # make sure we don't need to pass the position with each draw
                character_placement = self.last_placement or character_right

            active_scene = self.change_placement(character_placement)

            displayable_list.append(self.body_images.generate_item_displayable(self.body_type,self.tits,position)) #Add the body displayable
            displayable_list.append(self.expression_images.generate_emotion_displayable(position,emotion, special_modifier = special_modifier)) #Get the face displayable

            size_render = renpy.render(displayable_list[0], 10, 10, 0, 0) #We need a render object to check the actual size of the body displayable so we can build our composite accordingly.
            the_size = size_render.get_size() # Get the size. Without it our displayable would be stuck in the top left when we changed the size ofthings inside it.
            x_size = __builtin__.int(the_size[0])
            y_size = __builtin__.int(the_size[1])

            displayable_list.extend(self.outfit.generate_draw_list(self,position,emotion,special_modifier)) #Get the displayables for everything we wear. Note that extnsions do not return anything because they have nothing to show.
            displayable_list.append(self.hair_style.generate_item_displayable("standard_body",self.tits,position)) #Get hair

            #NOTE: default return for the_size is floats, even though it is in exact pixels. Use int here otherwise positional modifiers like xanchor and yalign do not work (no displayable is shown at all!)
            composite_list = [(x_size,y_size)] #Now we build a list of our parameters, done like this so they are arbitrarily long
            for display in displayable_list:
                composite_list.append((0,0)) #Center all displaybles on the top left corner, because of how they are rendered they will all line up.
                composite_list.append(display) #Append the actual displayable

            final_image = Composite(*composite_list) # Create a composite image using all of the displayables

            renpy.show(self.name,at_list=[character_placement, scale_person(self.height)],layer=active_scene,what=final_image,tag=self.name)
            renpy.scene

        # replace the default draw_person function of the person class
        Person.draw_person = draw_person_enhanced
        Person.last_placement = None

        def draw_animated_removal_enhanced(self, the_clothing, position = None, emotion = None, special_modifier = None, character_placement = None): #A special version of draw_person, removes the_clothing and animates it floating away. Otherwise draws as normal.
            #Note: this function includes a call to remove_clothing, it is not needed seperately.
            if position is None:
                position = self.idle_pose

            bottom_displayable = [] #Displayables under the piece of clothing being removed.
            top_displayable = []

            if emotion is None:
                emotion = self.get_emotion()

            if character_placement is None: # make sure we don't need to pass the position with each draw
                character_placement = self.last_placement or character_right

            active_scene = current_scene_layer(character_placement)

            renpy.scene(active_scene) # clear layer for new draw action
            # mc.log_event(self.title + " scene: " + active_scene, "float_text_green")

            bottom_displayable.append(self.expression_images.generate_emotion_displayable(position,emotion, special_modifier = special_modifier)) #Get the face displayable, also always under clothing.

            bottom_displayable.append(self.body_images.generate_item_displayable(self.body_type,self.tits,position))  #Body is always under clothing
            size_render = renpy.render(bottom_displayable[1], 10, 10, 0, 0) #We need a render object to check the actual size of the body displayable so we can build our composite accordingly.
            the_size = size_render.get_size()
            x_size = __builtin__.int(the_size[0])
            y_size = __builtin__.int(the_size[1])

            bottom_clothing, split_clothing, top_clothing = self.outfit.generate_split_draw_list(the_clothing, self, position, emotion, special_modifier) #Gets a split list of all of our clothing items.
            #We should remember that middle item can be None.
            for item in bottom_clothing:
                bottom_displayable.append(item)

            for item in top_clothing:
                top_displayable.append(item)

            top_displayable.append(self.hair_style.generate_item_displayable("standard_body",self.tits,position)) #Hair is always on top

            #Now we build our two composites, one for the bottom image and one for the top.
            composite_bottom_params = [(x_size,y_size)]
            for display in bottom_displayable:
                composite_bottom_params.append((0,0))
                composite_bottom_params.append(display)

            composite_top_params = [(x_size,y_size)]
            for display in top_displayable:
                composite_top_params.append((0,0))
                composite_top_params.append(display)

            final_bottom = Composite(*composite_bottom_params)
            final_top = Composite(*composite_top_params)

            renpy.show("Bottom Composite", at_list=[character_placement, scale_person(self.height)], layer=active_scene, what=final_bottom, tag=self.name+"Bottom")
            if split_clothing: #Only show this if we actually had something returned to us.
                renpy.show("Removed Item", at_list=[character_placement, scale_person(self.height), clothing_fade], layer=active_scene, what=split_clothing, tag=self.name+"Middle")
                self.outfit.remove_clothing(the_clothing)
            renpy.show("Top Composite", at_list=[character_placement, scale_person(self.height)], layer=active_scene, what=final_top, tag=self.name+"Top")        
        
        Person.draw_animated_removal = draw_animated_removal_enhanced

    #######################################
    # HELPER METHODS FOR CLASS EXTENSIONS #
    #######################################

        # Check if weight property exists on person, if not, add based on body type
        def check_person_weight_attribute(person):
            if not hasattr(person, "weight"):
                if (person.body_type == "thin_body"):
                    setattr(person, "weight", 60 * person.height)   # default weight thin body
                elif (person.body_type == "standard_body"):
                    setattr(person, "weight", 75 * person.height)   # default weight standard body
                else:
                    setattr(person, "weight", 90 * person.height)   # default weight curvy body
            return

        # calculates current player mental powers
        def player_willpower():
            mc.power = 0

            mc.power += int(mc.charisma*5) # Positive character modifiers
            mc.power += int(mc.current_stamina*1.5)
            return mc.power

        # calculates current willpower of a person
        def calculate_willpower(person):
            willpower = int(person.focus * 10 + person.happiness * 0.2 - person.obedience * 0.1 - person.love * 0.2 - person.suggestibility * 0.5)

            if willpower < 0:
                willpower = 0
            return willpower

        # log will power to event log in ui
        def log_willpower(person):
            if (person is mc):
                message = "Your: " + str(person.power)
            else:
                message = (person.title or person.name) + ": " + str(person.willpower)
            message += " Willpower"
            mc.log_event(message, "float_text_blue")
            return

        # get scene layer for placement position
        def current_scene_layer(character_placement):
            active_scene = "Active"
            if character_placement == character_center or character_placement == character_center_flipped:
                active_scene = "Active2"
            if character_placement == character_left or character_placement == character_left_flipped:
                active_scene = "Active3"
            return active_scene

#########################################
# Transormation for character_placement #
#########################################

    transform character_right_flipped():
        yalign 1.0
        yanchor 1.0
        xalign 1.0
        xanchor 1.0
        xzoom -1

    transform character_center():
        yalign 1.0
        yanchor 1.0
        xalign 0.75
        xanchor 1.0

    transform character_center_flipped():
        yalign 1.0
        yanchor 1.0
        xalign 0.75
        xanchor 1.0
        xzoom -1

    transform character_left():
        yalign 1.0
        yanchor 1.0
        xalign 0.5
        xanchor 1.0

    transform character_left_flipped():
        yalign 1.0
        yanchor 1.0
        xalign 0.5
        xanchor 1.0
        xzoom -1
