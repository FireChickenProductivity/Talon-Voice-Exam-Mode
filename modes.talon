^exam mode$: 
    mode.enable('user.exam_mode')
    user.exam_mode_cleanup_draft_window()
    
^(exit|turn off|disable) exam mode$: 
    mode.disable('user.exam_mode')
    user.exam_mode_cleanup_draft_window()
