import click
from chef_helpers import utils
from chef_helpers import api

@click.group()
def cli():
	if utils.check_if_initialized():
		if utils.check_if_token_expired():
			api.refresh_oauth2_token()

@cli.command()
def init():
	"""Get and store tokens for api calls."""
	if utils.check_if_initialized():
		click.echo('You have already initialized the application.')
		click.echo('Please run \"chef reinit\" to reinitialize the application.')
	else:
		api.new_oauth2_token()

@cli.command()
def contests():
	api.get_contests_list()