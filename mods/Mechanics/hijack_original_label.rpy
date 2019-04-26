## Hijack Original Label
# If you want run your MOD label after an an in game label you just need to call
# the add_label_hijack method, since we store all hijacked labels, you can attach
# your code to any base game code, without changing the original game code.

init 2 python:
    hijacklist = []
    # Keep track of the old callback so it can still be called
    original_label_callback = config.label_callback
    # Hijack the beginning of the class_selection label (which is not called or jumped to)
    def hijack_label_callback(label, abnormal):
        # Make sure to call the original label callback too
        if not original_label_callback is None:
            original_label_callback(label, abnormal)

        for hijack in hijacklist:
            # Jump to Mod setup choice and tutorial
            if label == hijack[0]:
                renpy.jump(hijack[1])
            
    config.label_callback = hijack_label_callback
    
    def add_label_hijack(orginal_label_name, hijack_label_name):
        hijacklist.append([orginal_label_name, hijack_label_name])

#label advance_time_extra:
#    "Testing hijack"
#    return

#init 200:
#    $ add_label_hijack("advance_time", "advance_time_extra")