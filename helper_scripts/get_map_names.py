import os

def list_maps_and_files(directory):
    maps_and_files = {}

    # Traverse the given directory
    for root, dirs, files in os.walk(directory):
        # Get the relative path of the current directory
        relative_path = os.path.relpath(root, directory)
        # Skip the root directory itself
        if relative_path == ".":
            continue

        # List files in the current directory
        maps_and_files[relative_path] = sorted(files)

    # Sort the map names
    sorted_maps = sorted(maps_and_files.keys())

    # Generate output file names based on the provided directory name
    base_name = os.path.basename(os.path.normpath(directory))
    map_names_file = f"{base_name}_map_names.txt"
    file_details_file = f"{base_name}_file_details.txt"

    # Write the map names to the map names file
    with open(map_names_file, 'w') as map_file:
        for map_name in sorted_maps:
            map_file.write(f"{map_name}\n")

    # Write the maps and their files to the file details file
    with open(file_details_file, 'w') as details_file:
        for map_name in sorted_maps:
            details_file.write(f"Map: {map_name}\n")
            for file_name in maps_and_files[map_name]:
                details_file.write(f"  {file_name}\n")
            details_file.write("\n")

if __name__ == "__main__":
    # Provide the path to the directory you want to explore
    directory_path = r"your path"
    list_maps_and_files(directory_path)
