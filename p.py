# This code sample uses the 'requests' library:
# http://docs.python-requests.org

import requests
from requests.auth import HTTPBasicAuth
import json


url = "https://vvchow.atlassian.net/rest/api/3/user"

auth = HTTPBasicAuth("vvchow124@gmail.com", "ATATT3xFfGF0x5mDGxMCEzF6qStK1KhkimbkbGne9OGn2sZ8JPbGirYkVSH_Oc2KkbULylJ909qYjTevdoqVsyx96HYr3p4zW1lzrbPtYNT5dVs7DnDnLxFrMI42Ib8gY5Ezlo6WFhsgl769LWQCzYQnumLt0c8qRbqcH-sUy7oAnDr29D9C4kU=7AE30CBD")

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

response = requests.request(
  "GET",
   url,
   headers=headers,
   auth=auth
)
print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))



# def create_or_update(project_name, op):
#     assigneeType = st.text_input("assigneeType")
#     description = st.text_input("description")
#     key = st.text_input("key")
#     name = project_name if op == "POST" else st.text_input("name")
#     url = st.text_input("URL")
#     clicked = st.button("ENTER", key=123)
#     payload = {}
#     if clicked:
#         payload = json.dumps({
#             "assigneeType": assigneeType if assigneeType != "" else "PROJECT_LEAD",
#             "avatarId": 10200,
#             "categoryId": 10120,
#             "description": description if description != "" else "Cloud migration initiative",
#             "issueSecurityScheme": 10001,
#             "key": key if key != "" else "EX",
#             "leadAccountId": "5b10a0effa615349cb016cd8",
#             "name": name if name != "" else "Example",
#             "notificationScheme": 10021,
#             "permissionScheme": 10011,
#             "projectTemplateKey": "com.atlassian.jira-core-project-templates:jira-core-simplified-process-control",
#             "projectTypeKey": "business",
#             "url": url if url != "" else "http://atlassian.com"
#         })

#     return payload

# def create_or_update(project_name, op):
#     payload = json.dumps( {
#         "assigneeType": "PROJECT_LEAD",
#         "avatarId": 10200,
#         "categoryId": 10120,
#         "description": "Cloud migration initiative",
#         "issueSecurityScheme": 10001,
#         "key": project_name,
#         "leadAccountId": "5b10a0effa615349cb016cd8",
#         "name": "Example",
#         "notificationScheme": 10021,
#         "permissionScheme": 10011,
#         "url": "http://atlassian.com"
#     } )
#     return payload

    # assigneeType = st.text_input("assigneeType")
    # description = st.text_input("description")
    # key = st.text_input("key")
    # name = project_name if op == "POST" else st.text_input("name")
    # url = st.text_input("URL")
    # clicked = st.button("ENTER", key=123)
    # payload = {}
    # if clicked:
    #     payload = json.dumps( {
    #         "assigneeType": assigneeType if assigneeType != "" else "PROJECT_LEAD",
    #         "avatarId": 10200,
    #         "categoryId": 10120,
    #         "description": description if description != "" else "Cloud migration initiative",
    #         "issueSecurityScheme": 10001,
    #         "key": key if key != "" else "EX",
    #         "leadAccountId": "5b10a0effa615349cb016cd8",
    #         "name": name if name != "" else "Example",
    #         "notificationScheme": 10021,
    #         "permissionScheme": 10011,
    #         "projectTemplateKey": "com.atlassian.jira-core-project-templates:jira-core-simplified-process-control",
    #         "projectTypeKey": "business",
    #         "url": url if url != "" else "http://atlassian.com"
    #     } )

    # return payload    
        
