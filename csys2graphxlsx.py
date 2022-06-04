from config_rm import *
from redminelib import Redmine
import argparse                     # This library allows us to easily parse the command line arguments
# Importing test configuration file
import config
import os
from pyexcel_xlsx import save_data
from collections import OrderedDict
from pathlib import Path

######### WE WILL PARSE THE COMMAND LINE ARGUMENTS FOR THE WRAPPER GEN #############
parser = argparse.ArgumentParser(description='Launches a cosmoSys graph generation XLSX from an cosmosys project so it can be imported to yEd to create a graph')

## The second argument is the api ODS file
parser.add_argument('prj_ident', help="the identifier of the cosmoSys project")

# Obtaining the arguments from the command line
args=parser.parse_args()

# Printing the obtained arguments:
print("/* The cosmoSys project identifier is:",args.prj_ident+" */")
prjName = args.prj_ident
print("Project name:",prjName)

import requests as req
prcfdict = {}
cfdict = {}
rmissues = {}
from redminelib import Redmine

if ignore_cert:
    redmine = Redmine(rm_server_url,key=rm_key_txt, requests={'verify': False})
else:
    redmine = Redmine(rm_server_url,key=rm_key_txt)

projects = redmine.project.all()

nodestable = []
edgestable = []
rm_issues_dict = {}
chapters_list = []

#################### PARAMETERS TO TUNE ############################
include_chapters = True
onlyblocks = True

def print_subprojects(p):
    global projects
    for cp in projects:
        if hasattr(cp,'parent'):
            if cp.parent.id == p.id:
                print(cp.name,"->",p.name)
                print_subprojects(cp)

def scan_project(p):
    global nodestable, edgestable, rm_issues_dict,projects,include_chapters,chapters_list

    for i in p.issues:
        i_ident = i.custom_fields.get(cfdict['csID'].id).value
        if hasattr(i,'parent') and (i.parent is not None):
            parent = redmine.issue.get(i.parent.id)
            parent_ident = parent.custom_fields.get(cfdict['csID'].id).value
            chapters_list += parent_ident

        else:
            parent_ident = ""

        rm_issues_dict[i_ident] = i
        if hasattr(i,'description'):
            idescription = i.description

        else:
            idescription = ""
        
        nodestable += [[i_ident,i.subject,parent_ident,str(i.id),rm_server_url+'/issues/'+str(i.id),i.tracker.name,idescription,i.status.name]]
        for r in i.relations:
            if (not onlyblocks) or (r.relation_type == "blocks"):
                if r.issue_id == i.id:
                    dst = redmine.issue.get(r.issue_to_id)
                    dst_ident = dst.custom_fields.get(cfdict['csID'].id).value
                    if (not onlyblocks) and (hasattr(r,'delay')):
                        rdelay = str(r.delay)
                    
                    else:
                        rdelay = ""

                    edgestable += [[i_ident,dst_ident,r.relation_type,rdelay]]

    for cp in projects:
        if hasattr(cp,'parent'):
            if cp.parent.id == p.id:
                print(cp.name,"->",p.name)
                scan_project(cp)

print("Proyectos:",len(projects))
continueProcess = False
for p in projects:
    print("\t",p.identifier," \t| ",p.name)
    if p.identifier == prjName:
        continueProcess = True

if continueProcess:
    continueProcess = False
    my_project = redmine.project.get(prjName)
    if my_project is None:
        print("No podemos obtener el proyecto")
    else:
        print ("Obtenemos proyecto: ",my_project.identifier," | ",my_project.name)

    # Now we obtain the csCode
    for cf in my_project.custom_fields:
        print(cf)
        prcfdict[cf.name] = cf
        if cf.name == "csCode":
            file_cscode = cf.value
            print("csCode:",file_cscode)

    cfields = redmine.custom_field.all()
    for cf in cfields:
        cfdict[cf.name] = cf
        print(cf.name)

    print_subprojects(my_project)


    scan_project(my_project)

    data = OrderedDict() # from collections import OrderedDict

    print(nodestable)
    print("**************************")

    if include_chapters:
        finalnodestable = nodestable
        finaledgestable = edgestable

    else:
        finalnodestable = []
        finaledgestable = []

        for n in nodestable:
            n[2] = ""
            if n[0] not in chapters_list:
                finalnodestable += [n]

        for e in edgestable:
            if e[0] not in chapters_list and e[1] not in chapters_list:
                if e[0] in rm_issues_dict.keys() and e[1] in rm_issues_dict.keys():
                    finaledgestable += [e]


    data.update({"Nodes": [['csID','subject','parentID','rmid','URL','tracker','description','status']]+finalnodestable})
    data.update({"Edges": [['src','dst','type','delay']]+finaledgestable})




    print(data)

    # Saving the information into the ODS file
    onlyname = prjName
    dirname = os.path.dirname('.')
    odsextension = ".xlsx"

    save_data(os.path.join(dirname,onlyname+odsextension), data)

