import os
import sys
import sh

from ..helpers import exceptions, pstor
from . import cli_command,inside_pstor
from .providers import get_remote_by_name

def args(subparsers):
    subparsers.add_parser('down')

@cli_command(args=args)
@inside_pstor
def down(**args):
    if not pstor.mounted():
        raise exceptions.PstorException("Already down")

    print "EncFS... ",
    sys.stdout.flush()
    sh.fusermount('-u', 'files')
    print "DOWN"

    for remote in os.listdir('.pstor/remotes'):
        remote = get_remote_by_name(remote)
        print remote.name() + "... ",
        sys.stdout.flush()
        remote.down()
        print "DOWN"