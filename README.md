# Git for Science
### Part 1: First steps. From cloning to pull request.

## Prerequisites

Some understanding of command line interfaces is helpful, but each command will be written almost exactly as it should be typed.


## Dependencies

* [git](https://github.com/git-guides/install-git)
* A [terminal program](https://en.wikipedia.org/wiki/List_of_terminal_emulators)
* A text editor or an IDE
* Github account (Note: the same steps can be used for any git service such as Gitlab, but pull request and other interfaces will be slightly different.)
* Python 3 (optional)

## What is git?

Git is a version control system.

* Used primarily for source code but many other uses (documents, web content) exist.

* Core features include tracking the contents of files over time, facilitating collaboration on files, and diffing (comparing) documents and whole repositories.

* Data structures are:
  * Branches
  * Commits
  * Repositories

* Free and open source

* Two popular services are built on git: Github and Gitlab. Github is the most widely used, but Gitlab has a very good open source implementation of the entire service. These services add the ability to host and distribute repos online on top of the basic functionality of a git server.


## Motivation

The ultimate goal for using version control in science is collaboration, reproduction and reuse, and to prevent errors.

Large and complex codebases are very difficult to manage and are sensitive to error. One small mistake in a codebase can have a major impact on its function and validity.

Git services can also satisfy journal or funder requirements, and repositories distributed this way can have a direct impact on the practice of science. At the very least, a canonical copy of a codebase is a prerequisite to any digital reproducibility. Usually, the standard is much higher and additional details will need to be included: documentation, a test suite, claims about expected results and so on.


## Topics

This tutorial will cover the complete workflow that ends with a pull request to a repository: cloning, checking out a branch, creating a new branch, creating commits, pushing a branch, opening a pull request.


## Vocabulary

(These topics will be reviewed throughout.)

Repository: A copy of all the code and history for a particular project. The remote repository is usually on a remote server or service such as github.com.

Branch: A copy of the files in a repository that can be modified independently of other branches. Reconciling the differences between two branches and consolidating them into one branch is *merging* them. The default branch is usually called "main."

Commit: A bundle of changes to the files in a repository. The history of a repository consists of a list of commits to various branches, and merges of the branches into one another. (Usually there's one default branch where all the changes eventually end up. The canonical current state of the repo is the state of this branch, and versioned releases are usually of this branch.)

Check out (a branch): Change your current working branch. Local files will be replaced with the branch's files. Commits will be attached to the branch.

Pull: Copy the latest version of files from the remote repository to your local repository.

Push: Copy the latest version of the file on a branch to the remote repository.



## Visualization of Branching and Merging

The process that this lesson covers is usually depicted as follows. Lines are branches. Dots are commits. Over time, the lines get longer left-to-right as commits are added (changes are made).


**State of the repository now**

_(One branch with a few commits.)_

![The main branch](images/main.png)

**After creating a new branch**

![After creating a branch](images/after_branching.png)

**After adding some commits to the branch**

![After adding commits](images/after_commits.png)

**After the branch has been merged in to main**

_(After the pull request has been accepted.)_

![After merging](images/after_merge.png)


## First steps

Clone a repository.

``` bash

git clone git@github.com:cobeylab/version-control-training.git

```

``` bash

# List files in the current directory. version-control-training should be one of them.

ls

# change to the repo directory

cd version-control-training

# List files again. README.md and a "src" directory should be included

ls

```

This repository is just a sample, but let's imagine:

1. The source code is under active development by multiple users.
2. The code is open source and public.
3. It is large, complex, sensitive to error, and valuable.

(All of these properties aren't necessary for git to be useful. Git is *particularly applicable* in science to the solo developer.)

In order to avoid undesirable changes to the main branch, the first step is usually to make a copy of the main branch and edit the files there.

Suppose you want to start a project to add a command line UI to the evolution of strings program.

Create, and check out a new branch.

``` bash

git checkout -b command-line-ui


```

Or

``` bash

git branch command-line-ui
git checkout command-line-ui

```

Checking out a branch means that changes you make to your local copy of the repo will be associated with that branch.

Make some changes to the source files and save them to disk. These changes will not be associated with the branch locally, or on the remote server yet. Changes may be made to any number of files between commits.


``` bash

# Any editor or IDE is fair game here.
vi src/evolve.py

```

Check to see what files have been changed.

``` bash

git status -s

```

Check to see what the changes were line by line.

_Note: In this interface, page through by pushing j on the keyboard, and quit by pushing q._

``` bash

git diff

```

Notice a few things about "diffing." Sometimes diffs will be difficult to follow.

Limitations to diffs:

1. Diffs are based only on the text itself. Small movements of blocks of text, nested changes (a move with a change inside it), changes to repeated blocks of text, can be computationally impossible to interpret perfectly, or may have different possible interpretations.
2. Differences can be difficult to display. In the simple command-line interface, a single character difference creates a fully red line for the old version, and a fully green line for the new.

For these reasons, and the difficulty interpreting large code changes in general, we split changes into small commits and make them on one "theme" at a time.

For instance, it's easier to understand a commit where all the extra spaces are removed from a file, and a separate commit that makes substantial code changes because we can diff them separately. Otherwise, we would have to read two similar lines of code looking for a change, only to find out the difference is a space character. Or we may think the change is a space when a substantial change is hidden in the diff.


## Undoing changes

Suppose you've done some coding on a file and the changes don't work well and you want to go back to the original version. (Specifically, this will be the last commit of the currently checked-out branch.)

Overwrite your changes. Note: Only do this if you are sure you don't want to keep changes to evolve.py.

``` bash

git checkout src/evolve.py

```

You could follow with

``` bash

git status -s

```

or

``` bash

git diff

```

to verify the file has been reset.

Now that the first attempt at changes to `evolve.py` have been overwritten, let's try again.

``` bash

vi src/evolve.py

```

_Note: To see what changes might look like, there's already a branch `command-line-ui-example-branch` with some simple modifications: https://github.com/cobeylab/version-control-training/compare/command-line-ui-example-branch_

Let's say we have something valuable to contribute. Check on the changes to make sure they're what you intended.

Did you inadvertently add any new files? Is evolve.py the only file that has changed?

``` bash

git status -s

```

What are the specific changes?

``` bash

git diff

```

We're ready to commit. The changes are all on a theme. They are small enough to compare with one diff. And they run.

Usually, it is not necessary to achieve perfection with every commit, but keep in mind that someone may want to roll back to a specific commit when there's a bug, for instance. They may want to compare the output between two commits. So any changes we make in a commit should leave the branch in a runnable state.

``` bash

git commit -am 'Add command line interface.'

```

The changes are now committed to your local `command-line-ui` branch. They have not been sent to the repository on github.com, and are not public.

You may do this several times before "pushing" the commits to the remote repository. Usually multiple commits are pushed at one time.

To look at all the commits you've added to the local branch, use `git log`.

``` bash

git log

```


Before you push, (and usually before you commit!) you should make sure the code passes any test suite for the repository. For this one, you can run it by typing `pytest` (requires [Pytest](https://docs.pytest.org)). For other repositories, the command may be different.

Once you're satisfied that your local commits are ready to be shared with other contributors, you can use `git push` to send any local commits that haven't been sent to the remote repository.

``` bash

git push

```

Navigate to https://github.com/cobeylab/version-control-training. You should see your branch listed at https://github.com/cobeylab/version-control-training/branches.


## Mental Model

You can think of this process as having four reservoirs where code can be stored, edited, compared, and approved.

The first is the _file buffer_ where you edit the file in an editor before its saved to disc.

The second is the _saved, "staged," files_ that can be compared to the last commit with `git diff`.

The third is the _branch_, which stores commits. A branch can also have new commits locally that haven't been pushed to the remote repository.

The fourth is the _pull request_. The pull request doesn't really store code, and in fact future commits to the same branch will be automatically included in the PR, but it can be thought of as one of these reservoirs where code is considered and modified before moving -- eventually -- to the main branch.


## Opening a pull request

Open a pull request. Click on "Pull requests" at the top of the page or go to https://github.com/cobeylab/version-control-training/pulls. Click "New pull request."

Choose your branch as the "compare" branch. The other, "base," branch is the branch your changes will be added to if the pull request is accepted.

Click "Create pull request."

Enter a title and description for the pull request. You should describe all of the changes that you've made in detail. Very specific details can be left to the diff, but generally you want to make it easy to review, and state your intentions clearly.

Once the pull request is approved, it is merged into the target branch. In large-scale projects, this branch may be several steps away from becoming canonical on the "main" branch. In smaller-scale projects, there may only be a "develop" branch and a "main" branch, and in many small projects, there's only a "main" branch. Larger, more error-sensitive projects, and those with more developers will have more elaborate branching strategies.

## Quiz

1. The first step to contributing to a repository is to make a copy, or ____ it.
  - a. merge
  - b. commit
  - c. clone
  - d. browse

2. The three main data structures in git are:
  - a. repositories, branches, commits
  - b. repositories, clones, upstreams
  - c. branches, commits, buffers
  - d. github, gitlab, subversion

3. `git checkout -b command-line-ui` is a combination of what two git commands? (Choose two)
  - a. branch
  - b. status
  - c. diff
  - d. checkout

4. What two git commands are used frequently to view changed files?
  - a. checkout and clone
  - b. push and pull
  - c. status and diff
  - d. branch and status

5. In order from "largest" to "smallest," the main git data structures are (Hint: The largest contains several of the next smallest, which contains several of the smallest.):
  - a. commits > repositories > branches
  - b. repositories > branches > commits
  - c. repositories > commits > branches
  - d. branches > commits > repositories

## Next steps

### Other Git Interfaces

#### Editors and Integrated Development Environments (IDEs)

Command-line git can be used with any editor or IDE. If you'd like to use git integrated with your coding environment, here are some options:

*Visual Studio Code:* VSCode provides git integration without a plug-in. Click "Source Control" in the lefthand menu bar. All of the functionality that should be familiar -- create a branch, commit, show status -- are available there. For more information, see [Use Git version-control tools in Visual Studio Code](https://docs.microsoft.com/en-us/learn/modules/use-git-from-vs-code/).

*RStudio:* RStudio also supports git out-of-the-box. Diff, commit, pull/push functions are in Tools --> Version Control. For more information, see [Using Git within RStudio](https://cfss.uchicago.edu/setup/git-with-rstudio/).

#### GUIs

There are a large number of graphical interfaces for git listed on the [git web site](https://git-scm.com/downloads/guis/).

#### Shell Integration

There are shell integrations that can make using git safer and easier on the command line. Customizing your prompt with git-related info is a common one. The prompt can show the current branch, whether there are local changes, whether or not a directory has git metadata et cetera. See instructions for [bash](https://www.git-scm.com/book/en/v2/Appendix-A%3A-Git-in-Other-Environments-Git-in-Bash) and [zsh](https://git-scm.com/book/en/v2/Appendix-A%3A-Git-in-Other-Environments-Git-in-Zsh).


## Funding and Acknowledgments

This work was funded by [Centers of Excellence for Influenza Research and Response (CEIRR)](https://www.ceirr-network.org/).

Portions of this tutorial were adapted from the [Cobey Lab Handbook](https://cobeylab.github.io/lab_handbook/).



