from tableau_api_lib import TableauServerConnection
from tableau_api_lib.utils.querying import get_projects, get_project_id
from constants.constants import REPORTS_DIR, XML_DIR, LOGS_DIR

import configparser
import xml.etree.ElementTree as ET

def read_config():
    config = configparser.ConfigParser()
    config.read('tsvt_config.ini')
    return config

def read_test_results(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    # Parse XML and extract test results data
    # Modify this part based on your XML structure and data
    test_results = []
    for test_case in root.iter('testcase'):
        test_name = test_case.attrib['name']
        status = "Passed" if test_case.find('failure') is None else "Failed"
        test_results.append((test_name, status))
    return test_results

def create_tableau_workbook(config, test_results):
    # Replace the following placeholders with actual Tableau Server connection details
    server = config.get('TableauServer', 'server')
    username = config.get('TableauServer', 'username')
    password = config.get('TableauServer', 'password')
    site = config.get('TableauServer', 'site')

    # Initialize Tableau Server connection
    connection = TableauServerConnection(server, username, password, site=site)
    connection.sign_in()

    # Placeholder: Create a new Tableau workbook
    workbook_name = "Test_Results_Workbook"
    project_name = "Your_Project_Name"

    # Check if the project exists, if not, create it
    projects = get_projects(connection)
    project_id = get_project_id(projects, project_name)
    if not project_id:
        project_id = connection.projects.create(project_name)['id']

    # Placeholder: Create a new workbook in the specified project
    new_workbook = connection.workbooks.create(workbook_name, project_id)

    # Placeholder: Create a new worksheet in the workbook
    new_worksheet = connection.workbooks.create_project_worksheet(new_workbook.id, 'Test_Results')

    # Placeholder: Create a view with test results data
    test_results_data = [{'Test Name': test_name, 'Status': status} for test_name, status in test_results]
    view = connection.views.create(new_worksheet.id, test_results_data, 'Test_Results_Viz')

    # Placeholder: Save changes and refresh the workbook
    connection.workbooks.populate()
    connection.workbooks.refresh(new_workbook.id)

    # Placeholder: Sign out
    connection.sign_out()

if __name__ == "__main__":
    # Read configuration from the tsvt_config.ini file
    config = read_config()

    # Specify the path to the XML test results file
    xml_results_file = REPORTS_DIR + '/test_results.xml'

    # Read and parse test results from XML file
    test_results = read_test_results(xml_results_file)

    # Create Tableau workbook and visualization
    create_tableau_workbook(config, test_results)
