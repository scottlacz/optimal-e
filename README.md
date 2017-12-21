# optimal-e
An assignment I did in computer security.

Original instructions:
The purpose of this assignment is to find various e and d values such that gcd(e,phi) = 1 and e(d) mod phi = 1 which produce the minimum number of multiplications for encryption and decryption for the RSA algorithm.

The complexity of the RSA system is a function of e and d parameters.

Let in binary form, d = dm dm-1 ...d1d0 and e = erer-1...e1e0  where gcd(e,phi) = 1 and  LaTeX: de\equiv1\:\mod\:z d e ≡ 1 mod z

We define Wd and We as weights of  and e:

LaTeX: W_d\:=\sum\:d_k\:and\:W_e=\sum e_k W d = ∑ d k a n d W e = ∑ e k

Then encryption requires r+we - 1 multiplications and m+wd - 1 multiplications for decryption

The goal of RSA cryptosystem design is to select the Optimal e and d that minimize the total number T of required multiplications for encryption and decryption per block of communication:

LaTeX: T\:=\:r\:+\:w_e\:+\:m\:+w_d T = r + w e + m + w d

Example p = 37, q = 31 n = 1147, phi = 1080

Select a variable e relatively prime with phi.

Let e = 77 = 1001101.

Then the corresponding d = 533 =1000010101.

Thus, m = 9 (length of d in binary), r =6 (length of e in binary), LaTeX: W_d=\sum d_k=\:4\:and\:W_e\:=\sum e_k\:=\:4 W d = ∑ d k = 4 a n d W e = ∑ e k = 4

Wd is the number of 1's in binary d and We is the number of 1's in binary e

Therefore T = 9+6+4+4 = 23.

The total number of multiplications is T-2 = 21.

Write a program and select 100 values of e.  You can start with e = 2 and increment until you have 100 e's.  Select two distinct 5 digit primes for p and q.  Also, run the same experiment for p = 1999 and q = 4999.

I got a 100/100.
