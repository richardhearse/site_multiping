#!/usr/bin/python3


import concurrent.futures
import time
import platform
import subprocess


def ping_task(host):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    ping = ['ping', param, '2', host]
    ping_return_code = subprocess.call(ping, stdout=subprocess.DEVNULL)
    if ping_return_code == 0:
        print(host +" is up")
    else:
        print(host + " device not reachable or not in use.")

def make_hosts(site_number):
    return  [ site_number + "fqdn",


            ]

def thread_worker(hosts_list):

    with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
        for host in hosts_list:
            executor.submit(ping_task, host)

def scan():
    site_number = input("Please enter site number: ")
    thread_worker(make_hosts(site_number))


def main():
    cont = True
    while cont == True:
        scan()
        if not input('Do another scan? [Y/n]: ').lower() in ["y", "yes"]:
            cont = False

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit('\nexiting due to keyboard interrupt!')
