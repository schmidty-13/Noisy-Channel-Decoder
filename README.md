# Noisy-Channel-Decoder
This project explores error-correcting codes and their applications to reliable communication over noisy channels. The problems focus on both the theoretical foundations of coding theory and its practical implementation using linear algebra and binary vector spaces.

Specifically, the project addresses:

Maximum likelihood decoding – determining which codeword was most likely transmitted given a noisy received message.

Error correction limits – relating the minimum Hamming distance of a code to the maximum number of bit flips it can reliably correct.

Code design in small dimensions – constructing codes in 
{
0
,
1
}
3
{0,1}
3
 with 2, 3, and 4 codewords that maximize minimum distance.

Linear codes via generator and parity-check matrices –

Verifying the minimum distance of a linear 
[
7
,
4
]
[7,4]-code.

Recovering the original message from its linear encoding.

Showing that the kernel of the parity-check matrix corresponds to the code space.

Using the parity-check matrix to test codeword validity.

Practical encoding/decoding with ASCII messages –

Encoding English text as binary, splitting into blocks, and applying linear codes to protect against noise.

Demonstrating the full round-trip of message encoding, transmission with simulated noise, and decoding back to the original message.

Correcting errors in a noisy 980-bit sequence using the parity-check matrix and recovering the hidden original message.

Through these problems, the project combines coding theory, Hamming distance, linear algebra over finite fields, and computational implementation to design and test reliable communication schemes.
