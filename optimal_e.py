'''
This program finds the optimal e and d values needed for encrypting and decrypting messages using RSA.
It also displays the total multiplications, which is how the optimal values are determined.
'''

from sys import argv

script, p, q = argv


def binary(x):
    return [int(i) for i in bin(x)[2:]]


# xgcd and modinv functions courtesy of wikibooks:
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm#Python

# Extended Euclidean Algorithm
def xgcd(b, rem):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while rem != 0:
        quo, b, rem = b // rem, rem, b % rem
        x0, x1 = x1, x0 - quo * x1
        y0, y1 = y1, y0 - quo * y1
    return b, x0, y0


# Modular Inverse
def modinv(b, n):
    g, x, _ = xgcd(b, n)
    if g == 1:
        return x % n
    else:
        return -1


# Convert p and q to integers
p = int(p)
q = int(q)

# Calculate phi
phi = (p-1)*(q-1)

# Initialize lists
T_list = []
e_list = []
d_list = []

for i in range(100):
    # e starts at 2 and will iterate 100 times, adding 1 each time.
    e = 2 + i
    d = modinv(e, phi)

    if d == -1:  # e and phi are not relatively prime. Try another e.
        continue
    else:  # e and phi are relatively prime.
        # Convert e and d to binary
        bin_e = binary(e)
        bin_d = binary(d)

        # find m and r
        m = len(bin_d)
        r = len(bin_e)

        # Find the weights wd and we
        wd = bin_d.count(1)
        we = bin_e.count(1)

        # Calculate the total multiplications
        T = r + m + we + wd - 2

        # save our values of T, e, and d in lists to compare later
        T_list.append(T)
        e_list.append(e)
        d_list.append(d)

# Find the smallest T value, which means the least multiplications.
# It's position in the list will tell us the optimal e and d values.
small_T = min(T_list)  # If there are multiple smallest T values, min() will pick the one closest to index 0.
small_T_pos = T_list.index(small_T)
optimal_e = e_list[small_T_pos]
optimal_d = d_list[small_T_pos]

# Print values to console
print('Optimal e:', optimal_e)
print('Optimal d:', optimal_d)
print('Total multiplications:', small_T)
