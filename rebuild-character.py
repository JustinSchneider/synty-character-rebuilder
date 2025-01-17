import bpy

def clean_name(name):
    """Remove .001 style suffixes from object names"""
    return name.split('.')[0]

def create_empty(name, parent=None):
    """Create or get an empty object and optionally set its parent"""
    # Check if empty already exists
    if name in bpy.data.objects:
        empty = bpy.data.objects[name]
    else:
        empty = bpy.data.objects.new(name, None)
        empty.empty_display_size = 1
        empty.empty_display_type = 'PLAIN_AXES'
        bpy.context.scene.collection.objects.link(empty)
    
    # Set parent if provided
    if parent:
        empty.parent = parent
    
    return empty

def setup_base_structure():
    """Create the Modular_Characters organization structure"""
    # Create main structure
    modular_chars = create_empty("Modular_Characters")
    all_gender = create_empty("All_Gender_Parts", modular_chars)
    female_parts = create_empty("Female_Parts", modular_chars)
    male_parts = create_empty("Male_Parts", modular_chars)
    
    # All Gender structure
    headcoverings = create_empty("All_00_HeadCoverings", all_gender)
    create_empty("HeadCoverings_Base_Hair", headcoverings)
    create_empty("HeadCoverings_No_FacialHair", headcoverings)
    create_empty("HeadCoverings_No_Hair", headcoverings)
    
    create_empty("All_01_Hair", all_gender)
    
    head_attach = create_empty("All_02_Head_Attachment", all_gender)
    create_empty("Hair", head_attach)
    create_empty("Helmet", head_attach)
    
    create_empty("All_03_Chest_Attachment", all_gender)
    create_empty("All_04_Back_Attachment", all_gender)
    create_empty("All_05_Shoulder_Attachment_Right", all_gender)
    create_empty("All_06_Shoulder_Attachment_Left", all_gender)
    create_empty("All_07_Elbow_Attachment_Right", all_gender)
    create_empty("All_08_Elbow_Attachment_Left", all_gender)
    create_empty("All_09_Hips_Attachment", all_gender)
    create_empty("All_10_Knee_Attachement_Right", all_gender)
    create_empty("All_11_Knee_Attachement_Left", all_gender)
    
    extra = create_empty("All_12_Extra", all_gender)
    create_empty("Elf_Ear", extra)
    
    # Female parts structure
    female_head = create_empty("Female_00_Head", female_parts)
    create_empty("Female_Head_All_Elements", female_head)
    create_empty("Female_Head_No_Elements", female_head)
    
    create_empty("Female_01_Eyebrows", female_parts)
    create_empty("Female_02_FacialHair", female_parts)
    create_empty("Female_03_Torso", female_parts)
    create_empty("Female_04_Arm_Upper_Right", female_parts)
    create_empty("Female_05_Arm_Upper_Left", female_parts)
    create_empty("Female_06_Arm_Lower_Right", female_parts)
    create_empty("Female_07_Arm_Lower_Left", female_parts)
    create_empty("Female_08_Hand_Right", female_parts)
    create_empty("Female_09_Hand_Left", female_parts)
    create_empty("Female_10_Hips", female_parts)
    create_empty("Female_11_Leg_Right", female_parts)
    create_empty("Female_12_Leg_Left", female_parts)
    
    # Male parts structure
    male_head = create_empty("Male_00_Head", male_parts)
    create_empty("Male_Head_All_Elements", male_head)
    create_empty("Male_Head_No_Elements", male_head)
    
    create_empty("Male_01_Eyebrows", male_parts)
    create_empty("Male_02_FacialHair", male_parts)
    create_empty("Male_03_Torso", male_parts)
    create_empty("Male_04_Arm_Upper_Right", male_parts)
    create_empty("Male_05_Arm_Upper_Left", male_parts)
    create_empty("Male_06_Arm_Lower_Right", male_parts)
    create_empty("Male_07_Arm_Lower_Left", male_parts)
    create_empty("Male_08_Hand_Right", male_parts)
    create_empty("Male_09_Hand_Left", male_parts)
    create_empty("Male_10_Hips", male_parts)
    create_empty("Male_11_Leg_Right", male_parts)
    create_empty("Male_12_Leg_Left", male_parts)
    
    return modular_chars

