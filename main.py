import os
import shutil
import argparse

class LargestFileFinder:
    def __init__(self, subtitle_folder_path):
        self.folder_path = subtitle_folder_path

    def find_largest_file(self, keyword):
        largest_file = None
        largest_file_size = 0

        for root, _, files in os.walk(self.folder_path):
            for file in files:
                if keyword in file:
                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)

                    if file_size > largest_file_size:
                        largest_file = file
                        largest_file_size = file_size

        return largest_file
    
class VideoFinder:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def find_videos(self):
        video_extensions = ['.mp4', '.avi', '.mkv', '.mov']
        video_files = []

        for _, _, files in os.walk(self.folder_path):
            for file in files:
                file_name, file_ext = os.path.splitext(file)
                if file_ext.lower() in video_extensions:
                    video_files.append(file_name)

        return video_files
    
class FileCopyRenamer:
    def __init__(self, file_path):
        self.file_path = file_path

    def copy_rename_file(self, keyword, destination_dir):
        _, file_ext = os.path.splitext(os.path.basename(self.file_path))
        new_file_name = f"{keyword}{file_ext}"
        new_file_path = os.path.join(destination_dir, new_file_name)
        shutil.copy2(self.file_path, new_file_path)

        return new_file_path


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Organise the subtitles according to file names')
    parser.add_argument('base_folder_path', help='Path to the base folder')
    args = parser.parse_args()

keyword = 'English'

video_finder = VideoFinder(args.base_folder_path)
videos = video_finder.find_videos()

for video in videos:
    subtitle_folder = args.base_folder_path + "\Subs\\" + video
    file_finder = LargestFileFinder(subtitle_folder)
    largest_file = file_finder.find_largest_file('English')
    file_copy_renamer = FileCopyRenamer(subtitle_folder + "\\" + largest_file)
    file_copy_renamer.copy_rename_file(video, args.base_folder_path)

