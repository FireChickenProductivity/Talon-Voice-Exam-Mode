from talon import Module, actions, Context
module = Module()
module.tag('exam_mode', 'disables stuff that should not be allowed during exams')
module.tag('exam_mode_disable_snippets', 'disables snippets in exam mode')
context = Context()

@module.action_class
class Actions:
    def exam_mode_complain_about_action(illegal_action: str):
        '''Complains about the specified action'''
        inform_user_they_cannot_perform_this_action_in_exam_mode(illegal_action)

    def inform_user_they_cannot_open_talon_stuff():
        '''Informs the user that they cannot open talon stuff'''
        inform_user_they_cannot_perform_this_action_in_exam_mode('open talon stuff')

    def inform_user_that_some_tab_management_commands_are_disabled():
        '''Informs the user that some tab management commands are disabled'''
        actions.app.notify('Some tab management commands are disabled in exam mode!')

    def inform_user_that_some_browser_commands_are_disabled():
        '''Informs the user that they cannot use certain browser commands'''
        inform_user_they_cannot_perform_this_action_in_exam_mode('use some browser commands')

    def inform_user_that_some_generic_editor_commands_are_disabled():
        '''Tells the user that some generic editor commands are disabled to prevent accidentally deleting stuff during an exam'''
        inform_user_they_cannot_perform_this_action_in_exam_mode('use some generic editor commands to prevent accidentally deleting alot')

    def inform_user_that_help_commands_are_disabled():
        '''Tells the user that help commands are disabled in exam mode'''
        inform_user_they_cannot_perform_this_action_in_exam_mode('use help commands')

    def inform_user_that_macro_commands_are_disabled():
        '''Tells the user that macro commands are disabled in exam mode'''
        inform_user_they_cannot_perform_this_action_in_exam_mode('use macro commands')

    def inform_user_that_desktop_commands_are_disabled():
        '''Tells the user that desktop commands are disabled in exam mode'''
        inform_user_they_cannot_perform_this_action_in_exam_mode('use desktop commands')

    def inform_user_that_date_insert_commands_are_disabled():
        '''Tells the user that date insert commands are disabled'''
        inform_user_they_cannot_perform_this_action_in_exam_mode('use date insert commands')

    def inform_user_they_cannot_open_settings_files():
        '''Tells the user that opening settings files is disabled'''
        inform_user_they_cannot_perform_this_action_in_exam_mode('open settings files')

    def inform_user_that_microphone_selection_commands_are_disabled():
        '''Tells the user that they cannot use microphones selection commands'''
        inform_user_they_cannot_perform_this_action_in_exam_mode('use microphone selection commands')

    def inform_user_that_screenshot_commands_are_disabled():
        '''Tells the user that they cannot use screenshot commands'''
        inform_user_they_cannot_perform_this_action_in_exam_mode('use screenshot commands')
    
    def inform_user_that_snippet_commands_are_disabled():
        '''Tells the user that they cannot use snippet commands'''
        inform_user_they_cannot_perform_this_action_in_exam_mode('use snippet commands')
    
    def inform_user_that_helper_commands_are_disabled():
        '''Tells the user that they cannot use helper commands'''
        inform_user_they_cannot_perform_this_action_in_exam_mode('talon scripting helper commands')
    
    def inform_user_that_some_window_management_commands_are_disabled():
        '''Tells the user that they cannot use some window management commands'''
        inform_user_they_cannot_perform_this_action_in_exam_mode('some window management commands')

    def exam_mode_activate():
        '''Activates the exam mode'''
        context.tags = ['user.exam_mode']

    def exam_mode_deactivate():
        '''Deactivates the exam mode'''
        context.tags = []

def inform_user_they_cannot_perform_this_action_in_exam_mode(illegal_action):
    actions.app.notify(f'You cannot {illegal_action} in exam mode!')


