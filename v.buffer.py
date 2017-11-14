#!/usr/bin/env python
#
########################################################################
#
# MODULE:       v.buffer
# AUTHOR:       Ryan Molumby
# PURPOSE:      Buffer
# COPYRIGHT:    (C) 2017 Ryan Molumby
#               This program is free software under the GNU General
#               Public License (>=v2). Read the file COPYING that
#               comes with GRASS for details.
#
########################################################################

#%module
#% description: Adds a buffer to a stream
#% keyword: vector
#%end
#%option G_OPT_V_MAP
#% key: avector
#%end
#%option G_OPT_V_OUTPUT
#%end

import sys
import os
import atexit

import grass.script as gscript 


def main():
    options, flags = gscript.parser()
    avector = options['avector']
    output = options['output']

    gscript.run_command('v.buffer', input=avector, output=output, distance=500, overwrite=True)



    return 0

if __name__ == "__main__":
     sys.exit(main())
