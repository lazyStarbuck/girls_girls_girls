init 5 python:
    add_label_hijack("normal_start", "activate_kaya_mod_core")
    add_label_hijack("after_load", "update_kaya_mod_core")


label activate_kaya_mod_core(stack):
    python:

        kaya_mod_initialization()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_kaya_mod_core(stack):
    python:
        if "kaya" not in globals():
            kaya_mod_initialization()
        execute_hijack_call(stack)
    return
