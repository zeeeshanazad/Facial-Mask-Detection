import numpy as np
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve
from sklearn import metrics
from sklearn.metrics import plot_roc_curve
import matplotlib.pyplot as plt
from Files import Architecture


#This function takes model as input as well as test dataset and hyper_parameters to evaluate the model and print the Classification report including
#Precision, Recall as well as AUC and ROC Curve to evaluate the model
def evalute_report(model,testX,testY,hyper_param):
    print("[INFO] evaluating network...")

    predIdxs = model.predict(testX, batch_size=hyper_param['batch_size'])
    # for each image in the testing set we need to find the index of the
    # label with corresponding largest predicted probability
    predIdxs = np.argmax(predIdxs, axis=1)

    transformY = np.argmax(testY, axis=1)

    # show a nicely formatted classification report
    print("\n\n", classification_report(testY.argmax(axis=1), predIdxs))

    fpr, tpr, thresholds = roc_curve(transformY, predIdxs)
    auc = metrics.roc_auc_score(transformY, predIdxs)
    print('\nAUC: %.2f' % auc)
    print('\n\n')

    #plot_roc_curve(model, testX, testY)

    COLOR = 'white'
    plt.rcParams['text.color'] = COLOR
    plt.rcParams['axes.labelcolor'] = COLOR
    plt.rcParams['xtick.color'] = COLOR
    plt.rcParams['ytick.color'] = COLOR
    plt.rcParams['axes.facecolor'] = 'black'

    plt.figure(figsize=(10, 6))
    plt.plot(fpr, tpr , '#76b4bd', linewidth=3, solid_capstyle="round", linestyle='-', marker="8", markersize=6, label='ROC')
    plt.plot([0, 1], [0, 1], '#d11141', linewidth=3, solid_capstyle="round", linestyle='dashed', marker="8", markersize=6)
    plt.title("ROC Curve")
    plt.xlabel("False Positive Rate", fontsize=20)
    plt.ylabel("True Positive Rate", fontsize=20)
    plt.title('Receiver Operating Characteristic (ROC) Curve',fontsize=20)
    legend = plt.legend(loc = 'lower right')
    #plt.setp(legend.get_texts(), color='black')
    plt.show()


#This function is used to perform actual face mask detection on an image and display the performed results
def show_img(imgPath):
    img = Architecture.mask_detection_on_image(imgPath)
    plt.axis('off')
    plt.imshow(img)