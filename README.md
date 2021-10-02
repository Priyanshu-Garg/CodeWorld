# 🚀 Welcome To CODEWORLD! 🚀
![Screenshot 2021-09-29 at 12 29 41 AM](https://user-images.githubusercontent.com/29686102/135149193-d87a9188-6b54-4839-80dd-48d2a4983a80.png)

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

### This repository aims to help code beginners with their first successful pull request and open source contribution. 🍾

😃 Feel free to use this project to make your first contribution to an open-source project on GitHub. Practice making your first pull request to a public repository before doing the real thing!

### This repository is open to all members of the GitHub community. Any member can contribute to this project! :grin:

## What is Hacktoberfest? :thinking:
Hacktoberfest — brought to you by [DigitalOcean](https://hacktoberfest.digitalocean.com/) in partnership with [GitHub](https://github.blog/2017-09-27-celebrate-open-source-this-october-with-hacktoberfest/) and [Intel](https://www.intel.in/) — is a month-long celebration of open source software. Maintainers are invited to guide would-be contributors towards resolving issues that will help move the project forward, and contributors get the opportunity to give back to both projects they like, and ones they've just discovered. **No contribution is too small** — bug fixes and documentation updates are valid ways of participating. Celebrated every month of October based on the German festivity Oktoberfest.

Hacktoberfest is *open to everyone* in the global community. Whether you’re a developer, student learning to code, event host, or company of any size, you can help drive growth of open source and make positive contributions to an [ever-growing community](https://github.com/open-source). 

Visit the official website of [Hacktoberfest] (https://hacktoberfest.digitalocean.com/).

## Rules :fire:
To qualify for the __official limited edition Hacktoberfest shirt__, you must register [here](https://hacktoberfest.digitalocean.com/) and make four Pull Requests (PRs) between October 1-31, 2021 (in any time zone). PRs can be made to any public repo on GitHub, not only the ones with issues labeled Hacktoberfest. This year, the __first 50,000__ participants who complete the challenge will earn a T-shirt.

## How To Contribute ❓

Add any programming question and its solution in their respective Language folder and make your way to Open Source.

:star: The file structure will be as follows:

```
<source code language>/
├── <solution> (Solution file in any language including C/Java/Python etc.)
```

## Steps to follow :scroll:

### 0. Star The Repo :star2:

Star the repo by pressing the topmost-right button to start your wonderful journey.


### 1. Fork it :fork_and_knife:

You can get your own fork/copy of [CodeWorld](https://github.com/Priyanshu-Garg/CodeWorld) by using the <a href="https://github.com/Priyanshu-Garg/CodeWorld/new/master?readme=1#fork-destination-box"><kbd><b>Fork</b></kbd></a> button or clicking [this](https://github.com/Priyanshu-Garg/CodeWorld/new/master?readme=1#fork-destination-box) at top-right of your screen.

 [![Fork Button](https://help.github.com/assets/images/help/repository/fork_button.jpg)](https://github.com/Priyanshu-Garg/CodeWorld)


### 2. Clone it :busts_in_silhouette:

`NOTE: commands are to be executed on Linux, Mac, and Windows(using Powershell)`

You need to clone (download) it to local machine using

```sh
$ git clone https://github.com/Your_Username/CodeWorld.git
```

> This makes a local copy of the repository in your machine.

Once you have cloned the `CodeWorld` repository in Github, move to that folder first using change directory command on Linux, Mac, and Windows(PowerShell to be used).

```sh
# This will change directory to a folder CodeWorld
$ cd CodeWorld
```

Move to this folder for all other commands.

### 3. Set it up :arrow_up:

Run the following commands to see that *your local copy* has a reference to *your forked remote repository* in Github :octocat:

```sh
$ git remote -v
origin  https://github.com/Your_Username/CodeWorld.git (fetch)
origin  https://github.com/Your_Username/CodeWorld.git (push)
```

### 4. Sync it :recycle:

Always keep your local copy of the repository updated with the original repository.
Before making any changes and/or in an appropriate interval, run the following commands *carefully* to update your local repository.

```sh
# Fetch all remote repositories and delete any deleted remote branches
$ git fetch --all --prune

# Switch to `main` branch
$ git checkout main

# Reset local `main` branch to match the `upstream` repository's `main` branch
$ git reset --hard upstream/main

# Push changes to your forked `CodeWorld` repo
$ git push origin main
```

### 5. Ready Steady Go... :turtle: :rabbit2:

Once you have completed these steps, you are ready to start contributing by checking our `Good First Issue` Issues and creating [pull requests](https://github.com/Priyanshu-Garg/CodeWorld/pulls).

### 6. Create a new branch :bangbang:

Whenever you are going to contribute. Please create a separate branch using command and keep your `main` branch clean (i.e. synced with remote branch).

```sh
# It will create a new branch with name Branch_Name and switch to branch Folder_Name
$ git checkout -b BranchName
```

Create a separate branch for contribution and try to use the same name of the branch as of folder.

To switch to the desired branch

```sh
# To switch from one folder to other
$ git checkout BranchName
```

To add the changes to the branch. Use

```sh
# To add all files to branch Folder_Name
$ git add .
```

Type in a message relevant for the code reviewer using

```sh
# This message get associated with all files you have changed
$ git commit -m 'relevant message'
```

Now, Push your awesome work to your remote repository using

```sh
# To push your work to your remote repository
$ git push -u origin BranchName
```

Finally, go to your repository in the browser and click on `compare and pull requests`.
Then add a title and description to your pull request that explains your precious effort.

## Awesome contributors :star_struck:
<a href="https://github.com/Priyanshu-Garg/CodeWorld/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=Priyanshu-Garg/CodeWorld&max=300" />
</a>

Made with [contributors-img](https://contributors-img.web.app).

## Help Contributing Guides :crown:

We love to have `articles` and `codes` in different languages and the `betterment` of existing ones.

Please discuss it with us first by creating a new issue.

:tada: :confetti_ball: :smiley: _**Happy Contributing**_ :smiley: :confetti_ball: :tada:

