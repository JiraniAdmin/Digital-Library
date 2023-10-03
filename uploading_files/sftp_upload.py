#!/usr/bin/python

# Imports: Standard Libraries
# ---------------------------
import logging      # Will be used later on when we are testing prototype
import pprint
import json
import time
from datetime import datetime, timedelta
import os
import paramiko
import requests
import sys

# Later import SQL to add PATH to SQL database

def main():
    """
    This function serves as the driver
    """
    # STEP: Prompt user for inputs
    # RESULT: Store the inputs
    # GETTING AN ERROR WHEN INPUTTING, HARDCODING FOR NOW
    print('Starting File\n\n')
    
    hostname = ''
    username = ''
    password = ''
    remote_file_path = ''
    local_dir_path = ''
    
    #hostname = input('Enter remote server hostname:\n')
    #username = input('Enter username for remoter server:\n')
    #password = input('Enter password for remote server:\n')
    #remote_file_path = input('Enter full path to file in remote server:\n')
    #local_dir_path = input('Enter fu       ll path to directory where file will be saved:\n')
    
    # STEP: Verify that local directory exists
    # RESULT: Path already exist then nothing, else create path
    if not os.path.exists(local_dir_path):
        print('\nLocal Path does not exist. Will now create the path.\n')
        os.makedirs(local_dir_path)
        
    local_file_path = os.path.join(local_dir_path, os.path.basename(remote_file_path))
    
    # STEP: Call the sftp function and pass in parameters
    # RESULT: File downloaded from remoter server
    success = sftp_get_file(hostname, username, password, remote_file_path, local_file_path)

    # STEP: Check if the file was transefered to local machine
    # RESULT:  Print the message to user
    if success:
        print('\nSuccessfully downloaded ' + remote_file_path + ' to ' + local_file_path)
    else:
        print('\nFailed to download ' + remote_file_path)


def sftp_get_file(hostname, username, password, remote_file_path, local_file_path):
    """
    This function will get a file from the remote server to the local machine

    Args:
        hostname (string): IP address or DNS of the server/raspPi
        username (string): Username for the server
        password (string): Password for user on remote server
        remote_file_path (string): Full path to the file on remote server
        local_file_path (string): Full path where file will be saved
    
    Returns:
        bool: Returns true if sftp.get was successful, otherwise false
    """
    # STEP: Start the ssh client instance, and connect to the remote server
    # RESULT: created the instance, and connected to remote server
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname, port=22, username=username, password=password)
    sftp = ssh_client.open_sftp()
    
    # STEP: Verify that file exists
    # RESULT: Continue program is file exists, else return false
    try:
        sftp.stat(remote_file_path)
    except FileNotFoundError:
        print('\nRemote file ' + remote_file_path + ' does not exist.\n')
        return False
        
    # STEP: Perform the sftp get operation
    # RESULT: Get the file if the file exists, close the sftp client
    try:
        print('\nPerforming the SFTP get operation.\n')
        sftp.get(remote_file_path, local_file_path)
        sftp.close()
        
        # Check if file was downloaded
        print('\nChecking if the file is in ' + local_file_path + '\n')
        if os.path.exists(local_file_path):
            return True
        else:
            print('\nLocal file ' + local_file_path + ' was not created.\n')
            return False
    
    # STEP: Handle errors
    # RESULT: Print the error message
    except Exception as e:
        print('Error: ' + e)
        return False
    
    # STEP: Ensure that ssh client was closed
    # RESULT: Closed ssh client
    finally:
        ssh_client.close()


if __name__ == "__main__":
    main()