from nipype.interfaces.base import CommandLine, TraitedSpec, File, CommandLineInputSpec, traits
from scripts import qsmxt_functions
import os

class PbMaskingInputSpec(CommandLineInputSpec):
    phase = File(
        exists=True,
        mandatory=True,
        argstr="--phase %s"
    )
    mask = File(
        argstr="--output %s",
        name_source=['phase'],
        name_template='%s_pb_mask.nii'
    )

class PbMaskingOutputSpec(TraitedSpec):
    mask = File()

class PbMaskingInterface(CommandLine):
    input_spec = PbMaskingInputSpec
    output_spec = PbMaskingOutputSpec
    _cmd = os.path.join(qsmxt_functions.get_qsmxt_dir(), "scripts", "hagberg_pb_masking.jl")


class RomeoMaskingInputSpec(CommandLineInputSpec):
    phase = File(
        exists=True,
        mandatory=True,
        argstr="--phase %s"
    )
    mag = File(
        exists=True,
        argstr="--mag %s"
    )
    weight_type = traits.Str(
        default_value="grad+second",
        argstr="--type %s"
    )
    out_file = File(
        argstr="--output %s",
        name_source=['phase'],
        name_template='%s_romeo_voxelquality.nii'
    )

class RomeoMaskingOutputSpec(TraitedSpec):
    out_file = File()

class RomeoMaskingInterface(CommandLine):
    input_spec = RomeoMaskingInputSpec
    output_spec = RomeoMaskingOutputSpec
    _cmd = "romeo_voxelquality.jl"