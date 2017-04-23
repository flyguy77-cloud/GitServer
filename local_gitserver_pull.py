#!/usr/bin/python
## For pulling from local git server (HTTP)
##
from git import *
from getpass import getpass
import os, shutil

try:
   username = raw_input("Username [defaul=git]: ") or "git"
   workdir = raw_input("Workdir [default=/tmp]: ") or "/tmp"
   git_server = raw_input("Git Server [default=127.0.0.1]: ") or "127.0.0.1"
   project = raw_input("Projectname: ")
   gitbase = "root"
   basedir = os.chdir(workdir)

   def clone():
      try:
         cloning = Repo.clone_from("http://%s@%s/%s/%s.git" %(username, git_server, gitbase, project), "%s" %project)
         print(" %s cloned.."%project)
      except GitCommandError:
         print(" Cloning into an existing directory is only allowed if the directory is empty")
         answer = raw_input(" Would you like to remove the contents from this directory? [y/n]: ")
         if answer == "y": 
           lstdir = "/tmp/%s"%project
           rmdr = os.listdir("/tmp/%s"%project)
           for a in rmdr:
              print("about to remove %s"%a)
           try:
              act_rm = shutil.rmtree(lstdir)
              print " File(s) removed.."
              clone()
           except OSError:
              print " Failed to remove.."
   clone()
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
#remote origin
#add
#init
#config
