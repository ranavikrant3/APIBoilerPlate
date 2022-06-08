from src.server.models.pmk_guidebookskills import GuidebookSkills
from src.server.managers.database import db
from src.server.helpers import database, generic_errors
import logging

def insert_guidebookskills(data: dict):
   guidebookskills = GuidebookSkills().from_json(data)
   db.session.add(guidebookskills)
   db.session.commit()


def select_guidebookskills(guidebookskills_id: int):
   """
       Query a guidbookskills base on the id

   @param guidebookskills_id: integer for a guidebookskill id in the Database
   @return: dictionary with all the fields of the GuidebookSkills class
   """
   guidebookskills = GuidebookSkills.query.get_or_404(guidebookskills_id)
   return guidebookskills.to_dictionary()

def select_list_guidebookskills(restful):
   """
       Query a guidbookskills base on the id

   @param guidebookskills_id: integer for a guidebookskill id in the Database
   @return: dictionary with all the fields of the GuidebookSkills class
   """
   query = GuidebookSkills.query.filter_by(**restful.filters)
   query = database.full_text_search(query, restful.q, [GuidebookSkills.GbookID, GuidebookSkills.name])
   query = query.order_by(*database.get_order_by(GuidebookSkills, restful.order_by))
   return database.get_list(query, restful.pagination)


def update_guidebookskills(guidebookskills_id: int, data: dict):
   db.session.query(GuidebookSkills).filter_by(GbookID=guidebookskills_id).update(data)
   db.session.commit()


def delete_guidebookskills(guidebookskills_id: int):
   try:
      db.session.query(GuidebookSkills).filter_by(GbookID=guidebookskills_id).delete(synchronize_session='fetch')
      db.session.commit()
   except Exception as e:
      logging.error(e)
      return generic_errors.not_found(message='not_found')



