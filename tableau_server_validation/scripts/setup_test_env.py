import os


def create_test_env():
    create_setup_structure()
    create_tsvt_ini_file()

def create_setup_structure():
    try:
        os.mkdir('tds')
    except:
        pass
    try:
        os.makedirs('../../config')
    except:
        pass

def create_tsvt_ini_file():
    try:
        ini_path = '../../config/tsvt_config.ini'
        if os.path.isfile(ini_path):
            return
    except:
        pass