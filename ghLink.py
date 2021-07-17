from os import error
import subprocess
import json
import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument('file', required=True, type=click.Path(exists=True))
@click.option('--line', '-l', help='Line in file')
def permalink(file, line):
 

    line_url = ''
    url = json.loads(
        subprocess.run(['gh', 'repo', 'view', '--json', 'url'],
                       stdout=subprocess.PIPE).stdout.decode('utf-8')
        ).get('url')

    commit = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'],
                            stdout=subprocess.PIPE).stdout.decode('utf-8').strip()

   
    relative = subprocess.run(
        ['git', 'rev-parse', '--show-prefix'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
    if file.startswith('./'):
         relative += file[2:]  # Crops out the relative part of the path.
    elif file.startswith('/'):
        relative = file[1:]
    else:
        relative += file
    line_url = '{}/blob/{}/{}'.format(url, commit, relative)

    if line is not None: 
        line_url += '#{}'.format('-'.join(list(map(lambda x: 'L' + x, line.split('-')))))
    click.echo(line_url)

if __name__ == '__main__':
    cli()
