
from src.server.models.pmk_experiment import Experiment
from src.server.managers.database import db
from flask_admin.contrib.sqla.view import ModelView

class ExperimentView(ModelView):
    def __init__(self, model=Experiment, session=db.session, template=None, name=None, *args, **kwargs):
        super(ExperimentView, self).__init__(model, session, template, *args, **kwargs)

    column_list = ['experiment_name', 'description', 'ai_name', 'ai_params']


def get_experiment():
    experiment_view = ExperimentView(name="Experiment", endpoint='experiment', menu_icon_type='fa', menu_icon_value='fa-connectdevelop')
    return experiment_view