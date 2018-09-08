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
	active_contests = api.get_active_contests_list()

@cli.command()
def rankings():
	active_contests = api.get_active_contests_list()
	index = 0
	idx_max = len(active_contests)-1

	for contest in active_contests:
		click.echo(str(index) + '. ' + contest['name'] + ' ('+ contest['code'] + ')')
		index += 1
	
	contest_no = click.prompt('Please enter a valid integer between 0 and '+str(idx_max), type=int)
	
	while contest_no > idx_max:
		contest_no = click.prompt('Please enter a valid integer', type=int)
	
	rankings = api.get_contest_rankings(active_contests[contest_no])