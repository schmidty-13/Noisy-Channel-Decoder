# Error-Correcting Codes Project

This project explores **error-correcting codes** and their applications to reliable communication over noisy channels. The problems focus on both the theoretical foundations of coding theory and its practical implementation using linear algebra and binary vector spaces.  

## Problems Solved

1. **Maximum Likelihood Decoding**  
   - Determining which codeword was most likely transmitted given a noisy received message.

2. **Error Correction Limits**  
   - Relating the minimum Hamming distance of a code to the maximum number of bit flips it can reliably correct.

3. **Code Design in Small Dimensions**  
   - Constructing codes in \{0,1\}³ with 2, 3, and 4 codewords that maximize minimum distance.

4. **Linear Codes via Generator and Parity-Check Matrices**  
   - Verifying the minimum distance of a linear [7,4]-code.  
   - Recovering the original message from its linear encoding.  
   - Showing that the kernel of the parity-check matrix corresponds to the code space.  
   - Using the parity-check matrix to test codeword validity.

5. **Practical Encoding/Decoding with ASCII Messages**  
   - Encoding English text as binary, splitting into blocks, and applying linear codes to protect against noise.  
   - Demonstrating the full round-trip of message encoding, transmission with simulated noise, and decoding back to the original message.  
   - Correcting errors in a noisy 980-bit sequence using the parity-check matrix and recovering the hidden original message.

---

Through these problems, the project combines **coding theory, Hamming distance, linear algebra over finite fields, and computational implementation** to design and test reliable communication schemes.
