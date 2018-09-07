import click
from chef_helpers import utils
from chef_helpers import api

@click.group()
def cli():
    pass

@cli.command()
def init():
    if utils.check_if_initialized():
        click.echo('You have already initialized the application.')
        click.echo('Please run \"chef reinit\" to reinitialize the application.')
    else:
        api.new_oauth2_token()