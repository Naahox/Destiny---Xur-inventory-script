import os, logging

#Dictionary for logging levels along with there "ranking" number.
log_levels_message = {

    'debug'        :      int(10),
    'info'         :      int(20),
    'warning'      :      int(30),
    'error'        :      int(40),
    'critical'     :      int(50)
}

try:

    from optparse import OptionParser

except ImportError as e:

    print logging.getLevelName(log_levels_message[str('critical')])
    print '\n\n[!!] Can not import OptionParser.'

try:

    import argparse

except ImportError as e:

    print logging.getLevelName(log_levels_message[str('critical')])
    print '\n\n[!!] Can not import argparse.'





def options():

    #So here i just created a little dictionary with some info...author and contact.

    information = {

        'author'     :  str('Naahox'),
        'contact'    :  str('Call Me Knox')
    }

    INFO = 'This is a parser file! \n\t\n' \
           'This file is only used for the users benefit.\n' \
           'The removal of this file will cause the script to fail, ' \
           'so be careful.' \
           '\nFor any additional information contact author > {0} < at the xbox GT ' \
           '> {1} <.'.format(information['author'], information['contact'])

    print INFO


    usage = 'usage %prog [options] arg1 arg2'

    parser = OptionParser(usage=usage)

    path = os.path.dirname(os.path.realpath(__file__))
    help_file = [h for h in os.listdir(path) if os.path.isfile(h)]

    for f in help_file:

        if f == 'help.txt':

            with open(path +'/help.txt', 'r') as the_file:

                file_content = the_file.read()

        else:

            continue

    parser.add_option('-f', '--output', dest='help_txt', default=file_content, help='Print help.txt file content')
    parser.add_option('-v', '--version', dest="version", default=1.0, type=float)
    (options, args) = parser.parse_args()



    """
    I don't like the standard output for parser.print_help(), so i made a very simple straight forward option
    output.
    """


    CLI_args = """
    -f      Print help file content

    -v      Version

    -?      Any key to exit/continue
    """

    print CLI_args

    args = raw_input('\n[>] Enter an option:\t')

    if args == '-f':

        print '\n\n'+str(options.help_txt)


    if args == '-v':

        print '\n\n'+str(options.version)

    raw_input()









options()


