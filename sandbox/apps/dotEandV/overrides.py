import bpy

from bpy.types import TEXT_HT_header


def TEXT_HT_header_app(self, context):
    layout = self.layout
    
    for item in ('Open', 'Save', 'Render'):
        layout.label(item)
    
    layout.separator()
    layout.template_running_jobs()
    layout.template_reports_banner()


def register():
    TEXT_HT_header.prepend(TEXT_HT_header_app)


def unregister():
    TEXT_HT_header.remove(TEXT_HT_header_app)

