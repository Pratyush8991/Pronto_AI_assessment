import git
import datetime
import argparse
import os

def git_status(git_dir):
    repo = git.Repo(git_dir)
    head_commit = repo.head.commit
    branch = repo.active_branch

    active_branch = branch.is_active()
    modified = repo.is_dirty()
    last_week = (datetime.datetime.now() - head_commit.authored_datetime) < datetime.timedelta(weeks=1)

    authored_by_rufus = head_commit.author.name == "Rufus"

    print("active branch: ", active_branch)
    print("local changes: ", modified)
    print("recent commit: ", last_week)
    print("blame Rufus: ", authored_by_rufus)

# the part below is to get the input from the user and check if it is valid or not
parser = argparse.ArgumentParser(description='Get git status')
parser.add_argument('git_dir', metavar='git_dir', type=str,
                   help='directory of the local git repository')

args = parser.parse_args()
if os.path.isdir(args.git_dir):
    git_status(args.git_dir)
else:
    print(args.git_dir, "Not a valid directory.")
