import math
import imagereader as ir
from neuralnetwork import *


if __name__ == "__main__":
    # Learn shape from the folder test1
    # We need a perceptron by each pixel

    # Training network only for hearts
    # Image 202×194 = 39188
    N = NeuralNetwork(39188)

    # Load images
    imA = ir.read_image_umbralized("test1/a.jpg")
    imB = ir.read_image_umbralized("test1/b.jpg")
    imC = ir.read_image_umbralized("test1/c.jpg")
    imD = ir.read_image_umbralized("test1/d.jpg")
    imE = ir.read_image_umbralized("test1/e.jpg")
    imF = ir.read_image_umbralized("test1/f.jpg")

    # Extract values
    vA = ir.extract_pixel_gray_scale(imA)
    vB = ir.extract_pixel_gray_scale(imB)
    vC = ir.extract_pixel_gray_scale(imC)
    vD = ir.extract_pixel_gray_scale(imD)
    vE = ir.extract_pixel_gray_scale(imE)
    vF = ir.extract_pixel_gray_scale(imF)

    # Add to training and apply function
    N.add_values_by_perceptron(vA)
    N.add_values_by_perceptron(vB)
    N.add_values_by_perceptron(vC)
    N.add_values_by_perceptron(vD)
    N.add_values_by_perceptron(vE)
    N.add_values_by_perceptron(vF)

    # Save memory image create concept
    # DONT USE THIS TO DO COMPARATION
    calculateW = N.get_weight_perceptrons()
    ir.create_synthetic("bank1.jpg", 202, 194, calculateW)

    # Image 202×194 = 39188
    N2 = NeuralNetwork(39188)

    # Load images
    imBA = ir.read_image_umbralized("test2/a.jpg")
    imBB = ir.read_image_umbralized("test2/b.jpg")
    imBC = ir.read_image_umbralized("test2/c.jpg")
    imBD = ir.read_image_umbralized("test2/d.jpg")
    imBE = ir.read_image_umbralized("test2/e.jpg")
    imBF = ir.read_image_umbralized("test2/f.jpg")
    # imTT = ir.read_image_umbralized("test2/test.jpg")  # Ball-8 confused (test2/test.jpg)

    # Extract values
    vBA = ir.extract_pixel_gray_scale(imBA)
    vBB = ir.extract_pixel_gray_scale(imBB)
    vBC = ir.extract_pixel_gray_scale(imBC)
    vBD = ir.extract_pixel_gray_scale(imBD)
    vBE = ir.extract_pixel_gray_scale(imBE)
    vBF = ir.extract_pixel_gray_scale(imBF)
    # vBTT = ir.extract_pixel_gray_scale(imTT)  # Ball-8 confused (test2/test.jpg)

    # Add to training and apply function
    N2.add_values_by_perceptron(vBA)
    N2.add_values_by_perceptron(vBB)
    N2.add_values_by_perceptron(vBC)
    N2.add_values_by_perceptron(vBD)
    N2.add_values_by_perceptron(vBE)
    N2.add_values_by_perceptron(vBF)
    # N2.add_values_by_perceptron(vBTT)  # Ball-8 confused (test2/test.jpg)

    # Save memory image create concept
    # DONT USE THIS TO DO COMPARATION
    calculateW = N2.get_weight_perceptrons()
    ir.create_synthetic("bank2.jpg", 202, 194, calculateW)

    # Test the knowledge comparations

    # Compare with test.jpg with de first arn and the second
    im_heart_test = ir.read_image_umbralized("test1/test.jpg")
    vH = ir.extract_pixel_gray_scale(im_heart_test)
    s1 = N.all_sigmas(vH)
    s2 = N2.all_sigmas(vH)
    print("Sigma for test1/test.jpg on N : " + str(s1))
    print("Sigma for test1/test.jpg on N2: " + str(s2))

    if s1<s2:
        print("Is a heart")
    else:
        print("Is a ball")

    if math.fabs(s1-s2)<30000:
        print("...but i'm not sure :S.\nI'm confused")

    N.write_sigmas_as_csv("sigmas.csv", vH)
