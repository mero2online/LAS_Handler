from HandleLithoLAS import gen_litho_LAS
from HandleLithoPercentLAS import gen_litho_Percent_LAS
from HandleRopLAS import gen_ROP_LAS
from HandleDrillLAS import gen_DRILL_LAS
from HelperFunc import resource_path


def convert_Litho_LAS(type, start_depth=''):
    if type == 'LITHO':
        gen_litho_LAS(resource_path('input.las'))
    if type == 'LITHO%':
        gen_litho_Percent_LAS(resource_path('input.las'), start_depth)
    if type == 'ROP':
        gen_ROP_LAS(resource_path('input.las'))
    if type == 'DRILL':
        gen_DRILL_LAS(resource_path('input.las'))
