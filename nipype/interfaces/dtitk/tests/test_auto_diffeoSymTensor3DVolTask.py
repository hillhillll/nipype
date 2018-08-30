# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..registration import diffeoSymTensor3DVolTask


def test_diffeoSymTensor3DVolTask_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        df=dict(
            argstr='-df %s',
            usedefault=True,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        flip=dict(argstr='-flip %d %d %d', ),
        in_file=dict(
            argstr='-in %s',
            mandatory=True,
        ),
        interpolation=dict(
            argstr='-interp %s',
            usedefault=True,
        ),
        out_file=dict(
            argstr='-out %s',
            keep_extension=True,
            name_source='in_file',
            name_template='%s_diffeoxfmd',
        ),
        reorient=dict(
            argstr='-reorient %s',
            usedefault=True,
        ),
        resampling_type=dict(argstr='-type %s', ),
        target=dict(
            argstr='-target %s',
            xor=['voxel_size'],
        ),
        transform=dict(
            argstr='-trans %s',
            mandatory=True,
        ),
        voxel_size=dict(
            argstr='-vsize %g %g %g',
            xor=['target'],
        ),
    )
    inputs = diffeoSymTensor3DVolTask.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_diffeoSymTensor3DVolTask_outputs():
    output_map = dict(out_file=dict(), )
    outputs = diffeoSymTensor3DVolTask.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
