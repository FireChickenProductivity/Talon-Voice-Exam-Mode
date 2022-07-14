mode: user.exam_mode
-
^grab screen$:                       user.inform_user_that_screenshot_commands_are_disabled()
^grab screen <number_small>$:        user.inform_user_that_screenshot_commands_are_disabled()
^grab window$:                       user.inform_user_that_screenshot_commands_are_disabled()
^grab selection$:                    user.inform_user_that_screenshot_commands_are_disabled()
^grab settings$:                     user.inform_user_that_screenshot_commands_are_disabled()
^grab screen clip$:                  user.inform_user_that_screenshot_commands_are_disabled()
^grab screen <number_small> clip$:   user.inform_user_that_screenshot_commands_are_disabled()
^grab window clip$:                  user.inform_user_that_screenshot_commands_are_disabled()
