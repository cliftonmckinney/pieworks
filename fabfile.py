from fabric.api import env
from fabric.operations import put


REMOTE_PROJECT_DIR = '/home/web/getpieworks.com'
env.hosts = ['root@getpieworks.com', ]


def upload():
    """Uploads the site content to the remote project directory."""
    put(local_path="site/*", remote_path=REMOTE_PROJECT_DIR)


def deploy():
    """Deploy the site."""
    upload()
