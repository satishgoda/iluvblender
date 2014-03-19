
bl_info = {
    'name': 'Debug Screen, Area, Region',
    'category': 'Development',
    'description': 'Debug Screen, Area, Region'
}


import bpy


class AreaRunCommand(bpy.types.Operator):
    bl_idname = 'debug.area_run_command'
    bl_label = 'Debug Area Run Command'
    bl_options = {'INTERNAL', 'REGISTER'}
    
    def draw(self, context):
        layout = self.layout
        import builtins
        
        try:
            input = context.window_manager.prompt.strip()
            data_path = eval(input)
            message = str(data_path)
        except builtins.SyntaxError as se:
            message = 'ERROR: >>> {0}'.format(input if input else "<empty command>") + '\n\t'
            message += str(se)
        except builtins.AttributeError as ae:
            message = 'ERROR: >>> {0}'.format(input if input else "<empty command>") + '\n\t'
            message += str(ae)
            
        layout.label(">>> {}".format(input))
        layout.label("{}".format(message))
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)
    
    def execute(self, context):
        return {'FINISHED'}


def debug_area_run_command_draw(self, context):
    layout = self.layout
    col = layout.column()
    col.alert = True
    col.scale_x = 3.0
    col.prop(context.window_manager, 'prompt', text='')


def execute_prompt(self, context):
    bpy.ops.debug.area_run_command('INVOKE_DEFAULT')


def register():
    bpy.utils.register_class(AreaRunCommand)
    bpy.types.WindowManager.prompt = bpy.props.StringProperty(name='prompt', default='', update=execute_prompt)
    bpy.types.TEXT_HT_header.append(debug_area_run_command_draw)


def unregister():
    bpy.utils.unregister_class(AreaRunCommand)
    bpy.types.TEXT_HT_header.remove(debug_area_run_command_draw)
    del bpy.types.WindowManager.prompt


if __name__ == '__main__':
    register()
    #bpy.ops.debug.area_run_command('INVOKE_DEFAULT')

