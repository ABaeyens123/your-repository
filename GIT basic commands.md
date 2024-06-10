# GIT basic commands

# Setting up a local repo
Move one folder up: cd ..
make a new directory: mkdir my-git-repo
move to a directory: cd my-git-repo
initialize git repo: git innit

# Creating a new file
Create file: echo "TEXT" > README.md
commit the file: git commit -m "COMMENT"

# Creating a new branch
Create new branch: git checkout -b new-feature
add changes: git add.
commit changes: git commit -m "COMMENT"
switch back to main: git checkout main
merge new branch to main: git merge new-feature

# Pushing to GitHub
Link to github repo: git remote add origin git@github.com:username/my-git-repo.git
