from src.server.managers.database import db
from flask_admin.contrib.sqla.view import ModelView
from src.server.models.pmk_guidebookskills import GuidebookSkills
from flask_admin import expose

class GuidebookSkillsView(ModelView):




    def __init__(self, model=GuidebookSkills, session=db.session, template=None, name=None, *args, **kwargs):
        super(GuidebookSkillsView, self).__init__(model, session, template, *args, **kwargs)

    can_export = True

    column_searchable_list = ['name', 'description']

    column_filters = ['work_center_id']



def get_guidebookskills():
    guidebookskills_view = GuidebookSkillsView(name="GuidebookSkills", endpoint='guidebook', menu_icon_type='fa', menu_icon_value='fa-connectdevelop')
    return guidebookskills_view