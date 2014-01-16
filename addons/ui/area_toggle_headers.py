for area in C.screen.areas:
    area.show_menus = not area.show_menus
    area.tag_redraw()

