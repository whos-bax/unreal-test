import os
import subprocess

def create_video_from_images(image_folder, image_prev_name, output_video, fps=12):

    print(f"Current working directory: {os.getcwd()}")
    os.chdir("/Users/whosbax/Documents/GitHub/unreal-test")  # 작업 디렉토리 설정
    print(f"Input folder exists: {(image_folder)}, {os.path.exists(image_folder)}")
    print(f"Sample file exists: {os.path.exists(os.path.join(image_folder, 'camera_act_1.0000.png'))}")
    print(f"Output folder exists: {os.path.exists(os.path.dirname(output_video))}")

    """
    Converts a sequence of images into an MP4 video.

    :param image_folder: Path to the folder containing images.
    :param output_video: Path to the output MP4 video file (e.g., output.mp4).
    :param fps: Frames per second for the output video.
    """
    # Ensure the output directory exists
    output_dir = os.path.dirname(output_video)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    # Ensure FFmpeg is installed
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except FileNotFoundError:
        raise EnvironmentError("FFmpeg is not installed or not found in PATH.")
    
    # Create an FFmpeg-compatible file pattern
    image_pattern = os.path.join(image_folder, image_prev_name + ".%04d.png")  # Adjust pattern as needed
    
    # FFmpeg command
    command = [
        "ffmpeg",
        "-y",  # Overwrite output file if it exists
        "-framerate", str(fps),  # Set input frame rate
        "-i", image_pattern,  # Input file pattern
        "-c:v", "libx264",  # Use H.264 codec
        "-pix_fmt", "yuv420p",  # Ensure compatibility with most players
        output_video  # Output video file
    ]
    
    # Run FFmpeg
    try:
        subprocess.run(command, check=True)
        print(f"Video created successfully: {output_video}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while creating video: {e}")

# Example usage
image_folder = "cesium1/Saved/MovieRenders/Scene03"  # Replace with your image folder path
image_prev_name = "scene03_hl" # {image_prev_name}.0001.png -> ex. frame.0001.png , frame.0002.png
output_video = "cesium1/Saved/Output/scenario_3_hl.mp4"  # Replace with your desired output video file name
create_video_from_images(image_folder, image_prev_name, output_video)