import bpy
import os

def write_object_hierarchy(file, obj, level=0):
    """
    Recursively write object and its children to file with proper indentation
    """
    # Write the current object with indentation
    indent = "    " * level  # 4 spaces per level
    file.write(f"{indent}{obj.name}\n")
    
    # Write all children
    for child in obj.children:
        write_object_hierarchy(file, child, level + 1)

def export_hierarchy():
    # Get the folder where the blend file is saved
    blend_file_path = bpy.data.filepath
    directory = os.path.dirname(blend_file_path)
    
    # If the file hasn't been saved, use the desktop
    if not directory:
        directory = os.path.expanduser("~/Desktop")
    
    # Create output file path
    output_path = os.path.join(directory, "scene_hierarchy.txt")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("=== SCENE HIERARCHY ===\n\n")
        
        # Get all root objects (objects with no parent)
        root_objects = [obj for obj in bpy.context.scene.objects if obj.parent is None]
        
        # Write each root object and its children
        for obj in root_objects:
            write_object_hierarchy(f, obj)
            
    print(f"Hierarchy exported to: {output_path}")

# Run the export
export_hierarchy()