import click

from lock.app import actions

@click.group()
def cli():
    '''Lock is a simple tool for the purpose of securely storing and sharing
    sensitive information.
    '''

cli.add_command(actions.add)
cli.add_command(actions.get)
