import logging
import time
import timeit

import numpy as np

import Adafruit_LSM303


# logging.basicConfig(filename='/home/pi/accelleration.log', level=logging.INFO, format='%(asctime)s - %(message)s')
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

lsm303 = Adafruit_LSM303.LSM303()

# shamelessly taken from here: https://github.com/adafruit/Adafruit_Python_LSM303/blob/master/examples/simpletest.py
# print('Printing accelerometer & magnetometer X, Y, Z axis values, press Ctrl-C to quit...')
tic = timeit.default_timer()
counter = 0
acc_x = []
acc_y = []
acc_z = []
interval = 5

while True:
    try:
        counter += 1
        # Read the X, Y, Z axis acceleration values and print them.
        accel, mag = lsm303.read()
        # Grab the X, Y, Z components from the reading and print them out.
        accel_x, accel_y, accel_z = accel
        if counter < interval:
            acc_x.append(accel_x)
            acc_y.append(accel_y)
            acc_z.append(accel_z)
        else:
            acc_x_min = np.min(acc_x)
            acc_x_max = np.max(acc_x)
            acc_x_mean = np.mean(acc_x)
            acc_x_std = np.std(acc_x)

            acc_y_min = np.min(acc_y)
            acc_y_max = np.max(acc_y)
            acc_y_mean = np.mean(acc_y)
            acc_y_std = np.std(acc_y)

            acc_z_min = np.min(acc_z)
            acc_z_max = np.max(acc_z)
            acc_z_mean = np.mean(acc_z)
            acc_z_std = np.std(acc_z)

            msg_x = "%.2f %.2f %.2f %.2f" % (acc_x_min, acc_x_max, acc_x_mean, acc_x_std)
            msg_y = "%.2f %.2f %.2f %.2f" % (acc_y_min, acc_y_max, acc_y_mean, acc_y_std)
            msg_z = "%.2f %.2f %.2f %.2f" % (acc_z_min, acc_z_max, acc_z_mean, acc_z_std)

            msg = " ".join([msg_x, msg_y, msg_z])

            logging.info(msg)
            # reset 
            counter = 0
            acc_x = []
            acc_y = []
            acc_z = []

        # mag_x, mag_y, mag_z = mag

        # msg = 'Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(accel_x, accel_y, accel_z, mag_x, mag_y, mag_z)
        # logging.info(msg)
        # print(msg)
        # Wait half a second and repeat.
        # time.sleep(0.5)
    except KeyboardInterrupt:
        break

toc = timeit.default_timer()
duration = toc - tic

print("ran %.2f seconds" % duration)
# print("measurements: %s" % counter)
