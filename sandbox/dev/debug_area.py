
bl_info = {
    'name': 'Debug Screen, Area, Region',
    'category': 'Development',
    'description': 'Debug Screen, Area, Region'
}


import bpy


class AreaRunCommand(bpy.types.Operator):
    bl_idname = 'debug.area_run_command'
    bl_label = 'Debug Area Run Command'
    bl_options = {'INTERNAL'}
    
    prompt = bpy.props.StringProperty(name='prompt', default='')
    
    def draw(self, context):
        layout = self.layout
        layout.label(context.area.type)
        layout.prop(self, 'prompt')
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=500)
    
    def execute(self, context):
        import builtins
        
        try:
            input = self.prompt.strip()
            data_path = eval(input)
            message = str(data_path)
        except builtins.SyntaxError as se:
            message = 'ERROR: >>> {0}'.format(input if input else "<empty command>") + '\n\t'
            message += str(se)
        except builtins.AttributeError as ae:
            message = 'ERROR: >>> {0}'.format(input if input else "<empty command>") + '\n\t'
            message += str(ae)
        
        self.report({'WARNING'}, str(message))
        return {'FINISHED'}


def register():
    bpy.utils.register_class(AreaRunCommand)


def unregister():
    bpy.utils.unregister_class(AreaRunCommand)


if __name__ == '__main__':
    register()
    bpy.ops.debug.area_run_command('INVOKE_DEFAULT')

