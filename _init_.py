from optparse import OptionParser
import os

def ___init___():


    path = os.path.dirname(os.path.realpath(__file__))
    help_file = [h for h in os.listdir(path) if os.path.isfile(h)]

    for f in help_file:

        if f == 'help.txt':

            with open(path +'/help.txt', 'r') as the_file:

                file_content = the_file.read()

        else:continue

    parser = OptionParser()
    parser.add_option('--version',
                          dest="version",
                          default=1.0,
                          type=float)

    parser.add_option('-o', '--output',
                      dest='help_txt',
                      default=file_content)

    (options, args) = parser.parse_args()

    #Getting inputs

    if raw_input('[>] PRESS ENTER TO CONTINUE\n\n') == '':

        try:

            parser.print_help(); print'\n'

        except OptionParser.print_help(): pass

        while 1:

            opt_input = raw_input('\n''[>]''\t')

            if opt_input == '-h': break

            if opt_input == '-v':

                print '\n'+float(options.version) +'\n'; break

            if opt_input == '-o':

                print '\n'+str(options.help_txt)+'\n'; break

            else: continue

    #To wait for input so the options output isn't cleared.
    raw_input('')


