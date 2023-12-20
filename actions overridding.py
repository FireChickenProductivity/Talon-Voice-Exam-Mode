from talon import actions, Context

context = Context()
context.matches = 'tag: user.exam_mode'

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

    def edit_text_file(path: str):
        '''Overwrites opening files with text editors'''
        actions.user.exam_mode_complain_about_action('open text files')
    
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