def get_target_parent(obj_name):
    """Determine which empty transform an object should be parented to based on its name"""
    name = clean_name(obj_name)
    
    # Handle special cases first
    if name.startswith("Chr_Head_No_Elements_Female"):
        return bpy.data.objects["Female_Head_No_Elements"]
    elif name.startswith("Chr_Head_No_Elements_Male"):
        return bpy.data.objects["Male_Head_No_Elements"]
    elif name.startswith("Chr_Head_Female"):
        return bpy.data.objects["Female_Head_All_Elements"]
    elif name.startswith("Chr_Head_Male"):
        return bpy.data.objects["Male_Head_All_Elements"]
    
    # Handle regular cases
    mapping = {
        "Chr_HeadCoverings_Base_Hair": "HeadCoverings_Base_Hair",
        "Chr_HeadCoverings_No_FacialHair": "HeadCoverings_No_FacialHair",
        "Chr_HeadCoverings_No_Hair": "HeadCoverings_No_Hair",
        "Chr_Hair": "All_01_Hair",
        "Chr_HelmetAttachment": "Helmet",
        "Chr_BackAttachment": "All_04_Back_Attachment",
        "Chr_ShoulderAttachRight": "All_05_Shoulder_Attachment_Right",
        "Chr_ShoulderAttachLeft": "All_06_Shoulder_Attachment_Left",
        "Chr_ElbowAttachRight": "All_07_Elbow_Attachment_Right",
        "Chr_ElbowAttachLeft": "All_08_Elbow_Attachment_Left",
        "Chr_HipsAttachment": "All_09_Hips_Attachment",
        "Chr_KneeAttachRight": "All_10_Knee_Attachement_Right",
        "Chr_KneeAttachLeft": "All_11_Knee_Attachement_Left",
        "Chr_Ear": "Elf_Ear",
        
        # Female parts
        "Chr_Eyebrow_Female": "Female_01_Eyebrows",
        "Chr_Torso_Female": "Female_03_Torso",
        "Chr_ArmUpperRight_Female": "Female_04_Arm_Upper_Right",
        "Chr_ArmUpperLeft_Female": "Female_05_Arm_Upper_Left",
        "Chr_ArmLowerRight_Female": "Female_06_Arm_Lower_Right",
        "Chr_ArmLowerLeft_Female": "Female_07_Arm_Lower_Left",
        "Chr_HandRight_Female": "Female_08_Hand_Right",
        "Chr_HandLeft_Female": "Female_09_Hand_Left",
        "Chr_Hips_Female": "Female_10_Hips",
        "Chr_LegRight_Female": "Female_11_Leg_Right",
        "Chr_LegLeft_Female": "Female_12_Leg_Left",
        
        # Male parts
        "Chr_Eyebrow_Male": "Male_01_Eyebrows",
        "Chr_FacialHair_Male": "Male_02_FacialHair",
        "Chr_Torso_Male": "Male_03_Torso",
        "Chr_ArmUpperRight_Male": "Male_04_Arm_Upper_Right",
        "Chr_ArmUpperLeft_Male": "Male_05_Arm_Upper_Left",
        "Chr_ArmLowerRight_Male": "Male_06_Arm_Lower_Right",
        "Chr_ArmLowerLeft_Male": "Male_07_Arm_Lower_Left",
        "Chr_HandRight_Male": "Male_08_Hand_Right",
        "Chr_HandLeft_Male": "Male_09_Hand_Left",
        "Chr_Hips_Male": "Male_10_Hips",
        "Chr_LegRight_Male": "Male_11_Leg_Right",
        "Chr_LegLeft_Male": "Male_12_Leg_Left"
    }
    
    for prefix, empty_name in mapping.items():
        if name.startswith(prefix):
            return bpy.data.objects[empty_name]
    
    return None

def organize_scene():
    """Main function to organize the scene"""
    # Find the existing armature
    armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            armature = obj
            # Ensure the armature object is named Root
            armature.name = "Root"
            break
    
    if not armature:
        raise Exception("No armature found in scene")
    
    # Create the organization structure
    modular_chars = setup_base_structure()
    
    # Both the armature and Modular_Characters should share the same parent
    # (typically the scene root or FBX root)
    if armature.parent:
        modular_chars.parent = armature.parent
    
    # Process all mesh objects
    for obj in bpy.data.objects:
        if obj.type != 'MESH':
            continue
            
        # Clean the object name
        obj.name = clean_name(obj.name)
        
        # Get target parent
        target_parent = get_target_parent(obj.name)
        if not target_parent:
            print(f"Warning: No parent transform found for object {obj.name}")
            continue
        
        # Setup parenting
        obj.parent = target_parent
        
        # Ensure armature modifier points to root armature
        if obj.find_armature():
            # Add armature modifier if it doesn't exist
            if not any(mod.type == 'ARMATURE' for mod in obj.modifiers):
                mod = obj.modifiers.new(name="Armature", type='ARMATURE')
                mod.object = armature

def main():
    """Main execution function"""
    organize_scene()
    print("Scene organization complete!")

if __name__ == "__main__":
    main()