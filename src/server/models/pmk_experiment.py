from src.server.managers.database import db
from datetime import datetime
import json
from src.server.helpers.serialize import get_json_clean_response


class Experiment(db.Model):
    """
        The Experiment object allow the software to store the AI experiment
        The reference table in the databse is pmk_experiment
    """

    __tablename__ = 'pmk_experiment'

    id = db.Column(db.Integer, primary_key=True)
    updated_on = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    experiment_name = db.Column(db.String(140))
    description = db.Column(db.String(255), nullable=True)
    ai_name = db.Column(db.String(255), nullable=True)
    ai_params  = db.Column(db.String(255), nullable=True)

    def from_json(self, json : dict):
        """
            Convert a dictionary to a Experiment

        @param json: dictionary with the Experiment columns
        @return: dictionary with all the input values
        """

        self.updated_on = json.get('updated_on', None)
        self.experiment_name = json.get('experiment_name', None)
        self.description = json.get('description', None)
        self.ai_name = json.get('ai_name', None)
        self.ai_params = json.get('ai_params', None)
        return self


    def to_dictionary(self):
        """
            Convert a Experiment to a dictionary

        @return: dictionary with all the experiment fields
        """
        data = {
            'experiment_id': self.id,
            'updated_on': self.updated_on,
            'experiment_name': self.experiment_name,
            'description': self.description,
            'ai_name': self.ai_name,
            'ai_param': self.ai_params
        }
        return data
