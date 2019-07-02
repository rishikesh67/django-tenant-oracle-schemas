import os 
import re


def check_domain(host):
    match = re.match(r'([a-zA-Z0-9]+)(\.[0-9a-zA-Z]+)?(\.[0-9a-zA-Z]{2,4})?(:\d{4})?', host)

    if match:
        return match.groups()

    return match


def is_main_domain(tup, main_domain='localhost'):
    """
    Description
    ===========

    
    `tup` can be in the following form:

        ('localhost', '.com', None, ':9000')
        ('localhost', None, None, ':9001')
        ('localhost', '.com', None, None)
        ('localhost', None, None, None)
        ('cfd', '.localhost', '.com', ':9000')
        ('nmf2', '.localhost', None, ':9001')
        ('tenant1', '.localhost', '.com', None)
        ('tenant2', '.localhost', None, None)
    """
    d = {'is_main_domain': False}

    if tup[0] == main_domain:
        d['is_main_domain'] = True
        d['domain'] = main_domain
    elif tup[1] == '.' + main_domain:
        d['subdomain'] = tup[0]
        d['is_main_domain'] = True
        d['domain'] = main_domain

    return d

def main(output_type='simple'):
    host = 'localhost'

    hosts = [
        '{host}.com:9000',
        '{host}:9001',
        '{host}.com',
        '{host}',
        'cfd.{host}.com:9000',
        'nmf2.{host}:9001',
        'tenant1.{host}.com',
        'tenant2.{host}'
    ]

    tups = [] 
    for host_str in hosts:
        host_str = host_str.format(host=host)
        tup = check_domain(host_str)
        tups.append(tup)

        if output_type == 'lbl_det':
            print("%-30s - %s" % (host_str, tup), '\n') 
        elif output_type == 'only_det': 
            print(tup)
        else:
            print(host_str)
            print(tup)

    print(tups)

    
if __name__ == "__main__":
    main('only_det')



"""
localhost.com:9000             - ('localhost', '.com', None, ':9000') 

localhost:9001                 - ('localhost', None, None, ':9001') 

localhost.com                  - ('localhost', '.com', None, None) 

localhost                      - ('localhost', None, None, None) 

cfd.localhost.com:9000         - ('cfd', '.localhost', '.com', ':9000') 

nmf2.localhost:9001            - ('nmf2', '.localhost', None, ':9001') 

tenant1.localhost.com          - ('tenant1', '.localhost', '.com', None) 

tenant2.localhost              - ('tenant2', '.localhost', None, None) 
"""
