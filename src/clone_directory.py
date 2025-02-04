import os, shutil
def clone_directory(destination, source):
    #return if source doesnt have directory
    if not os.path.isdir(source):
        print(f"Warning: Source directory '{source}' does not exist. Skipping...")

        return
    
    #delete everything at that destination if exists
    if os.path.exists(destination):
        try:
            shutil.rmtree(destination)
        except Exception as e:
            print(f"Error: Unable to delete directory '{destination}': {str(e)}")
            return
    
    
    try:
        shutil.copytree(source, destination)
    
    except Exception as e:
        print(f"Error: Unable to clone directory '{source}' to '{destination}': {str(e)}")
        return


        


    