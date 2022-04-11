from xlutils.filter import process,XLRDReader,XLWTWriter

#
# suggested patch by John Machin
# https://stackoverflow.com/a/5285650/2363712
# 
def copy2(wb):
    w = XLWTWriter()
    process(
        XLRDReader(wb,'unknown.xls'),
        w
        )
    return w.output[0][1], w.style_list