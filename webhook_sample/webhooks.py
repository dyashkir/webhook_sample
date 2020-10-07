import hmac
from flask import request, Blueprint, jsonify, current_app 
from git import Repo

webhook = Blueprint('webhook', __name__, url_prefix='')
import subprocess
import sys


def run_command(command, directory):
    result = subprocess.run(command.split(' '), capture_output=True)
    return result
#yoyo apply --database=sqlite:///instance/csapi.sqlite csapi/migrations
#gunicorn "csapi.app:create_app()" -c gunicorn.conf.py --daemon

target_dir = '.'
#start-stop-daemon --stop gunicorn
on_push_commands ='''pip install -r requirements.txt
        ls -l'''

@webhook.route('/github', methods=['POST']) 
def handle_github_hook(): 
    signature = request.headers.get('X-Hub-Signature') 
    #sha, signature = signature.split('=')

    #secret = str.encode(current_app.config.get('GITHUB_SECRET'))

    for c in on_push_commands.split('\n'):
        print(f'COMMAND {c}')
        r = run_command(c, target_dir)
        print(r)

    #hashhex = hmac.new(secret, request.data, digestmod='sha1').hexdigest()
    if False and hmac.compare_digest(hashhex, signature): 
        repo = Repo(current_app.config.get('REPO_PATH')) 
        origin = repo.remotes.origin 
        origin.pull('--rebase')

        commit = request.json['after'][0:6]
        print('Repository updated with commit {}'.format(commit))
    return jsonify({}), 200
