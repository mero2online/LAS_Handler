from HandleLithoLAS import gen_litho_LAS
from HelperFunc import resource_path


def convert_Litho_LAS():
    gen_litho_LAS(resource_path('input.las'))

    f = open(resource_path('draft.las'), 'r')
    txt = f.read()
    f.close()

    startOne = '~Well ------------------------------------------------------'
    endOne = '~Curve Information -----------------------------------------'
    textOneLas = txt[txt.find(startOne)+len(startOne):txt.rfind(endOne)]
    startTwo = '~Curve Information -----------------------------------------'
    endTwo = '~Params ----------------------------------------------------'
    textTwoLas = txt[txt.find(startTwo)+len(startTwo):txt.rfind(endTwo)]
    startThree = '~ASCII -----------------------------------------------------'
    textThreeLas = txt[txt.find(startThree)+len(startThree):len(txt)-1]

    return {'textOneLas': textOneLas, 'textTwoLas': textTwoLas, 'textThreeLas': textThreeLas}
