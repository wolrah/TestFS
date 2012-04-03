#!/usr/bin/env python
"""
TestFS
An ongoing attempt at learning by doing with Python-FUSE
Copyright (c) 2012 Sean Harlow (firstname) at (firstname)(lastname) dot info

Released under the BSD license, see COPYING file for info.
"""

import errno, fuse, stat, time
import logging as log

# Setup FUSE
fuse.fuse_python_api = (0, 2)

# Setup logging
log.basicConfig(level=log.DEBUG)

directories = ['/', '/testdir1', '/testdir2', '/testdir3', '/testdir1/testsubdir']
files = ['/file1.txt', '/file2.txt', '/testdir2/file3.txt']
dummytext = 'This is a dummy file in a TestFS filesystem.  All files on the system will return this text.'

class EmptyStat(fuse.Stat):
	def __init__(self):
		self.st_mode = 0
		self.st_ino = 0
		self.st_dev = 0
		self.st_nlink = 0
		self.st_uid = 0
		self.st_gid = 0
		self.st_size = 0
		self.st_atime = int(time.time())
		self.st_mtime = 0
		self.st_ctime = 0

class TestFS(fuse.Fuse):
	def __init__(self, *args, **kw):
		log.info('Initializing FUSE')
		fuse.Fuse.__init__(self, *args, **kw)
		log.info('Initializing TestFS')
	
	def getattr(self, path):
		log.info('getattr %s', path)
		st = EmptyStat()
		# Check above lists for dummy files/folders
		if path in directories:
			log.debug('%s is a directory', path)
			st.st_mode = stat.S_IFDIR | 0755
			st.st_nlink = 2
		elif path in files:
			log.debug('%s is a file', path)
			st.st_mode = stat.S_IFREG | 0644
			st.st_nlink = 1
			st.st_size = len(dummytext)
		return st
	
	def readdir(self, path, offset):
		log.info('readdir %s, %i', path, offset)
		# The basics
		yield fuse.Direntry('.')
		yield fuse.Direntry('..')
		# Create a new blank list
		entrylist = []
		# Get file list
		for file in files:
			if (file.startswith(path)) & (len(file.split('/')) == len(path.split('/'))):
				log.debug('Matched file %s', file)
				entrylist.append(file[len(path):])
		# Get directory list
		for directory in directories:
			if (directory.startswith(path)) & (len(directory.split('/')) == len(path.split('/'))) & (directory != path):
				log.debug('Matched directory %s', directory)
				entrylist.append(directory[len(path):])
		# Sort it
		entrylist.sort()
		for entry in entrylist:
			yield fuse.Direntry(entry)


if __name__ == '__main__':  
	fs = TestFS()
	fs.parse(errex=1)
	fs.main()