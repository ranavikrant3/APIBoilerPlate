from src.server.managers.database import db
import datetime


class GuidebookSkills(db.Model):

   __tablename__ = 'GuidebookSkills'

   GbookID = db.Column(db.Integer, primary_key=True, autoincrement=True)
   name = db.Column(db.String(100), nullable=True)
   description = db.Column(db.Text, nullable=True)
   work_center_id = db.Column(db.BigInteger, nullable=True)
   category_id = db.Column(db.BigInteger, nullable=True)
   erp_part_number = db.Column(db.String(100), nullable=True)
   is_template = db.Column(db.Float, nullable=True)
   status = db.Column(db.String(10), nullable=True)
   last_version_num = db.Column(db.String(20), nullable=True)
   last_version_id = db.Column(db.Integer, nullable=True)
   SkillsGroups = db.Column(db.Text, nullable=True)

   def from_json(self, json: dict):
       print(json)
       """
           Convert a dictionary to a GuidebookSkills

       @param json: dictionary with the GuidebookSkills columns
       @return: dictionary with all the input values
       """
       self.GbookID = json.get('GbookID', None)
       self.name = json.get('name', None)
       self.description = json.get('description', None)
       self.work_center_id = json.get('work_center_id', None)
       self.erp_part_number = json.get('erp_part_number', None)
       self.category_id = json.get('category_id', None)
       self.is_template = json.get('is_template', None)
       self.status = json.get('status', None)
       self.last_version_num = json.get('last_version_num', None)
       self.last_version_id = json.get('last_version_id', None)
       self.SkillsGroups = json.get('SkillsGroups', None)
       return self

   def to_dictionary(self):
       """
           Convert a Pick List to a dictionary

       @return: dictionary with all the GuidebookSkills fields
       """
       data = {
           'GbookID': self.GbookID,
           'name': self.name,
           'description': self.description,
           'work_center_id': self.work_center_id,
           'category_id': self.category_id,
           'erp_part_number': self.erp_part_number,
           'is_template': self.is_template,
           'status': self.status,
           'last_version_num': self.last_version_num,
           'last_version_id': self.last_version_id,
           'SkillsGroups': self.SkillsGroups
       }
       return data
