from flask import request
from src.server.handlers.database.pmk_guidebookskills import select_guidebookskills, insert_guidebookskills, select_list_guidebookskills, delete_guidebookskills, update_guidebookskills

def create_guidebookskills():
   data = request.json
   return insert_guidebookskills(data)

def get_guidebookskills(guidebookskills_id):
   return select_guidebookskills(guidebookskills_id)

def get_guidebookskills_list():
   return select_list_guidebookskills(request.restful)

def remove_guidebookskills(guidebookskills_id):
   return delete_guidebookskills(guidebookskills_id)

def edit_guidebookskills(guidebookskills_id):
   data = request.json
   return update_guidebookskills(guidebookskills_id, data)