from HandleLithoLAS import gen_litho_LAS
from HandleLithoPercentLAS import gen_litho_Percent_LAS
from HelperFunc import resource_path, readLocalFile


def convert_Litho_LAS(type):
    if type == 'LITHO':
        gen_litho_LAS(resource_path('input.las'))
    if type == 'LITHO%':
        gen_litho_Percent_LAS(resource_path('input.las'))
