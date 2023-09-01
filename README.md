# MO-tracker
The script enabling on-the-fly tracking of active space stability during MD simulations in Molcas/OpenMolcas.

Usage of MO-tracker requires few modifications in Molcas/OpenMolcas. The template of Molcas/OpenMolcas input file with these modifications is included in the repository. The MO-tracker consist out of one Python and two Shell scripts that allow for seamless integration of MO-tracker functionality into Molcas/OpenMolcas MD calculations via EMIL commands.

The MO-tracker functionality is shown on example of uracil. Here, the Z-axis initial velocity along one of the C=O groups was intentionally increased to cause the dissociation of C=O bond, which occurs after 6 fs. Such example allows for very quick testing of MO-tracker functionality by any user. During the calculations the MO-tracker prints `Consistent with previous step` in _"MO-track-list.txt"_ for first 5 fs of uracil MD simulations. At 6 fs uracil molecule undergoes dissociation of oxygen atom, which leads to instability of active space. MO-tracker captures this event and prints `Warning: potential change in active space!` in  _"MO-track-list.txt"_.

# Modifications of MO-tracker for specific system

User must specify `active_space_start=` and `active_space_end=` in _"MO-track-list.txt"_, where these values correspond to the range of orbitals included in the specific active space of the system of interest. 

Change of `cosine_similarity_threshold = 0.5` is not recomended, because this value provide reasonable sensitivity to change of the active space, while allowing for moderate distortion of orbitals within the active space.
