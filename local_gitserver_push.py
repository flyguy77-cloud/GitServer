#!/usr/bin/python
## For pulling from local git server (HTTP)
##
from git import Repo, repo
import os, shutil
#import os.path as osp

try:
   username = raw_input("Username [default=git]: ") or "git"
   workdir = raw_input("Workdir [default=/tmp]: ") or "/tmp"
   git_server = raw_input("Git Server [default=127.0.0.1]: ") or "127.0.0.1"
   project = raw_input("Projectname: ")
   add_files = raw_input("Files to add [default=all]: ") or "."
   gitbase = "root"
   basedir = os.chdir(workdir)

   def push():
#      try:
      repo = Repo.clone_from("http://%s@%s/%s/%s.git" %(username, git_server, gitbase, project), "%s" %project)
      initialize = Repo.init("%s/%s"%(workdir,project))
      print initialize
      adding = initialize.index.add("%s"%add_files)
      comment = raw_input("Commit comment(s): ")
      commit = initialize.index.commit(comment)
      origin = initialize.create_remote('origin', repo.remotes.origin.url)
#      assert origin.exists()
#      assert origin == initialize.remotes.origin == initialize.remotes['origin']
#      origin.fetch()
      origin.push()
#      except GitCommandError:
#         print " O oo.."
   push()
except KeyboardInterrupt:
   print " \nInterrupt by user.."


###commit
# Repo.commit("v0.1")
# Repo.init(workdir)
# Repo.index.add(workdir)
# Repo.index.add([file_name])
# Repo.index.commit("initial commit")

##push
# remote = Repo.create_remote('test', 'http://root@127.0.0.1/root/xxx.git')
# origin = empty_repo.create_remote('origin', empty_repo.remotes['origin']
# origin.push()

##remote origin

##add

##init

##config
