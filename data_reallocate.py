import os
import shutil

SOURCE_PATH = os.getcwd()
BASE_PATH = os.path.join(SOURCE_PATH  'data', 'archive-6')

def data_reallocate(base_path: str, source_path: str):

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
    reallocate_data()