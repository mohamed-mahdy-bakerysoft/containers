# Run the script with sudo!

singularity build --force base.sif base.def
singularity test      base.sif
singularity test --nv base.sif

singularity build --force pip.sif pip.def
singularity test      pip.sif
singularity test --nv pip.sif

singularity build --force pyvista.sif pyvista.def
singularity test      pip.sif
singularity test --nv pip.sif
