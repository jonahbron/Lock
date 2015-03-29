import click

@click.command()
def add():
    '''Adds a new set of credentials to the secure storage'''
    click.echo('Added one')

@click.command()
def get():
    '''Retrieves an encrypted credential set'''
    click.echo('Got one')
