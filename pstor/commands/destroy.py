import os
import shutil

from ..helpers import exceptions
from . import cli_command,inside_pstor
from . import down

def args(subparsers):
    destroy = subparsers.add_parser('destroy')
    destroy.add_argument('--force', action="store_true", default=False)

@cli_command(args=args)
@inside_pstor
def destroy(**args):
    if not os.path.isdir(".pstor"):
        raise exceptions.PstorException("No pstor here")
    else:
        if not args['force']:
            raise exceptions.PstorException("Add --force to confirm")
        down.down(force=True)
        shutil.rmtree('.pstor')
        shutil.rmtree('files')
        print "DEMOLISHED"