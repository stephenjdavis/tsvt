from tableau_api_lib import TableauServerConnection
from tableau_api_lib.utils.querying import get_projects, get_project_id
from constants.constants import Paths

import configparser
import xml.etree.ElementTree as ET

def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
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
    # Rest of the Tableau workbook creation script
    # ...

    # Create a basic test results visualization (modify as needed)
    connection.workbooks.populate()
    test_results_viz = connection.workbooks.get_by_name('Test Results')

    # Create a worksheet
    new_worksheet = connection.workbooks.create_project_worksheet(test_results_viz.id, 'Test Results')

    # Create a basic test results visualization (modify as needed)
    test_results_data = [{'Test Name': test_name, 'Status': status} for test_name, status in test_results]
    view = connection.views.create(new_worksheet.id, test_results_data, 'Test Results Viz')

    # Save changes
    connection.workbooks.populate()
    connection.workbooks.refresh(test_results_viz.id)

    # Sign out
    connection.sign_out()

if __name__ == "__main__":
    # Read configuration from the config.ini file
    config = read_config()

    # Specify the path to the XML test results file
    xml_results_file = 'Paths.RESULT_DIR/test_results.xml'

    # Read and parse test results from XML file
    test_results = read_test_results(xml_results_file)

    # Create Tableau workbook and visualization
    create_tableau_workbook(config, test_results)

