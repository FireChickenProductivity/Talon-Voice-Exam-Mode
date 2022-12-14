from talon import Module, actions

module = Module()
@module.action_class
class Actions:
    def exam_mode_cleanup_draft_window():
        '''Erases the content of the draft window'''
        actions.user.draft_show("")
        actions.sleep(0.2)
        actions.user.draft_hide()