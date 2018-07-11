import databaseConnection
import jwt
import constants
import linuxService
import utilities
import os

db = databaseConnection.getDatabaseInstance()


class Storage:
    def __init__(self,name,size):
        size=0

    def createStorage(self,name,size,protocol):
        drive = self.createDrive(name,size,protocol)
        return drive

    def createDrive(self,name,size,protocol):
        command = "lvcreate --name "
        command += name
        command += " --size "
        if(type(size) == int):
            command += "+"
            command += str(size)+"G "
        else:
            return constants.ERRORS['INVALID_ENTITY']
        
        vgstore = "vgstore"
        command += vgstore  
        #Execute command to create Logical Volume
        driveDetails = linuxService.executeCommand(command)
        if(driveDetails['error']):
            return constants.ERRORS['DRIVE_ERROR']
        #create an XFS format partition for created drive
        partitionCommand = "sudo mkfs.xfs /dev/"+vgstore+"/"+name
        mountCommand     = "sudo mount -e /dev/"+vgstore+"/"+name
        mountCommand    += " /media/"+name
        linuxService.executeCommand(partitionCommand)
        mountpath = linuxService.executeCommand(mountCommand)
        if(mountpath['error']):
            return constants.ERRORS['DRIVE_MOUNT_ERROR']
            
        #CHECK for protocol and create download file
        if(protocol == constants.MOUNT_TYPES['NFS']):
            exportFile = open('/etc/exports','a+',2)
            bufferString = "/media/"+name+" *(rw,no_root_squash) "
            exportFile.write(bufferString)
            exportFile.close()
            exportFile = open('/uploads/'+name,'w+',0)
            bufferString = " mkdir /media/"+name+";\n"
            bufferString+= " mount 192.168.1.3:/media/"+name+"  /media/"+name
            exportFile.write(bufferString)
            exportFile.close()
        return {"success":True}    
       