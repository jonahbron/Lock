@click.group()
def cli():
    pass

@click.command()
def add():
    click.echo('Added one')

@click.command()
def get():
    click.echo('Got one')

cli.add_command(get)
cli.add_command(add)