import tensorflow as tf
import argparse


def save_model(model):
    # serialize the model to disk
    print("[INFO] saving mask detector model...")
    tf.keras.models.save_model(model, save_format="h5")


