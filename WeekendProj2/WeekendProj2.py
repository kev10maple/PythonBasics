import logging
import pandas as pd
import os
import re
import matplotlib.pyplot as plt

STATES = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL',
          'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE',
          'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC',
          'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'VI', 'WA', 'WV', 'WI', 'WY']

logging.basicConfig(filename = 'results.log', level = logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")

def get_sorted_files():
    files = []

    try:
        files = os.listdir('data/')
        logging.info("Successfully accessed data directory")
    except:
        logging.error("Unable to access data directory")

    try:
        files = list(filter(lambda x : re.match(r"NYL_FieldAgent_[0-9]{8}.csv", x) != None, files))
        logging.info("Successfully filtered data directory")
    except:
        logging.warning("Unable to filter data directory")

    try:
        files = sorted(files, reverse = True)
        logging.info("Successfully sorted filenames")
    except:
        logging.warning("Unable to sort the filenames")

    return files

def create_reference_list():

    with open('NYL.lst', 'w') as file:
        pass

def check_files(filename):

    reference_file = 'NYL.lst'
    finished_files = []

    try:
        with open(reference_file, 'r') as f:
            logging.info(f"Successfully opened {reference_file}")
            
            try:
                finished_files = f.read().split('\n')
                print(finished_files)
                logging.info(f"Successfully read from {reference_file}")
          
            except:
                logging.error(f"The {reference_file} is empty")
    except:
        logging.error(f"Unable to read {reference_file} since empty")

    if filename in finished_files:
        logging.info(f"The file {filename} has already been processed")

def process_file(filename):
    reference_file = 'NYL.lst'

    try:
        check_files(filename)
    except:
        logging.error(f"Unable to check if {filename} is already processed")

    try:
        file = open(reference_file, 'w')
        logging.info(f"Successfully opened {reference_file} for writing")
    except:
        logging.error(f"Unable to open {reference_file} for writing")

    try:
        file.write(filename + '\n')
        logging.info(f"Successfully wrote to {reference_file}")
    except:
        logging.error(f"Unable to write to {reference_file}")

    file.close()

def get_line_count(f):

    real_path = os.path.join('data/', f)
    print(real_path)

    try:
        df = pd.read_csv(real_path)
        logging.info(f"Successfully read {f} as csv")
    except:
        logging.error(f"Could not read {f} as csv")

    num_lines = len(df.index)

    if num_lines < 0:
        logging.error(f"There are no lines in {f}")

    print(num_lines)
    return num_lines


def check_variance(files):
    accepted = 500

    if len(files) >= 2:
        latest_file = files[0]
        second_latest_file = files[1]
        lines_latest = get_line_count(latest_file)
        lines_second_latest = get_line_count(second_latest_file)

        difference = abs(lines_latest - lines_second_latest)

        if difference <= accepted:
            logging.info(f"Successfully passed variance check of {accepted}")
        else:
            logging.error(f"Failed the variance check of {accepted}")

    elif len(files) == 1:
        pass
    else:
        logging.error("No files available to check for variance")

def replace_headers(f):

    real_path = os.path.join('data/', f)
    try:
        df = pd.read_csv(real_path)
        logging.info(f"Successfully read csv to replace headers for {f}")
    except:
        logging.error(f"Could not read csv to replace headers for {f}")

    try:
        df.rename(columns={
            "Agent Writing Contract Start Date (Carrier appointment start date)": 'Agent Writing Contract Start Date',
            "Agent Writing Contract Status (actually active and cancelled\'s should come in two different files)": 'Agent Writing Contract Status'
        })
        logging.info(f"Successfully replaced headers for {f}")
    except:
        logging.error(f"Unable to replace headers for {f}")

    return df

def is_valid_phone(number):

    if re.match(r'[0-9]{3}.[0-9]{3}.[0-9]{4}', number):
        return True
    
    return False

def log_valid_phone(df):

    try:
        col = 'Agency Phone Number'
        agency_nums = df[col]

        for row, number in agency_nums.items():
            if not is_valid_phone(number):
                line = row + 2
                logging.info(f"Invalid {col} at line {line}")
    except:
        logging.error(f"Unable to find column {col}")

    try:
        col = 'Agent Phone Number'
        agent_nums = df[col]

        for row, number in agent_nums.items():
            if not is_valid_phone(number):
                line = row + 2
                logging.info(f"Invalid {col} at line {line}")
    except:
        logging.error(f"Unable to find column {col}")

def is_valid_state(state):

    if state in STATES:
        return True

    return False

def log_valid_state(df):

    try:
        col = 'Agency State'
        agency_states = df[col]

        for row, state in agency_states.items():
            if not is_valid_state(state):
                line = row + 2
                logging.info(f"Invalid {col} at line {line}")
    except:
        logging.error(f"Unable to find column {col}")

    try:
        col = 'Agent State'
        agent_states = df[col]

        for row, state in agent_states.items():
            if not is_valid_state(state):
                line = row + 2
                logging.info(f"Invalid {col} at line {line}")
    except:
        logging.error(f"Unable to find column {col}")

def is_valid_email(e):

    if re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', e):
        return True

    return False

def log_valid_email(df):

    try:
        col = 'Agent Email Address'
        agent_emails = df[col]

        for row, email in agent_emails.items():
            if not is_valid_email(email):
                line = row + 2
                logging.info(f"Invalid {col} at line {line}")
    except:
        logging.error(f"Unable to find column {col}")

def agency_state_display(df):

    try:
        col = 'Agency State'
        new_df = df.set_index([col]).sort_index()
        logging.info(f"Agency State Dataframe:\n {new_df}")
    except:
        logging.error(f"Unable to group all the agents by {col}")

    return new_df

def agent_display(df):

    try:
        cols = ['Agent First Name', 'Agent Writing Contract Start Date', 'Date when an agent became A2O']
        new_df = df[cols]
        logging.info(f"Agent Dataframe:\n {new_df}")
    except:
        logging.error(f"Unable to group all the agents by {cols}")

    return new_df

def create_visualization(df, filepath):
    data = df[['Agency State', 'Agent Id']].groupby('Agency State').agg('count')

    fig = plt.figure(figsize = (20, 8))
    states = list(data.index)
    num = list(data['Agent Id'].values)
    plt.plot(states, num)
    fig.suptitle('Data Visualization for Dataframe')
    plt.xlabel('States', fontsize = 18)
    plt.ylabel('Number of Agents', fontsize = 16)
    plt.savefig(os.path.join('figures/', filepath))
    logging.info("Saved Graph")
    plt.clf()

def main():

    files = get_sorted_files()
    print(files)
    if not os.path.exists('NYL.lst'):
        create_reference_list
    
    try:
        process_file(files[0])
    except:
        logging.error("Was unable to process the file")

    try:
        check_variance(files)
    except:
        logging.error("Unable to check for variance")

    df = replace_headers(files[0])
    log_valid_phone(df)
    log_valid_state(df)
    log_valid_email(df)

    logging.info(f"Dataframe Display:\n {df}")
    agency_df = agency_state_display(df)
    agent_df = agent_display(df)

    figure_path = 'Agent_Count.png'
    create_visualization(df, figure_path)

if __name__ == "__main__":
    main()