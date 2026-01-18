from talon import actions, Context

from typing import Optional

context = Context()
context.matches = r'''
tag: user.exam_mode
'''

@context.action_class('user')
class Actions:
    def switcher_launch(path: str):
        '''Overwrites the application launching action'''
        actions.user.exam_mode_complain_about_action('launch applications')

    def open_url(url: str):
        '''Overwrites opening websites'''
        actions.user.exam_mode_complain_about_action('open webpages')

    def search_with_search_engine(search_template: str, search_text: str):
        '''Overwrites using search engines'''
        actions.user.exam_mode_complain_about_action('use search engines')

    def edit_text_file(file: str):
        '''Overwrites opening files with text editors'''
        actions.user.exam_mode_complain_about_action('open text files')

    def talon_create_app_context(platform_suffix: str = None):
        '''Overwrites creating new app context files'''
        actions.user.exam_mode_complain_about_action('create app context files')
    
    def talon_add_context_clipboard_python():
        '''Overwrites copying the talon python context to the clipboard'''
        actions.user.inform_user_that_helper_commands_are_disabled()

    def talon_add_context_clipboard():
        '''Overwrites copying the python context to the clipboard'''
        actions.user.inform_user_that_helper_commands_are_disabled()
    
    def gamepad_tester_toggle():
        ''''Overwrites opening the gamepad tester'''
        actions.user.exam_mode_complain_about_action('open the gamepad tester')

    def check_vocabulary_for_selection():
        '''Overwrites checking the vocabulary'''
        actions.user.exam_mode_complain_about_action('check the vocabulary')
    
    def help_list(ab: str):
        """Provides the symbol dictionary"""
        actions.user.inform_user_that_help_commands_are_disabled()

    def help_formatters(ab: dict, reformat: bool):
        """Provides the list of formatter keywords"""
        # what you say is stored as a trigger
        actions.user.inform_user_that_help_commands_are_disabled()

    def help_context_enabled():
        """Display contextual command info"""
        actions.user.inform_user_that_help_commands_are_disabled()

    def help_context():
        """Display contextual command info"""
        actions.user.inform_user_that_help_commands_are_disabled()

    def help_search(phrase: str, enabled_only: Optional[bool] = False):
        """Display command info for search phrase"""
        actions.user.inform_user_that_help_commands_are_disabled()

    def help_selected_context(m: str):
        """Display command info for selected context"""
        actions.user.inform_user_that_help_commands_are_disabled()

    def help_next():
        """Navigates to next page"""
        actions.user.inform_user_that_help_commands_are_disabled()

    def help_select_index(index: int):
        """Select the context by a number"""
        actions.user.inform_user_that_help_commands_are_disabled()

    def help_previous():
        """Navigates to previous page"""
        actions.user.inform_user_that_help_commands_are_disabled()

    def help_return():
        """Returns to the main help window"""
        actions.user.inform_user_that_help_commands_are_disabled()

    def help_refresh():
        """Refreshes the help"""
        actions.user.inform_user_that_help_commands_are_disabled()

    def help_scope_toggle():
        """Toggle help scope gui"""
        actions.user.inform_user_that_help_commands_are_disabled()

    def desktop_next():
        actions.user.inform_user_that_desktop_commands_are_disabled()

    def desktop_last():
        actions.user.inform_user_that_desktop_commands_are_disabled()
    
    def play_pause():
        actions.user.exam_mode_complain_about_action("Play media")

snippet_context = Context()
snippet_context.matches = r'''
tag: user.exam_mode
and tag: user.exam_mode_disable_snippets
'''

@snippet_context.action_class('user')
class SnippetActions:
    def insert_snippet(body: str):
        '''Overwrites inserting snippets'''
        actions.user.inform_user_that_snippet_commands_are_disabled()

@context.action_class('app')
class AppActions:
    def tab_open():
        '''Overwrites opening tabs'''
        actions.user.exam_mode_complain_about_action('open tabs')

    def window_open():
        '''Overwrites opening windows'''
        actions.user.exam_mode_complain_about_action('open windows')

    def window_close():
        '''Overwrites closing windows'''
        actions.user.exam_mode_complain_about_action('close windows')



