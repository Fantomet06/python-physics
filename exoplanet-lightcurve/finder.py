import lightkurve as lk # type: ignore
import numpy as np
from lightkurve import TessTargetPixelFile, search_targetpixelfile # type: ignore

pixelFile = search_targetpixelfile("KIC 6922244", author="Kepler", cadence="long", quarter=4).download()

pixelFile.plot(frame=42)
