#!/usr/bin/python

# Imports: Standard Libraries
# ---------------------------
import pprint
import time
from datetime import datetime, timedelta
import os
import paramiko
import requests
import sys
import getpass
from src import sftp_requests
# Later import SQL to add PATH to SQL database


def main():
    """
    This function serves as the driver
    """
    # STEP: Prompt user for inputs
    # RESULT: Store the inputs
    # GETTING AN ERROR WHEN INPUTTING, HARDCODING FOR NOW
    print('Starting File\n\n')
    current_dateTime = datetime.now()
    print(current_dateTime)
    
    host = input('\nEnter remote server host(IP or DNS): ')
    username = input(f'Enter username for {host}: ')
    password = getpass.getpass('Enter password for remote server: ')
    remote_file_path = input('Enter full path to file on server: ')
    local_dir_path = '/home/jirani/Desktop'
    
    # STEP: Verify that local directory exists
    # RESULT: Path already exist then nothing, else create path
    if not os.path.exists(local_dir_path):
        print('\nLocal Path does not exist. Creating the path.\n')
        os.makedirs(local_dir_path)
        
    local_file_path = os.path.join(local_dir_path, os.path.basename(remote_file_path))
    
    # STEP: Call the sftp function and pass in parameters
    # RESULT: File downloaded from remoter server
    success = sftp_get_file(host, username, password, remote_file_path, local_file_path)

    # STEP: Check if the file was transefered to local machine
    # RESULT:  Print the message to user
    if success:
        print('\nSuccessfully downloaded ' + remote_file_path + ' to ' + local_file_path)
    else:
        print('\nFailed to download ' + remote_file_path)
