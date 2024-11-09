import json
import os.path
import traceback


def json2xml(json_obj, Line_spacing=""):
   result_list = list()
   json_obj_type = type(json_obj)
      
  
   if json_obj_type is list:
       for sub_elem in json_obj:
           result_list.append(json2xml(sub_elem, Line_spacing))
  
       return "\n".join(result_list)
   
   if json_obj_type is dict:
       for tag_name in json_obj:
           sub_obj = json_obj[tag_name]
           if(type(sub_obj)==str):
               result_list.append("<string name=\"%s\">"%(tag_name))
               result_list.append(json2xml(sub_obj, "\t" + Line_spacing))
               result_list.append("</string>") 
           elif(type(sub_obj)==int)or(type(sub_obj)==float):
               result_list.append("<number name=\"%s\">"%(tag_name))
               result_list.append(json2xml(sub_obj, "\t" + Line_spacing))
               result_list.append("</number>")
           elif(type(sub_obj)==bool):
               result_list.append("<boolean name=\"%s\">"%(tag_name))
               result_list.append(json2xml(sub_obj, "\t" + Line_spacing))
               result_list.append("</boolean>")
           elif(type(sub_obj)==list):
               result_list.append("<array name=\"%s\">"%(tag_name))
            #    result_list.append(json2xml(sub_obj, "\t" + Line_spacing))
               for i in sub_obj:
                   if type(i)==str:
                       result_list.append("<string>")
                       result_list.append(json2xml(i, "\t" + Line_spacing))
                       result_list.append("</string>")
                   if type(i)==int or type(i)==float:
                       result_list.append("<number>")
                       result_list.append(json2xml(i, "\t" + Line_spacing))
                       result_list.append("</number>")
                   if type(i)==bool:
                       result_list.append("<boolean>")
                       result_list.append(json2xml(i, "\t" + Line_spacing))
                       result_list.append("</boolean>")
                   if type(i)==dict:
                       result_list.append("<object>")
                       result_list.append(json2xml(i, "\t" + Line_spacing))
                       result_list.append("</object>")

               result_list.append("</array>")
           elif(sub_obj== None):
               result_list.append("<null name=\"%s\"/>"%(tag_name))
               result_list.append(json2xml("null", "\t" + Line_spacing))                              
           else:
               result_list.append("<object>")
               result_list.append("<object name=\"%s\">"%(tag_name))
               result_list.append(json2xml(sub_obj, "\t" + Line_spacing))
               result_list.append("</object>")
               result_list.append("</object>")
           # print(result_list)
       return "\n".join(result_list)
        
   return "%s%s" % (Line_spacing, json_obj)



json_path=input("Enter the path to the json file=")

check_file = os.path.isfile(json_path)
if(check_file==True):
    try:
        xml_path=input("Enter the path where the xml file to be stored=")
        with open(json_path)as f:
            data=json.load(f)
            xml_data=json2xml(data)
            f = open("xml1.xml", "w")
            f.write(xml_data)
            f.close()
        print("The file is successfully created")
    except Exception as e:
        print("The Json file is invalid")
else:
    print("Enter Valid Json Path")