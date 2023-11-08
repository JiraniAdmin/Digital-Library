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
import getpass
# import our database once it has been created


def sftp_get_file(host, username, password, remote_file_path, local_file_path):
    """
    This function will get a file from the remote server to the local machine

    Args:
        host (string): IP address or DNS of the server/computer where book is
        username (string): Username for the server
        password (string): Password for user on server
        remote_file_path (string): Full path to the file on server
        local_file_path (string): Full path where file will be saved
    
    Returns:
        bool: Returns true if sftp.get was successful, otherwise false
    """
    # STEP: Start the ssh client instance, and connect to the remote server
    # RESULT: created the instance, and connected to remote server
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(host, port=22, username=username, password=password)
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
    except Exception as err:
        print('Error: ' + err)
        return False
    
    # STEP: Ensure that ssh client was closed
    # RESULT: Closed ssh client
    finally:
        ssh_client.close()


if __name__ == "__main__":
    main()
