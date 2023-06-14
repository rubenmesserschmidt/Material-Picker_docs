Features
########

Material Pick
*************

:Area: 3D Viewport
:Menu: Context Menu ‣ Material Picker
:Hotkey: ``Alt + M`` (Changable in the *Preferences*)

Hover over any material in the viewport and then press `Leftclick` to select it.
For showing the material the following cases are considered:

#. The material is assigned to a material slot of the object
   The object will be selected and the according material slot will be made active.

#. The material is otherwise assigned to the object (e.g. Geometry Nodes 'Set Material Node')
   A new hidden object will be created and the material will be assigned to it. Then **1** will be applied.

#. The material is part of an object that is instanced (e.g. Collection Instance)
   The original object will be searched. Then **1** or **2** will be applied.

#. The material is part of an object that is linked from another *.blend* file
   A popup window will appear asking if you want to load the linked file or show the material locally

   * **Load File**: The linked file will be loaded in a new blender instance.
                    Then **1** or **2** will be applied and the *Shading* workspace will be activated.

     :Auto Reload: If the linked file is changed, the changes will be applied automatically. Needs to be enabled in the *Preferences*.

   * **Show Local**: **1** or **2** will be applied but the material is not editable, since it remains linked.



Material Search
***************