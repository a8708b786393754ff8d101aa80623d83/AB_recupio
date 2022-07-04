import argparse

def args(): 
    arg = argparse.ArgumentParser()
    
    arg.add_argument('-f', '--file', type=str)
    arg.add_argument('-d', '--folder', type=str)
    
    return arg.parse_args()
