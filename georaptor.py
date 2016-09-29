#!/usr/bin/python

import time
import argparse
from clint.textui import puts, indent, colored


def read_file(filename):
    # Read file by lines into a set
    with open(filename) as f:
        geohashes = set(f.read().splitlines())

    return geohashes


# Combination generator for a given geohash at the next level
def getCombinations(string):
    base32 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'm',
              'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return [string + '{0}'.format(i) for i in base32]


# Recursive optimization of the geohash set
def compress(geohashes):
    deletegh = set()
    final_geohashes = set()
    flag = True
    final_geohashes_size = 0

    # Input size less than 32
    if len(geohashes) < 32:
        puts(colored.red(
            'Need a minimum of 32 geohashes to compress! Could read only ' + str(len(geohashes)) + '!\n'))
        return False


    while flag == True:
        final_geohashes.clear()
        deletegh.clear()

        for geohash in geohashes:

            # Get geohash to generate combinations for
            part = geohash[:-1]

            # Proceed only if not already processed
            if part not in deletegh and geohash not in deletegh:

                # Generate combinations
                combinations = set(getCombinations(part))

                # If all generated combinations exist in the input set
                if combinations.issubset(geohashes):
                    # Add part to temporary output
                    final_geohashes.add(part)
                    # Add part to deleted geohash set
                    deletegh.add(part)

                # Else add the geohash to the temp out and deleted set
                else:
                    deletegh.add(geohash)
                    final_geohashes.add(geohash)

                # Break if compressed output size same as the last iteration
                if final_geohashes_size == len(final_geohashes):
                    flag = False

        final_geohashes_size = len(final_geohashes)

        if flag == True:
            with indent(4):
                puts(colored.red('Compressed to: ' + str("{:,}".format(len(final_geohashes)))))

        geohashes.clear()

        # Temp output moved to the primary geohash set
        geohashes = geohashes.union(final_geohashes)

    return geohashes


def main():
    start_time = time.time()

    # Fetch input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='input filename containing list of geohashes')
    parser.add_argument('--output', default='output.csv', help='output filename containing a optimized list of geohashes (default: output.csv)')

    args = parser.parse_args()

    filename = args.input

    if 'output' in args:
        output_file  = args.output
    else:
        output_file = 'output.csv'

    fp = open(output_file, "a");

    puts(colored.green('\nReading the file'))

    geohashes = read_file(filename)

    puts(colored.green(str("{:,}".format(len(geohashes))) + ' geohashes read\n'))

    time.sleep(1);

    puts(colored.red('Starting compression\n'))

    georaptor_out = compress(geohashes)


    if georaptor_out != False:

        # Output to file
        for geohash in georaptor_out:
            fp.write(geohash+'\n')

        puts(colored.red('\nCompression complete!'))

        time.sleep(1)

        puts(colored.white('\nOutput available at ' + output_file + '\n'))


    et = time.time() - start_time

    puts(colored.green('Total execution time: '+str(et)+' seconds\n'))
