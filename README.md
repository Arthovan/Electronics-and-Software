# Author - Arun Parkugan
## Please dont change the content until unless necessary.Entire content is for learning purpose only.
## Feel free to download and use it on your own
### command used in local for pushing the content
1.	Open Git Bash.
2.	Navigate to the root directory of your project.
3.	Initialize the local directory as a Git repository. By default, the initial branch is called main.
	(If you’re using Git 2.28.0 or a later version, you can set the name of the default branch using -b.)
====>>> git init -b main
	(If you’re using Git 2.27.1 or an earlier version, you can set the name of the default branch using git symbolic-ref.)
====>>> git init && git symbolic-ref HEAD refs/heads/main
4.	Add the files in your new local repository. This stages them for the first commit.
====>>> git add .
	(Adds the files in the local repository and stages them for commit. To unstage a file, use 'git reset HEAD YOUR-FILE'.)
5.	Commit the files that you've staged in your local repository.
	(Refer this to give good commit message : https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/ )
====>>> git commit -m "docs: added the GIT versin control system folder and generic README.md"
	(# Commits the tracked changes and prepares them to be pushed to a remote repository. To remove this commit and modify the file, use 'git reset --soft HEAD~1' and commit and add the file again.)
6.	To add the URL for the remote repository where your local repository will be pushed, run the following command. 
	(Replace REMOTE-URL with the repository's full URL on GitHub. My remote url is : https://github.com/Arthovan/Electronics-and-Software.git )
====>>> git remote add origin REMOTE-URL
7.	To verify that you set the remote URL correctly, run the following command.)
====>>> git remote -v
8.	To push the changes in your local repository to GitHub, run the following command.
====>>> git push origin main
	(If your default branch is not named "main," replace "main" with the name of your default branch.)
