import time

def get_image_layers(image, width, height):
    pixel = 0
    layer = 0
    image_layer = {}

    while pixel < len(image):
        layer += 1
        for pixel_h in range(height):
            layer_pixels = ""
            for pixel_w in range(width):
                # Get one layer of pixels
                layer_pixels += image[pixel]
                pixel += 1
            if pixel_h == 0:
                image_layer[layer] = [layer_pixels]
            else:
                image_layer[layer].append(layer_pixels)
            #print image_layer
            #raw_input()

    return layer, image_layer

def get_count(layers, pixel_char):
    pixel = 0
    pixel_count = 0
    for layer in layers:
        for pixel in range(len(layer)):
            if layer[pixel] == pixel_char:
                pixel_count += 1
    return pixel_count

        
input_file = open("C:\\Users\\Wim\\Documents\\AOC\\2019\\input_8.txt")

image = input_file.read().rstrip()

width = 25
height = 6

# Test
#image = "123456789012"
#width  = 3
#height = 2

layers, image_layer = get_image_layers(image, width, height)

min_layer = 0
layer_count = 0
layer_nr = 0

for layer in range(layers):
    layer_list = image_layer[layer + 1]
    layer_count   = get_count(layer_list, "0")
    layer_count_1 = get_count(layer_list, "1")
    layer_count_2 = get_count(layer_list, "2")
    #print layer + 1, layer_count, layer_count_1, layer_count_2, layer_count + layer_count_1 + layer_count_2, layer_count_1 * layer_count_2
    #print layer + 1, layer_list
    if min_layer == 0 or layer_count < min_layer:
        layer_nr = layer + 1
        min_layer = layer_count

#layer_nr = 2
#print image_layer[layer_nr]
#print get_count(image_layer[layer_nr], "0")
#print get_count(image_layer[layer_nr], "1")
#print get_count(image_layer[layer_nr], "2")

#print min_layer, layer_nr, get_count(image_layer[layer_nr], "1") * get_count(image_layer[layer_nr], "2")

# Part 2 - Construct image
for row in range(height):
    row_pixel = ""
    for col in range(width):
        show_pixel = ""
        for layer in range(layers):
            #print layer, image_layer[layer + 1]
            pixel_layer = image_layer[100 - layer]
            pixel_string = pixel_layer[row]
            pixel = pixel_string[col]
            if pixel == "0":
                # Black
                show_pixel = " "
            if pixel == "1":
                # White
                show_pixel = "#"
        row_pixel = row_pixel + show_pixel
    print row_pixel
