#!/usr/bin/env python

import errno, fuse, stat, time

fuse.fuse_python_api = (0, 2)

class TestFS(fuse.Fuse):
	"""
	"""

	def __init__(self, *args, **kw):
		fuse.Fuse.__init__(self, *args, **kw)

		print 'Init complete.'

	def getattr(self, path):
		"""
		- st_mode (protection bits)
		- st_ino (inode number)
		- st_dev (device)
		- st_nlink (number of hard links)
		- st_uid (user ID of owner)
		- st_gid (group ID of owner)
		- st_size (size of file, in bytes)
		- st_atime (time of most recent access)
		- st_mtime (time of most recent content modification)
		- st_ctime (platform dependent; time of most recent metadata change on Unix,
					or the time of creation on Windows).
		"""

		print '*** getattr', path
		
		if path == '/':  
			pass  
		else:  
			return - errno.ENOENT
		
		st = fuse.Stat()
		st.st_mode = stat.S_IFDIR | 0777
		st.st_nlink = 2
		st.st_atime = int(time.time())
		st.st_mtime = st.st_atime
		st.st_ctime = st.st_atime
		return st
		#return -errno.ENOSYS


	def readdir(self, path, offset):
		"""
		return: [[('file1', 0), ('file2', 0), ... ]]
		"""

		print '*** readdir', path
		return -errno.ENOSYS

	def mythread ( self ):
		print '*** mythread'
		return -errno.ENOSYS

	def chmod ( self, path, mode ):
		print '*** chmod', path, oct(mode)
		return -errno.ENOSYS

	def chown ( self, path, uid, gid ):
		print '*** chown', path, uid, gid
		return -errno.ENOSYS

	def fsync ( self, path, isFsyncFile ):
		print '*** fsync', path, isFsyncFile
		return -errno.ENOSYS

	def link ( self, targetPath, linkPath ):
		print '*** link', targetPath, linkPath
		return -errno.ENOSYS

	def mkdir ( self, path, mode ):
		print '*** mkdir', path, oct(mode)
		return -errno.ENOSYS

	def mknod ( self, path, mode, dev ):
		print '*** mknod', path, oct(mode), dev
		return -errno.ENOSYS

	def open ( self, path, flags ):
		print '*** open', path, flags
		return -errno.ENOSYS

	def read ( self, path, length, offset ):
		print '*** read', path, length, offset
		return -errno.ENOSYS

	def readlink ( self, path ):
		print '*** readlink', path
		return -errno.ENOSYS

	def release ( self, path, flags ):
		print '*** release', path, flags
		return -errno.ENOSYS

	def rename ( self, oldPath, newPath ):
		print '*** rename', oldPath, newPath
		return -errno.ENOSYS

	def rmdir ( self, path ):
		print '*** rmdir', path
		return -errno.ENOSYS

	def statfs ( self ):
		print '*** statfs'
		return -errno.ENOSYS

	def symlink ( self, targetPath, linkPath ):
		print '*** symlink', targetPath, linkPath
		return -errno.ENOSYS

	def truncate ( self, path, size ):
		print '*** truncate', path, size
		return -errno.ENOSYS

	def unlink ( self, path ):
		print '*** unlink', path
		return -errno.ENOSYS

	def utime ( self, path, times ):
		print '*** utime', path, times
		return -errno.ENOSYS

	def write ( self, path, buf, offset ):
		print '*** write', path, buf, offset
		return -errno.ENOSYS

if __name__ == '__main__':  
	fs = TestFS()
	fs.parse(errex=1)
	fs.main()