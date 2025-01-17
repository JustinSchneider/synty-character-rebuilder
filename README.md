# Synty Modular Character Rebuilder

Included in this repository is a script that allows you to rebuild the intended structure of Synty's [Modular Fantasy Hero Character](https://assetstore.unity.com/packages/3d/characters/humanoids/fantasy/polygon-modular-fantasy-hero-characters-low-poly-3d-art-by-synty-143468) FBX after importing it into Blender.

## Purpose

Synty's models are fantastic, and the modular character package is great for making a wide variety of characters. There are great enhancements available such as Battledrake's [SyntyEditorTools](https://github.com/Battledrake/SyntyEditorTools), which allows you to quickly toggle the various pieces on and off using an Editor panel. This tool, however, expects the model to be in a specific structure, as defined in the FBX included in the Asset Store package.

Attempting to open the FBX in Blender causes all objects to be placed in the scene root, but leaves empty transforms intact with the intended organization. This script moves the pieces back into their original structure and renames the rig as well. Exporting again as FBX will allow you to use your edited model with Battledrake's tool again.

## Steps

1. Import ModularCharacters.fbx into Blender. I recommend the FixedScale version.
2. Select all objects in the hierarchy. Viewport Rendering is disabled by default for many of the parts, so if selecting from the Layout view, you'll have to re-enable that first
3. Apply rotation and scale to all parts. This will ensure all parts are at scale (1,1,1) and rotation (0,0,0) when imported
4. Run the script from the Scripting tab
5. Export FBX with Unity-appropriate settings or use the handy [Blender to Unity FBX Exporter](https://github.com/EdyJ/blender-to-unity-fbx-exporter)

## Known Issues

Perhaps due to some weirdness with how Blender imports FBX files, there'll end up being an additional Root transform in the armature. This didn't seem to be an issue for Unity, as the Mecanim rig was resolved just the same, and I was even able to retarget an animation made with the original Synty model to one exported from this script, so I don't think it's a problem. I'm willing to fix it if anyone knows how, though.
