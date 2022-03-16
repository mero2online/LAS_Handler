from HandleLithoLAS import gen_litho_LAS
from HandleLithoPercentLAS import gen_litho_Percent_LAS
from HelperFunc import resource_path, readLocalFile


def convert_Litho_LAS(type):
    if type == 'LITHO':
        gen_litho_LAS(resource_path('input.las'))
    if type == 'LITHO%':
        gen_litho_Percent_LAS(resource_path('input.las'))

    txt = readLocalFile(resource_path('draft.las'))

    startOne = '~Well ------------------------------------------------------'
    endOne = '~Curve Information -----------------------------------------'
    textOneLas = txt[txt.find(startOne)+len(startOne):txt.rfind(endOne)]

    startTwo = '~Curve Information -----------------------------------------'
    endTwo = '~Params ----------------------------------------------------'
    textTwoLas = txt[txt.find(startTwo)+len(startTwo):txt.rfind(endTwo)]

    startThree = '~ASCII -----------------------------------------------------'
    textThreeLas = txt[txt.find(startThree)+len(startThree):len(txt)-1]

    return {'textOneLas': textOneLas, 'textTwoLas': textTwoLas, 'textThreeLas': textThreeLas}
