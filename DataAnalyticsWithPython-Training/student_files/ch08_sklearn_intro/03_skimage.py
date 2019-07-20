from skimage import data, io, exposure, filters

image = data.camera()
io.imshow(image)
io.show()

flter = exposure.equalize_hist(image)
io.imshow(flter)
io.show()

flter = filters.roberts(image)
io.imshow(flter)
io.show()
