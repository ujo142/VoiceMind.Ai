import os
import shutil

SOURCE_PATH = os.getcwd()
BASE_PATH = os.path.join(SOURCE_PATH,  'data', 'archive-6')



def data_reallocate(source_path: str, base_path: str) -> None:
    """
    Moves all audio .wav files from innter folders of each speaker to main /data folder
    and deletes empty speaker folders
    
    Args:
        source_path (str): Main directory path where all files are stored(src, data, etc.)
        base_path (str): Path of downloaded raw audio files
      
    """    
    
    base_path = os.path.join(source_path, 'data', 'archive-6')
    for actor_folder in os.listdir(base_path):
        actor_path = os.path.join(base_path, actor_folder)
        if os.path.isdir(actor_path):
            for file_name in os.listdir(actor_path):
                file_path = os.path.join(actor_path, file_name)
                if file_name.endswith('.wav'):
                    destination_path = os.path.join(base_path, file_name)
                    destination_path = os.path.join(*destination_path.split('/archive-6/'))
                    shutil.move(file_path, destination_path)
            if not actor_path.endswith('actors_01-24'):
                os.rmdir(actor_path)  
            else:
                pass
    shutil.rmtree(os.path.join(source_path, 'data', 'archive-6'))
    
    
    
if __name__ == '__main__':
    data_reallocate(SOURCE_PATH, BASE_PATH)